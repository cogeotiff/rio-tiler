"""Cold timings: run each reader/tile in a fresh process, N times, print medians.

uv run python docs/scripts/cog_vs_geozarr/drive.py 10
"""

import json
import os
import statistics
import subprocess
import sys

S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "measure.py")
N = int(sys.argv[1])
JOBS = [(r, ti) for r in ("cog1", "zarr1") for ti in range(4)] + [
    (r, ti) for r in ("cog3", "zarr3") for ti in range(3)
]

res: dict = {}
for run in range(N):
    for r, ti in JOBS:
        p = subprocess.run(
            ["uv", "run", "python", "-W", "ignore", S, "one", r, str(ti)],
            capture_output=True,
            text=True,
        )
        line = [li for li in p.stdout.splitlines() if li.startswith("RESULT ")]
        if not line:
            print("FAIL", r, ti, p.stderr[-500:], flush=True)
            continue
        res.setdefault((r, ti), []).append(json.loads(line[0][7:]))
    print("run", run, "done", flush=True)

for (r, ti), v in sorted(res.items()):
    tot = [x["open"] + x["tile"] for x in v]
    print(
        f"{r:6s} tile{ti} n={len(v)} GETs={sorted({x['gets'] for x in v})} "
        f"ranges={sorted({x['ranges'] for x in v})} bytes={sorted({x['bytes'] for x in v})} "
        f"open={statistics.median(x['open'] for x in v):.0f} tile={statistics.median(x['tile'] for x in v):.0f} "
        f"total={statistics.median(tot):.0f} (min {min(tot):.0f} max {max(tot):.0f})"
    )
