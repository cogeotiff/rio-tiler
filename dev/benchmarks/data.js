window.BENCHMARK_DATA = {
  "lastUpdate": 1730815259206,
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
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "distinct": true,
          "id": "60f6aadc4e8c096bacc3f4ee287964261eeea6c8",
          "message": "add migration guide",
          "timestamp": "2024-10-11T16:30:45+02:00",
          "tree_id": "63c4d209be3f144271d20af5295f7a2d38a260f2",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/60f6aadc4e8c096bacc3f4ee287964261eeea6c8"
        },
        "date": 1728657768258,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.61414791076274,
            "unit": "iter/sec",
            "range": "stddev: 0.00041009533361686587",
            "extra": "mean: 25.897243733333163 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.98631371338939,
            "unit": "iter/sec",
            "range": "stddev: 0.00023407466905700275",
            "extra": "mean: 12.050179785713937 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.356409884647526,
            "unit": "iter/sec",
            "range": "stddev: 0.00015567600301775328",
            "extra": "mean: 20.67978169565243 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 132.71103807276987,
            "unit": "iter/sec",
            "range": "stddev: 0.000048128327079685965",
            "extra": "mean: 7.5351682461534715 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.28468338918484,
            "unit": "iter/sec",
            "range": "stddev: 0.0007704644919183364",
            "extra": "mean: 26.120106305554376 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 126.15915634977668,
            "unit": "iter/sec",
            "range": "stddev: 0.00005305060956993641",
            "extra": "mean: 7.926495618181661 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.212293463191074,
            "unit": "iter/sec",
            "range": "stddev: 0.0008455458018111051",
            "extra": "mean: 26.872839777778285 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 116.17793534762731,
            "unit": "iter/sec",
            "range": "stddev: 0.00009075231770177778",
            "extra": "mean: 8.607486413042222 msec\nrounds: 46"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 29.763780086738883,
            "unit": "iter/sec",
            "range": "stddev: 0.0008683133939975103",
            "extra": "mean: 33.59788296667148 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 78.67074323148373,
            "unit": "iter/sec",
            "range": "stddev: 0.00041580583341020944",
            "extra": "mean: 12.711205702704024 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.200567308624954,
            "unit": "iter/sec",
            "range": "stddev: 0.0006140637086013502",
            "extra": "mean: 34.24590999999615 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 73.54497317029718,
            "unit": "iter/sec",
            "range": "stddev: 0.0015216600344400038",
            "extra": "mean: 13.59712237142909 msec\nrounds: 35"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.06793145883315,
            "unit": "iter/sec",
            "range": "stddev: 0.0008082217627263296",
            "extra": "mean: 30.240778781246647 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 94.05561795903404,
            "unit": "iter/sec",
            "range": "stddev: 0.00017087267698488888",
            "extra": "mean: 10.632007121951506 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.491954050181526,
            "unit": "iter/sec",
            "range": "stddev: 0.000427977066112668",
            "extra": "mean: 37.747309923072585 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 72.89248115515664,
            "unit": "iter/sec",
            "range": "stddev: 0.00039049257277723524",
            "extra": "mean: 13.718836074072325 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.441699838530113,
            "unit": "iter/sec",
            "range": "stddev: 0.0008814981062181316",
            "extra": "mean: 39.30554980000011 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 69.68433570818715,
            "unit": "iter/sec",
            "range": "stddev: 0.0008011186134853248",
            "extra": "mean: 14.350427392859697 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.437317652843674,
            "unit": "iter/sec",
            "range": "stddev: 0.0009520296568913225",
            "extra": "mean: 39.312321119998614 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 73.58273163297089,
            "unit": "iter/sec",
            "range": "stddev: 0.0006071003890656326",
            "extra": "mean: 13.590145103445993 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 45.16712298730695,
            "unit": "iter/sec",
            "range": "stddev: 0.0001177869783626676",
            "extra": "mean: 22.139997720931305 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.43292460531183,
            "unit": "iter/sec",
            "range": "stddev: 0.000055249696288445615",
            "extra": "mean: 9.66810136922924 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 58.27893532476274,
            "unit": "iter/sec",
            "range": "stddev: 0.00015818541602410956",
            "extra": "mean: 17.158858418182177 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 161.21927515300771,
            "unit": "iter/sec",
            "range": "stddev: 0.00005921446786786379",
            "extra": "mean: 6.202732266665596 msec\nrounds: 90"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.57870103431394,
            "unit": "iter/sec",
            "range": "stddev: 0.0002514136764025285",
            "extra": "mean: 24.050775399999225 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.38839336706026,
            "unit": "iter/sec",
            "range": "stddev: 0.00035723410834756676",
            "extra": "mean: 8.819244812498628 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.14463866338455,
            "unit": "iter/sec",
            "range": "stddev: 0.0006163747429159617",
            "extra": "mean: 24.304503150003853 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 109.35502145149631,
            "unit": "iter/sec",
            "range": "stddev: 0.00018796543929051725",
            "extra": "mean: 9.144527491529443 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.11438740150905,
            "unit": "iter/sec",
            "range": "stddev: 0.0006063055100603597",
            "extra": "mean: 31.138691437502253 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 104.15047354908235,
            "unit": "iter/sec",
            "range": "stddev: 0.0005759191208408672",
            "extra": "mean: 9.601492589745511 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.144082961047737,
            "unit": "iter/sec",
            "range": "stddev: 0.0005566296458958184",
            "extra": "mean: 32.10882790322359 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 102.09820619704657,
            "unit": "iter/sec",
            "range": "stddev: 0.0006274800360917915",
            "extra": "mean: 9.794491375000547 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.227845834503064,
            "unit": "iter/sec",
            "range": "stddev: 0.0004047092573732955",
            "extra": "mean: 27.603076500000157 msec\nrounds: 28"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 140.93978601336698,
            "unit": "iter/sec",
            "range": "stddev: 0.0003079823106354161",
            "extra": "mean: 7.0952285957434205 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.459436166526128,
            "unit": "iter/sec",
            "range": "stddev: 0.0011455529845020255",
            "extra": "mean: 42.626770434784916 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 97.14966551482078,
            "unit": "iter/sec",
            "range": "stddev: 0.0001987666064023307",
            "extra": "mean: 10.293396222218016 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.817052168387708,
            "unit": "iter/sec",
            "range": "stddev: 0.0006924308520723402",
            "extra": "mean: 43.826870913038796 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 91.42836678383051,
            "unit": "iter/sec",
            "range": "stddev: 0.00022201814980486547",
            "extra": "mean: 10.937524481481322 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 23.085760970228574,
            "unit": "iter/sec",
            "range": "stddev: 0.00044268232842273385",
            "extra": "mean: 43.31674408695478 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 90.32401935460786,
            "unit": "iter/sec",
            "range": "stddev: 0.0010376045319410742",
            "extra": "mean: 11.071252222225045 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.41644327047526,
            "unit": "iter/sec",
            "range": "stddev: 0.00014273454735017014",
            "extra": "mean: 22.018456928574352 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 128.8727638780323,
            "unit": "iter/sec",
            "range": "stddev: 0.00004026016750403344",
            "extra": "mean: 7.759591475406079 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 50.00796398106195,
            "unit": "iter/sec",
            "range": "stddev: 0.00029110649640902664",
            "extra": "mean: 19.99681491489437 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.55900860764703,
            "unit": "iter/sec",
            "range": "stddev: 0.0001306632739445583",
            "extra": "mean: 6.686324075759282 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 43.12059842516422,
            "unit": "iter/sec",
            "range": "stddev: 0.00009466342427657824",
            "extra": "mean: 23.190772774999857 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 146.9857223568828,
            "unit": "iter/sec",
            "range": "stddev: 0.00006762577771484748",
            "extra": "mean: 6.803381879309271 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.80180939641592,
            "unit": "iter/sec",
            "range": "stddev: 0.0001694994456455308",
            "extra": "mean: 23.363498274999017 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 145.25356588183683,
            "unit": "iter/sec",
            "range": "stddev: 0.0003121200919554987",
            "extra": "mean: 6.884512568961617 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.33916525678375,
            "unit": "iter/sec",
            "range": "stddev: 0.000344434824577591",
            "extra": "mean: 29.121267000002234 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 125.36720410234946,
            "unit": "iter/sec",
            "range": "stddev: 0.00007497000363954122",
            "extra": "mean: 7.9765677727294815 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.24405398710308,
            "unit": "iter/sec",
            "range": "stddev: 0.004624808663740118",
            "extra": "mean: 31.01346996875698 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 121.5700811032972,
            "unit": "iter/sec",
            "range": "stddev: 0.0001464928309790404",
            "extra": "mean: 8.225708093015973 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.61151882651707,
            "unit": "iter/sec",
            "range": "stddev: 0.00031322829349274",
            "extra": "mean: 27.313808114284452 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 136.12577145439326,
            "unit": "iter/sec",
            "range": "stddev: 0.0001724226079159684",
            "extra": "mean: 7.346147531917084 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.456177748895154,
            "unit": "iter/sec",
            "range": "stddev: 0.00030726641416461324",
            "extra": "mean: 36.42167562964005 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.46598766535597,
            "unit": "iter/sec",
            "range": "stddev: 0.0003608029122545907",
            "extra": "mean: 8.971346515155883 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.818042219955153,
            "unit": "iter/sec",
            "range": "stddev: 0.0008896489659513478",
            "extra": "mean: 37.28832969231085 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 105.95167377848853,
            "unit": "iter/sec",
            "range": "stddev: 0.00017515496296485698",
            "extra": "mean: 9.438265242422542 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.437646401372064,
            "unit": "iter/sec",
            "range": "stddev: 0.00104481718361285",
            "extra": "mean: 36.44627477778099 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 108.0009372456342,
            "unit": "iter/sec",
            "range": "stddev: 0.00027580399762730463",
            "extra": "mean: 9.259178906249943 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 45.727721160132404,
            "unit": "iter/sec",
            "range": "stddev: 0.00040184308468020456",
            "extra": "mean: 21.86857281818468 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 141.09648172857098,
            "unit": "iter/sec",
            "range": "stddev: 0.00010757377354812041",
            "extra": "mean: 7.087348938464052 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.36357795384018,
            "unit": "iter/sec",
            "range": "stddev: 0.0001298934911586696",
            "extra": "mean: 19.85561869564811 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.96144492441357,
            "unit": "iter/sec",
            "range": "stddev: 0.00005207480255839364",
            "extra": "mean: 5.849272041670715 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.41700465192419,
            "unit": "iter/sec",
            "range": "stddev: 0.00031227185689507674",
            "extra": "mean: 22.51389997674413 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 175.48461196744518,
            "unit": "iter/sec",
            "range": "stddev: 0.00006220297348678729",
            "extra": "mean: 5.698505349206995 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 44.40863135040809,
            "unit": "iter/sec",
            "range": "stddev: 0.0002477352736199002",
            "extra": "mean: 22.518144999999205 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-none",
            "value": 176.21869230865056,
            "unit": "iter/sec",
            "range": "stddev: 0.00005508670635170031",
            "extra": "mean: 5.674766887093226 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.518052696036264,
            "unit": "iter/sec",
            "range": "stddev: 0.0003769050779622841",
            "extra": "mean: 28.970348032258226 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.13522759063503,
            "unit": "iter/sec",
            "range": "stddev: 0.000603038147547139",
            "extra": "mean: 7.455163106383079 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 33.440144193904636,
            "unit": "iter/sec",
            "range": "stddev: 0.0006108236703042607",
            "extra": "mean: 29.90417727272471 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 133.73214676588827,
            "unit": "iter/sec",
            "range": "stddev: 0.00010923683855872487",
            "extra": "mean: 7.477633644441539 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.29837068057255,
            "unit": "iter/sec",
            "range": "stddev: 0.00041220779357414904",
            "extra": "mean: 26.81082261110311 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 157.43986149074965,
            "unit": "iter/sec",
            "range": "stddev: 0.0004202111165803558",
            "extra": "mean: 6.3516316041649645 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.01684765198164,
            "unit": "iter/sec",
            "range": "stddev: 0.0011867711157864684",
            "extra": "mean: 38.43663203846422 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 113.6872367749958,
            "unit": "iter/sec",
            "range": "stddev: 0.0005532801301666358",
            "extra": "mean: 8.796062147056587 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.76104527045076,
            "unit": "iter/sec",
            "range": "stddev: 0.0005824549648182167",
            "extra": "mean: 37.36774815385065 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 107.4779961944876,
            "unit": "iter/sec",
            "range": "stddev: 0.0005177255014363932",
            "extra": "mean: 9.30423003226114 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-none",
            "value": 25.51264715189953,
            "unit": "iter/sec",
            "range": "stddev: 0.0006064037680419964",
            "extra": "mean: 39.196246239996526 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-none",
            "value": 103.78927651132086,
            "unit": "iter/sec",
            "range": "stddev: 0.00044454112636479364",
            "extra": "mean: 9.634906741939998 msec\nrounds: 31"
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
          "id": "0ee8dfb06d703c6269de3ab26a71e633231e1e28",
          "message": "relax morecantile dependency (#748)\n\n* relax morecantile dependency\r\n\r\n* fix tests\r\n\r\n* fix tests",
          "timestamp": "2024-10-18T00:06:38+02:00",
          "tree_id": "fc96588a40728a7b0ca53d65a1744bcf4aab2e64",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/0ee8dfb06d703c6269de3ab26a71e633231e1e28"
        },
        "date": 1729203163833,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.12456727929443,
            "unit": "iter/sec",
            "range": "stddev: 0.0005860796005262785",
            "extra": "mean: 26.936340899998374 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.93231879351002,
            "unit": "iter/sec",
            "range": "stddev: 0.0005127724236338183",
            "extra": "mean: 12.510584142858539 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.253810011805015,
            "unit": "iter/sec",
            "range": "stddev: 0.00036336534714589085",
            "extra": "mean: 21.619840608693153 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.5853162951423,
            "unit": "iter/sec",
            "range": "stddev: 0.0000734521961113296",
            "extra": "mean: 7.657828830768774 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.61775340468871,
            "unit": "iter/sec",
            "range": "stddev: 0.0004070833900375265",
            "extra": "mean: 26.583193027028532 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 118.8148368649426,
            "unit": "iter/sec",
            "range": "stddev: 0.00032101297608281",
            "extra": "mean: 8.416457290908077 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.823264814141744,
            "unit": "iter/sec",
            "range": "stddev: 0.00043145612387078124",
            "extra": "mean: 27.15674465714285 msec\nrounds: 35"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 107.65464712167251,
            "unit": "iter/sec",
            "range": "stddev: 0.00036161876773397044",
            "extra": "mean: 9.288962685185234 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.234535598800996,
            "unit": "iter/sec",
            "range": "stddev: 0.0007201835162566619",
            "extra": "mean: 32.01584338709961 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.61984657767567,
            "unit": "iter/sec",
            "range": "stddev: 0.0002623034741117414",
            "extra": "mean: 12.559682578946171 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.57113281785353,
            "unit": "iter/sec",
            "range": "stddev: 0.00015591222684140964",
            "extra": "mean: 33.81676333333606 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 79.48730584610367,
            "unit": "iter/sec",
            "range": "stddev: 0.0006291677073324668",
            "extra": "mean: 12.580625162162523 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.19735967262551,
            "unit": "iter/sec",
            "range": "stddev: 0.0006786835350399157",
            "extra": "mean: 31.058447343749407 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.32953847084352,
            "unit": "iter/sec",
            "range": "stddev: 0.0001864453748459114",
            "extra": "mean: 10.830770049996374 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.101147004645966,
            "unit": "iter/sec",
            "range": "stddev: 0.00029514826777637796",
            "extra": "mean: 39.838816919996134 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 72.74480281091363,
            "unit": "iter/sec",
            "range": "stddev: 0.0005540355312063422",
            "extra": "mean: 13.746686517239056 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.091407923791078,
            "unit": "iter/sec",
            "range": "stddev: 0.0002850669160607913",
            "extra": "mean: 39.854280120001704 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.79178909807007,
            "unit": "iter/sec",
            "range": "stddev: 0.00019006349012716138",
            "extra": "mean: 13.551643241377295 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.427156652859683,
            "unit": "iter/sec",
            "range": "stddev: 0.00028699104317811945",
            "extra": "mean: 39.32803079999644 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.97907418066839,
            "unit": "iter/sec",
            "range": "stddev: 0.00021184966743488244",
            "extra": "mean: 13.33705451724325 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.62482891432776,
            "unit": "iter/sec",
            "range": "stddev: 0.0003587144428705202",
            "extra": "mean: 22.92272599999971 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.89800174945772,
            "unit": "iter/sec",
            "range": "stddev: 0.00018597762713714274",
            "extra": "mean: 9.718361707692443 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.3445543791627,
            "unit": "iter/sec",
            "range": "stddev: 0.00031866555387630624",
            "extra": "mean: 17.747944074073985 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.73145691081368,
            "unit": "iter/sec",
            "range": "stddev: 0.00011011817574115831",
            "extra": "mean: 6.38034010344866 msec\nrounds: 87"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.13543891159767,
            "unit": "iter/sec",
            "range": "stddev: 0.00026732227080525643",
            "extra": "mean: 24.915636333331257 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 105.84589681761926,
            "unit": "iter/sec",
            "range": "stddev: 0.0006159983113175739",
            "extra": "mean: 9.447697360655162 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.660919396732254,
            "unit": "iter/sec",
            "range": "stddev: 0.00021116716394135008",
            "extra": "mean: 25.213737230771105 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.44549603988249,
            "unit": "iter/sec",
            "range": "stddev: 0.00020430625685633716",
            "extra": "mean: 9.307044379308481 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.224461097781397,
            "unit": "iter/sec",
            "range": "stddev: 0.0006315834609780978",
            "extra": "mean: 32.0261732258064 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 106.16370604524359,
            "unit": "iter/sec",
            "range": "stddev: 0.0002722646094887355",
            "extra": "mean: 9.41941495122478 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.095048801392675,
            "unit": "iter/sec",
            "range": "stddev: 0.0008584715534956453",
            "extra": "mean: 33.22805710000125 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 97.00603363600277,
            "unit": "iter/sec",
            "range": "stddev: 0.0004105118257207315",
            "extra": "mean: 10.308637128204987 msec\nrounds: 39"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.30146238110612,
            "unit": "iter/sec",
            "range": "stddev: 0.0005786877146887908",
            "extra": "mean: 29.153275999999885 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 136.5356881155356,
            "unit": "iter/sec",
            "range": "stddev: 0.00023663842248921742",
            "extra": "mean: 7.324092431817581 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.9428479028569,
            "unit": "iter/sec",
            "range": "stddev: 0.0009235623617383005",
            "extra": "mean: 45.57293585714563 msec\nrounds: 21"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 89.56721765315197,
            "unit": "iter/sec",
            "range": "stddev: 0.0002940018762043287",
            "extra": "mean: 11.16479919999847 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.337399008757618,
            "unit": "iter/sec",
            "range": "stddev: 0.000269056295494798",
            "extra": "mean: 46.86606833333177 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 86.74365582491917,
            "unit": "iter/sec",
            "range": "stddev: 0.00031038564401130413",
            "extra": "mean: 11.528220599998349 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.648577835005607,
            "unit": "iter/sec",
            "range": "stddev: 0.00045569131393331775",
            "extra": "mean: 46.19241077273015 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.21805729440459,
            "unit": "iter/sec",
            "range": "stddev: 0.00033620870502715374",
            "extra": "mean: 11.465515640006743 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.820693962772694,
            "unit": "iter/sec",
            "range": "stddev: 0.0003129309193670256",
            "extra": "mean: 22.82026845237862 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 122.57252394076448,
            "unit": "iter/sec",
            "range": "stddev: 0.0004793886963870537",
            "extra": "mean: 8.158435250001617 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.891386932006114,
            "unit": "iter/sec",
            "range": "stddev: 0.0007212692836673937",
            "extra": "mean: 20.880581333335613 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.86691168174013,
            "unit": "iter/sec",
            "range": "stddev: 0.00007190805630579544",
            "extra": "mean: 6.717409454546097 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.602203297061564,
            "unit": "iter/sec",
            "range": "stddev: 0.00029779701676184303",
            "extra": "mean: 24.03718843589786 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.49728934523267,
            "unit": "iter/sec",
            "range": "stddev: 0.00015093565621164453",
            "extra": "mean: 7.01767735088117 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.182480341538955,
            "unit": "iter/sec",
            "range": "stddev: 0.00036138736799206815",
            "extra": "mean: 24.28217027499784 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.42428551774248,
            "unit": "iter/sec",
            "range": "stddev: 0.00016548896571759962",
            "extra": "mean: 7.0709213508774935 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.139818884259306,
            "unit": "iter/sec",
            "range": "stddev: 0.00034961135770147304",
            "extra": "mean: 30.1751800000023 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 115.62625014996898,
            "unit": "iter/sec",
            "range": "stddev: 0.0003215770123442812",
            "extra": "mean: 8.648555139537821 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.703375690050024,
            "unit": "iter/sec",
            "range": "stddev: 0.0003631183347340542",
            "extra": "mean: 31.542382419353718 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 110.59304622801935,
            "unit": "iter/sec",
            "range": "stddev: 0.00035081821174129597",
            "extra": "mean: 9.042159829273647 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 32.92230957173033,
            "unit": "iter/sec",
            "range": "stddev: 0.0038057197196832175",
            "extra": "mean: 30.37453972726987 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 129.98818392630622,
            "unit": "iter/sec",
            "range": "stddev: 0.00029785970585117073",
            "extra": "mean: 7.6930069318217935 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.433423263799657,
            "unit": "iter/sec",
            "range": "stddev: 0.00024080569692332395",
            "extra": "mean: 37.83089273077586 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.9364976557066,
            "unit": "iter/sec",
            "range": "stddev: 0.00022923000077973394",
            "extra": "mean: 9.096160249999485 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.52132966258641,
            "unit": "iter/sec",
            "range": "stddev: 0.00023767815529367997",
            "extra": "mean: 39.182911439993404 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.42800528070167,
            "unit": "iter/sec",
            "range": "stddev: 0.00020462396260759538",
            "extra": "mean: 9.575975307696512 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.08111220680128,
            "unit": "iter/sec",
            "range": "stddev: 0.0010120405007390183",
            "extra": "mean: 38.34192315384563 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 104.3697817453926,
            "unit": "iter/sec",
            "range": "stddev: 0.0003535439279376925",
            "extra": "mean: 9.5813173437449 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.77916712559722,
            "unit": "iter/sec",
            "range": "stddev: 0.0002636409547566132",
            "extra": "mean: 22.84191467441852 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 137.22621112360446,
            "unit": "iter/sec",
            "range": "stddev: 0.00012944505692317072",
            "extra": "mean: 7.287237560609066 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.62545904139177,
            "unit": "iter/sec",
            "range": "stddev: 0.0002666197849753608",
            "extra": "mean: 20.565358553196656 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.45775808284762,
            "unit": "iter/sec",
            "range": "stddev: 0.00007708267777796637",
            "extra": "mean: 5.866556097223628 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.08922701787704,
            "unit": "iter/sec",
            "range": "stddev: 0.0002762512529814504",
            "extra": "mean: 23.2076569761884 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 167.44165510582206,
            "unit": "iter/sec",
            "range": "stddev: 0.00018132640126171186",
            "extra": "mean: 5.972229546871155 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.20059174936771,
            "unit": "iter/sec",
            "range": "stddev: 0.0003314157634060336",
            "extra": "mean: 23.14783107142592 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 170.9094898564989,
            "unit": "iter/sec",
            "range": "stddev: 0.00011530246953947707",
            "extra": "mean: 5.851050171875372 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.44122523120199,
            "unit": "iter/sec",
            "range": "stddev: 0.00035000582514209183",
            "extra": "mean: 29.903210575758457 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 118.04930321961527,
            "unit": "iter/sec",
            "range": "stddev: 0.0004285193778114551",
            "extra": "mean: 8.47103686956653 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 32.34370020081608,
            "unit": "iter/sec",
            "range": "stddev: 0.00027052819603402053",
            "extra": "mean: 30.917921999993325 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.79704519905135,
            "unit": "iter/sec",
            "range": "stddev: 0.00019940819319737025",
            "extra": "mean: 7.764153272728694 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.56900380067266,
            "unit": "iter/sec",
            "range": "stddev: 0.0006971149922970142",
            "extra": "mean: 28.11436625000694 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 151.99459129776966,
            "unit": "iter/sec",
            "range": "stddev: 0.0002909806462631635",
            "extra": "mean: 6.579181479168028 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.47759262284086,
            "unit": "iter/sec",
            "range": "stddev: 0.0009353134047220122",
            "extra": "mean: 37.767784037033316 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 117.69375869995096,
            "unit": "iter/sec",
            "range": "stddev: 0.00035500872878381625",
            "extra": "mean: 8.496627272729091 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.599475041188835,
            "unit": "iter/sec",
            "range": "stddev: 0.0003597016107583932",
            "extra": "mean: 39.0633010400029 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-none",
            "value": 109.85733415064612,
            "unit": "iter/sec",
            "range": "stddev: 0.00027126497761896957",
            "extra": "mean: 9.102714968749481 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.384810990911344,
            "unit": "iter/sec",
            "range": "stddev: 0.00019884103504094668",
            "extra": "mean: 37.9005936538437 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 116.47864700605376,
            "unit": "iter/sec",
            "range": "stddev: 0.0001487636538668542",
            "extra": "mean: 8.585264558816748 msec\nrounds: 34"
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
          "id": "0900af93721904a2fc613c9976c1a2d421ae2aed",
          "message": "Release/v7.0.0 (#750)\n\n* update changelog\r\n\r\n* Bump version: 6.7.0 → 7.0.0\r\n\r\n* remove deprecate method and update docs\r\n\r\n* allow bench to fail\r\n\r\n* fix type information for `bounds`",
          "timestamp": "2024-10-21T19:33:11+02:00",
          "tree_id": "936456c45a8e87a58059cf51ed72bd8cb3ddf1e1",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/0900af93721904a2fc613c9976c1a2d421ae2aed"
        },
        "date": 1729532375852,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.593065675335026,
            "unit": "iter/sec",
            "range": "stddev: 0.00037507369682889685",
            "extra": "mean: 26.600650466665833 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.4929987705642,
            "unit": "iter/sec",
            "range": "stddev: 0.00022664817772146152",
            "extra": "mean: 12.270992785716539 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.705814787198754,
            "unit": "iter/sec",
            "range": "stddev: 0.00014689155310250218",
            "extra": "mean: 21.879054222222926 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.73065880519428,
            "unit": "iter/sec",
            "range": "stddev: 0.00008241688603386306",
            "extra": "mean: 7.7681572461559565 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.979396781165555,
            "unit": "iter/sec",
            "range": "stddev: 0.00048435789432243933",
            "extra": "mean: 27.042085243243413 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.21618610054074,
            "unit": "iter/sec",
            "range": "stddev: 0.00015770941082670782",
            "extra": "mean: 8.182222272730334 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.91307167259908,
            "unit": "iter/sec",
            "range": "stddev: 0.0002939724347518694",
            "extra": "mean: 27.090674243246717 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.65925082104933,
            "unit": "iter/sec",
            "range": "stddev: 0.00018225170851878176",
            "extra": "mean: 8.955818641508259 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.111391474928116,
            "unit": "iter/sec",
            "range": "stddev: 0.0003756125392762345",
            "extra": "mean: 32.14256748387081 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.8707314738949,
            "unit": "iter/sec",
            "range": "stddev: 0.0001922345351741716",
            "extra": "mean: 12.520230897432581 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.776318538338273,
            "unit": "iter/sec",
            "range": "stddev: 0.0009039385396511377",
            "extra": "mean: 33.58373529999881 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 76.77202071011115,
            "unit": "iter/sec",
            "range": "stddev: 0.00032044228380602376",
            "extra": "mean: 13.025578729729807 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.85847918730906,
            "unit": "iter/sec",
            "range": "stddev: 0.0003151862298696992",
            "extra": "mean: 30.433544848485575 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 86.12684579876515,
            "unit": "iter/sec",
            "range": "stddev: 0.00011923234910866326",
            "extra": "mean: 11.61078164102856 msec\nrounds: 39"
          },
          {
            "name": "equator-float64-nodata",
            "value": 24.898580909162124,
            "unit": "iter/sec",
            "range": "stddev: 0.0011125433804332642",
            "extra": "mean: 40.16293152000571 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.33212349944087,
            "unit": "iter/sec",
            "range": "stddev: 0.00016581166734084928",
            "extra": "mean: 13.453133758616787 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.015847564448176,
            "unit": "iter/sec",
            "range": "stddev: 0.001048597746944244",
            "extra": "mean: 39.9746599599996 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 70.97770547177208,
            "unit": "iter/sec",
            "range": "stddev: 0.00017719056396874204",
            "extra": "mean: 14.088931071429199 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.232700870599356,
            "unit": "iter/sec",
            "range": "stddev: 0.0003475653427977749",
            "extra": "mean: 39.631112227275686 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 70.16543465852098,
            "unit": "iter/sec",
            "range": "stddev: 0.00019480871538657353",
            "extra": "mean: 14.252031714287382 msec\nrounds: 28"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.44104033079165,
            "unit": "iter/sec",
            "range": "stddev: 0.0003498737362936775",
            "extra": "mean: 23.562099142854517 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.37155621100028,
            "unit": "iter/sec",
            "range": "stddev: 0.00019306190409589314",
            "extra": "mean: 10.063241818178364 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.93616003568693,
            "unit": "iter/sec",
            "range": "stddev: 0.0005499675861048588",
            "extra": "mean: 17.877523222223445 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 159.77379305370502,
            "unit": "iter/sec",
            "range": "stddev: 0.00005481629254919263",
            "extra": "mean: 6.258848719100437 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.66719951920557,
            "unit": "iter/sec",
            "range": "stddev: 0.00015632057781070246",
            "extra": "mean: 25.209745384617648 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 114.6044390539455,
            "unit": "iter/sec",
            "range": "stddev: 0.00017779729134423044",
            "extra": "mean: 8.72566550000118 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.84152437587801,
            "unit": "iter/sec",
            "range": "stddev: 0.0001759647108411082",
            "extra": "mean: 24.484884324999 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 105.0144755601944,
            "unit": "iter/sec",
            "range": "stddev: 0.00016889703571815689",
            "extra": "mean: 9.522496728813342 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.08561534899252,
            "unit": "iter/sec",
            "range": "stddev: 0.0001155816999483698",
            "extra": "mean: 32.169220032261954 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 96.86737549969592,
            "unit": "iter/sec",
            "range": "stddev: 0.0017598758251053768",
            "extra": "mean: 10.323393142855812 msec\nrounds: 28"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.19655292619058,
            "unit": "iter/sec",
            "range": "stddev: 0.0001177164820293444",
            "extra": "mean: 33.116362733332494 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 100.96224056042716,
            "unit": "iter/sec",
            "range": "stddev: 0.0002926001384040304",
            "extra": "mean: 9.904693026314996 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.26182810233964,
            "unit": "iter/sec",
            "range": "stddev: 0.0006873978529813947",
            "extra": "mean: 29.18700067646749 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 135.7837477420578,
            "unit": "iter/sec",
            "range": "stddev: 0.00014705654251150654",
            "extra": "mean: 7.364651636362654 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.755396097450507,
            "unit": "iter/sec",
            "range": "stddev: 0.00033365708194208973",
            "extra": "mean: 45.965607590899666 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 88.15915551478713,
            "unit": "iter/sec",
            "range": "stddev: 0.0001835250161819956",
            "extra": "mean: 11.343121360007444 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.297169819972325,
            "unit": "iter/sec",
            "range": "stddev: 0.000964692787196907",
            "extra": "mean: 46.954595772730684 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 79.11820419524159,
            "unit": "iter/sec",
            "range": "stddev: 0.0005614419662907742",
            "extra": "mean: 12.639316200002213 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.491906739969576,
            "unit": "iter/sec",
            "range": "stddev: 0.0003983648160561072",
            "extra": "mean: 46.52914290476842 msec\nrounds: 21"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 85.12657717631855,
            "unit": "iter/sec",
            "range": "stddev: 0.00015542329948759135",
            "extra": "mean: 11.747212599993873 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 42.89989117866516,
            "unit": "iter/sec",
            "range": "stddev: 0.00019214055171699632",
            "extra": "mean: 23.310082439027653 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 124.29757523973626,
            "unit": "iter/sec",
            "range": "stddev: 0.0001387707142231368",
            "extra": "mean: 8.045209233335981 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.307095473699796,
            "unit": "iter/sec",
            "range": "stddev: 0.0004847853015098558",
            "extra": "mean: 21.13847806521849 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.42144549970016,
            "unit": "iter/sec",
            "range": "stddev: 0.00011599554643342436",
            "extra": "mean: 6.876564846153052 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.55727328260502,
            "unit": "iter/sec",
            "range": "stddev: 0.00022019394441196778",
            "extra": "mean: 24.656489923076244 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 135.0176697623717,
            "unit": "iter/sec",
            "range": "stddev: 0.00015243548397650457",
            "extra": "mean: 7.4064380000038454 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 39.84965155617949,
            "unit": "iter/sec",
            "range": "stddev: 0.000723130692848884",
            "extra": "mean: 25.0943223076923 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 135.34839598723713,
            "unit": "iter/sec",
            "range": "stddev: 0.00016878998389327867",
            "extra": "mean: 7.3883402363652415 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.514991455945015,
            "unit": "iter/sec",
            "range": "stddev: 0.00035374147359419053",
            "extra": "mean: 30.75504421875408 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 111.19779832598232,
            "unit": "iter/sec",
            "range": "stddev: 0.0002043222703412837",
            "extra": "mean: 8.992983809521537 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.09887979016101,
            "unit": "iter/sec",
            "range": "stddev: 0.001770795557178736",
            "extra": "mean: 32.155499064515425 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 107.25168256632432,
            "unit": "iter/sec",
            "range": "stddev: 0.0002152502611108628",
            "extra": "mean: 9.323863048783418 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.447991354375155,
            "unit": "iter/sec",
            "range": "stddev: 0.00015253932302230745",
            "extra": "mean: 29.029268781240347 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-mask",
            "value": 122.53675569354402,
            "unit": "iter/sec",
            "range": "stddev: 0.00023234628082734055",
            "extra": "mean: 8.160816681820197 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.2059821328345,
            "unit": "iter/sec",
            "range": "stddev: 0.00016669301860794167",
            "extra": "mean: 38.159226200000376 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-mask",
            "value": 102.83264017997912,
            "unit": "iter/sec",
            "range": "stddev: 0.00024373911899960033",
            "extra": "mean: 9.724538806450813 msec\nrounds: 31"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.76776172098922,
            "unit": "iter/sec",
            "range": "stddev: 0.0002403689088571645",
            "extra": "mean: 38.808182519999264 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 99.68186068972494,
            "unit": "iter/sec",
            "range": "stddev: 0.00018811956537345887",
            "extra": "mean: 10.031915466673052 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.62378753362873,
            "unit": "iter/sec",
            "range": "stddev: 0.0008959135819860293",
            "extra": "mean: 39.026236799988965 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 96.5085510000213,
            "unit": "iter/sec",
            "range": "stddev: 0.00032166494264948217",
            "extra": "mean: 10.361776129037304 msec\nrounds: 31"
          },
          {
            "name": "equator-int8-none",
            "value": 42.64547621548328,
            "unit": "iter/sec",
            "range": "stddev: 0.00011314027437807226",
            "extra": "mean: 23.449146046513846 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 134.87895349617716,
            "unit": "iter/sec",
            "range": "stddev: 0.00007867345484853978",
            "extra": "mean: 7.414055151520305 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 46.47996020306255,
            "unit": "iter/sec",
            "range": "stddev: 0.0001245117268333935",
            "extra": "mean: 21.514648369559282 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-none",
            "value": 166.62561428092985,
            "unit": "iter/sec",
            "range": "stddev: 0.00011107191399483546",
            "extra": "mean: 6.00147825000066 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.777316836547236,
            "unit": "iter/sec",
            "range": "stddev: 0.00012670135179312025",
            "extra": "mean: 23.37687526828798 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-none",
            "value": 166.27200993411844,
            "unit": "iter/sec",
            "range": "stddev: 0.00011673616619236292",
            "extra": "mean: 6.0142413650753825 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 41.83548321527664,
            "unit": "iter/sec",
            "range": "stddev: 0.0007993732801099451",
            "extra": "mean: 23.90315404878221 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.8960374404309,
            "unit": "iter/sec",
            "range": "stddev: 0.00010071299391582224",
            "extra": "mean: 5.817469761899204 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.49276817958603,
            "unit": "iter/sec",
            "range": "stddev: 0.00048810765754067745",
            "extra": "mean: 29.857191696967703 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 117.21675017878894,
            "unit": "iter/sec",
            "range": "stddev: 0.0012980709420555108",
            "extra": "mean: 8.531203931816188 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-none",
            "value": 31.85542171567937,
            "unit": "iter/sec",
            "range": "stddev: 0.00008125348150157504",
            "extra": "mean: 31.39183053124661 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 124.04984740597105,
            "unit": "iter/sec",
            "range": "stddev: 0.00014690500782817888",
            "extra": "mean: 8.061275534885226 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-none",
            "value": 35.53011146276563,
            "unit": "iter/sec",
            "range": "stddev: 0.00033873294805019473",
            "extra": "mean: 28.14514108822784 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-none",
            "value": 142.68596913542035,
            "unit": "iter/sec",
            "range": "stddev: 0.0002449748601080217",
            "extra": "mean: 7.0083975744729345 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-none",
            "value": 26.265405169022333,
            "unit": "iter/sec",
            "range": "stddev: 0.00015057629766660507",
            "extra": "mean: 38.07289450000221 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 107.58681654285917,
            "unit": "iter/sec",
            "range": "stddev: 0.0002053667545105647",
            "extra": "mean: 9.294819124995968 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-none",
            "value": 25.592808763063672,
            "unit": "iter/sec",
            "range": "stddev: 0.00020102734277233477",
            "extra": "mean: 39.07347604000506 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-none",
            "value": 104.60571954978536,
            "unit": "iter/sec",
            "range": "stddev: 0.00014031871135297778",
            "extra": "mean: 9.559706718752281 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-none",
            "value": 25.928447002014945,
            "unit": "iter/sec",
            "range": "stddev: 0.00019779644051534564",
            "extra": "mean: 38.567678192307014 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 112.69758768587677,
            "unit": "iter/sec",
            "range": "stddev: 0.00023252141381189476",
            "extra": "mean: 8.873304393944181 msec\nrounds: 33"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ama6fy@virginia.edu",
            "name": "Dr. Andrew Annex",
            "username": "AndrewAnnex"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "06c62d88088ea56c8775d008e7a6bed33b89c08c",
          "message": "Add CRS_to_urn (#752)\n\n* adds CRS_to_urn function\r\n\r\n* fix CRS expected type\r\n\r\n* switch to using typing's version of Tuple\r\n\r\n* format\r\n\r\n* make the crs info function private\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-10-22T21:58:34+02:00",
          "tree_id": "4cb21efbf94994f3941b1f30120d6510b7cf584d",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/06c62d88088ea56c8775d008e7a6bed33b89c08c"
        },
        "date": 1729627492672,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 36.11780580588631,
            "unit": "iter/sec",
            "range": "stddev: 0.0005950315121673296",
            "extra": "mean: 27.687174724136334 msec\nrounds: 29"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 78.63265816474282,
            "unit": "iter/sec",
            "range": "stddev: 0.0003617289684172248",
            "extra": "mean: 12.717362268294504 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.10893492020623,
            "unit": "iter/sec",
            "range": "stddev: 0.0005602167146825454",
            "extra": "mean: 22.16855711111142 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 125.91346752735393,
            "unit": "iter/sec",
            "range": "stddev: 0.0002537762730257402",
            "extra": "mean: 7.941962203389848 msec\nrounds: 59"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.77587099878632,
            "unit": "iter/sec",
            "range": "stddev: 0.00027604748613157236",
            "extra": "mean: 27.19174210810676 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.72951729214941,
            "unit": "iter/sec",
            "range": "stddev: 0.0002033945498008731",
            "extra": "mean: 8.21493440740434 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 35.96499897089421,
            "unit": "iter/sec",
            "range": "stddev: 0.0005227015440461652",
            "extra": "mean: 27.804811027779564 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 110.11852461271826,
            "unit": "iter/sec",
            "range": "stddev: 0.00029749174830873826",
            "extra": "mean: 9.081124211543457 msec\nrounds: 52"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.597264032325334,
            "unit": "iter/sec",
            "range": "stddev: 0.00092798613035182",
            "extra": "mean: 32.68266074193831 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 78.31054009116963,
            "unit": "iter/sec",
            "range": "stddev: 0.0007275338312310308",
            "extra": "mean: 12.769673135133454 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.424985805617432,
            "unit": "iter/sec",
            "range": "stddev: 0.0004656274331184811",
            "extra": "mean: 33.98472327585943 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 78.06442013089297,
            "unit": "iter/sec",
            "range": "stddev: 0.0002782220247571726",
            "extra": "mean: 12.809933108108275 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.066369720486755,
            "unit": "iter/sec",
            "range": "stddev: 0.0011483149956193089",
            "extra": "mean: 31.185319969697538 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 86.4388042255521,
            "unit": "iter/sec",
            "range": "stddev: 0.0007155155654798538",
            "extra": "mean: 11.568878224999679 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 24.72542773084291,
            "unit": "iter/sec",
            "range": "stddev: 0.0008972850836266615",
            "extra": "mean: 40.44419416666282 msec\nrounds: 24"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.14545398109361,
            "unit": "iter/sec",
            "range": "stddev: 0.00033648694884620207",
            "extra": "mean: 13.487003535712258 msec\nrounds: 28"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.08270839991188,
            "unit": "iter/sec",
            "range": "stddev: 0.0002756148626029853",
            "extra": "mean: 39.86810291999859 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 70.58811760770863,
            "unit": "iter/sec",
            "range": "stddev: 0.0005956496517453731",
            "extra": "mean: 14.166690285714521 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.18923239089071,
            "unit": "iter/sec",
            "range": "stddev: 0.0002746837595574606",
            "extra": "mean: 39.69950272726986 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 73.84270535654147,
            "unit": "iter/sec",
            "range": "stddev: 0.00041610657843347274",
            "extra": "mean: 13.542299068968406 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.011115460773865,
            "unit": "iter/sec",
            "range": "stddev: 0.0005760339158909475",
            "extra": "mean: 23.803224195123036 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.48651653005983,
            "unit": "iter/sec",
            "range": "stddev: 0.0003032518064395817",
            "extra": "mean: 10.051613373133335 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 54.777066479087516,
            "unit": "iter/sec",
            "range": "stddev: 0.0004432613998863597",
            "extra": "mean: 18.25581514814734 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 148.32885398946777,
            "unit": "iter/sec",
            "range": "stddev: 0.0003356122784597443",
            "extra": "mean: 6.741776620690442 msec\nrounds: 87"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.227771662650845,
            "unit": "iter/sec",
            "range": "stddev: 0.00033892671183289637",
            "extra": "mean: 25.492143897434534 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 103.25320883764222,
            "unit": "iter/sec",
            "range": "stddev: 0.00042005072868341406",
            "extra": "mean: 9.684929032786027 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.178850000641326,
            "unit": "iter/sec",
            "range": "stddev: 0.00023916893042955648",
            "extra": "mean: 25.523975307688485 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 103.62065897232948,
            "unit": "iter/sec",
            "range": "stddev: 0.00031315629858922624",
            "extra": "mean: 9.650585220337547 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.510763328256242,
            "unit": "iter/sec",
            "range": "stddev: 0.00028934990041814466",
            "extra": "mean: 32.775318966664216 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 96.844301373045,
            "unit": "iter/sec",
            "range": "stddev: 0.00046726721467006167",
            "extra": "mean: 10.325852794869078 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-alpha",
            "value": 29.82811620038437,
            "unit": "iter/sec",
            "range": "stddev: 0.0003790238510433701",
            "extra": "mean: 33.52541586206888 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 96.87940277047518,
            "unit": "iter/sec",
            "range": "stddev: 0.00028820614132104736",
            "extra": "mean: 10.322111526318766 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 33.956285782805175,
            "unit": "iter/sec",
            "range": "stddev: 0.00038601654105370356",
            "extra": "mean: 29.449628454546147 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 133.27357718061594,
            "unit": "iter/sec",
            "range": "stddev: 0.0003383529175696983",
            "extra": "mean: 7.503362790696111 msec\nrounds: 43"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.748207539177688,
            "unit": "iter/sec",
            "range": "stddev: 0.000355700076106574",
            "extra": "mean: 45.980800863638 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 82.21920635598634,
            "unit": "iter/sec",
            "range": "stddev: 0.00024074466124897326",
            "extra": "mean: 12.162608279995766 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.089169987749088,
            "unit": "iter/sec",
            "range": "stddev: 0.0006852350010926804",
            "extra": "mean: 47.41770304762635 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 84.7121256804451,
            "unit": "iter/sec",
            "range": "stddev: 0.00028372123722604124",
            "extra": "mean: 11.804685480001353 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.285080728336002,
            "unit": "iter/sec",
            "range": "stddev: 0.0008406471770269143",
            "extra": "mean: 46.981264142857526 msec\nrounds: 21"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 80.20648382864499,
            "unit": "iter/sec",
            "range": "stddev: 0.000255863934395281",
            "extra": "mean: 12.467819959997541 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 41.88616340130504,
            "unit": "iter/sec",
            "range": "stddev: 0.00040534773328026633",
            "extra": "mean: 23.87423241463178 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 121.40401238167631,
            "unit": "iter/sec",
            "range": "stddev: 0.0001623902441231705",
            "extra": "mean: 8.236960050843686 msec\nrounds: 59"
          },
          {
            "name": "equator-uint8-mask",
            "value": 46.15097520819599,
            "unit": "iter/sec",
            "range": "stddev: 0.0005158022125026448",
            "extra": "mean: 21.668014499992825 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 132.73334051591982,
            "unit": "iter/sec",
            "range": "stddev: 0.0014690600924112448",
            "extra": "mean: 7.533902153845527 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 39.91055339197922,
            "unit": "iter/sec",
            "range": "stddev: 0.000396590653170047",
            "extra": "mean: 25.056029421054554 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 136.44817054616794,
            "unit": "iter/sec",
            "range": "stddev: 0.0003443144660017008",
            "extra": "mean: 7.328790089286282 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.14651538730776,
            "unit": "iter/sec",
            "range": "stddev: 0.0004889869749849246",
            "extra": "mean: 24.90876207692357 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 128.75542077005392,
            "unit": "iter/sec",
            "range": "stddev: 0.0008191336829613504",
            "extra": "mean: 7.766663290906515 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.44715107402045,
            "unit": "iter/sec",
            "range": "stddev: 0.0005390662468481868",
            "extra": "mean: 30.819346750003973 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 111.98184610031615,
            "unit": "iter/sec",
            "range": "stddev: 0.0003690186440733082",
            "extra": "mean: 8.930018880954819 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.465584485502855,
            "unit": "iter/sec",
            "range": "stddev: 0.000668911283766957",
            "extra": "mean: 31.78075400000055 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-mask",
            "value": 112.0364554675141,
            "unit": "iter/sec",
            "range": "stddev: 0.0003654681985604231",
            "extra": "mean: 8.925666166669814 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 33.98633415888242,
            "unit": "iter/sec",
            "range": "stddev: 0.0005725989515653555",
            "extra": "mean: 29.4235911212168 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 118.62496081567737,
            "unit": "iter/sec",
            "range": "stddev: 0.00036863644129238955",
            "extra": "mean: 8.429929022727574 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.073852440084956,
            "unit": "iter/sec",
            "range": "stddev: 0.0004065857481331679",
            "extra": "mean: 38.35259873077435 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 99.14274146596576,
            "unit": "iter/sec",
            "range": "stddev: 0.0004336285640743809",
            "extra": "mean: 10.086467099997282 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.389236485293008,
            "unit": "iter/sec",
            "range": "stddev: 0.0009908278147388275",
            "extra": "mean: 39.38676929411646 msec\nrounds: 17"
          },
          {
            "name": "dateline-int64-mask",
            "value": 90.21362927898447,
            "unit": "iter/sec",
            "range": "stddev: 0.0006827708883500978",
            "extra": "mean: 11.084799580643331 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.697276192996405,
            "unit": "iter/sec",
            "range": "stddev: 0.0009445144063587234",
            "extra": "mean: 38.914630192305836 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 96.96236904359108,
            "unit": "iter/sec",
            "range": "stddev: 0.00033665073360892363",
            "extra": "mean: 10.313279366662679 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-none",
            "value": 42.52674536884767,
            "unit": "iter/sec",
            "range": "stddev: 0.0007037212121632248",
            "extra": "mean: 23.514613952389006 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-none",
            "value": 136.74710604538,
            "unit": "iter/sec",
            "range": "stddev: 0.0001247683591282626",
            "extra": "mean: 7.31276901514937 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 46.80715030521356,
            "unit": "iter/sec",
            "range": "stddev: 0.0007905371897116822",
            "extra": "mean: 21.364257244445323 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-none",
            "value": 161.85859854781987,
            "unit": "iter/sec",
            "range": "stddev: 0.00018866347042030006",
            "extra": "mean: 6.1782321666683515 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 41.086621403694444,
            "unit": "iter/sec",
            "range": "stddev: 0.00047357481753187227",
            "extra": "mean: 24.338822853662084 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-none",
            "value": 162.1434762218887,
            "unit": "iter/sec",
            "range": "stddev: 0.00038887638889508033",
            "extra": "mean: 6.167377333341051 msec\nrounds: 60"
          },
          {
            "name": "equator-int16-none",
            "value": 41.84732776639669,
            "unit": "iter/sec",
            "range": "stddev: 0.00063099938050522",
            "extra": "mean: 23.8963884523828 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 157.3223061426861,
            "unit": "iter/sec",
            "range": "stddev: 0.0007374050341576167",
            "extra": "mean: 6.356377709674769 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-none",
            "value": 32.78921532951319,
            "unit": "iter/sec",
            "range": "stddev: 0.0005319050260634368",
            "extra": "mean: 30.497832593752605 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-none",
            "value": 120.17855374108781,
            "unit": "iter/sec",
            "range": "stddev: 0.0004582006678633862",
            "extra": "mean: 8.320952190474816 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-none",
            "value": 31.815493901549726,
            "unit": "iter/sec",
            "range": "stddev: 0.00032191372793914403",
            "extra": "mean: 31.431226656245315 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 126.42528601457803,
            "unit": "iter/sec",
            "range": "stddev: 0.00022780342634912473",
            "extra": "mean: 7.909810066672031 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 35.349217720345756,
            "unit": "iter/sec",
            "range": "stddev: 0.0008902933910264573",
            "extra": "mean: 28.289169166661228 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 138.9661566453596,
            "unit": "iter/sec",
            "range": "stddev: 0.0004840214444396056",
            "extra": "mean: 7.195996666670368 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.178379345974967,
            "unit": "iter/sec",
            "range": "stddev: 0.00021138420569848527",
            "extra": "mean: 38.19946173076424 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 113.35598206462525,
            "unit": "iter/sec",
            "range": "stddev: 0.00023152168039061046",
            "extra": "mean: 8.821766454547507 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.89147394509729,
            "unit": "iter/sec",
            "range": "stddev: 0.00020839838807282357",
            "extra": "mean: 38.6227528846173 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 103.72619283115519,
            "unit": "iter/sec",
            "range": "stddev: 0.0002920686098180007",
            "extra": "mean: 9.640766451611634 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.013030056818277,
            "unit": "iter/sec",
            "range": "stddev: 0.0003871603101076222",
            "extra": "mean: 38.44227288461884 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 107.54771186194691,
            "unit": "iter/sec",
            "range": "stddev: 0.00029404899558820464",
            "extra": "mean: 9.298198749998932 msec\nrounds: 32"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "distinct": true,
          "id": "abec15162c1d8cf9dd67cb5945d8532e2b6f562c",
          "message": "update changelog",
          "timestamp": "2024-10-23T13:43:25+02:00",
          "tree_id": "d11106d395fddaf7667ea1ec42da4f85bf5dba28",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/abec15162c1d8cf9dd67cb5945d8532e2b6f562c"
        },
        "date": 1729684170425,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.10512599497154,
            "unit": "iter/sec",
            "range": "stddev: 0.00006575700333759572",
            "extra": "mean: 26.243188387094243 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.60132270598264,
            "unit": "iter/sec",
            "range": "stddev: 0.00018351264043699815",
            "extra": "mean: 12.106343666668332 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.20517066557887,
            "unit": "iter/sec",
            "range": "stddev: 0.00008128272472454214",
            "extra": "mean: 21.18411999999783 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 131.48123445403948,
            "unit": "iter/sec",
            "range": "stddev: 0.00002260234272884275",
            "extra": "mean: 7.605648092310538 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.44599736753493,
            "unit": "iter/sec",
            "range": "stddev: 0.000051224607667969914",
            "extra": "mean: 26.01051002631637 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 124.95865151693901,
            "unit": "iter/sec",
            "range": "stddev: 0.00005431643594809331",
            "extra": "mean: 8.00264717857045 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.96026055434314,
            "unit": "iter/sec",
            "range": "stddev: 0.00007772318980280992",
            "extra": "mean: 26.343338675676907 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 115.47697179401558,
            "unit": "iter/sec",
            "range": "stddev: 0.00004561192586482321",
            "extra": "mean: 8.659735222220501 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.17888931394063,
            "unit": "iter/sec",
            "range": "stddev: 0.00044512477829845555",
            "extra": "mean: 32.07298341935748 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.3763649890413,
            "unit": "iter/sec",
            "range": "stddev: 0.00012377204131572045",
            "extra": "mean: 12.139404307692285 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.26860284445048,
            "unit": "iter/sec",
            "range": "stddev: 0.001568473489974728",
            "extra": "mean: 34.16630460000268 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.09210467127495,
            "unit": "iter/sec",
            "range": "stddev: 0.0002730087744038452",
            "extra": "mean: 12.181439421054488 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.723158293581776,
            "unit": "iter/sec",
            "range": "stddev: 0.0007292084922965002",
            "extra": "mean: 29.65321312121353 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.75666673496133,
            "unit": "iter/sec",
            "range": "stddev: 0.0007490350143731727",
            "extra": "mean: 10.780896243904003 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.92322800149438,
            "unit": "iter/sec",
            "range": "stddev: 0.00025939761298702276",
            "extra": "mean: 38.57544284000255 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 78.48620208644985,
            "unit": "iter/sec",
            "range": "stddev: 0.00017625977201524175",
            "extra": "mean: 12.741092999996795 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.963325297147904,
            "unit": "iter/sec",
            "range": "stddev: 0.00032254522813962214",
            "extra": "mean: 38.51586761538018 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 76.10136426705178,
            "unit": "iter/sec",
            "range": "stddev: 0.00017542382665374252",
            "extra": "mean: 13.140368896552774 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.463319458866867,
            "unit": "iter/sec",
            "range": "stddev: 0.001257171567697859",
            "extra": "mean: 39.27217743999904 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.10610001167841,
            "unit": "iter/sec",
            "range": "stddev: 0.0005190965025892713",
            "extra": "mean: 12.969142517239764 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.45953660751709,
            "unit": "iter/sec",
            "range": "stddev: 0.00013084083079417026",
            "extra": "mean: 22.492362186044982 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.91078556135746,
            "unit": "iter/sec",
            "range": "stddev: 0.000037907761959357366",
            "extra": "mean: 9.623640073527477 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.05939019261406,
            "unit": "iter/sec",
            "range": "stddev: 0.0004826511140046877",
            "extra": "mean: 17.52559914545745 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 159.9234954747747,
            "unit": "iter/sec",
            "range": "stddev: 0.00003272089067005516",
            "extra": "mean: 6.2529898876412044 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.286635614829486,
            "unit": "iter/sec",
            "range": "stddev: 0.00008645491352279178",
            "extra": "mean: 24.22091277500016 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 117.94337177779511,
            "unit": "iter/sec",
            "range": "stddev: 0.0001432144233562012",
            "extra": "mean: 8.478645174601217 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.09661129055154,
            "unit": "iter/sec",
            "range": "stddev: 0.00007101686103468562",
            "extra": "mean: 24.332906500004015 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 108.51960938304353,
            "unit": "iter/sec",
            "range": "stddev: 0.000053444576661123975",
            "extra": "mean: 9.214924433337046 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.18880264941058,
            "unit": "iter/sec",
            "range": "stddev: 0.0007441578617594761",
            "extra": "mean: 31.066703874998325 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 111.9075786642668,
            "unit": "iter/sec",
            "range": "stddev: 0.0006725836486673062",
            "extra": "mean: 8.935945285708428 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.063404633478275,
            "unit": "iter/sec",
            "range": "stddev: 0.0007135560002442239",
            "extra": "mean: 32.19222141935659 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 110.38381875319399,
            "unit": "iter/sec",
            "range": "stddev: 0.00010658076817390103",
            "extra": "mean: 9.059298829259472 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.802755675296815,
            "unit": "iter/sec",
            "range": "stddev: 0.00015937252482304992",
            "extra": "mean: 27.93081094285656 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 146.12393678321106,
            "unit": "iter/sec",
            "range": "stddev: 0.00009811555490395442",
            "extra": "mean: 6.843505739128807 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.444963477875664,
            "unit": "iter/sec",
            "range": "stddev: 0.0002576994617611166",
            "extra": "mean: 44.55342513636589 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 99.50029154928788,
            "unit": "iter/sec",
            "range": "stddev: 0.00018594409502303873",
            "extra": "mean: 10.050221807688331 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.93966392768331,
            "unit": "iter/sec",
            "range": "stddev: 0.00031450995829267187",
            "extra": "mean: 45.579549590921815 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 89.55432512769569,
            "unit": "iter/sec",
            "range": "stddev: 0.0004072861477684514",
            "extra": "mean: 11.166406519998873 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.100087495044782,
            "unit": "iter/sec",
            "range": "stddev: 0.00037848630812797966",
            "extra": "mean: 45.24868963637439 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.96720850602043,
            "unit": "iter/sec",
            "range": "stddev: 0.0009363118580479398",
            "extra": "mean: 10.642010291663931 msec\nrounds: 24"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.483596882297356,
            "unit": "iter/sec",
            "range": "stddev: 0.0005299704411976498",
            "extra": "mean: 22.48019652381031 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.54038173101921,
            "unit": "iter/sec",
            "range": "stddev: 0.00004137894726425882",
            "extra": "mean: 7.840653967219459 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.23397305502229,
            "unit": "iter/sec",
            "range": "stddev: 0.00010644367523254881",
            "extra": "mean: 20.311178195642114 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 150.47425859201905,
            "unit": "iter/sec",
            "range": "stddev: 0.00003838855902589973",
            "extra": "mean: 6.645654940299793 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.27245744618705,
            "unit": "iter/sec",
            "range": "stddev: 0.0005099977184792638",
            "extra": "mean: 23.65606497500181 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 144.08167467248583,
            "unit": "iter/sec",
            "range": "stddev: 0.0001455284317499566",
            "extra": "mean: 6.940507890910588 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.44960857374274,
            "unit": "iter/sec",
            "range": "stddev: 0.00037798549809265356",
            "extra": "mean: 23.557343250004692 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.95390820115216,
            "unit": "iter/sec",
            "range": "stddev: 0.00007436810061881079",
            "extra": "mean: 6.946667947372868 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.92752354710158,
            "unit": "iter/sec",
            "range": "stddev: 0.000562944103213274",
            "extra": "mean: 29.47459453124246 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 123.0383840135106,
            "unit": "iter/sec",
            "range": "stddev: 0.00012466856829720731",
            "extra": "mean: 8.127544977266542 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.988586080136685,
            "unit": "iter/sec",
            "range": "stddev: 0.0006714665436860014",
            "extra": "mean: 30.31351503125279 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 120.11681772351724,
            "unit": "iter/sec",
            "range": "stddev: 0.0002249424070806641",
            "extra": "mean: 8.325228880953059 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.345737947457806,
            "unit": "iter/sec",
            "range": "stddev: 0.00011210174469007049",
            "extra": "mean: 27.51354234286347 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 133.4717768372345,
            "unit": "iter/sec",
            "range": "stddev: 0.000255426890651998",
            "extra": "mean: 7.492220630429419 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.26504077154202,
            "unit": "iter/sec",
            "range": "stddev: 0.00017475250006338629",
            "extra": "mean: 36.677003653842085 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 108.92827575436715,
            "unit": "iter/sec",
            "range": "stddev: 0.00015158750579791607",
            "extra": "mean: 9.180352787874805 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.657232735979782,
            "unit": "iter/sec",
            "range": "stddev: 0.00025105761610482325",
            "extra": "mean: 37.51327115999857 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 102.40874161013289,
            "unit": "iter/sec",
            "range": "stddev: 0.0009552054221207425",
            "extra": "mean: 9.764791406254858 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.752953805459722,
            "unit": "iter/sec",
            "range": "stddev: 0.0008962181552418712",
            "extra": "mean: 37.37905007692724 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 109.524041952768,
            "unit": "iter/sec",
            "range": "stddev: 0.0002079245690457956",
            "extra": "mean: 9.130415406247039 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.5451802271932,
            "unit": "iter/sec",
            "range": "stddev: 0.00019624604933784218",
            "extra": "mean: 22.449117837209617 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.05273144203,
            "unit": "iter/sec",
            "range": "stddev: 0.00006123947468797723",
            "extra": "mean: 7.140167776120208 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.102637333954505,
            "unit": "iter/sec",
            "range": "stddev: 0.0002880074146074678",
            "extra": "mean: 20.365504874999846 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 172.10238522540297,
            "unit": "iter/sec",
            "range": "stddev: 0.000041685097874056534",
            "extra": "mean: 5.810494716213824 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.234828053213576,
            "unit": "iter/sec",
            "range": "stddev: 0.00013170077821745272",
            "extra": "mean: 22.6066211627865 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 174.80782106134598,
            "unit": "iter/sec",
            "range": "stddev: 0.00002622210841282749",
            "extra": "mean: 5.720567843752633 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 42.59285376490579,
            "unit": "iter/sec",
            "range": "stddev: 0.0002551206856567463",
            "extra": "mean: 23.478116904764573 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.97330562640084,
            "unit": "iter/sec",
            "range": "stddev: 0.00034135047923242027",
            "extra": "mean: 5.814855953123477 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.017260071191345,
            "unit": "iter/sec",
            "range": "stddev: 0.0005875143951821409",
            "extra": "mean: 29.39684142424167 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 135.94565894505416,
            "unit": "iter/sec",
            "range": "stddev: 0.0000689869273935989",
            "extra": "mean: 7.355880340424663 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.94126638086352,
            "unit": "iter/sec",
            "range": "stddev: 0.00034200358770412306",
            "extra": "mean: 30.357060000004353 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 132.8095231299117,
            "unit": "iter/sec",
            "range": "stddev: 0.00006057164078561326",
            "extra": "mean: 7.529580533331328 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.08449645551685,
            "unit": "iter/sec",
            "range": "stddev: 0.0006643950039581106",
            "extra": "mean: 26.96544636110963 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 160.26006285033776,
            "unit": "iter/sec",
            "range": "stddev: 0.0001264066927149855",
            "extra": "mean: 6.239857780000193 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 26.825797775975595,
            "unit": "iter/sec",
            "range": "stddev: 0.0009967088503116388",
            "extra": "mean: 37.27754933333505 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 123.33313097042533,
            "unit": "iter/sec",
            "range": "stddev: 0.00014926107788464384",
            "extra": "mean: 8.108121411754276 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 25.988177016714747,
            "unit": "iter/sec",
            "range": "stddev: 0.0008842479721325482",
            "extra": "mean: 38.47903603845829 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 114.62359248219376,
            "unit": "iter/sec",
            "range": "stddev: 0.00015372294178204457",
            "extra": "mean: 8.724207454546022 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.71469667733437,
            "unit": "iter/sec",
            "range": "stddev: 0.0007480074377724356",
            "extra": "mean: 37.43257923075852 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 120.65704161076631,
            "unit": "iter/sec",
            "range": "stddev: 0.00010763799676828405",
            "extra": "mean: 8.287953911765472 msec\nrounds: 34"
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
          "id": "d3a552ed339a8c44626aa81343bd8104c17a600d",
          "message": "expand xarray capabilities (#755)\n\n* expand xarray capabilities\r\n\r\n* update changelog\r\n\r\n* update version\r\n\r\n* fix attrs encoding\r\n\r\n* refactor feature and update docs\r\n\r\n* handle 2D dataset and invalid bounds\r\n\r\n* update example with NetCDF\r\n\r\n* check if the Y bounds are inverted and flip the image on the Y axis (#756)\r\n\r\n* check if the Y bounds are inverted and flip the image on the Y axis\r\n\r\n* Update tests/test_io_xarray.py\r\n\r\nCo-authored-by: Henry Rodman <henry.rodman@gmail.com>\r\n\r\n* Update tests/test_io_xarray.py\r\n\r\nCo-authored-by: Henry Rodman <henry.rodman@gmail.com>\r\n\r\n---------\r\n\r\nCo-authored-by: Henry Rodman <henry.rodman@gmail.com>\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Henry Rodman <henry.rodman@gmail.com>",
          "timestamp": "2024-10-28T12:17:31+01:00",
          "tree_id": "d7f94f8dba0f2877a20126a56b6e652000dba202",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/d3a552ed339a8c44626aa81343bd8104c17a600d"
        },
        "date": 1730114629325,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 36.99800879676299,
            "unit": "iter/sec",
            "range": "stddev: 0.0006706832004448979",
            "extra": "mean: 27.02848160000144 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.06732796194335,
            "unit": "iter/sec",
            "range": "stddev: 0.0002875147694824636",
            "extra": "mean: 12.335425690476006 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.89918027185113,
            "unit": "iter/sec",
            "range": "stddev: 0.0005886311361646074",
            "extra": "mean: 21.78688146666698 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.4251960514505,
            "unit": "iter/sec",
            "range": "stddev: 0.00005905013330409667",
            "extra": "mean: 7.66723018461492 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.81272688479515,
            "unit": "iter/sec",
            "range": "stddev: 0.0004481878876904181",
            "extra": "mean: 27.1645184864866 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.35745929959565,
            "unit": "iter/sec",
            "range": "stddev: 0.00010453338907436476",
            "extra": "mean: 8.17277512727256 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.38748633940635,
            "unit": "iter/sec",
            "range": "stddev: 0.0004871144769512312",
            "extra": "mean: 27.481975277776627 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 108.8895805865495,
            "unit": "iter/sec",
            "range": "stddev: 0.0003081335738553395",
            "extra": "mean: 9.183615132075587 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.624429620616418,
            "unit": "iter/sec",
            "range": "stddev: 0.000787158527681837",
            "extra": "mean: 32.65366938709605 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.21270551947251,
            "unit": "iter/sec",
            "range": "stddev: 0.0003296726087736462",
            "extra": "mean: 12.466852894735476 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.63146429283453,
            "unit": "iter/sec",
            "range": "stddev: 0.0006417232127154507",
            "extra": "mean: 33.747910333335085 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.54035783152787,
            "unit": "iter/sec",
            "range": "stddev: 0.0002111369038250165",
            "extra": "mean: 12.263865729730052 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.38228446091818,
            "unit": "iter/sec",
            "range": "stddev: 0.0003598858879727622",
            "extra": "mean: 30.881082562500772 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.32645658476345,
            "unit": "iter/sec",
            "range": "stddev: 0.00016700119969482758",
            "extra": "mean: 10.715075195121686 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.10089392164894,
            "unit": "iter/sec",
            "range": "stddev: 0.00017356085410667022",
            "extra": "mean: 39.83921860000066 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.179626810613,
            "unit": "iter/sec",
            "range": "stddev: 0.000260123348479523",
            "extra": "mean: 13.126869241379437 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 24.961363827573503,
            "unit": "iter/sec",
            "range": "stddev: 0.000274208695622772",
            "extra": "mean: 40.061913560001585 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.44782480406559,
            "unit": "iter/sec",
            "range": "stddev: 0.0001815299162152813",
            "extra": "mean: 13.432225892856309 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.11779436765465,
            "unit": "iter/sec",
            "range": "stddev: 0.0009641413881830254",
            "extra": "mean: 39.81241287999978 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 75.29366137662139,
            "unit": "iter/sec",
            "range": "stddev: 0.0002917776800789136",
            "extra": "mean: 13.28133048276092 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.57196434539331,
            "unit": "iter/sec",
            "range": "stddev: 0.00046279853228549953",
            "extra": "mean: 23.489637261904015 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.03639001695696,
            "unit": "iter/sec",
            "range": "stddev: 0.00014496433019480835",
            "extra": "mean: 9.800425121212292 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 54.233514218363595,
            "unit": "iter/sec",
            "range": "stddev: 0.00033477077715477084",
            "extra": "mean: 18.438783000003305 msec\nrounds: 52"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 158.21542453989733,
            "unit": "iter/sec",
            "range": "stddev: 0.00006823331354721884",
            "extra": "mean: 6.320496265822863 msec\nrounds: 79"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.532075086039605,
            "unit": "iter/sec",
            "range": "stddev: 0.000653270321303457",
            "extra": "mean: 25.295914717948637 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.99253473185102,
            "unit": "iter/sec",
            "range": "stddev: 0.00023519817157964166",
            "extra": "mean: 8.772504290323381 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.21697982361658,
            "unit": "iter/sec",
            "range": "stddev: 0.00039576798552975106",
            "extra": "mean: 25.499158897437503 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.2693742271383,
            "unit": "iter/sec",
            "range": "stddev: 0.00022197733070865845",
            "extra": "mean: 9.322325288134365 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.84290947469138,
            "unit": "iter/sec",
            "range": "stddev: 0.0002678457260880813",
            "extra": "mean: 32.422362774191754 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 104.47846440140118,
            "unit": "iter/sec",
            "range": "stddev: 0.0010158242636099054",
            "extra": "mean: 9.571350476190469 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.02863819213045,
            "unit": "iter/sec",
            "range": "stddev: 0.0002089229845310544",
            "extra": "mean: 33.30154346666537 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 107.49301939658957,
            "unit": "iter/sec",
            "range": "stddev: 0.00021378728824918643",
            "extra": "mean: 9.302929675001081 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 33.95063686042364,
            "unit": "iter/sec",
            "range": "stddev: 0.0004100454183977975",
            "extra": "mean: 29.454528470589693 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 136.7936026994464,
            "unit": "iter/sec",
            "range": "stddev: 0.00043950822134756156",
            "extra": "mean: 7.310283377777043 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.903900404448684,
            "unit": "iter/sec",
            "range": "stddev: 0.00023006577205354417",
            "extra": "mean: 45.65396945454061 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 90.8284629779206,
            "unit": "iter/sec",
            "range": "stddev: 0.0001821733709845924",
            "extra": "mean: 11.00976464000155 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.368641199119985,
            "unit": "iter/sec",
            "range": "stddev: 0.00029715736432348174",
            "extra": "mean: 46.7975474285741 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 87.98212864769083,
            "unit": "iter/sec",
            "range": "stddev: 0.0003328102330222071",
            "extra": "mean: 11.365944600003104 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.597650967225633,
            "unit": "iter/sec",
            "range": "stddev: 0.0002572870862929992",
            "extra": "mean: 46.30133163636623 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 92.23176275458718,
            "unit": "iter/sec",
            "range": "stddev: 0.00027749476578741534",
            "extra": "mean: 10.84225184615443 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.30506714428556,
            "unit": "iter/sec",
            "range": "stddev: 0.00032014408137208915",
            "extra": "mean: 23.09198590243862 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 125.34681478994578,
            "unit": "iter/sec",
            "range": "stddev: 0.00018414673641935073",
            "extra": "mean: 7.977865266666603 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.696571220431714,
            "unit": "iter/sec",
            "range": "stddev: 0.0002825170094467141",
            "extra": "mean: 20.965867659091423 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.33264010570477,
            "unit": "iter/sec",
            "range": "stddev: 0.00017387986570221596",
            "extra": "mean: 6.880766765625879 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.11683800712171,
            "unit": "iter/sec",
            "range": "stddev: 0.0006343640819280088",
            "extra": "mean: 24.927188923077033 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.39958377482435,
            "unit": "iter/sec",
            "range": "stddev: 0.00013746878842274137",
            "extra": "mean: 7.0224924363633985 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.275780255137214,
            "unit": "iter/sec",
            "range": "stddev: 0.00043395369980742587",
            "extra": "mean: 24.227282775000702 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.93784028013317,
            "unit": "iter/sec",
            "range": "stddev: 0.00012616026042462685",
            "extra": "mean: 7.045337578945596 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.88653092918764,
            "unit": "iter/sec",
            "range": "stddev: 0.00047605073320297435",
            "extra": "mean: 30.40758546875111 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 121.23733721121432,
            "unit": "iter/sec",
            "range": "stddev: 0.00016749170385260906",
            "extra": "mean: 8.248284093025271 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.00609627343107,
            "unit": "iter/sec",
            "range": "stddev: 0.0003147544961584004",
            "extra": "mean: 31.244047741933493 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.1998223317975,
            "unit": "iter/sec",
            "range": "stddev: 0.0007256946311888705",
            "extra": "mean: 8.532436142854886 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.70788480548287,
            "unit": "iter/sec",
            "range": "stddev: 0.00036744355845863487",
            "extra": "mean: 28.811896939395975 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.2814930543339,
            "unit": "iter/sec",
            "range": "stddev: 0.00014228483050210367",
            "extra": "mean: 7.391994111111444 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.1887980832848,
            "unit": "iter/sec",
            "range": "stddev: 0.000277828117718193",
            "extra": "mean: 38.18426476922809 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.19923109627261,
            "unit": "iter/sec",
            "range": "stddev: 0.00019613806508080763",
            "extra": "mean: 8.992867937497095 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.76078669287419,
            "unit": "iter/sec",
            "range": "stddev: 0.0003264906649335118",
            "extra": "mean: 38.81869028000665 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 97.86827825247671,
            "unit": "iter/sec",
            "range": "stddev: 0.0003272122456466376",
            "extra": "mean: 10.217815392851191 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.965036027750056,
            "unit": "iter/sec",
            "range": "stddev: 0.0002659041537276953",
            "extra": "mean: 38.51332996153955 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.96200623642945,
            "unit": "iter/sec",
            "range": "stddev: 0.000284363400808565",
            "extra": "mean: 9.349114093742728 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.26271491291989,
            "unit": "iter/sec",
            "range": "stddev: 0.0019297719901768496",
            "extra": "mean: 23.114591906976276 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.6838736454741,
            "unit": "iter/sec",
            "range": "stddev: 0.00013282078893052455",
            "extra": "mean: 7.210643701490195 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 46.3021829493134,
            "unit": "iter/sec",
            "range": "stddev: 0.000908856001251167",
            "extra": "mean: 21.597253872343156 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.74191939980605,
            "unit": "iter/sec",
            "range": "stddev: 0.0002310773643868503",
            "extra": "mean: 5.92620970270384 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.237110043460454,
            "unit": "iter/sec",
            "range": "stddev: 0.0005169110618736532",
            "extra": "mean: 23.67586226829999 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-none",
            "value": 172.79402234631095,
            "unit": "iter/sec",
            "range": "stddev: 0.00006756634631103796",
            "extra": "mean: 5.78723723437502 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 41.78440113949286,
            "unit": "iter/sec",
            "range": "stddev: 0.0018019526855174981",
            "extra": "mean: 23.932376023808608 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 172.31643338989835,
            "unit": "iter/sec",
            "range": "stddev: 0.00008909644750123956",
            "extra": "mean: 5.803277031258602 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.12185364449497,
            "unit": "iter/sec",
            "range": "stddev: 0.0003106451445426473",
            "extra": "mean: 30.191546968755034 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-none",
            "value": 132.16308172675224,
            "unit": "iter/sec",
            "range": "stddev: 0.0003911037592204487",
            "extra": "mean: 7.566409521741513 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 32.00518822684925,
            "unit": "iter/sec",
            "range": "stddev: 0.0004101010764554028",
            "extra": "mean: 31.244934193547316 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-none",
            "value": 127.66198337803365,
            "unit": "iter/sec",
            "range": "stddev: 0.0005118542720393765",
            "extra": "mean: 7.833185522731479 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.27756117019985,
            "unit": "iter/sec",
            "range": "stddev: 0.000568821442963449",
            "extra": "mean: 28.346630742851175 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 161.15652854607396,
            "unit": "iter/sec",
            "range": "stddev: 0.00021065621239713553",
            "extra": "mean: 6.205147312503101 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.040053351824117,
            "unit": "iter/sec",
            "range": "stddev: 0.0006664532007213892",
            "extra": "mean: 38.402379076921115 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 115.34025374860092,
            "unit": "iter/sec",
            "range": "stddev: 0.00028536871275599743",
            "extra": "mean: 8.669999999996794 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.745982107774264,
            "unit": "iter/sec",
            "range": "stddev: 0.0007350362247484814",
            "extra": "mean: 38.841012000006 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.84936937698895,
            "unit": "iter/sec",
            "range": "stddev: 0.0002345288752684944",
            "extra": "mean: 8.783535696967316 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.021203117144378,
            "unit": "iter/sec",
            "range": "stddev: 0.0002984053424590111",
            "extra": "mean: 38.43019846154378 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.45446039288873,
            "unit": "iter/sec",
            "range": "stddev: 0.0004381777536965482",
            "extra": "mean: 8.737099424236433 msec\nrounds: 33"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "Martenz@users.noreply.github.com",
            "name": "Martino Boni",
            "username": "Martenz"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b83378301706718de3fd21ee8ba4aaf04e61f32a",
          "message": "create_cutline expose rasterio rowcol op parameter to fix pixel raste… (#759)\n\n* create_cutline expose rasterio rowcol op parameter to fix pixel raster x,y approximation\r\n\r\n* fix pydantic operator input type (got error with tox validation)\r\n\r\n* test update added op param to exists tests with default math.floor value. TODO: next need to test with specific feat and round or ceiling operators\r\n\r\n* UT create_cutline check callable operator passed rasies exception if not one of the accepted methods by rasterio.transform.rowcol\r\n\r\n* edit PR\r\n\r\n* update type\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Martino <martino.boni@generali.com>\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-10-29T21:24:48+01:00",
          "tree_id": "c963370e3a239294b9e1bc10d06f2696ada07972",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/b83378301706718de3fd21ee8ba4aaf04e61f32a"
        },
        "date": 1730233855495,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.57650717773174,
            "unit": "iter/sec",
            "range": "stddev: 0.00031413077944549684",
            "extra": "mean: 26.61237233333414 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.25849954797877,
            "unit": "iter/sec",
            "range": "stddev: 0.00007427660788201181",
            "extra": "mean: 12.156798452380375 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.95279564692513,
            "unit": "iter/sec",
            "range": "stddev: 0.0001069161801389925",
            "extra": "mean: 21.297986333333245 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.99783163031395,
            "unit": "iter/sec",
            "range": "stddev: 0.00006873525717403696",
            "extra": "mean: 7.633714142857553 msec\nrounds: 63"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.06144606156126,
            "unit": "iter/sec",
            "range": "stddev: 0.00254080278495931",
            "extra": "mean: 26.982217540539043 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 120.79764022942973,
            "unit": "iter/sec",
            "range": "stddev: 0.00021784031962376895",
            "extra": "mean: 8.278307408163853 msec\nrounds: 49"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.96161450975049,
            "unit": "iter/sec",
            "range": "stddev: 0.0006140492470547123",
            "extra": "mean: 27.05509521874916 msec\nrounds: 32"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 115.28481543834457,
            "unit": "iter/sec",
            "range": "stddev: 0.000055391171548254476",
            "extra": "mean: 8.674169240742808 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.55086741781794,
            "unit": "iter/sec",
            "range": "stddev: 0.0002887061669606853",
            "extra": "mean: 31.694849677421644 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.35396935591426,
            "unit": "iter/sec",
            "range": "stddev: 0.00025661607132238326",
            "extra": "mean: 12.291963230768925 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.44471193529858,
            "unit": "iter/sec",
            "range": "stddev: 0.00013419542847848727",
            "extra": "mean: 32.846426733325984 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.20212793554563,
            "unit": "iter/sec",
            "range": "stddev: 0.0014618785625976863",
            "extra": "mean: 12.468497105259464 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.40633809362113,
            "unit": "iter/sec",
            "range": "stddev: 0.00015338736598445463",
            "extra": "mean: 29.93443930302998 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 95.15562813222715,
            "unit": "iter/sec",
            "range": "stddev: 0.00009118938938308042",
            "extra": "mean: 10.509099878048325 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.299787939706224,
            "unit": "iter/sec",
            "range": "stddev: 0.00019192687073295935",
            "extra": "mean: 39.52602300000194 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.93491224714289,
            "unit": "iter/sec",
            "range": "stddev: 0.000276002445971393",
            "extra": "mean: 12.998000137930054 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.30254623955852,
            "unit": "iter/sec",
            "range": "stddev: 0.00036665437239731514",
            "extra": "mean: 39.52171415999942 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.95953555032193,
            "unit": "iter/sec",
            "range": "stddev: 0.000237654249355914",
            "extra": "mean: 13.340530896548561 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.680925060975973,
            "unit": "iter/sec",
            "range": "stddev: 0.0002790270241736168",
            "extra": "mean: 38.939407269233165 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.23714255302693,
            "unit": "iter/sec",
            "range": "stddev: 0.0001754990123231231",
            "extra": "mean: 12.947138733329666 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.22215891734438,
            "unit": "iter/sec",
            "range": "stddev: 0.00016267077312202122",
            "extra": "mean: 22.61309769767459 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 104.70821198927753,
            "unit": "iter/sec",
            "range": "stddev: 0.00008654115606995679",
            "extra": "mean: 9.550349308824062 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.62040971015783,
            "unit": "iter/sec",
            "range": "stddev: 0.0002830298894903375",
            "extra": "mean: 17.661475872729294 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 160.04559163026414,
            "unit": "iter/sec",
            "range": "stddev: 0.00004083600602662438",
            "extra": "mean: 6.248219584268155 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.55245558547475,
            "unit": "iter/sec",
            "range": "stddev: 0.0003148970875295432",
            "extra": "mean: 24.65941915384735 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 114.10808575181184,
            "unit": "iter/sec",
            "range": "stddev: 0.00020846708410020832",
            "extra": "mean: 8.763620854836063 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.53260049061364,
            "unit": "iter/sec",
            "range": "stddev: 0.00024915139116228396",
            "extra": "mean: 24.671498692307583 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 108.0417728530408,
            "unit": "iter/sec",
            "range": "stddev: 0.00007581551241011746",
            "extra": "mean: 9.25567929508346 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.841886533228468,
            "unit": "iter/sec",
            "range": "stddev: 0.0007366204640431002",
            "extra": "mean: 31.405174406248015 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 111.65722987169227,
            "unit": "iter/sec",
            "range": "stddev: 0.00012405390731354553",
            "extra": "mean: 8.955980738095702 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.868472846109256,
            "unit": "iter/sec",
            "range": "stddev: 0.00021573022000143682",
            "extra": "mean: 32.39551256666857 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 106.07648567031256,
            "unit": "iter/sec",
            "range": "stddev: 0.0008212621188053461",
            "extra": "mean: 9.427159975001587 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.93363571943269,
            "unit": "iter/sec",
            "range": "stddev: 0.0008976528672067499",
            "extra": "mean: 28.625706411764227 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 143.6420516515942,
            "unit": "iter/sec",
            "range": "stddev: 0.00016258003941036837",
            "extra": "mean: 6.96174963043214 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.03688244701037,
            "unit": "iter/sec",
            "range": "stddev: 0.001000265704113901",
            "extra": "mean: 45.37846959090463 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 88.00064867037582,
            "unit": "iter/sec",
            "range": "stddev: 0.0002097029631301341",
            "extra": "mean: 11.36355260000073 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.562857251519738,
            "unit": "iter/sec",
            "range": "stddev: 0.00024474235522103493",
            "extra": "mean: 46.37604322727317 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.06730105857599,
            "unit": "iter/sec",
            "range": "stddev: 0.001051987096742011",
            "extra": "mean: 11.354952269229557 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.548084605647635,
            "unit": "iter/sec",
            "range": "stddev: 0.0011496011926412006",
            "extra": "mean: 46.407837090908096 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.3338312293134,
            "unit": "iter/sec",
            "range": "stddev: 0.0005232996322118539",
            "extra": "mean: 11.450316400001839 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.15355475170776,
            "unit": "iter/sec",
            "range": "stddev: 0.00026699564874809476",
            "extra": "mean: 22.648233095237305 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.3932665536499,
            "unit": "iter/sec",
            "range": "stddev: 0.00005618572727403818",
            "extra": "mean: 7.849708442626863 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 46.76742049280068,
            "unit": "iter/sec",
            "range": "stddev: 0.0009926551860492648",
            "extra": "mean: 21.382406586951674 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.82417282039748,
            "unit": "iter/sec",
            "range": "stddev: 0.00008637662996165597",
            "extra": "mean: 6.674490378790579 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.29649639256324,
            "unit": "iter/sec",
            "range": "stddev: 0.0004170059703233103",
            "extra": "mean: 23.642620199998987 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.40248100093132,
            "unit": "iter/sec",
            "range": "stddev: 0.00012498360991650633",
            "extra": "mean: 7.022349561405886 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.53543481138693,
            "unit": "iter/sec",
            "range": "stddev: 0.0003370122307115103",
            "extra": "mean: 24.07582837500115 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.5001774337359,
            "unit": "iter/sec",
            "range": "stddev: 0.00009199116238180445",
            "extra": "mean: 7.067128947370381 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.39099600823979,
            "unit": "iter/sec",
            "range": "stddev: 0.000544531184701727",
            "extra": "mean: 29.948193212123208 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.9211249199174,
            "unit": "iter/sec",
            "range": "stddev: 0.00022793146617829525",
            "extra": "mean: 8.338814372094939 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.23014532880647,
            "unit": "iter/sec",
            "range": "stddev: 0.0003514234930202934",
            "extra": "mean: 31.026853580651586 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 114.53862616904289,
            "unit": "iter/sec",
            "range": "stddev: 0.00029240416863672244",
            "extra": "mean: 8.730679190477986 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.51273381356547,
            "unit": "iter/sec",
            "range": "stddev: 0.00023542972001123314",
            "extra": "mean: 28.974812757572483 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 129.51919173295332,
            "unit": "iter/sec",
            "range": "stddev: 0.00036739746857944954",
            "extra": "mean: 7.72086349999644 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.59601041758408,
            "unit": "iter/sec",
            "range": "stddev: 0.0001817620981611574",
            "extra": "mean: 37.59962431579006 msec\nrounds: 19"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.8237730004823,
            "unit": "iter/sec",
            "range": "stddev: 0.00017397304464162266",
            "extra": "mean: 8.863380238096852 msec\nrounds: 21"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.126587627947494,
            "unit": "iter/sec",
            "range": "stddev: 0.00035266573567368863",
            "extra": "mean: 38.27518596153386 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 105.82780353294143,
            "unit": "iter/sec",
            "range": "stddev: 0.00015564095942942563",
            "extra": "mean: 9.449312625001483 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.144644040497194,
            "unit": "iter/sec",
            "range": "stddev: 0.00038384022385951695",
            "extra": "mean: 38.24875176923552 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 107.32948964730848,
            "unit": "iter/sec",
            "range": "stddev: 0.00026178208255442874",
            "extra": "mean: 9.31710383871258 msec\nrounds: 31"
          },
          {
            "name": "equator-int8-none",
            "value": 43.82244534941783,
            "unit": "iter/sec",
            "range": "stddev: 0.00027783064489774834",
            "extra": "mean: 22.819356428572387 msec\nrounds: 35"
          },
          {
            "name": "dateline-int8-none",
            "value": 139.81806893744633,
            "unit": "iter/sec",
            "range": "stddev: 0.00006207700005792314",
            "extra": "mean: 7.1521514179071755 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 47.95940519102972,
            "unit": "iter/sec",
            "range": "stddev: 0.00046735115419875274",
            "extra": "mean: 20.850967521737303 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.92002016883313,
            "unit": "iter/sec",
            "range": "stddev: 0.00023856380110189398",
            "extra": "mean: 5.91996140540662 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.976840901922984,
            "unit": "iter/sec",
            "range": "stddev: 0.0002996253247241335",
            "extra": "mean: 23.268345904765077 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 173.46533181370577,
            "unit": "iter/sec",
            "range": "stddev: 0.00007813575155406624",
            "extra": "mean: 5.7648406718753264 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 42.538080256551865,
            "unit": "iter/sec",
            "range": "stddev: 0.00026988285772690457",
            "extra": "mean: 23.508348142861394 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 172.67522860955904,
            "unit": "iter/sec",
            "range": "stddev: 0.0000440158139423038",
            "extra": "mean: 5.791218625001093 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.40678571043189,
            "unit": "iter/sec",
            "range": "stddev: 0.0007839592910292595",
            "extra": "mean: 29.93403821211483 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 132.4837725911962,
            "unit": "iter/sec",
            "range": "stddev: 0.00048447254068925856",
            "extra": "mean: 7.5480942340439645 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 31.582990800692894,
            "unit": "iter/sec",
            "range": "stddev: 0.002582222652626369",
            "extra": "mean: 31.66261252173943 msec\nrounds: 23"
          },
          {
            "name": "dateline-int32-none",
            "value": 123.21442796599939,
            "unit": "iter/sec",
            "range": "stddev: 0.0003895615789578831",
            "extra": "mean: 8.115932659087187 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.57954235681179,
            "unit": "iter/sec",
            "range": "stddev: 0.0002549418710290215",
            "extra": "mean: 28.106038857145318 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 154.3093321005976,
            "unit": "iter/sec",
            "range": "stddev: 0.00029760680900923787",
            "extra": "mean: 6.48048945833087 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.552898743086683,
            "unit": "iter/sec",
            "range": "stddev: 0.00015710606860424808",
            "extra": "mean: 37.66067161538663 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 121.29586325229978,
            "unit": "iter/sec",
            "range": "stddev: 0.00020892323453543802",
            "extra": "mean: 8.24430424242881 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.95471760878556,
            "unit": "iter/sec",
            "range": "stddev: 0.0006460121361886871",
            "extra": "mean: 38.5286411153826 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 112.22016355071982,
            "unit": "iter/sec",
            "range": "stddev: 0.0005044155150783496",
            "extra": "mean: 8.911054558818504 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.429080186916323,
            "unit": "iter/sec",
            "range": "stddev: 0.00017188515409255202",
            "extra": "mean: 37.83710946153353 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.51407924086517,
            "unit": "iter/sec",
            "range": "stddev: 0.00021793494922577348",
            "extra": "mean: 8.5096186470587 msec\nrounds: 34"
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
          "id": "03cb853d084724cd1934095ba3cc84e996b2d81d",
          "message": "Patch/2d xarray point (#761)\n\n* fix point method for 2D dataarray\r\n\r\n* add more tests",
          "timestamp": "2024-10-29T21:49:18+01:00",
          "tree_id": "5f2d62c65be881e651d07ef2bd84bae2ff5db534",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/03cb853d084724cd1934095ba3cc84e996b2d81d"
        },
        "date": 1730235328900,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 35.89052862716072,
            "unit": "iter/sec",
            "range": "stddev: 0.0006888244097856858",
            "extra": "mean: 27.862504071428873 msec\nrounds: 28"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 80.6575092611649,
            "unit": "iter/sec",
            "range": "stddev: 0.00018198596596231061",
            "extra": "mean: 12.398101666666287 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.78369870837594,
            "unit": "iter/sec",
            "range": "stddev: 0.0005495868264364689",
            "extra": "mean: 21.841835155556232 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 124.82858227009658,
            "unit": "iter/sec",
            "range": "stddev: 0.0006058605211383517",
            "extra": "mean: 8.010985800000999 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.05556756567806,
            "unit": "iter/sec",
            "range": "stddev: 0.0005742076290865542",
            "extra": "mean: 26.98649799999903 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 118.21104371306724,
            "unit": "iter/sec",
            "range": "stddev: 0.0003724880567679909",
            "extra": "mean: 8.459446500001237 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.68770185475634,
            "unit": "iter/sec",
            "range": "stddev: 0.00017225454264042944",
            "extra": "mean: 26.53385456756886 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.55414142896201,
            "unit": "iter/sec",
            "range": "stddev: 0.00012168119752939291",
            "extra": "mean: 8.729496703706044 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.482849855155077,
            "unit": "iter/sec",
            "range": "stddev: 0.0004994187196173947",
            "extra": "mean: 31.76332525806134 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.16192962169472,
            "unit": "iter/sec",
            "range": "stddev: 0.00015592159736105643",
            "extra": "mean: 12.17108707894747 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.175141044899704,
            "unit": "iter/sec",
            "range": "stddev: 0.0004839387424531071",
            "extra": "mean: 33.1398616666623 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.25899274879525,
            "unit": "iter/sec",
            "range": "stddev: 0.0003632797832358255",
            "extra": "mean: 12.30633024324346 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.896895110591124,
            "unit": "iter/sec",
            "range": "stddev: 0.0011549980649479485",
            "extra": "mean: 30.398005545454982 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.57960016005572,
            "unit": "iter/sec",
            "range": "stddev: 0.00026725716379686",
            "extra": "mean: 10.80151565000449 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.354324941608574,
            "unit": "iter/sec",
            "range": "stddev: 0.0003586916779690685",
            "extra": "mean: 39.44100276000313 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.41478315666686,
            "unit": "iter/sec",
            "range": "stddev: 0.0012122943601262557",
            "extra": "mean: 13.438190068963594 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.38294156092817,
            "unit": "iter/sec",
            "range": "stddev: 0.0010345630547673394",
            "extra": "mean: 39.39653714285404 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.97967619621143,
            "unit": "iter/sec",
            "range": "stddev: 0.0002689470007967828",
            "extra": "mean: 13.517225965517417 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.245698047276555,
            "unit": "iter/sec",
            "range": "stddev: 0.0003576857154260373",
            "extra": "mean: 39.61070904545171 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.3419385966251,
            "unit": "iter/sec",
            "range": "stddev: 0.00018574781017527604",
            "extra": "mean: 13.098960000004608 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.651746282885235,
            "unit": "iter/sec",
            "range": "stddev: 0.0005438983332033613",
            "extra": "mean: 22.908590953486666 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.7159674477203,
            "unit": "iter/sec",
            "range": "stddev: 0.0003968027550124238",
            "extra": "mean: 9.928912220587867 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.549030747663615,
            "unit": "iter/sec",
            "range": "stddev: 0.0005756742306678947",
            "extra": "mean: 17.68376905454416 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.39736969106406,
            "unit": "iter/sec",
            "range": "stddev: 0.0002307131621107893",
            "extra": "mean: 6.393969425287183 msec\nrounds: 87"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.22334025767671,
            "unit": "iter/sec",
            "range": "stddev: 0.0007837768662904354",
            "extra": "mean: 24.861187399998386 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 110.62674009063352,
            "unit": "iter/sec",
            "range": "stddev: 0.0002351046751299672",
            "extra": "mean: 9.039405836063928 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.39334354363078,
            "unit": "iter/sec",
            "range": "stddev: 0.0002892642375319806",
            "extra": "mean: 24.756554230769538 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 109.03805695694219,
            "unit": "iter/sec",
            "range": "stddev: 0.00006533573771700887",
            "extra": "mean: 9.1711098666669 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.436360385164,
            "unit": "iter/sec",
            "range": "stddev: 0.0005324185674126501",
            "extra": "mean: 31.810298258062268 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 107.00624619919762,
            "unit": "iter/sec",
            "range": "stddev: 0.0005087556884848541",
            "extra": "mean: 9.345248857141002 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.380001289104516,
            "unit": "iter/sec",
            "range": "stddev: 0.0009154584142379813",
            "extra": "mean: 32.91639096666662 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 103.08883391071834,
            "unit": "iter/sec",
            "range": "stddev: 0.0006038682625675591",
            "extra": "mean: 9.700371631578113 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.99396802080232,
            "unit": "iter/sec",
            "range": "stddev: 0.0003697425206823117",
            "extra": "mean: 28.576353484850465 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 131.73637079076215,
            "unit": "iter/sec",
            "range": "stddev: 0.0004955973316423569",
            "extra": "mean: 7.590918088887595 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.85235918968858,
            "unit": "iter/sec",
            "range": "stddev: 0.0012113484021122338",
            "extra": "mean: 45.761649409088406 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 93.98812716672629,
            "unit": "iter/sec",
            "range": "stddev: 0.00047798105272343135",
            "extra": "mean: 10.639641730769803 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.476322658354597,
            "unit": "iter/sec",
            "range": "stddev: 0.0006513689769648162",
            "extra": "mean: 46.56290631818132 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 86.84445161740055,
            "unit": "iter/sec",
            "range": "stddev: 0.0008646469886902414",
            "extra": "mean: 11.514840400001276 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.689508012433688,
            "unit": "iter/sec",
            "range": "stddev: 0.00034476988399435117",
            "extra": "mean: 46.10524127272697 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 89.36162622402279,
            "unit": "iter/sec",
            "range": "stddev: 0.0001928396623643411",
            "extra": "mean: 11.190485695650572 msec\nrounds: 23"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.4566412298195,
            "unit": "iter/sec",
            "range": "stddev: 0.00011450109205114639",
            "extra": "mean: 22.49382707142629 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.1109801974315,
            "unit": "iter/sec",
            "range": "stddev: 0.00009249983975769247",
            "extra": "mean: 7.9295236499982975 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.208385796330134,
            "unit": "iter/sec",
            "range": "stddev: 0.0009877043551088246",
            "extra": "mean: 20.74327906818496 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 146.9121729046748,
            "unit": "iter/sec",
            "range": "stddev: 0.0004003674260997896",
            "extra": "mean: 6.806787893940268 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.638449200475854,
            "unit": "iter/sec",
            "range": "stddev: 0.0004795107236601254",
            "extra": "mean: 24.016264275005028 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 141.8175222645832,
            "unit": "iter/sec",
            "range": "stddev: 0.0003993118897028913",
            "extra": "mean: 7.051314844821083 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.06814749413083,
            "unit": "iter/sec",
            "range": "stddev: 0.0002892788080257981",
            "extra": "mean: 23.77095402500231 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.09206066866787,
            "unit": "iter/sec",
            "range": "stddev: 0.000137799542658262",
            "extra": "mean: 7.0875710175382585 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.52456221090091,
            "unit": "iter/sec",
            "range": "stddev: 0.0004954646180137626",
            "extra": "mean: 29.82887572726716 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.38203866011598,
            "unit": "iter/sec",
            "range": "stddev: 0.000546724654463071",
            "extra": "mean: 8.376469452385782 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.715010761822697,
            "unit": "iter/sec",
            "range": "stddev: 0.00040425281023006025",
            "extra": "mean: 31.530810678574994 msec\nrounds: 28"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.20025672221165,
            "unit": "iter/sec",
            "range": "stddev: 0.0002498769908983739",
            "extra": "mean: 8.460218511624303 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.01604689718557,
            "unit": "iter/sec",
            "range": "stddev: 0.0006635411903397267",
            "extra": "mean: 28.558335066668405 msec\nrounds: 30"
          },
          {
            "name": "dateline-float32-mask",
            "value": 136.45725763850055,
            "unit": "iter/sec",
            "range": "stddev: 0.00017179210499259552",
            "extra": "mean: 7.32830204348073 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.542012499688568,
            "unit": "iter/sec",
            "range": "stddev: 0.0004063708424110347",
            "extra": "mean: 37.67611819230865 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 108.05412193242044,
            "unit": "iter/sec",
            "range": "stddev: 0.00022245749539773118",
            "extra": "mean: 9.254621500005555 msec\nrounds: 20"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.890174552695793,
            "unit": "iter/sec",
            "range": "stddev: 0.0003727638039837829",
            "extra": "mean: 38.624691307686675 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 100.99931531621007,
            "unit": "iter/sec",
            "range": "stddev: 0.0004804552445252793",
            "extra": "mean: 9.901057218746345 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 24.870988562437407,
            "unit": "iter/sec",
            "range": "stddev: 0.005127387779482027",
            "extra": "mean: 40.20748903846538 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.00915442715461,
            "unit": "iter/sec",
            "range": "stddev: 0.0002959341626543254",
            "extra": "mean: 9.433147593750135 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.496572811874564,
            "unit": "iter/sec",
            "range": "stddev: 0.00024373015809952184",
            "extra": "mean: 22.473640930232165 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.73350940203318,
            "unit": "iter/sec",
            "range": "stddev: 0.00009548854383389639",
            "extra": "mean: 7.208063893937255 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.334429640437,
            "unit": "iter/sec",
            "range": "stddev: 0.0007872314619715517",
            "extra": "mean: 20.689185895831724 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.12513861249388,
            "unit": "iter/sec",
            "range": "stddev: 0.00014732177866857106",
            "extra": "mean: 5.947950486481782 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.77808021829679,
            "unit": "iter/sec",
            "range": "stddev: 0.00027672309124751956",
            "extra": "mean: 22.842481785714664 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 172.8882194295529,
            "unit": "iter/sec",
            "range": "stddev: 0.00005258056178617143",
            "extra": "mean: 5.784084093754416 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.57723202636208,
            "unit": "iter/sec",
            "range": "stddev: 0.0002870288454533098",
            "extra": "mean: 22.947763166670363 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.62019530019688,
            "unit": "iter/sec",
            "range": "stddev: 0.00013162692916687097",
            "extra": "mean: 5.826820079366573 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.420866516653014,
            "unit": "iter/sec",
            "range": "stddev: 0.0005819144424187074",
            "extra": "mean: 29.921426468751733 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-none",
            "value": 132.49929593541708,
            "unit": "iter/sec",
            "range": "stddev: 0.00020929326837085672",
            "extra": "mean: 7.547209914892083 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.4867585241299,
            "unit": "iter/sec",
            "range": "stddev: 0.0007026847037796705",
            "extra": "mean: 30.781772187497225 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 131.93439057554974,
            "unit": "iter/sec",
            "range": "stddev: 0.00008728261501014556",
            "extra": "mean: 7.579524911113822 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.74517269664231,
            "unit": "iter/sec",
            "range": "stddev: 0.0003313745294710753",
            "extra": "mean: 27.214459114281908 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 154.79598541481332,
            "unit": "iter/sec",
            "range": "stddev: 0.00029291772485723247",
            "extra": "mean: 6.460115857140984 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.505729609572832,
            "unit": "iter/sec",
            "range": "stddev: 0.00037765524139855616",
            "extra": "mean: 37.72769188888274 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 117.38529839634194,
            "unit": "iter/sec",
            "range": "stddev: 0.00023301364718338415",
            "extra": "mean: 8.518954363634032 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 26.057831317641586,
            "unit": "iter/sec",
            "range": "stddev: 0.00024220768575577276",
            "extra": "mean: 38.37617903846754 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 108.52692462068113,
            "unit": "iter/sec",
            "range": "stddev: 0.0012995678054186241",
            "extra": "mean: 9.214303303029723 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.167705409608235,
            "unit": "iter/sec",
            "range": "stddev: 0.000549191639984577",
            "extra": "mean: 38.21504347999962 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-none",
            "value": 107.50234778613905,
            "unit": "iter/sec",
            "range": "stddev: 0.0005205848473460618",
            "extra": "mean: 9.30212242424101 msec\nrounds: 33"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "distinct": true,
          "id": "9a39c802044b485a26c29065b539ec44c817d8a6",
          "message": "update changelog",
          "timestamp": "2024-10-29T22:00:59+01:00",
          "tree_id": "4562e35a5a33df9a03bee5ec0bd6f1494823e4dd",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/9a39c802044b485a26c29065b539ec44c817d8a6"
        },
        "date": 1730236103799,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.19191905525372,
            "unit": "iter/sec",
            "range": "stddev: 0.0006339258382052458",
            "extra": "mean: 26.887561206894496 msec\nrounds: 29"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.5957637413761,
            "unit": "iter/sec",
            "range": "stddev: 0.0004907150203875887",
            "extra": "mean: 12.56348269047605 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.78686857370987,
            "unit": "iter/sec",
            "range": "stddev: 0.000456490720704202",
            "extra": "mean: 21.37351847825765 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 131.03961219824345,
            "unit": "iter/sec",
            "range": "stddev: 0.000045256641520924444",
            "extra": "mean: 7.63128021538364 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.46229547787581,
            "unit": "iter/sec",
            "range": "stddev: 0.0006677708770476997",
            "extra": "mean: 26.69350575675674 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.94992175255109,
            "unit": "iter/sec",
            "range": "stddev: 0.0008540342159185927",
            "extra": "mean: 8.133392732145037 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.55319447637983,
            "unit": "iter/sec",
            "range": "stddev: 0.0004564549472913767",
            "extra": "mean: 27.357390081082688 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.53249206381791,
            "unit": "iter/sec",
            "range": "stddev: 0.0007172362731784731",
            "extra": "mean: 8.808051173913178 msec\nrounds: 46"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.737147868179186,
            "unit": "iter/sec",
            "range": "stddev: 0.0008295235137117748",
            "extra": "mean: 32.533922935486665 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.7290694132234,
            "unit": "iter/sec",
            "range": "stddev: 0.00016292720835767976",
            "extra": "mean: 12.235548589743326 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.34293036763271,
            "unit": "iter/sec",
            "range": "stddev: 0.0003072899015025071",
            "extra": "mean: 32.95660596666418 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.72008219905544,
            "unit": "iter/sec",
            "range": "stddev: 0.0006654843095272033",
            "extra": "mean: 12.088962842101948 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.10525450404362,
            "unit": "iter/sec",
            "range": "stddev: 0.001894633310248413",
            "extra": "mean: 31.147549379309584 msec\nrounds: 29"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 94.31053524127181,
            "unit": "iter/sec",
            "range": "stddev: 0.0001350766102558286",
            "extra": "mean: 10.603269268292562 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.294222855557614,
            "unit": "iter/sec",
            "range": "stddev: 0.0009149635637761313",
            "extra": "mean: 39.534719279990895 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.9069860377732,
            "unit": "iter/sec",
            "range": "stddev: 0.0002481772971132092",
            "extra": "mean: 13.002719928575093 msec\nrounds: 28"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.551729411209244,
            "unit": "iter/sec",
            "range": "stddev: 0.0001593209515684906",
            "extra": "mean: 39.136294217381305 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.673454336059,
            "unit": "iter/sec",
            "range": "stddev: 0.0002563445499342988",
            "extra": "mean: 13.391639758616481 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.612126246367595,
            "unit": "iter/sec",
            "range": "stddev: 0.00029036104427058453",
            "extra": "mean: 39.04400557692174 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.28728954607284,
            "unit": "iter/sec",
            "range": "stddev: 0.0004762764112896564",
            "extra": "mean: 13.108343551727073 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.64073302406512,
            "unit": "iter/sec",
            "range": "stddev: 0.0007087752125654225",
            "extra": "mean: 22.914372209297284 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.65116984138756,
            "unit": "iter/sec",
            "range": "stddev: 0.0003751716085823058",
            "extra": "mean: 9.647744463764878 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.86808750602336,
            "unit": "iter/sec",
            "range": "stddev: 0.00046505144623223656",
            "extra": "mean: 17.899306109094677 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 159.8902045103612,
            "unit": "iter/sec",
            "range": "stddev: 0.000052773922821926945",
            "extra": "mean: 6.25429183146237 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.689024482015235,
            "unit": "iter/sec",
            "range": "stddev: 0.00024458791930988304",
            "extra": "mean: 24.576652124997622 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 116.92904917346249,
            "unit": "iter/sec",
            "range": "stddev: 0.00009956971084987333",
            "extra": "mean: 8.552194746033681 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.86080606521567,
            "unit": "iter/sec",
            "range": "stddev: 0.000800306220670173",
            "extra": "mean: 25.087300000002884 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.26021111442101,
            "unit": "iter/sec",
            "range": "stddev: 0.00007274801852848426",
            "extra": "mean: 9.323121683335483 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.630155085858156,
            "unit": "iter/sec",
            "range": "stddev: 0.0007706231645013182",
            "extra": "mean: 31.615399838715934 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 110.04532966263355,
            "unit": "iter/sec",
            "range": "stddev: 0.00021601185397790998",
            "extra": "mean: 9.087164380948328 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.592621573015894,
            "unit": "iter/sec",
            "range": "stddev: 0.00046303571720721873",
            "extra": "mean: 32.68762036667188 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 106.6519177019323,
            "unit": "iter/sec",
            "range": "stddev: 0.0004902368108326395",
            "extra": "mean: 9.376296474994206 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.73821837002108,
            "unit": "iter/sec",
            "range": "stddev: 0.0004884187672906906",
            "extra": "mean: 28.78673826470604 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 143.37152118773358,
            "unit": "iter/sec",
            "range": "stddev: 0.000184412706467493",
            "extra": "mean: 6.974885888882909 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.12198532960879,
            "unit": "iter/sec",
            "range": "stddev: 0.00037995561646189056",
            "extra": "mean: 45.20389942857285 msec\nrounds: 21"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 88.12546449169021,
            "unit": "iter/sec",
            "range": "stddev: 0.0002102945642946319",
            "extra": "mean: 11.347457920001034 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.53231023224156,
            "unit": "iter/sec",
            "range": "stddev: 0.00032019292122171573",
            "extra": "mean: 46.441835047622654 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 84.78141341599317,
            "unit": "iter/sec",
            "range": "stddev: 0.0002429714657767196",
            "extra": "mean: 11.795038083327825 msec\nrounds: 24"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.702084055177203,
            "unit": "iter/sec",
            "range": "stddev: 0.00039648182662349065",
            "extra": "mean: 46.07852395454353 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 88.69064513316474,
            "unit": "iter/sec",
            "range": "stddev: 0.00038522523329680554",
            "extra": "mean: 11.275146307691731 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.866870481899596,
            "unit": "iter/sec",
            "range": "stddev: 0.0007623748407351406",
            "extra": "mean: 22.796246666664338 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.92350345608934,
            "unit": "iter/sec",
            "range": "stddev: 0.00004569638627647163",
            "extra": "mean: 7.817171770496867 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.807911536309746,
            "unit": "iter/sec",
            "range": "stddev: 0.001678185115967065",
            "extra": "mean: 20.917040043477062 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 150.2363025320076,
            "unit": "iter/sec",
            "range": "stddev: 0.000042271376427006864",
            "extra": "mean: 6.656180850743127 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.93195713762481,
            "unit": "iter/sec",
            "range": "stddev: 0.000652147303303357",
            "extra": "mean: 24.43078880000087 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 141.81597814907443,
            "unit": "iter/sec",
            "range": "stddev: 0.00015670829554629065",
            "extra": "mean: 7.051391620687605 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.155300779632576,
            "unit": "iter/sec",
            "range": "stddev: 0.0005584426945159496",
            "extra": "mean: 24.298206575005565 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 142.9682266610081,
            "unit": "iter/sec",
            "range": "stddev: 0.00013120976812980447",
            "extra": "mean: 6.994561122808774 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.65716053586128,
            "unit": "iter/sec",
            "range": "stddev: 0.00045479330331608654",
            "extra": "mean: 29.711359606063994 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 122.02740682301582,
            "unit": "iter/sec",
            "range": "stddev: 0.00010226288626389599",
            "extra": "mean: 8.194880363641294 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.020730063641416,
            "unit": "iter/sec",
            "range": "stddev: 0.0005060767996513407",
            "extra": "mean: 31.2297689032228 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.19521873087494,
            "unit": "iter/sec",
            "range": "stddev: 0.0005331276964783483",
            "extra": "mean: 8.5327713095223 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.87162755952006,
            "unit": "iter/sec",
            "range": "stddev: 0.0005233660199034561",
            "extra": "mean: 28.676608176465713 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.28657900146806,
            "unit": "iter/sec",
            "range": "stddev: 0.0002674508764043765",
            "extra": "mean: 7.391716217387304 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.276093101131817,
            "unit": "iter/sec",
            "range": "stddev: 0.0004296466984061539",
            "extra": "mean: 38.057408160002524 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.65684874201024,
            "unit": "iter/sec",
            "range": "stddev: 0.00021093479593389022",
            "extra": "mean: 8.876513156248933 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.967539199725756,
            "unit": "iter/sec",
            "range": "stddev: 0.00039042318450286295",
            "extra": "mean: 38.509617423069535 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 99.2148727062195,
            "unit": "iter/sec",
            "range": "stddev: 0.0002889557054782657",
            "extra": "mean: 10.079134032264024 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.233369589938878,
            "unit": "iter/sec",
            "range": "stddev: 0.00031885305575386796",
            "extra": "mean: 38.119388230764066 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 108.43668408289086,
            "unit": "iter/sec",
            "range": "stddev: 0.00020897808022641792",
            "extra": "mean: 9.221971406240925 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.30556059359558,
            "unit": "iter/sec",
            "range": "stddev: 0.00035285047329207186",
            "extra": "mean: 22.570530348837323 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.35100096937117,
            "unit": "iter/sec",
            "range": "stddev: 0.0000508217793250732",
            "extra": "mean: 7.124993716419809 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.05308747992802,
            "unit": "iter/sec",
            "range": "stddev: 0.0006232236357691284",
            "extra": "mean: 20.810317347822952 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.1700381104201,
            "unit": "iter/sec",
            "range": "stddev: 0.000055884037129498954",
            "extra": "mean: 5.876475148645845 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.56642212492307,
            "unit": "iter/sec",
            "range": "stddev: 0.000244102893048591",
            "extra": "mean: 22.953457071424953 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 174.67491070981305,
            "unit": "iter/sec",
            "range": "stddev: 0.00004035771015164836",
            "extra": "mean: 5.724920630767044 msec\nrounds: 65"
          },
          {
            "name": "equator-int16-none",
            "value": 43.434178550564404,
            "unit": "iter/sec",
            "range": "stddev: 0.0002584210405522042",
            "extra": "mean: 23.023343214280853 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.8696846747336,
            "unit": "iter/sec",
            "range": "stddev: 0.0001346611132366304",
            "extra": "mean: 5.818361754095946 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.710328157370796,
            "unit": "iter/sec",
            "range": "stddev: 0.0004404142974693714",
            "extra": "mean: 29.664499121209207 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 135.1840699805927,
            "unit": "iter/sec",
            "range": "stddev: 0.00011823272911132939",
            "extra": "mean: 7.397321297868617 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.714398150600225,
            "unit": "iter/sec",
            "range": "stddev: 0.000256291982183605",
            "extra": "mean: 30.567580531254634 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 125.33815557826405,
            "unit": "iter/sec",
            "range": "stddev: 0.0005730540073031193",
            "extra": "mean: 7.978416431822925 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.01891116532021,
            "unit": "iter/sec",
            "range": "stddev: 0.00022557476796441461",
            "extra": "mean: 28.555999222223566 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 150.0887859401736,
            "unit": "iter/sec",
            "range": "stddev: 0.00026171100750814854",
            "extra": "mean: 6.662722959186349 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.232582152037086,
            "unit": "iter/sec",
            "range": "stddev: 0.0010102862250123117",
            "extra": "mean: 38.12053248148678 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 122.39972766731653,
            "unit": "iter/sec",
            "range": "stddev: 0.00020527022205127168",
            "extra": "mean: 8.169952818179532 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 26.078990053160208,
            "unit": "iter/sec",
            "range": "stddev: 0.00022339175522945954",
            "extra": "mean: 38.34504319230037 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.64187393674767,
            "unit": "iter/sec",
            "range": "stddev: 0.0002515599531421018",
            "extra": "mean: 8.799573303029073 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.356057314429897,
            "unit": "iter/sec",
            "range": "stddev: 0.0003762850520833842",
            "extra": "mean: 37.94194207691685 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 118.87219593461747,
            "unit": "iter/sec",
            "range": "stddev: 0.00016596637984122816",
            "extra": "mean: 8.412396121209232 msec\nrounds: 33"
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
          "id": "9fd71073deee89cc55bbd6ddb0522eeaa8c38a26",
          "message": "add kwargs to xarrayReader methods for compatibility (#762)\n\n* add kwargs to xarrayReader methods for compatibility\r\n\r\n* add netcdf backend\r\n\r\n* add get_asset_list method\r\n\r\n* add STAC+netcdf example",
          "timestamp": "2024-11-05T14:54:46+01:00",
          "tree_id": "ce96491a0804bfa8f89a5b769d6dbec392e650c5",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/9fd71073deee89cc55bbd6ddb0522eeaa8c38a26"
        },
        "date": 1730815258366,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.745276164853394,
            "unit": "iter/sec",
            "range": "stddev: 0.00016582673502734375",
            "extra": "mean: 26.493381466662907 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.60023675259515,
            "unit": "iter/sec",
            "range": "stddev: 0.00020113725156198332",
            "extra": "mean: 12.254866404761954 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.82383574101002,
            "unit": "iter/sec",
            "range": "stddev: 0.000056256417192380575",
            "extra": "mean: 21.35664420000012 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 127.93776703910196,
            "unit": "iter/sec",
            "range": "stddev: 0.000035042299483987517",
            "extra": "mean: 7.816300246153018 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.05250887914544,
            "unit": "iter/sec",
            "range": "stddev: 0.0002380578965224164",
            "extra": "mean: 26.27947616216304 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 116.83593589313267,
            "unit": "iter/sec",
            "range": "stddev: 0.001343718080004578",
            "extra": "mean: 8.559010482140346 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.56472798584276,
            "unit": "iter/sec",
            "range": "stddev: 0.0006427768997364971",
            "extra": "mean: 26.620717189190774 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 109.94248358970222,
            "unit": "iter/sec",
            "range": "stddev: 0.00015196295650737694",
            "extra": "mean: 9.095665000000649 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.646095030713596,
            "unit": "iter/sec",
            "range": "stddev: 0.0009257526287072342",
            "extra": "mean: 31.599475354841296 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.46636073693897,
            "unit": "iter/sec",
            "range": "stddev: 0.0001467142834714214",
            "extra": "mean: 12.275005179488447 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.480419988394576,
            "unit": "iter/sec",
            "range": "stddev: 0.0006984070524242562",
            "extra": "mean: 32.80794688461478 msec\nrounds: 26"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.3460391761899,
            "unit": "iter/sec",
            "range": "stddev: 0.00013410579499356653",
            "extra": "mean: 12.143874921055666 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.62552296043672,
            "unit": "iter/sec",
            "range": "stddev: 0.0005277060384378243",
            "extra": "mean: 29.73931442424211 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.40964089925836,
            "unit": "iter/sec",
            "range": "stddev: 0.00030491793106796126",
            "extra": "mean: 10.705533073170605 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.55329901640298,
            "unit": "iter/sec",
            "range": "stddev: 0.0008694478376517524",
            "extra": "mean: 39.133890280002106 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.56604675635315,
            "unit": "iter/sec",
            "range": "stddev: 0.0006324207227562152",
            "extra": "mean: 13.410929551723868 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.76522921428927,
            "unit": "iter/sec",
            "range": "stddev: 0.00029354997411179404",
            "extra": "mean: 38.811997040003234 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.5200994672957,
            "unit": "iter/sec",
            "range": "stddev: 0.000873893376637452",
            "extra": "mean: 13.601722620694153 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 24.850450015695266,
            "unit": "iter/sec",
            "range": "stddev: 0.005210798708841409",
            "extra": "mean: 40.24071996154642 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.74484365607064,
            "unit": "iter/sec",
            "range": "stddev: 0.0010013440047108835",
            "extra": "mean: 13.378849310346798 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.85532907979711,
            "unit": "iter/sec",
            "range": "stddev: 0.00037601101938468487",
            "extra": "mean: 22.802245952377795 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.92785614330396,
            "unit": "iter/sec",
            "range": "stddev: 0.00004207431532595066",
            "extra": "mean: 9.908067388057216 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.43045112166562,
            "unit": "iter/sec",
            "range": "stddev: 0.0004106141959265335",
            "extra": "mean: 17.72092868518758 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 152.69142229557434,
            "unit": "iter/sec",
            "range": "stddev: 0.0003102696266217751",
            "extra": "mean: 6.549156363638014 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.76801031571319,
            "unit": "iter/sec",
            "range": "stddev: 0.00017710428269106603",
            "extra": "mean: 24.529036179491214 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 108.63537734859203,
            "unit": "iter/sec",
            "range": "stddev: 0.0004569573767970235",
            "extra": "mean: 9.205104491800807 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.45617448746756,
            "unit": "iter/sec",
            "range": "stddev: 0.0004927774401476821",
            "extra": "mean: 24.71810576923872 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.24789902527547,
            "unit": "iter/sec",
            "range": "stddev: 0.0004332270872455472",
            "extra": "mean: 9.41195081666611 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.459349124642195,
            "unit": "iter/sec",
            "range": "stddev: 0.0011090926913609976",
            "extra": "mean: 31.787053064511664 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 107.93962172119993,
            "unit": "iter/sec",
            "range": "stddev: 0.0007559662642212838",
            "extra": "mean: 9.264438619054328 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.73050261391126,
            "unit": "iter/sec",
            "range": "stddev: 0.0001768554431334234",
            "extra": "mean: 32.54095816666904 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 106.86457530063512,
            "unit": "iter/sec",
            "range": "stddev: 0.0001318431108221926",
            "extra": "mean: 9.357637899994131 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.33629181422493,
            "unit": "iter/sec",
            "range": "stddev: 0.0007386863237372023",
            "extra": "mean: 28.29951725714019 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 140.70689719725584,
            "unit": "iter/sec",
            "range": "stddev: 0.00012159414374111768",
            "extra": "mean: 7.106972152176082 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.5997279675284,
            "unit": "iter/sec",
            "range": "stddev: 0.003426036908540835",
            "extra": "mean: 46.29687936363522 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 96.13422503048143,
            "unit": "iter/sec",
            "range": "stddev: 0.00013620584561910648",
            "extra": "mean: 10.402122653851201 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.59520529258424,
            "unit": "iter/sec",
            "range": "stddev: 0.0001888054132655325",
            "extra": "mean: 46.30657529999951 msec\nrounds: 20"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.58567619589863,
            "unit": "iter/sec",
            "range": "stddev: 0.0006190378095096566",
            "extra": "mean: 11.288506708337328 msec\nrounds: 24"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.710890016045305,
            "unit": "iter/sec",
            "range": "stddev: 0.0006214966315010702",
            "extra": "mean: 46.059834454550504 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 85.78995441505155,
            "unit": "iter/sec",
            "range": "stddev: 0.0019971295789171406",
            "extra": "mean: 11.656376399992041 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.01038206169911,
            "unit": "iter/sec",
            "range": "stddev: 0.00019791746112142797",
            "extra": "mean: 22.721911357144734 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.93257608708107,
            "unit": "iter/sec",
            "range": "stddev: 0.00012925492447403677",
            "extra": "mean: 8.068903524585426 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.76002224626351,
            "unit": "iter/sec",
            "range": "stddev: 0.00009204130341017533",
            "extra": "mean: 20.50860426087337 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 144.18967895342413,
            "unit": "iter/sec",
            "range": "stddev: 0.0005120404933582237",
            "extra": "mean: 6.935309151517134 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.859476648542646,
            "unit": "iter/sec",
            "range": "stddev: 0.0006403429010779964",
            "extra": "mean: 23.889453000001026 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 137.8327394773991,
            "unit": "iter/sec",
            "range": "stddev: 0.0001098869179042712",
            "extra": "mean: 7.255170315786792 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.67636376804951,
            "unit": "iter/sec",
            "range": "stddev: 0.0003145477765304394",
            "extra": "mean: 23.99441576922393 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 138.34712706780516,
            "unit": "iter/sec",
            "range": "stddev: 0.00045715455968791497",
            "extra": "mean: 7.228194912279537 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.207783172890416,
            "unit": "iter/sec",
            "range": "stddev: 0.000837187024467542",
            "extra": "mean: 31.04839580644312 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.09636843573516,
            "unit": "iter/sec",
            "range": "stddev: 0.00018911110081711177",
            "extra": "mean: 8.396561651160704 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.599497370218245,
            "unit": "iter/sec",
            "range": "stddev: 0.0002471363178213691",
            "extra": "mean: 30.675319580649877 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.28658735178448,
            "unit": "iter/sec",
            "range": "stddev: 0.000056891411217244895",
            "extra": "mean: 8.454043880951597 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.71199755807921,
            "unit": "iter/sec",
            "range": "stddev: 0.0002702735688500031",
            "extra": "mean: 28.001794029406444 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 132.3914952474199,
            "unit": "iter/sec",
            "range": "stddev: 0.00006742188184421587",
            "extra": "mean: 7.553355282611995 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.866002511789233,
            "unit": "iter/sec",
            "range": "stddev: 0.0010239372174001458",
            "extra": "mean: 37.221763809527815 msec\nrounds: 21"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.9914731515561,
            "unit": "iter/sec",
            "range": "stddev: 0.00013506483234678756",
            "extra": "mean: 9.091613843757784 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.759613782862974,
            "unit": "iter/sec",
            "range": "stddev: 0.000855017289814632",
            "extra": "mean: 38.82045780768915 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.73203316002039,
            "unit": "iter/sec",
            "range": "stddev: 0.00009107007251685604",
            "extra": "mean: 9.548177093746446 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.656259762120722,
            "unit": "iter/sec",
            "range": "stddev: 0.00030813950834958055",
            "extra": "mean: 37.51464042307344 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 104.24184532898511,
            "unit": "iter/sec",
            "range": "stddev: 0.00016073798237269953",
            "extra": "mean: 9.593076531253075 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.61649052010384,
            "unit": "iter/sec",
            "range": "stddev: 0.00007300592054555182",
            "extra": "mean: 22.413237534884278 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 136.49361856988926,
            "unit": "iter/sec",
            "range": "stddev: 0.000029375648844582984",
            "extra": "mean: 7.326349835820103 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.24224398675074,
            "unit": "iter/sec",
            "range": "stddev: 0.00006604625439253037",
            "extra": "mean: 20.30776664583082 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.42865908658086,
            "unit": "iter/sec",
            "range": "stddev: 0.00003509506816740054",
            "extra": "mean: 5.902189189191324 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.91589537784455,
            "unit": "iter/sec",
            "range": "stddev: 0.000056870533846290134",
            "extra": "mean: 22.770798395345874 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 167.14222459926532,
            "unit": "iter/sec",
            "range": "stddev: 0.00004880043855505793",
            "extra": "mean: 5.982928624993278 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.653776550075584,
            "unit": "iter/sec",
            "range": "stddev: 0.00029349806470197035",
            "extra": "mean: 22.907525511633395 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 168.1707212193809,
            "unit": "iter/sec",
            "range": "stddev: 0.000044713184778272724",
            "extra": "mean: 5.946338296875631 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.00675996576924,
            "unit": "iter/sec",
            "range": "stddev: 0.00017195786206600008",
            "extra": "mean: 29.40591814705626 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.92797420636228,
            "unit": "iter/sec",
            "range": "stddev: 0.00010139825882453606",
            "extra": "mean: 7.696571936169173 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.70719436788926,
            "unit": "iter/sec",
            "range": "stddev: 0.0006890350954792914",
            "extra": "mean: 30.574313062503577 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 127.21826711161624,
            "unit": "iter/sec",
            "range": "stddev: 0.00011202785659829986",
            "extra": "mean: 7.860506377772304 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.52268035166755,
            "unit": "iter/sec",
            "range": "stddev: 0.00014147694744791003",
            "extra": "mean: 27.38024674999906 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 154.8433954382973,
            "unit": "iter/sec",
            "range": "stddev: 0.00010705595576610763",
            "extra": "mean: 6.458137895836084 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 27.04376596556432,
            "unit": "iter/sec",
            "range": "stddev: 0.0002575397398866964",
            "extra": "mean: 36.97709857692644 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 120.33061953506476,
            "unit": "iter/sec",
            "range": "stddev: 0.00011920104932106562",
            "extra": "mean: 8.31043672727536 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 26.286051861016173,
            "unit": "iter/sec",
            "range": "stddev: 0.0004426937607380732",
            "extra": "mean: 38.04298969230375 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 111.44559762375624,
            "unit": "iter/sec",
            "range": "stddev: 0.0007959073609476956",
            "extra": "mean: 8.972987909096515 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.536067220913495,
            "unit": "iter/sec",
            "range": "stddev: 0.0004426640478483262",
            "extra": "mean: 37.684559346152255 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 116.47358599124472,
            "unit": "iter/sec",
            "range": "stddev: 0.00013350175675046615",
            "extra": "mean: 8.58563760606778 msec\nrounds: 33"
          }
        ]
      }
    ]
  }
}