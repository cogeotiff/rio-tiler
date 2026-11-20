import json
import os
import statistics
import subprocess
import sys
from typing import Any

S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multiband_measure.py")
N = int(sys.argv[1])
res: dict[tuple[int, str], Any] = {}
for run in range(N):
    for ti in range(3):
        for r in ("cog", "zarr"):
            p = subprocess.run(
                ["uv", "run", "python", "-W", "ignore", S, "one", r, str(ti)],
                capture_output=True,
                text=True,
            )
            line = [l for l in p.stdout.splitlines() if l.startswith("RESULT ")]
            if not line:
                print("FAIL", r, ti, p.stderr[-500:], flush=True)
                continue
            res.setdefault((ti, r), []).append(json.loads(line[0][7:]))
    print("run", run, "done", flush=True)
for (ti, r), v in sorted(res.items()):
    med = lambda k: statistics.median(x[k] for x in v)
    tot = [x["open"] + x["tile"] for x in v]
    print(
        f"tile{ti} {r:7s} n={len(v)} GETs={sorted(set(x['gets'] for x in v))} "
        f"bytes={sorted(set(x['bytes'] for x in v))} open={med('open'):.0f} tile={med('tile'):.0f} "
        f"total={statistics.median(tot):.0f} (min {min(tot):.0f} max {max(tot):.0f})"
    )
print(json.dumps({f"{ti}-{r}": v for (ti, r), v in res.items()}))
