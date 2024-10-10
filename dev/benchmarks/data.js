window.BENCHMARK_DATA = {
  "lastUpdate": 1728556225697,
  "repoUrl": "https://github.com/cogeotiff/rio-tiler",
  "entries": {
    "rio-tiler Benchmarks": [
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "bb33ffb7c0307c5d4f5ebc9061eac200e64b4326",
          "message": "refactor benchmark (#743)\n\n* refactor benchmark\r\n\r\n* optional filled\r\n\r\n* update benchmark names",
          "timestamp": "2024-10-04T13:21:10+02:00",
          "tree_id": "1c1f45b03db5dfaeebee9f4e0171467795eeb99b",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/bb33ffb7c0307c5d4f5ebc9061eac200e64b4326"
        },
        "date": 1728041228506,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.76276131783638,
            "unit": "iter/sec",
            "range": "stddev: 0.00007391350365293588",
            "extra": "mean: 26.481114333333267 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.58036750855081,
            "unit": "iter/sec",
            "range": "stddev: 0.00007192352210341151",
            "extra": "mean: 12.10941571429135 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.90343334988268,
            "unit": "iter/sec",
            "range": "stddev: 0.00010068963824537124",
            "extra": "mean: 21.320400844440556 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.86221228749852,
            "unit": "iter/sec",
            "range": "stddev: 0.000032499014204739925",
            "extra": "mean: 7.641625359374515 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.16391211496715,
            "unit": "iter/sec",
            "range": "stddev: 0.0000813007812931822",
            "extra": "mean: 26.202764459459576 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.19491837714298,
            "unit": "iter/sec",
            "range": "stddev: 0.00031784006033426315",
            "extra": "mean: 8.117217927273982 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.49930002995818,
            "unit": "iter/sec",
            "range": "stddev: 0.00017036549843868476",
            "extra": "mean: 26.66716443243208 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 115.12069651413807,
            "unit": "iter/sec",
            "range": "stddev: 0.00003832232991610246",
            "extra": "mean: 8.686535351852994 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.532076387667786,
            "unit": "iter/sec",
            "range": "stddev: 0.0006515608685175501",
            "extra": "mean: 31.713737709677144 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.30788038038294,
            "unit": "iter/sec",
            "range": "stddev: 0.00008416929272145614",
            "extra": "mean: 12.149504948718587 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.36145116332878,
            "unit": "iter/sec",
            "range": "stddev: 0.00020078420763907032",
            "extra": "mean: 32.936502099999146 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.9294322759945,
            "unit": "iter/sec",
            "range": "stddev: 0.0010233741311505501",
            "extra": "mean: 12.35644402631776 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.462209619863934,
            "unit": "iter/sec",
            "range": "stddev: 0.00022759488034360578",
            "extra": "mean: 29.88445806060509 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 94.72818737812352,
            "unit": "iter/sec",
            "range": "stddev: 0.00006492301116960595",
            "extra": "mean: 10.556519951219288 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.327429205655903,
            "unit": "iter/sec",
            "range": "stddev: 0.00019336526398907661",
            "extra": "mean: 39.48288600000069 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.51764258777322,
            "unit": "iter/sec",
            "range": "stddev: 0.00020645890637812177",
            "extra": "mean: 12.900289103447646 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.69365389897325,
            "unit": "iter/sec",
            "range": "stddev: 0.0002645395926339708",
            "extra": "mean: 38.92011638095433 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.43089731019965,
            "unit": "iter/sec",
            "range": "stddev: 0.0001435324473797666",
            "extra": "mean: 13.257166965515887 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.627217880019945,
            "unit": "iter/sec",
            "range": "stddev: 0.00012823173376528527",
            "extra": "mean: 39.021012920003386 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.7818581816455,
            "unit": "iter/sec",
            "range": "stddev: 0.00018042199566462375",
            "extra": "mean: 13.023909862070093 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.03965375077298,
            "unit": "iter/sec",
            "range": "stddev: 0.0005286118850085342",
            "extra": "mean: 22.70680886046812 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.05523615167974,
            "unit": "iter/sec",
            "range": "stddev: 0.00003914315827085536",
            "extra": "mean: 9.703534117647068 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.76965970768052,
            "unit": "iter/sec",
            "range": "stddev: 0.0002193156172617514",
            "extra": "mean: 17.615043055555034 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 158.77002764825076,
            "unit": "iter/sec",
            "range": "stddev: 0.00006066628018188116",
            "extra": "mean: 6.298417999998486 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.60056497817108,
            "unit": "iter/sec",
            "range": "stddev: 0.00020495760735210578",
            "extra": "mean: 24.63019912500357 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 114.36590871496011,
            "unit": "iter/sec",
            "range": "stddev: 0.00006175531116003686",
            "extra": "mean: 8.743864419355509 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.70530020753356,
            "unit": "iter/sec",
            "range": "stddev: 0.0000967680130141987",
            "extra": "mean: 24.56682532499599 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 108.91287772470544,
            "unit": "iter/sec",
            "range": "stddev: 0.00007466282905341271",
            "extra": "mean: 9.181650699999485 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.8627714404749,
            "unit": "iter/sec",
            "range": "stddev: 0.0007220877067496915",
            "extra": "mean: 31.38458943749356 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 110.53833799735932,
            "unit": "iter/sec",
            "range": "stddev: 0.00016665058716320544",
            "extra": "mean: 9.046635023804043 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.673699078562546,
            "unit": "iter/sec",
            "range": "stddev: 0.00021195971259910733",
            "extra": "mean: 32.601219612892635 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 109.03136062207416,
            "unit": "iter/sec",
            "range": "stddev: 0.00010320839355492986",
            "extra": "mean: 9.17167312500311 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.19260408131007,
            "unit": "iter/sec",
            "range": "stddev: 0.0002396355862256263",
            "extra": "mean: 28.41506123529732 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 142.1761359445455,
            "unit": "iter/sec",
            "range": "stddev: 0.00018481260606762257",
            "extra": "mean: 7.033529173911723 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.04976336124014,
            "unit": "iter/sec",
            "range": "stddev: 0.0005446320042225627",
            "extra": "mean: 45.35196063635929 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 93.65866872664255,
            "unit": "iter/sec",
            "range": "stddev: 0.0007742145805413876",
            "extra": "mean: 10.677068269234706 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.336543466725573,
            "unit": "iter/sec",
            "range": "stddev: 0.0006190419734751719",
            "extra": "mean: 46.86794754546368 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 90.8879556586454,
            "unit": "iter/sec",
            "range": "stddev: 0.00020851080446981408",
            "extra": "mean: 11.002557959998285 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.803373687545076,
            "unit": "iter/sec",
            "range": "stddev: 0.00011617264264631945",
            "extra": "mean: 45.8644618181836 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.62926202371635,
            "unit": "iter/sec",
            "range": "stddev: 0.0002181289878466405",
            "extra": "mean: 10.680421679994652 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.21750071890218,
            "unit": "iter/sec",
            "range": "stddev: 0.0003053646035160289",
            "extra": "mean: 22.615479928573127 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.18480799738403,
            "unit": "iter/sec",
            "range": "stddev: 0.00002850448558536009",
            "extra": "mean: 7.862574278687187 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.85893125942185,
            "unit": "iter/sec",
            "range": "stddev: 0.00007501117814535257",
            "extra": "mean: 20.467087065216187 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 143.2890750577382,
            "unit": "iter/sec",
            "range": "stddev: 0.0010086102342290783",
            "extra": "mean: 6.978899121213889 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.15388988850382,
            "unit": "iter/sec",
            "range": "stddev: 0.00011910743666163981",
            "extra": "mean: 23.72260312500174 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 139.7374654421162,
            "unit": "iter/sec",
            "range": "stddev: 0.0005996724097464159",
            "extra": "mean: 7.156276928568112 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.95935577002589,
            "unit": "iter/sec",
            "range": "stddev: 0.0004157928665409713",
            "extra": "mean: 23.832587074998912 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.3820880393689,
            "unit": "iter/sec",
            "range": "stddev: 0.0003483906597199344",
            "extra": "mean: 6.974371859652557 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.953090245604855,
            "unit": "iter/sec",
            "range": "stddev: 0.00019737723859358246",
            "extra": "mean: 29.452400142854376 msec\nrounds: 28"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 123.44612852050352,
            "unit": "iter/sec",
            "range": "stddev: 0.00006309560626402972",
            "extra": "mean: 8.100699568183762 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.678569698645134,
            "unit": "iter/sec",
            "range": "stddev: 0.0001463123053887776",
            "extra": "mean: 30.60109451612444 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 121.07789216185543,
            "unit": "iter/sec",
            "range": "stddev: 0.00005783700532188281",
            "extra": "mean: 8.2591460930226 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.29595812976059,
            "unit": "iter/sec",
            "range": "stddev: 0.0015609636103879308",
            "extra": "mean: 28.33185591176309 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.61862442477897,
            "unit": "iter/sec",
            "range": "stddev: 0.00013733517039354906",
            "extra": "mean: 7.214037826083373 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.76360361105735,
            "unit": "iter/sec",
            "range": "stddev: 0.0007151938230388985",
            "extra": "mean: 37.364176160001534 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-mask",
            "value": 113.26108822008403,
            "unit": "iter/sec",
            "range": "stddev: 0.00013106936445725354",
            "extra": "mean: 8.8291576190478 msec\nrounds: 21"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.147201554270264,
            "unit": "iter/sec",
            "range": "stddev: 0.00023068669792912998",
            "extra": "mean: 38.24501057692286 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 108.28529687583976,
            "unit": "iter/sec",
            "range": "stddev: 0.00015789869370283363",
            "extra": "mean: 9.234864093752293 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.384230809316854,
            "unit": "iter/sec",
            "range": "stddev: 0.0003764751471445386",
            "extra": "mean: 37.90142707692194 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 110.4709686712875,
            "unit": "iter/sec",
            "range": "stddev: 0.00008852996537435136",
            "extra": "mean: 9.052152000002422 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.68679796691284,
            "unit": "iter/sec",
            "range": "stddev: 0.0003226438283458133",
            "extra": "mean: 22.377973931818154 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.72907254741892,
            "unit": "iter/sec",
            "range": "stddev: 0.00003755371899669918",
            "extra": "mean: 7.10585227272814 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.011784053406345,
            "unit": "iter/sec",
            "range": "stddev: 0.00009937633582359653",
            "extra": "mean: 20.403256468084013 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.19782585238065,
            "unit": "iter/sec",
            "range": "stddev: 0.000046215470252971956",
            "extra": "mean: 5.875515712329603 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.40913411526998,
            "unit": "iter/sec",
            "range": "stddev: 0.0004916218915294304",
            "extra": "mean: 23.03662628571601 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 173.13078577668801,
            "unit": "iter/sec",
            "range": "stddev: 0.00007173899140637796",
            "extra": "mean: 5.775980253967343 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 43.491792665819716,
            "unit": "iter/sec",
            "range": "stddev: 0.0003838412455341195",
            "extra": "mean: 22.992843906981605 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 172.21334595470626,
            "unit": "iter/sec",
            "range": "stddev: 0.00008843462909373452",
            "extra": "mean: 5.80675089062499 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.74376408720591,
            "unit": "iter/sec",
            "range": "stddev: 0.00023128256928156156",
            "extra": "mean: 29.63510524242772 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.80299420050102,
            "unit": "iter/sec",
            "range": "stddev: 0.00010258994896204216",
            "extra": "mean: 7.418232851064397 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.41529145628003,
            "unit": "iter/sec",
            "range": "stddev: 0.00057726099438485",
            "extra": "mean: 30.84963778125349 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 130.33072127199952,
            "unit": "iter/sec",
            "range": "stddev: 0.00009212421246228582",
            "extra": "mean: 7.672788044447366 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.490423696126825,
            "unit": "iter/sec",
            "range": "stddev: 0.00020589040584667546",
            "extra": "mean: 27.404450228571672 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 161.98998869468258,
            "unit": "iter/sec",
            "range": "stddev: 0.0001312856503386252",
            "extra": "mean: 6.1732210000013765 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 26.57782859812539,
            "unit": "iter/sec",
            "range": "stddev: 0.00024199477632999114",
            "extra": "mean: 37.62534611539081 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 115.76457414596076,
            "unit": "iter/sec",
            "range": "stddev: 0.0003652412459132356",
            "extra": "mean: 8.638221212122794 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 26.034235670761376,
            "unit": "iter/sec",
            "range": "stddev: 0.000560867674423758",
            "extra": "mean: 38.41096057692539 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 114.04047572254217,
            "unit": "iter/sec",
            "range": "stddev: 0.00018174416669541324",
            "extra": "mean: 8.768816454545286 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.238560546431632,
            "unit": "iter/sec",
            "range": "stddev: 0.00024685115316226095",
            "extra": "mean: 38.111846807693766 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.36239734402221,
            "unit": "iter/sec",
            "range": "stddev: 0.0001815298951081314",
            "extra": "mean: 8.52061667647022 msec\nrounds: 34"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "cd039d382d875a7be6efd793195186eed1945277",
          "message": "remove geographic_crs and update info model (#746)\n\n* remove geographic_crs and update info model\r\n\r\n* update changelog",
          "timestamp": "2024-10-10T12:24:16+02:00",
          "tree_id": "7170024e49836f46e410c306741af7a084a6ccdc",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/cd039d382d875a7be6efd793195186eed1945277"
        },
        "date": 1728556224863,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.00154024296496,
            "unit": "iter/sec",
            "range": "stddev: 0.00032645599891997936",
            "extra": "mean: 26.314722866663942 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.27188365282142,
            "unit": "iter/sec",
            "range": "stddev: 0.00010056945540332613",
            "extra": "mean: 12.154820767443388 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.2641964476893,
            "unit": "iter/sec",
            "range": "stddev: 0.00009303882263451918",
            "extra": "mean: 21.157664260869687 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.85912901061863,
            "unit": "iter/sec",
            "range": "stddev: 0.00006318915799936727",
            "extra": "mean: 7.6418054098377395 msec\nrounds: 61"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.73505190603744,
            "unit": "iter/sec",
            "range": "stddev: 0.00018852308610343133",
            "extra": "mean: 26.500559810810927 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.86123922641875,
            "unit": "iter/sec",
            "range": "stddev: 0.00011024401546380123",
            "extra": "mean: 8.139263499997083 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.96469442664676,
            "unit": "iter/sec",
            "range": "stddev: 0.0001067512727730975",
            "extra": "mean: 26.340262054055078 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 115.20936274232139,
            "unit": "iter/sec",
            "range": "stddev: 0.00006189093401267382",
            "extra": "mean: 8.679850111111296 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.05929205769639,
            "unit": "iter/sec",
            "range": "stddev: 0.0005654036547532682",
            "extra": "mean: 31.192204687499725 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 83.10344605649615,
            "unit": "iter/sec",
            "range": "stddev: 0.00009991907713287964",
            "extra": "mean: 12.03319534210616 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.838068295995058,
            "unit": "iter/sec",
            "range": "stddev: 0.00013191644617816572",
            "extra": "mean: 32.42745266667271 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 83.88669689638398,
            "unit": "iter/sec",
            "range": "stddev: 0.00015313660266987072",
            "extra": "mean: 11.920841289473946 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.848977892418695,
            "unit": "iter/sec",
            "range": "stddev: 0.0007386414820887542",
            "extra": "mean: 29.54298954545314 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 95.77065974832858,
            "unit": "iter/sec",
            "range": "stddev: 0.00005838999236712846",
            "extra": "mean: 10.441611268292974 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.81678629564714,
            "unit": "iter/sec",
            "range": "stddev: 0.0003470061769097787",
            "extra": "mean: 38.73448804000077 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 78.2651836547784,
            "unit": "iter/sec",
            "range": "stddev: 0.0002547995048096194",
            "extra": "mean: 12.777073448277099 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.914358358069535,
            "unit": "iter/sec",
            "range": "stddev: 0.00031687411555009323",
            "extra": "mean: 38.588645961539214 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.95996839465444,
            "unit": "iter/sec",
            "range": "stddev: 0.0001398132168795555",
            "extra": "mean: 13.16482906897014 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.063648106330064,
            "unit": "iter/sec",
            "range": "stddev: 0.00023871365502235368",
            "extra": "mean: 38.36761438461604 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.66925964022131,
            "unit": "iter/sec",
            "range": "stddev: 0.0001342925787246449",
            "extra": "mean: 12.875106633334592 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.40376944425,
            "unit": "iter/sec",
            "range": "stddev: 0.0001397007391316737",
            "extra": "mean: 22.520610581394987 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 104.78354069013027,
            "unit": "iter/sec",
            "range": "stddev: 0.000044515192520698896",
            "extra": "mean: 9.543483579708733 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.118459578864716,
            "unit": "iter/sec",
            "range": "stddev: 0.0003545279883780635",
            "extra": "mean: 17.507474945455733 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 158.32058700145248,
            "unit": "iter/sec",
            "range": "stddev: 0.0002685601882951757",
            "extra": "mean: 6.316297955557894 msec\nrounds: 90"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.18676037955219,
            "unit": "iter/sec",
            "range": "stddev: 0.00011323594004543857",
            "extra": "mean: 24.279646924997422 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 114.78774127574104,
            "unit": "iter/sec",
            "range": "stddev: 0.0000624298912785165",
            "extra": "mean: 8.71173166129141 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.92921712139496,
            "unit": "iter/sec",
            "range": "stddev: 0.00043595832622748726",
            "extra": "mean: 24.432424325000568 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.93318960990705,
            "unit": "iter/sec",
            "range": "stddev: 0.00031335213299893086",
            "extra": "mean: 9.351633516665933 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.145888263329226,
            "unit": "iter/sec",
            "range": "stddev: 0.0004059083318047135",
            "extra": "mean: 31.10817756250217 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 108.91638430569569,
            "unit": "iter/sec",
            "range": "stddev: 0.00013146104194150244",
            "extra": "mean: 9.181355095238008 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.17481505116063,
            "unit": "iter/sec",
            "range": "stddev: 0.00012202789196659808",
            "extra": "mean: 32.07717506451639 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.08061123214924,
            "unit": "iter/sec",
            "range": "stddev: 0.00018053839694902787",
            "extra": "mean: 9.252353300001914 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.53182226549963,
            "unit": "iter/sec",
            "range": "stddev: 0.00024000782963380136",
            "extra": "mean: 28.14378594286089 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 135.87387709398715,
            "unit": "iter/sec",
            "range": "stddev: 0.0007434971170718218",
            "extra": "mean: 7.359766434781843 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.96402490397142,
            "unit": "iter/sec",
            "range": "stddev: 0.0002512340966785479",
            "extra": "mean: 45.52899590908701 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 97.8825489826073,
            "unit": "iter/sec",
            "range": "stddev: 0.0001498225009643778",
            "extra": "mean: 10.216325692312012 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.731773993073197,
            "unit": "iter/sec",
            "range": "stddev: 0.0004515219342952221",
            "extra": "mean: 46.01557149999538 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 92.66764216233888,
            "unit": "iter/sec",
            "range": "stddev: 0.00012183432323550558",
            "extra": "mean: 10.791253307688136 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.091883013397624,
            "unit": "iter/sec",
            "range": "stddev: 0.0006057398740262852",
            "extra": "mean: 45.26549409090886 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 95.58182217550348,
            "unit": "iter/sec",
            "range": "stddev: 0.00044365426472908124",
            "extra": "mean: 10.462240384618745 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.58930528295312,
            "unit": "iter/sec",
            "range": "stddev: 0.00008570898226196668",
            "extra": "mean: 22.426902452375924 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.25467326732438,
            "unit": "iter/sec",
            "range": "stddev: 0.000030202355687976637",
            "extra": "mean: 7.858257573765454 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.9834238964722,
            "unit": "iter/sec",
            "range": "stddev: 0.00048037775700611197",
            "extra": "mean: 20.415069434785266 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.393418243382,
            "unit": "iter/sec",
            "range": "stddev: 0.00003704417513898293",
            "extra": "mean: 6.693735318184268 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.50132612637865,
            "unit": "iter/sec",
            "range": "stddev: 0.00009235285626593961",
            "extra": "mean: 23.528677599999526 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.2478912173668,
            "unit": "iter/sec",
            "range": "stddev: 0.00009207750056960701",
            "extra": "mean: 7.02998119298595 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.50983290694365,
            "unit": "iter/sec",
            "range": "stddev: 0.00006646377626658295",
            "extra": "mean: 23.523969199997907 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 144.58613025593698,
            "unit": "iter/sec",
            "range": "stddev: 0.00003508826365143009",
            "extra": "mean: 6.916292719293787 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.2220318666091,
            "unit": "iter/sec",
            "range": "stddev: 0.0005668061861835564",
            "extra": "mean: 29.22094175757324 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 124.10369039837818,
            "unit": "iter/sec",
            "range": "stddev: 0.00005924061143923759",
            "extra": "mean: 8.057778111109807 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.89728935794094,
            "unit": "iter/sec",
            "range": "stddev: 0.00023164776322969694",
            "extra": "mean: 30.397641249996 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 120.86708665018661,
            "unit": "iter/sec",
            "range": "stddev: 0.00010428757911965104",
            "extra": "mean: 8.273550953488263 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.785064097934395,
            "unit": "iter/sec",
            "range": "stddev: 0.0007154024254458776",
            "extra": "mean: 27.944619500003146 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.4296364490261,
            "unit": "iter/sec",
            "range": "stddev: 0.00018367467435646682",
            "extra": "mean: 7.223886630434297 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.203258103252896,
            "unit": "iter/sec",
            "range": "stddev: 0.00023154849128077774",
            "extra": "mean: 36.76030261538498 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 113.54932635732371,
            "unit": "iter/sec",
            "range": "stddev: 0.00015785697670475822",
            "extra": "mean: 8.806745333328893 msec\nrounds: 21"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.704708386532303,
            "unit": "iter/sec",
            "range": "stddev: 0.00024709799437123655",
            "extra": "mean: 37.4465800384594 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 106.70434112406046,
            "unit": "iter/sec",
            "range": "stddev: 0.0005331192399809356",
            "extra": "mean: 9.371689937500705 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.928298101427785,
            "unit": "iter/sec",
            "range": "stddev: 0.00019675524757700483",
            "extra": "mean: 37.13565544444779 msec\nrounds: 18"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 110.5847096484712,
            "unit": "iter/sec",
            "range": "stddev: 0.00009182034631622804",
            "extra": "mean: 9.042841484856442 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 44.864891927114975,
            "unit": "iter/sec",
            "range": "stddev: 0.00007582724820930367",
            "extra": "mean: 22.28914318181229 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.39803593387822,
            "unit": "iter/sec",
            "range": "stddev: 0.00003115279273602799",
            "extra": "mean: 7.122606761186883 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.94072782414394,
            "unit": "iter/sec",
            "range": "stddev: 0.0005410571318224852",
            "extra": "mean: 20.432879617018482 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.58763453510838,
            "unit": "iter/sec",
            "range": "stddev: 0.00009302087060134408",
            "extra": "mean: 5.896656337835633 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.1182697993652,
            "unit": "iter/sec",
            "range": "stddev: 0.00021762773532534168",
            "extra": "mean: 22.666346720931216 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 173.2988868218571,
            "unit": "iter/sec",
            "range": "stddev: 0.00012870964137035718",
            "extra": "mean: 5.770377515626812 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.08998873336139,
            "unit": "iter/sec",
            "range": "stddev: 0.00010946777499086284",
            "extra": "mean: 22.68088581395654 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 173.7548043169411,
            "unit": "iter/sec",
            "range": "stddev: 0.00003627932267499786",
            "extra": "mean: 5.755236546875153 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.44750743124881,
            "unit": "iter/sec",
            "range": "stddev: 0.00011347291754107047",
            "extra": "mean: 29.029676588235734 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.60557058044415,
            "unit": "iter/sec",
            "range": "stddev: 0.00010453969203586943",
            "extra": "mean: 7.429113042556968 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 33.09865391300996,
            "unit": "iter/sec",
            "range": "stddev: 0.00012210055808312584",
            "extra": "mean: 30.212709031255613 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 131.82487013270887,
            "unit": "iter/sec",
            "range": "stddev: 0.00009660623945129018",
            "extra": "mean: 7.58582200000117 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.93215060322838,
            "unit": "iter/sec",
            "range": "stddev: 0.0002740891393163174",
            "extra": "mean: 27.07667936111433 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 162.56698735291528,
            "unit": "iter/sec",
            "range": "stddev: 0.0003387405776987263",
            "extra": "mean: 6.151310399995964 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.26039750507641,
            "unit": "iter/sec",
            "range": "stddev: 0.000411732694013817",
            "extra": "mean: 36.683250851855 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 125.25268670422419,
            "unit": "iter/sec",
            "range": "stddev: 0.00010186578348390083",
            "extra": "mean: 7.983860676469423 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.665450202505614,
            "unit": "iter/sec",
            "range": "stddev: 0.0008030871436090121",
            "extra": "mean: 37.50171073076558 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 117.38566709833114,
            "unit": "iter/sec",
            "range": "stddev: 0.0001590719255119498",
            "extra": "mean: 8.518927606062196 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.858085065331355,
            "unit": "iter/sec",
            "range": "stddev: 0.0006844289584764912",
            "extra": "mean: 37.23273634615181 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 120.4591203002885,
            "unit": "iter/sec",
            "range": "stddev: 0.00013233498419066417",
            "extra": "mean: 8.301571500000444 msec\nrounds: 34"
          }
        ]
      }
    ]
  }
}