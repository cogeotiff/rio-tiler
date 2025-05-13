window.BENCHMARK_DATA = {
  "lastUpdate": 1747148018259,
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
          "id": "dd5ce03f8f463ec93f3a8787d7155d318397cd7c",
          "message": "Bump version: 7.1.0 → 7.2.0",
          "timestamp": "2024-11-05T14:55:12+01:00",
          "tree_id": "fa3213751eebab87f7e57dc18c7dad6461b2b397",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/dd5ce03f8f463ec93f3a8787d7155d318397cd7c"
        },
        "date": 1730815317598,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 35.72403208374352,
            "unit": "iter/sec",
            "range": "stddev: 0.00032850885389582084",
            "extra": "mean: 27.99236093103436 msec\nrounds: 29"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 77.08668408153945,
            "unit": "iter/sec",
            "range": "stddev: 0.00019256682862915563",
            "extra": "mean: 12.972409073170626 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 42.22804009488993,
            "unit": "iter/sec",
            "range": "stddev: 0.0009723400785854378",
            "extra": "mean: 23.68094748780471 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 118.70163621020025,
            "unit": "iter/sec",
            "range": "stddev: 0.00017422966933760127",
            "extra": "mean: 8.424483704918536 msec\nrounds: 61"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 35.524424020409604,
            "unit": "iter/sec",
            "range": "stddev: 0.0005388167230013235",
            "extra": "mean: 28.14964711111085 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 110.3396347746846,
            "unit": "iter/sec",
            "range": "stddev: 0.0003833011322111903",
            "extra": "mean: 9.062926500001717 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 35.182000074950246,
            "unit": "iter/sec",
            "range": "stddev: 0.00043848733438887503",
            "extra": "mean: 28.423625657144058 msec\nrounds: 35"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 101.5235928676132,
            "unit": "iter/sec",
            "range": "stddev: 0.0004391367240452185",
            "extra": "mean: 9.849927211539885 msec\nrounds: 52"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.061375589067325,
            "unit": "iter/sec",
            "range": "stddev: 0.000231970760232453",
            "extra": "mean: 33.26527746666651 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 74.320322671694,
            "unit": "iter/sec",
            "range": "stddev: 0.0002569506298713307",
            "extra": "mean: 13.455269891890081 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.327470002152744,
            "unit": "iter/sec",
            "range": "stddev: 0.0004983881309599597",
            "extra": "mean: 34.09772475861696 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 76.64390640706164,
            "unit": "iter/sec",
            "range": "stddev: 0.0003061789901871934",
            "extra": "mean: 13.04735166666641 msec\nrounds: 36"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.065441847217876,
            "unit": "iter/sec",
            "range": "stddev: 0.0002296441132932145",
            "extra": "mean: 31.186222375001016 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 83.7087571688292,
            "unit": "iter/sec",
            "range": "stddev: 0.00022994865645187222",
            "extra": "mean: 11.94618142499877 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 24.630665923116997,
            "unit": "iter/sec",
            "range": "stddev: 0.00028322372719714433",
            "extra": "mean: 40.599795520000725 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 71.75854123854631,
            "unit": "iter/sec",
            "range": "stddev: 0.0002738138236973097",
            "extra": "mean: 13.93562331034167 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 24.632654625629677,
            "unit": "iter/sec",
            "range": "stddev: 0.00041364858048937594",
            "extra": "mean: 40.59651771999938 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 69.14317483882245,
            "unit": "iter/sec",
            "range": "stddev: 0.00019044642753350733",
            "extra": "mean: 14.462743464283635 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 24.933941586000167,
            "unit": "iter/sec",
            "range": "stddev: 0.00015282255136320644",
            "extra": "mean: 40.10597348000033 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 71.63478549878293,
            "unit": "iter/sec",
            "range": "stddev: 0.00016914718962197342",
            "extra": "mean: 13.959698392856776 msec\nrounds: 28"
          },
          {
            "name": "equator-int8-alpha",
            "value": 41.51458536636115,
            "unit": "iter/sec",
            "range": "stddev: 0.00031195495765998487",
            "extra": "mean: 24.08791973170687 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 95.50579974396238,
            "unit": "iter/sec",
            "range": "stddev: 0.00019042469590114597",
            "extra": "mean: 10.470568307692929 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 53.13307504596407,
            "unit": "iter/sec",
            "range": "stddev: 0.001687330209245842",
            "extra": "mean: 18.820668653845566 msec\nrounds: 52"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 145.0951477796616,
            "unit": "iter/sec",
            "range": "stddev: 0.0001470235043746308",
            "extra": "mean: 6.892029232559718 msec\nrounds: 86"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 38.02919409960781,
            "unit": "iter/sec",
            "range": "stddev: 0.00050261892490254",
            "extra": "mean: 26.29558747368546 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 95.77308716276589,
            "unit": "iter/sec",
            "range": "stddev: 0.00046591817213173406",
            "extra": "mean: 10.441346620690057 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-alpha",
            "value": 38.09381527691525,
            "unit": "iter/sec",
            "range": "stddev: 0.000574928774273276",
            "extra": "mean: 26.250980447369294 msec\nrounds: 38"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.14267246246212,
            "unit": "iter/sec",
            "range": "stddev: 0.0002428071703551369",
            "extra": "mean: 9.790227491526663 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.333745645293682,
            "unit": "iter/sec",
            "range": "stddev: 0.0002815571831504903",
            "extra": "mean: 32.966584862069325 msec\nrounds: 29"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 92.81188424667582,
            "unit": "iter/sec",
            "range": "stddev: 0.0006390326589939312",
            "extra": "mean: 10.774482256412291 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-alpha",
            "value": 29.177771760135332,
            "unit": "iter/sec",
            "range": "stddev: 0.0010648235206794925",
            "extra": "mean: 34.27266510344935 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 92.13931319642846,
            "unit": "iter/sec",
            "range": "stddev: 0.0003352428978636457",
            "extra": "mean: 10.853130605262232 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 33.20973913791303,
            "unit": "iter/sec",
            "range": "stddev: 0.00048700715454458104",
            "extra": "mean: 30.111648750001052 msec\nrounds: 24"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 121.81792274872474,
            "unit": "iter/sec",
            "range": "stddev: 0.0006158633977605316",
            "extra": "mean: 8.208972681817205 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.634627913409247,
            "unit": "iter/sec",
            "range": "stddev: 0.00040208580912873054",
            "extra": "mean: 46.22219545454698 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 79.2259607786672,
            "unit": "iter/sec",
            "range": "stddev: 0.00035418811481590523",
            "extra": "mean: 12.622125250000948 msec\nrounds: 24"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.007220370703838,
            "unit": "iter/sec",
            "range": "stddev: 0.000951384013011997",
            "extra": "mean: 47.602680523815316 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 82.10045461548594,
            "unit": "iter/sec",
            "range": "stddev: 0.0003768567493800422",
            "extra": "mean: 12.1802005200027 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.30832567569505,
            "unit": "iter/sec",
            "range": "stddev: 0.0013045577112788856",
            "extra": "mean: 46.93001295454347 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 79.89993868609777,
            "unit": "iter/sec",
            "range": "stddev: 0.00010698843539315449",
            "extra": "mean: 12.515654159994938 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.08231494109251,
            "unit": "iter/sec",
            "range": "stddev: 0.00015866778945354586",
            "extra": "mean: 22.684834073172127 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.35264242142861,
            "unit": "iter/sec",
            "range": "stddev: 0.00013619058953175204",
            "extra": "mean: 8.106838900001396 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 46.8281176209597,
            "unit": "iter/sec",
            "range": "stddev: 0.0007932142624467015",
            "extra": "mean: 21.3546913863651 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 144.84786926761535,
            "unit": "iter/sec",
            "range": "stddev: 0.00003526824906752777",
            "extra": "mean: 6.903795030304785 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 39.84206006694488,
            "unit": "iter/sec",
            "range": "stddev: 0.002537476684709917",
            "extra": "mean: 25.099103769226378 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 131.61296081748125,
            "unit": "iter/sec",
            "range": "stddev: 0.0002632293719568183",
            "extra": "mean: 7.598035890908829 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.19040010371953,
            "unit": "iter/sec",
            "range": "stddev: 0.0004094026640698456",
            "extra": "mean: 24.88156369230701 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 134.45156281968954,
            "unit": "iter/sec",
            "range": "stddev: 0.0009832498690313645",
            "extra": "mean: 7.437622732143926 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.50929945646353,
            "unit": "iter/sec",
            "range": "stddev: 0.0003821328263639344",
            "extra": "mean: 29.84246212903482 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 112.11421466145153,
            "unit": "iter/sec",
            "range": "stddev: 0.0003070875808235529",
            "extra": "mean: 8.91947558139416 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.926303911993074,
            "unit": "iter/sec",
            "range": "stddev: 0.00048069156012569354",
            "extra": "mean: 31.322134962962352 msec\nrounds: 27"
          },
          {
            "name": "dateline-int32-mask",
            "value": 98.40699041465082,
            "unit": "iter/sec",
            "range": "stddev: 0.0004107681547951675",
            "extra": "mean: 10.161879717958737 msec\nrounds: 39"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.09514513990557,
            "unit": "iter/sec",
            "range": "stddev: 0.0004024341804840971",
            "extra": "mean: 28.493969636356685 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 124.84592556255588,
            "unit": "iter/sec",
            "range": "stddev: 0.00022072212164819214",
            "extra": "mean: 8.009872933329612 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 25.721766669646378,
            "unit": "iter/sec",
            "range": "stddev: 0.0009600472268771309",
            "extra": "mean: 38.877578388893305 msec\nrounds: 18"
          },
          {
            "name": "dateline-float64-mask",
            "value": 104.96944909893223,
            "unit": "iter/sec",
            "range": "stddev: 0.00022027863069610016",
            "extra": "mean: 9.526581387099727 msec\nrounds: 31"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.426876548822648,
            "unit": "iter/sec",
            "range": "stddev: 0.00021065257049115478",
            "extra": "mean: 39.32846404000429 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 95.59662760802918,
            "unit": "iter/sec",
            "range": "stddev: 0.00018407023920980598",
            "extra": "mean: 10.460620055555284 msec\nrounds: 18"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.037088534621116,
            "unit": "iter/sec",
            "range": "stddev: 0.0004982829111234135",
            "extra": "mean: 39.94074624999655 msec\nrounds: 16"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 90.23678312363532,
            "unit": "iter/sec",
            "range": "stddev: 0.0001324717958123217",
            "extra": "mean: 11.081955333335399 msec\nrounds: 18"
          },
          {
            "name": "equator-int8-none",
            "value": 41.09878630704392,
            "unit": "iter/sec",
            "range": "stddev: 0.0003869745672196733",
            "extra": "mean: 24.33161876190514 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-none",
            "value": 128.31825220796694,
            "unit": "iter/sec",
            "range": "stddev: 0.0002123859823515757",
            "extra": "mean: 7.793123603174457 msec\nrounds: 63"
          },
          {
            "name": "equator-uint8-none",
            "value": 47.317475084936476,
            "unit": "iter/sec",
            "range": "stddev: 0.0003328565724724383",
            "extra": "mean: 21.133841106376998 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 164.64863897006458,
            "unit": "iter/sec",
            "range": "stddev: 0.0000791157969942583",
            "extra": "mean: 6.073539424652116 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 41.91929081918168,
            "unit": "iter/sec",
            "range": "stddev: 0.00033414030217647993",
            "extra": "mean: 23.855365404760473 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 160.13203971459367,
            "unit": "iter/sec",
            "range": "stddev: 0.00010948526479397844",
            "extra": "mean: 6.244846451605304 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-none",
            "value": 41.501110428512625,
            "unit": "iter/sec",
            "range": "stddev: 0.00035900968074304394",
            "extra": "mean: 24.095740804876563 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-none",
            "value": 159.81182445857,
            "unit": "iter/sec",
            "range": "stddev: 0.00010514304043191279",
            "extra": "mean: 6.257359262294403 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-none",
            "value": 32.4777944152593,
            "unit": "iter/sec",
            "range": "stddev: 0.00019525836184759496",
            "extra": "mean: 30.790268181824626 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 121.50273808856797,
            "unit": "iter/sec",
            "range": "stddev: 0.0003355489978773926",
            "extra": "mean: 8.230267199995625 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-none",
            "value": 31.401713545780634,
            "unit": "iter/sec",
            "range": "stddev: 0.00038493158693546787",
            "extra": "mean: 31.845395906248797 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 111.20191871028398,
            "unit": "iter/sec",
            "range": "stddev: 0.00019325693339886953",
            "extra": "mean: 8.992650590906754 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 34.880642869941425,
            "unit": "iter/sec",
            "range": "stddev: 0.00016500032893045313",
            "extra": "mean: 28.66919637142798 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 143.9044300459317,
            "unit": "iter/sec",
            "range": "stddev: 0.00014465447066984373",
            "extra": "mean: 6.949056395837279 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 26.14694223322091,
            "unit": "iter/sec",
            "range": "stddev: 0.0002445609723928978",
            "extra": "mean: 38.24538988461349 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 110.05237465888415,
            "unit": "iter/sec",
            "range": "stddev: 0.00042602816907975834",
            "extra": "mean: 9.086582666658284 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.491443934596525,
            "unit": "iter/sec",
            "range": "stddev: 0.0006403630437911121",
            "extra": "mean: 39.228848807690255 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 109.74740026199818,
            "unit": "iter/sec",
            "range": "stddev: 0.0002647502339132325",
            "extra": "mean: 9.111833151516267 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 25.654493187336694,
            "unit": "iter/sec",
            "range": "stddev: 0.0008683349165409932",
            "extra": "mean: 38.97952661538485 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 109.8565828833813,
            "unit": "iter/sec",
            "range": "stddev: 0.0002894708661750723",
            "extra": "mean: 9.102777218744862 msec\nrounds: 32"
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
          "id": "f83010d1f6e85247d50e80be11271907628987df",
          "message": "add floating point values support in colormap Keys (#765)",
          "timestamp": "2024-11-14T20:37:07+01:00",
          "tree_id": "e0617f46e9778b405187c7a2a954feeef2e79230",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/f83010d1f6e85247d50e80be11271907628987df"
        },
        "date": 1731613396362,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 36.125954948221725,
            "unit": "iter/sec",
            "range": "stddev: 0.0008436103849483996",
            "extra": "mean: 27.68092916666897 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 77.64198415681741,
            "unit": "iter/sec",
            "range": "stddev: 0.00016298912105831593",
            "extra": "mean: 12.879629634145486 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 44.838419017753466,
            "unit": "iter/sec",
            "range": "stddev: 0.0002391610251085619",
            "extra": "mean: 22.302302844443663 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 126.96361581048147,
            "unit": "iter/sec",
            "range": "stddev: 0.00006750810361335363",
            "extra": "mean: 7.87627221874887 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.0649811388551,
            "unit": "iter/sec",
            "range": "stddev: 0.0004928901651191417",
            "extra": "mean: 26.97964410810675 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 119.11138880631464,
            "unit": "iter/sec",
            "range": "stddev: 0.00024763249822024085",
            "extra": "mean: 8.395502814815517 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.19010548036985,
            "unit": "iter/sec",
            "range": "stddev: 0.0003207454075906864",
            "extra": "mean: 26.88887237837582 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.75479718854334,
            "unit": "iter/sec",
            "range": "stddev: 0.00020504250937664696",
            "extra": "mean: 8.948161735848204 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.634525394327085,
            "unit": "iter/sec",
            "range": "stddev: 0.0016908991021199076",
            "extra": "mean: 32.64290819355016 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.07308886118841,
            "unit": "iter/sec",
            "range": "stddev: 0.00023733775753002182",
            "extra": "mean: 12.488590289473672 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.064541113764676,
            "unit": "iter/sec",
            "range": "stddev: 0.000647404428979329",
            "extra": "mean: 33.261774933333754 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.69645199707048,
            "unit": "iter/sec",
            "range": "stddev: 0.00014505050244435365",
            "extra": "mean: 12.240433648646803 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.730799646760886,
            "unit": "iter/sec",
            "range": "stddev: 0.0009317510989537819",
            "extra": "mean: 30.552263030303394 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 91.85111492546474,
            "unit": "iter/sec",
            "range": "stddev: 0.00016982771747340062",
            "extra": "mean: 10.887184121950824 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.197475741878012,
            "unit": "iter/sec",
            "range": "stddev: 0.00021967510344439298",
            "extra": "mean: 39.68651503999695 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.11995209159764,
            "unit": "iter/sec",
            "range": "stddev: 0.00015408742733350578",
            "extra": "mean: 12.966813034482575 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.319844364139698,
            "unit": "iter/sec",
            "range": "stddev: 0.0002682452184128126",
            "extra": "mean: 39.49471353845651 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.50066082515535,
            "unit": "iter/sec",
            "range": "stddev: 0.0001376681616239349",
            "extra": "mean: 13.422699730770002 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.5821623187222,
            "unit": "iter/sec",
            "range": "stddev: 0.0009728685737592204",
            "extra": "mean: 39.0897371199992 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.96321903807309,
            "unit": "iter/sec",
            "range": "stddev: 0.00013949630278221848",
            "extra": "mean: 13.339875379312483 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.54239635390087,
            "unit": "iter/sec",
            "range": "stddev: 0.0006656306396180792",
            "extra": "mean: 22.966122302325058 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.57042820463535,
            "unit": "iter/sec",
            "range": "stddev: 0.000028781620932931223",
            "extra": "mean: 9.749398705881665 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.187243444145565,
            "unit": "iter/sec",
            "range": "stddev: 0.0007976087219148164",
            "extra": "mean: 18.120129537038565 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 148.10381522920048,
            "unit": "iter/sec",
            "range": "stddev: 0.00039734637278559945",
            "extra": "mean: 6.752020523255486 msec\nrounds: 86"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.207668691119,
            "unit": "iter/sec",
            "range": "stddev: 0.0003196550139074397",
            "extra": "mean: 24.870877435897654 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 112.52614189800462,
            "unit": "iter/sec",
            "range": "stddev: 0.00006931489287632933",
            "extra": "mean: 8.886823836068379 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.57745862524081,
            "unit": "iter/sec",
            "range": "stddev: 0.00020714792193680516",
            "extra": "mean: 24.644224500002565 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 97.6316282278674,
            "unit": "iter/sec",
            "range": "stddev: 0.0007854743590555575",
            "extra": "mean: 10.242582431034023 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.416976135169392,
            "unit": "iter/sec",
            "range": "stddev: 0.00107264876296199",
            "extra": "mean: 31.829925187502717 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 105.85938649666171,
            "unit": "iter/sec",
            "range": "stddev: 0.000282121306278468",
            "extra": "mean: 9.446493439025694 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.717569551191588,
            "unit": "iter/sec",
            "range": "stddev: 0.00039245610219426673",
            "extra": "mean: 32.55465893333375 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 105.84009239758359,
            "unit": "iter/sec",
            "range": "stddev: 0.00013166220646573088",
            "extra": "mean: 9.44821548571164 msec\nrounds: 35"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.559109624627084,
            "unit": "iter/sec",
            "range": "stddev: 0.0009713094884980257",
            "extra": "mean: 28.935930666668348 msec\nrounds: 27"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 132.57491203403046,
            "unit": "iter/sec",
            "range": "stddev: 0.00015579925430163862",
            "extra": "mean: 7.542905250001685 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.911312407328758,
            "unit": "iter/sec",
            "range": "stddev: 0.0010922533612088775",
            "extra": "mean: 45.63852595454421 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 87.96731115768827,
            "unit": "iter/sec",
            "range": "stddev: 0.00021534184718893781",
            "extra": "mean: 11.367859115386873 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.399187570875366,
            "unit": "iter/sec",
            "range": "stddev: 0.00019060721129888415",
            "extra": "mean: 46.73074604762172 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 86.249533860067,
            "unit": "iter/sec",
            "range": "stddev: 0.00031447529647841185",
            "extra": "mean: 11.594265560001986 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.73141251933356,
            "unit": "iter/sec",
            "range": "stddev: 0.0015273976523321664",
            "extra": "mean: 46.0163369090868 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 89.71689051899858,
            "unit": "iter/sec",
            "range": "stddev: 0.00026966175606476335",
            "extra": "mean: 11.146173192306955 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.47161759105636,
            "unit": "iter/sec",
            "range": "stddev: 0.00008069047308483991",
            "extra": "mean: 22.48625199999716 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 124.37988217798795,
            "unit": "iter/sec",
            "range": "stddev: 0.00009259924292551866",
            "extra": "mean: 8.039885409836593 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.94674739659237,
            "unit": "iter/sec",
            "range": "stddev: 0.00006741116127279538",
            "extra": "mean: 20.430366739131255 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.52087399107705,
            "unit": "iter/sec",
            "range": "stddev: 0.000027678624954338857",
            "extra": "mean: 6.871866369228358 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.376777774958406,
            "unit": "iter/sec",
            "range": "stddev: 0.00007812271093675196",
            "extra": "mean: 23.59783004999798 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 140.84674513095334,
            "unit": "iter/sec",
            "range": "stddev: 0.00003268783295857715",
            "extra": "mean: 7.099915578952445 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.46735164416619,
            "unit": "iter/sec",
            "range": "stddev: 0.00006685287253655805",
            "extra": "mean: 23.547500875001504 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 140.76602544707075,
            "unit": "iter/sec",
            "range": "stddev: 0.00003836363298821859",
            "extra": "mean: 7.103986894735539 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.957126082474375,
            "unit": "iter/sec",
            "range": "stddev: 0.0009558567317265237",
            "extra": "mean: 29.448899696965533 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 120.08076752506199,
            "unit": "iter/sec",
            "range": "stddev: 0.00009399296231167656",
            "extra": "mean: 8.327728249998824 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.63180585864,
            "unit": "iter/sec",
            "range": "stddev: 0.0010109083433611362",
            "extra": "mean: 30.644948193549872 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 116.60787394836332,
            "unit": "iter/sec",
            "range": "stddev: 0.00009517659347994506",
            "extra": "mean: 8.575750214285042 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.96757504490832,
            "unit": "iter/sec",
            "range": "stddev: 0.00014521363389961855",
            "extra": "mean: 27.802819588238076 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 133.62401406461302,
            "unit": "iter/sec",
            "range": "stddev: 0.00008155907570832447",
            "extra": "mean: 7.483684777770981 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.732764262559954,
            "unit": "iter/sec",
            "range": "stddev: 0.00015950784033179946",
            "extra": "mean: 37.40728007692532 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.50813633479422,
            "unit": "iter/sec",
            "range": "stddev: 0.0001390650377286376",
            "extra": "mean: 9.131741562496742 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.215756488589076,
            "unit": "iter/sec",
            "range": "stddev: 0.000181814160646351",
            "extra": "mean: 38.144998807692986 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.10670161323142,
            "unit": "iter/sec",
            "range": "stddev: 0.00016598333808315544",
            "extra": "mean: 9.605529562497495 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.469850837351704,
            "unit": "iter/sec",
            "range": "stddev: 0.0001580002406501509",
            "extra": "mean: 37.7788301923068 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.60937976115359,
            "unit": "iter/sec",
            "range": "stddev: 0.0001407483779673549",
            "extra": "mean: 9.38003768749418 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.25324285420753,
            "unit": "iter/sec",
            "range": "stddev: 0.000681455994177804",
            "extra": "mean: 22.59721402326387 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 133.70671541368657,
            "unit": "iter/sec",
            "range": "stddev: 0.000264768799029555",
            "extra": "mean: 7.479055909091888 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.700980156648455,
            "unit": "iter/sec",
            "range": "stddev: 0.00037397545529744446",
            "extra": "mean: 20.533467638299353 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.03948447798805,
            "unit": "iter/sec",
            "range": "stddev: 0.00006312730477052736",
            "extra": "mean: 5.8809870135159805 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.10774520317204,
            "unit": "iter/sec",
            "range": "stddev: 0.000374268447947778",
            "extra": "mean: 23.19768745237958 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 165.46168085590654,
            "unit": "iter/sec",
            "range": "stddev: 0.00009137056517618297",
            "extra": "mean: 6.04369540323271 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-none",
            "value": 43.48588109969642,
            "unit": "iter/sec",
            "range": "stddev: 0.00023867019119609725",
            "extra": "mean: 22.995969604649016 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 165.9864624867233,
            "unit": "iter/sec",
            "range": "stddev: 0.00008443282724603717",
            "extra": "mean: 6.02458769840936 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.616106726023936,
            "unit": "iter/sec",
            "range": "stddev: 0.00032406221357345467",
            "extra": "mean: 29.74764472727739 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 126.08435557810837,
            "unit": "iter/sec",
            "range": "stddev: 0.00015636631607497467",
            "extra": "mean: 7.931198088889839 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-none",
            "value": 31.78596005184814,
            "unit": "iter/sec",
            "range": "stddev: 0.000782479168179154",
            "extra": "mean: 31.46043090625028 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 122.12924349350492,
            "unit": "iter/sec",
            "range": "stddev: 0.00016541340454753723",
            "extra": "mean: 8.188047116276309 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-none",
            "value": 35.7256925998469,
            "unit": "iter/sec",
            "range": "stddev: 0.000938554473360271",
            "extra": "mean: 27.99105985713725 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 151.7497663298539,
            "unit": "iter/sec",
            "range": "stddev: 0.00053511279940667",
            "extra": "mean: 6.589795979166979 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 25.94505821045426,
            "unit": "iter/sec",
            "range": "stddev: 0.002819006608638737",
            "extra": "mean: 38.54298540741225 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 116.72195453800101,
            "unit": "iter/sec",
            "range": "stddev: 0.0003873757096058569",
            "extra": "mean: 8.567368529409189 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.071729402291933,
            "unit": "iter/sec",
            "range": "stddev: 0.00036974634609377637",
            "extra": "mean: 38.355721807702224 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 110.41291227207248,
            "unit": "iter/sec",
            "range": "stddev: 0.00021180131181844925",
            "extra": "mean: 9.056911727279358 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.162564706238143,
            "unit": "iter/sec",
            "range": "stddev: 0.00020270757247582846",
            "extra": "mean: 38.22255238461244 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 100.40096311172843,
            "unit": "iter/sec",
            "range": "stddev: 0.0006793428186245799",
            "extra": "mean: 9.96006381818447 msec\nrounds: 33"
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
          "id": "4663e21c85693a828e9d638e83d725923997e931",
          "message": "cast data to uint8 (#766)",
          "timestamp": "2024-11-14T22:56:50+01:00",
          "tree_id": "d93c3f4ca29d4264aa9fab8d4f060a39011956d3",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/4663e21c85693a828e9d638e83d725923997e931"
        },
        "date": 1731621780873,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 35.91443562889362,
            "unit": "iter/sec",
            "range": "stddev: 0.0010085091291762384",
            "extra": "mean: 27.843956962962473 msec\nrounds: 27"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 78.90762075828907,
            "unit": "iter/sec",
            "range": "stddev: 0.00040887232352148235",
            "extra": "mean: 12.673047170731635 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.12884319891692,
            "unit": "iter/sec",
            "range": "stddev: 0.0006949163594685959",
            "extra": "mean: 22.158777604651736 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 124.1285075673283,
            "unit": "iter/sec",
            "range": "stddev: 0.0003233828039190827",
            "extra": "mean: 8.056167109377288 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 35.88881412107833,
            "unit": "iter/sec",
            "range": "stddev: 0.0009428222410329248",
            "extra": "mean: 27.863835138890163 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 117.81228272154664,
            "unit": "iter/sec",
            "range": "stddev: 0.00018549968130922116",
            "extra": "mean: 8.488079314815877 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 35.31998752953281,
            "unit": "iter/sec",
            "range": "stddev: 0.0010025894251474406",
            "extra": "mean: 28.31258077777774 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 104.96704704654925,
            "unit": "iter/sec",
            "range": "stddev: 0.0006938076717429146",
            "extra": "mean: 9.526799392160996 msec\nrounds: 51"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.20341111418542,
            "unit": "iter/sec",
            "range": "stddev: 0.0009262669657061449",
            "extra": "mean: 33.10884311111261 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 75.77974303913905,
            "unit": "iter/sec",
            "range": "stddev: 0.0006353567121924918",
            "extra": "mean: 13.196138702707342 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.316998252362612,
            "unit": "iter/sec",
            "range": "stddev: 0.0007288865622477582",
            "extra": "mean: 34.10990413793171 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 77.00545899607143,
            "unit": "iter/sec",
            "range": "stddev: 0.0006591090422204765",
            "extra": "mean: 12.986092324324913 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.00254845893911,
            "unit": "iter/sec",
            "range": "stddev: 0.0006810533868351426",
            "extra": "mean: 31.247511468752265 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 84.74699690213077,
            "unit": "iter/sec",
            "range": "stddev: 0.0008821894629471475",
            "extra": "mean: 11.799828153849981 msec\nrounds: 39"
          },
          {
            "name": "equator-float64-nodata",
            "value": 24.764132206757584,
            "unit": "iter/sec",
            "range": "stddev: 0.0003777611717428252",
            "extra": "mean: 40.38098293333784 msec\nrounds: 15"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 69.0444602635766,
            "unit": "iter/sec",
            "range": "stddev: 0.0009677873547863489",
            "extra": "mean: 14.483421206893487 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 24.582337288982366,
            "unit": "iter/sec",
            "range": "stddev: 0.0007832466622537715",
            "extra": "mean: 40.67961432000175 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 65.88850429193654,
            "unit": "iter/sec",
            "range": "stddev: 0.0008648629117713727",
            "extra": "mean: 15.177154357143 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 24.769472795480112,
            "unit": "iter/sec",
            "range": "stddev: 0.001127904263933691",
            "extra": "mean: 40.37227632000622 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 72.22473168577481,
            "unit": "iter/sec",
            "range": "stddev: 0.0005177145682157151",
            "extra": "mean: 13.845672758614864 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 41.035273469684824,
            "unit": "iter/sec",
            "range": "stddev: 0.0007223606305985495",
            "extra": "mean: 24.369278317074187 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 96.27260353724566,
            "unit": "iter/sec",
            "range": "stddev: 0.000553146175294275",
            "extra": "mean: 10.38717104615461 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 52.52545551557469,
            "unit": "iter/sec",
            "range": "stddev: 0.0008250250222071471",
            "extra": "mean: 19.038387962261137 msec\nrounds: 53"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 145.9175016504774,
            "unit": "iter/sec",
            "range": "stddev: 0.0006055671699757351",
            "extra": "mean: 6.853187511360659 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 38.04103822724465,
            "unit": "iter/sec",
            "range": "stddev: 0.0008296394670461008",
            "extra": "mean: 26.28740030769741 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 100.9857045732739,
            "unit": "iter/sec",
            "range": "stddev: 0.0008712605479011299",
            "extra": "mean: 9.902391672421446 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-alpha",
            "value": 38.21940991198955,
            "unit": "iter/sec",
            "range": "stddev: 0.001085292614900972",
            "extra": "mean: 26.16471584210139 msec\nrounds: 38"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 101.68698877804415,
            "unit": "iter/sec",
            "range": "stddev: 0.00021299245729773476",
            "extra": "mean: 9.834099839289527 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 29.816000278144106,
            "unit": "iter/sec",
            "range": "stddev: 0.0008234162921238563",
            "extra": "mean: 33.53903912903521 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 100.87057306356968,
            "unit": "iter/sec",
            "range": "stddev: 0.0009591353533660536",
            "extra": "mean: 9.913694049996025 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 29.769367865641513,
            "unit": "iter/sec",
            "range": "stddev: 0.0002807030609391047",
            "extra": "mean: 33.591576566667904 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 104.235146986663,
            "unit": "iter/sec",
            "range": "stddev: 0.00018973812149380073",
            "extra": "mean: 9.59369300000077 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.85681659382027,
            "unit": "iter/sec",
            "range": "stddev: 0.0008867771401920786",
            "extra": "mean: 28.688793117650594 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 130.7380809352898,
            "unit": "iter/sec",
            "range": "stddev: 0.00023365709866929898",
            "extra": "mean: 7.648880822221649 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.82643903785817,
            "unit": "iter/sec",
            "range": "stddev: 0.0003051495666360522",
            "extra": "mean: 45.815994000005695 msec\nrounds: 19"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 94.46291299345114,
            "unit": "iter/sec",
            "range": "stddev: 0.0002397337522702812",
            "extra": "mean: 10.586165176478596 msec\nrounds: 17"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.292891731897246,
            "unit": "iter/sec",
            "range": "stddev: 0.00031748024132025293",
            "extra": "mean: 46.964029714290845 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 89.48283282241256,
            "unit": "iter/sec",
            "range": "stddev: 0.00018174694460236707",
            "extra": "mean: 11.175327919988831 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.299472841048043,
            "unit": "iter/sec",
            "range": "stddev: 0.0003913732567645825",
            "extra": "mean: 46.94951877272822 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 79.76951767818629,
            "unit": "iter/sec",
            "range": "stddev: 0.0005878995306781665",
            "extra": "mean: 12.536116916668524 msec\nrounds: 24"
          },
          {
            "name": "equator-int8-mask",
            "value": 41.49643492234129,
            "unit": "iter/sec",
            "range": "stddev: 0.0007294467349278479",
            "extra": "mean: 24.098455731714182 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 115.77534558304858,
            "unit": "iter/sec",
            "range": "stddev: 0.0004622354672488287",
            "extra": "mean: 8.637417534484273 msec\nrounds: 58"
          },
          {
            "name": "equator-uint8-mask",
            "value": 45.34079422077469,
            "unit": "iter/sec",
            "range": "stddev: 0.0010163283432947047",
            "extra": "mean: 22.055193720929797 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 138.5247092576,
            "unit": "iter/sec",
            "range": "stddev: 0.00033761723450072815",
            "extra": "mean: 7.218928704917214 msec\nrounds: 61"
          },
          {
            "name": "equator-uint16-mask",
            "value": 39.82807173221796,
            "unit": "iter/sec",
            "range": "stddev: 0.001233778714555615",
            "extra": "mean: 25.10791902564226 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 132.5786832549855,
            "unit": "iter/sec",
            "range": "stddev: 0.0004351342097430734",
            "extra": "mean: 7.542690690906346 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 39.4945749534685,
            "unit": "iter/sec",
            "range": "stddev: 0.0007620537692141992",
            "extra": "mean: 25.319933210527637 msec\nrounds: 38"
          },
          {
            "name": "dateline-int16-mask",
            "value": 135.38620169425866,
            "unit": "iter/sec",
            "range": "stddev: 0.0001923324913464812",
            "extra": "mean: 7.386277090912782 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.33511011967753,
            "unit": "iter/sec",
            "range": "stddev: 0.0005223744136020347",
            "extra": "mean: 30.92613559375046 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 106.01279241724453,
            "unit": "iter/sec",
            "range": "stddev: 0.0009739852673211644",
            "extra": "mean: 9.43282388095397 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.081482156854285,
            "unit": "iter/sec",
            "range": "stddev: 0.00038811094535033707",
            "extra": "mean: 32.173497870965384 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 99.31203525373756,
            "unit": "iter/sec",
            "range": "stddev: 0.0009935724612543894",
            "extra": "mean: 10.069273048780516 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.05174813827753,
            "unit": "iter/sec",
            "range": "stddev: 0.0004166743935670827",
            "extra": "mean: 29.367067909089254 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 119.47655020716316,
            "unit": "iter/sec",
            "range": "stddev: 0.0007305043691270166",
            "extra": "mean: 8.369843272726547 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 25.90981906107151,
            "unit": "iter/sec",
            "range": "stddev: 0.0009722269774354062",
            "extra": "mean: 38.595406538460196 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 94.89929309979019,
            "unit": "iter/sec",
            "range": "stddev: 0.0009119306153527297",
            "extra": "mean: 10.537486290318963 msec\nrounds: 31"
          },
          {
            "name": "equator-int64-mask",
            "value": 24.419772569381077,
            "unit": "iter/sec",
            "range": "stddev: 0.004448472547688612",
            "extra": "mean: 40.950422333329094 msec\nrounds: 24"
          },
          {
            "name": "dateline-int64-mask",
            "value": 92.45139793480725,
            "unit": "iter/sec",
            "range": "stddev: 0.0007434209484883746",
            "extra": "mean: 10.816494096770253 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.593775140281597,
            "unit": "iter/sec",
            "range": "stddev: 0.001129594512719928",
            "extra": "mean: 39.07200069231355 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 96.49214261480103,
            "unit": "iter/sec",
            "range": "stddev: 0.0008442090845939597",
            "extra": "mean: 10.363538137939628 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-none",
            "value": 41.62013210211985,
            "unit": "iter/sec",
            "range": "stddev: 0.0010860799370263714",
            "extra": "mean: 24.02683387804689 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-none",
            "value": 128.4568403099909,
            "unit": "iter/sec",
            "range": "stddev: 0.0003276917422137065",
            "extra": "mean: 7.784715843755841 msec\nrounds: 64"
          },
          {
            "name": "equator-uint8-none",
            "value": 46.43672324359541,
            "unit": "iter/sec",
            "range": "stddev: 0.0009099176962959915",
            "extra": "mean: 21.53468053191976 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 162.811857010375,
            "unit": "iter/sec",
            "range": "stddev: 0.0003352501214363764",
            "extra": "mean: 6.142058805559082 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 41.37661940926156,
            "unit": "iter/sec",
            "range": "stddev: 0.0008351864728916778",
            "extra": "mean: 24.168238349993487 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-none",
            "value": 155.95703908023253,
            "unit": "iter/sec",
            "range": "stddev: 0.0005430602163313213",
            "extra": "mean: 6.412022220334327 msec\nrounds: 59"
          },
          {
            "name": "equator-int16-none",
            "value": 41.43451267779718,
            "unit": "iter/sec",
            "range": "stddev: 0.0010640165840276406",
            "extra": "mean: 24.13446992308548 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-none",
            "value": 162.51398759957672,
            "unit": "iter/sec",
            "range": "stddev: 0.00021354863884808927",
            "extra": "mean: 6.153316491525217 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-none",
            "value": 32.20848662903678,
            "unit": "iter/sec",
            "range": "stddev: 0.000781736889689549",
            "extra": "mean: 31.047717687501475 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-none",
            "value": 118.05842298141819,
            "unit": "iter/sec",
            "range": "stddev: 0.0007953187939399908",
            "extra": "mean: 8.470382500005062 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-none",
            "value": 31.263066133763083,
            "unit": "iter/sec",
            "range": "stddev: 0.00046952487323891366",
            "extra": "mean: 31.986625870967693 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-none",
            "value": 98.7341929303972,
            "unit": "iter/sec",
            "range": "stddev: 0.0025205141308008473",
            "extra": "mean: 10.128203516130943 msec\nrounds: 31"
          },
          {
            "name": "equator-float32-none",
            "value": 34.43472445311579,
            "unit": "iter/sec",
            "range": "stddev: 0.0009181893025026323",
            "extra": "mean: 29.040453085708254 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 142.7286766363784,
            "unit": "iter/sec",
            "range": "stddev: 0.000629216525863129",
            "extra": "mean: 7.006300510636991 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-none",
            "value": 25.85855203953938,
            "unit": "iter/sec",
            "range": "stddev: 0.0012983498744008968",
            "extra": "mean: 38.671925576920785 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 99.51451650520686,
            "unit": "iter/sec",
            "range": "stddev: 0.0008153866125173275",
            "extra": "mean: 10.048785193541862 msec\nrounds: 31"
          },
          {
            "name": "equator-int64-none",
            "value": 25.34731861702248,
            "unit": "iter/sec",
            "range": "stddev: 0.0004299049315923193",
            "extra": "mean: 39.45190475999425 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-none",
            "value": 106.25011168698241,
            "unit": "iter/sec",
            "range": "stddev: 0.0007967455710379277",
            "extra": "mean: 9.411754812512996 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-none",
            "value": 25.57494522870479,
            "unit": "iter/sec",
            "range": "stddev: 0.0003239634775846017",
            "extra": "mean: 39.10076799998855 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 102.89137965639864,
            "unit": "iter/sec",
            "range": "stddev: 0.0007545883497988859",
            "extra": "mean: 9.718987181816953 msec\nrounds: 33"
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
          "id": "ad0c7cd005ca2c1bc2cedfcc03cc7c087a41d259",
          "message": "Bump version: 7.2.0 → 7.2.1",
          "timestamp": "2024-11-14T22:59:01+01:00",
          "tree_id": "2e5f3c8a0b573d51d0695550e53a35791cf57f08",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ad0c7cd005ca2c1bc2cedfcc03cc7c087a41d259"
        },
        "date": 1731621939093,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 36.512854165859956,
            "unit": "iter/sec",
            "range": "stddev: 0.00032682212812364927",
            "extra": "mean: 27.387615206893752 msec\nrounds: 29"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.10810255379928,
            "unit": "iter/sec",
            "range": "stddev: 0.000484844395055314",
            "extra": "mean: 12.640930166665635 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 44.97270745799534,
            "unit": "iter/sec",
            "range": "stddev: 0.000705229418928357",
            "extra": "mean: 22.235708200001152 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 125.6022375587925,
            "unit": "iter/sec",
            "range": "stddev: 0.00010858517307734052",
            "extra": "mean: 7.961641603175383 msec\nrounds: 63"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.17096682214313,
            "unit": "iter/sec",
            "range": "stddev: 0.00028912672154630487",
            "extra": "mean: 26.90271697222278 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 111.74409172672493,
            "unit": "iter/sec",
            "range": "stddev: 0.0014642746038070842",
            "extra": "mean: 8.949018999998172 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.57263820389099,
            "unit": "iter/sec",
            "range": "stddev: 0.0004234434047131592",
            "extra": "mean: 27.34284561111069 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.2268749699302,
            "unit": "iter/sec",
            "range": "stddev: 0.00011892847936655606",
            "extra": "mean: 8.99063288679419 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.04959600518517,
            "unit": "iter/sec",
            "range": "stddev: 0.0003711536927679354",
            "extra": "mean: 33.27831761290389 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 74.1927869892845,
            "unit": "iter/sec",
            "range": "stddev: 0.00015387820934610545",
            "extra": "mean: 13.4783991891884 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.171653682414583,
            "unit": "iter/sec",
            "range": "stddev: 0.001847163673063699",
            "extra": "mean: 34.27985299999724 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 74.35530007444721,
            "unit": "iter/sec",
            "range": "stddev: 0.0010854926709971768",
            "extra": "mean: 13.448940411763033 msec\nrounds: 34"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.145660926155685,
            "unit": "iter/sec",
            "range": "stddev: 0.00043656831302692174",
            "extra": "mean: 31.108397562494616 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 85.95916113779639,
            "unit": "iter/sec",
            "range": "stddev: 0.00023089924872737774",
            "extra": "mean: 11.633431349998347 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.013544308957954,
            "unit": "iter/sec",
            "range": "stddev: 0.00023385946941987564",
            "extra": "mean: 39.978340840001465 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 72.24149392777791,
            "unit": "iter/sec",
            "range": "stddev: 0.00017241101006668566",
            "extra": "mean: 13.842460137933076 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 24.930166142136436,
            "unit": "iter/sec",
            "range": "stddev: 0.00019204135338844283",
            "extra": "mean: 40.11204715999952 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 69.66726893140074,
            "unit": "iter/sec",
            "range": "stddev: 0.00012767503624933104",
            "extra": "mean: 14.353942896551173 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.043672608830363,
            "unit": "iter/sec",
            "range": "stddev: 0.00026780632606604866",
            "extra": "mean: 39.93024567999669 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 71.21785722861348,
            "unit": "iter/sec",
            "range": "stddev: 0.00029491797597055726",
            "extra": "mean: 14.041422178568805 msec\nrounds: 28"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.45610255571925,
            "unit": "iter/sec",
            "range": "stddev: 0.0005366807915014283",
            "extra": "mean: 23.553739976193135 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.43776064630832,
            "unit": "iter/sec",
            "range": "stddev: 0.00014461693712660432",
            "extra": "mean: 10.056541835821456 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 54.289729062392254,
            "unit": "iter/sec",
            "range": "stddev: 0.0003264928325966798",
            "extra": "mean: 18.419690377359483 msec\nrounds: 53"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 146.568406843178,
            "unit": "iter/sec",
            "range": "stddev: 0.0001493335744079996",
            "extra": "mean: 6.822752744184207 msec\nrounds: 86"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 38.38618773783381,
            "unit": "iter/sec",
            "range": "stddev: 0.00019587792459750648",
            "extra": "mean: 26.051037076922075 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 106.34460868354594,
            "unit": "iter/sec",
            "range": "stddev: 0.00023937052312374425",
            "extra": "mean: 9.403391599998656 msec\nrounds: 60"
          },
          {
            "name": "equator-int16-alpha",
            "value": 38.61407460465105,
            "unit": "iter/sec",
            "range": "stddev: 0.0003636432677812829",
            "extra": "mean: 25.89729289743358 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 100.62536208693324,
            "unit": "iter/sec",
            "range": "stddev: 0.00033062269989973445",
            "extra": "mean: 9.937852438593666 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.487913058657565,
            "unit": "iter/sec",
            "range": "stddev: 0.0007659164723099116",
            "extra": "mean: 32.79988361538681 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 97.27972379410993,
            "unit": "iter/sec",
            "range": "stddev: 0.00044010381595314594",
            "extra": "mean: 10.279634449995712 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 29.914495457462724,
            "unit": "iter/sec",
            "range": "stddev: 0.0007451719585669409",
            "extra": "mean: 33.428609933333554 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 97.14484877879208,
            "unit": "iter/sec",
            "range": "stddev: 0.0004516447969464472",
            "extra": "mean: 10.2939065999999 msec\nrounds: 25"
          },
          {
            "name": "equator-float32-alpha",
            "value": 33.56836358728786,
            "unit": "iter/sec",
            "range": "stddev: 0.000237652568230488",
            "extra": "mean: 29.78995378787824 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 107.67138589960193,
            "unit": "iter/sec",
            "range": "stddev: 0.00025328995869192854",
            "extra": "mean: 9.287518607148318 msec\nrounds: 28"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.24273166659018,
            "unit": "iter/sec",
            "range": "stddev: 0.0007255975222943988",
            "extra": "mean: 47.074925000006694 msec\nrounds: 21"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 81.94687249039876,
            "unit": "iter/sec",
            "range": "stddev: 0.00038625606346960335",
            "extra": "mean: 12.203028250006298 msec\nrounds: 24"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.02991088430897,
            "unit": "iter/sec",
            "range": "stddev: 0.0003755701631072055",
            "extra": "mean: 47.55131895238459 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 76.8134781230357,
            "unit": "iter/sec",
            "range": "stddev: 0.0004312204976955839",
            "extra": "mean: 13.018548624998516 msec\nrounds: 24"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.35465996513519,
            "unit": "iter/sec",
            "range": "stddev: 0.00031707475238166823",
            "extra": "mean: 46.82818652381521 msec\nrounds: 21"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 76.07827998537121,
            "unit": "iter/sec",
            "range": "stddev: 0.0011463160104778244",
            "extra": "mean: 13.144356052637969 msec\nrounds: 19"
          },
          {
            "name": "equator-int8-mask",
            "value": 42.483113268146504,
            "unit": "iter/sec",
            "range": "stddev: 0.0003841280504254496",
            "extra": "mean: 23.538764536585692 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 122.11767210450162,
            "unit": "iter/sec",
            "range": "stddev: 0.00011072820883232817",
            "extra": "mean: 8.188822983329183 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.40119054347408,
            "unit": "iter/sec",
            "range": "stddev: 0.00031936260947377116",
            "extra": "mean: 21.09651653333155 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 143.3237802005964,
            "unit": "iter/sec",
            "range": "stddev: 0.00007530112654814454",
            "extra": "mean: 6.977209215389079 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.14474320980102,
            "unit": "iter/sec",
            "range": "stddev: 0.0002535731220616886",
            "extra": "mean: 24.909861666666682 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 132.90847462243323,
            "unit": "iter/sec",
            "range": "stddev: 0.00010642692525171712",
            "extra": "mean: 7.52397469642777 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.060997779156814,
            "unit": "iter/sec",
            "range": "stddev: 0.00022720519899654295",
            "extra": "mean: 24.961934435898804 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 131.62126958935042,
            "unit": "iter/sec",
            "range": "stddev: 0.00016728923395499306",
            "extra": "mean: 7.597556254547106 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.43018435232561,
            "unit": "iter/sec",
            "range": "stddev: 0.00028968074024839834",
            "extra": "mean: 30.83547071875614 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 113.63195947558334,
            "unit": "iter/sec",
            "range": "stddev: 0.0006183722159364104",
            "extra": "mean: 8.8003410714296 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.31307323845625,
            "unit": "iter/sec",
            "range": "stddev: 0.00046195583600427693",
            "extra": "mean: 31.93554309999437 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-mask",
            "value": 111.30562931155264,
            "unit": "iter/sec",
            "range": "stddev: 0.00018553957743657298",
            "extra": "mean: 8.984271560973134 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.218469426311955,
            "unit": "iter/sec",
            "range": "stddev: 0.00029282416484069645",
            "extra": "mean: 29.223983911771924 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 125.84875762879413,
            "unit": "iter/sec",
            "range": "stddev: 0.00026974004048651234",
            "extra": "mean: 7.946045863635927 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.161761283262873,
            "unit": "iter/sec",
            "range": "stddev: 0.0002992955547513012",
            "extra": "mean: 38.223726192309364 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 106.23059848376482,
            "unit": "iter/sec",
            "range": "stddev: 0.0002847824960781334",
            "extra": "mean: 9.413483631581249 msec\nrounds: 19"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.549165986210983,
            "unit": "iter/sec",
            "range": "stddev: 0.0002332971134572501",
            "extra": "mean: 39.14022087999683 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 96.42848498738458,
            "unit": "iter/sec",
            "range": "stddev: 0.0002462902051066141",
            "extra": "mean: 10.370379666659979 msec\nrounds: 18"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.864364607962,
            "unit": "iter/sec",
            "range": "stddev: 0.0010765863055194357",
            "extra": "mean: 38.66323473077561 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 103.83259213255572,
            "unit": "iter/sec",
            "range": "stddev: 0.00016222278833958226",
            "extra": "mean: 9.630887368422535 msec\nrounds: 19"
          },
          {
            "name": "equator-int8-none",
            "value": 44.07527734697339,
            "unit": "iter/sec",
            "range": "stddev: 0.000232558536597002",
            "extra": "mean: 22.68845620931003 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 134.75706211217897,
            "unit": "iter/sec",
            "range": "stddev: 0.00008845394910612394",
            "extra": "mean: 7.420761363642276 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.1312628591231,
            "unit": "iter/sec",
            "range": "stddev: 0.0003041100743728156",
            "extra": "mean: 20.776516978724025 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 167.54461089928768,
            "unit": "iter/sec",
            "range": "stddev: 0.00010116189288432057",
            "extra": "mean: 5.9685596250010535 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.251883778388844,
            "unit": "iter/sec",
            "range": "stddev: 0.00020859787289997185",
            "extra": "mean: 23.12038026190337 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 164.156273843827,
            "unit": "iter/sec",
            "range": "stddev: 0.00013283682692624138",
            "extra": "mean: 6.091756206353512 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 43.38295749393259,
            "unit": "iter/sec",
            "range": "stddev: 0.00020298353383580036",
            "extra": "mean: 23.050526238093774 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 164.42551685766466,
            "unit": "iter/sec",
            "range": "stddev: 0.00007566496000811237",
            "extra": "mean: 6.081781095239934 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.36149569266386,
            "unit": "iter/sec",
            "range": "stddev: 0.0002432688359764391",
            "extra": "mean: 29.974675272724614 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 126.44488536140902,
            "unit": "iter/sec",
            "range": "stddev: 0.0001669356185276373",
            "extra": "mean: 7.908584021740117 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 32.033622297765454,
            "unit": "iter/sec",
            "range": "stddev: 0.0007642112493287144",
            "extra": "mean: 31.21720018749663 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 124.62626424421309,
            "unit": "iter/sec",
            "range": "stddev: 0.00016938969664472255",
            "extra": "mean: 8.023990818182886 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.852891015385744,
            "unit": "iter/sec",
            "range": "stddev: 0.0003482901834989306",
            "extra": "mean: 27.89175354285557 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 152.67264145962366,
            "unit": "iter/sec",
            "range": "stddev: 0.00037928924756049456",
            "extra": "mean: 6.549961999998955 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.386030636218344,
            "unit": "iter/sec",
            "range": "stddev: 0.0007667364580286703",
            "extra": "mean: 37.89884176922643 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 114.54753126376441,
            "unit": "iter/sec",
            "range": "stddev: 0.00034102771069718517",
            "extra": "mean: 8.730000454547874 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 25.82209788198002,
            "unit": "iter/sec",
            "range": "stddev: 0.00032613298849627916",
            "extra": "mean: 38.726520384614105 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 109.5280699701161,
            "unit": "iter/sec",
            "range": "stddev: 0.00026608044756290696",
            "extra": "mean: 9.130079625002452 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-none",
            "value": 25.986257245806986,
            "unit": "iter/sec",
            "range": "stddev: 0.00020173258898506408",
            "extra": "mean: 38.481878730780096 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 111.79150280380448,
            "unit": "iter/sec",
            "range": "stddev: 0.00027530764065412196",
            "extra": "mean: 8.945223696965707 msec\nrounds: 33"
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
          "id": "444289eca559514f99670c20cfd438a2f75715be",
          "message": "catch and expend image encoding error (#767)",
          "timestamp": "2024-11-18T07:24:17Z",
          "tree_id": "91d5bc808d10fa1fffb6fb32e95949caebd84090",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/444289eca559514f99670c20cfd438a2f75715be"
        },
        "date": 1731915031687,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.766176769190075,
            "unit": "iter/sec",
            "range": "stddev: 0.00014767183307065244",
            "extra": "mean: 26.478719466668583 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.14968342552388,
            "unit": "iter/sec",
            "range": "stddev: 0.00009322921854763465",
            "extra": "mean: 12.322906976190021 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.976839021308045,
            "unit": "iter/sec",
            "range": "stddev: 0.00009080165204396518",
            "extra": "mean: 21.287085739132294 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 127.81566322790744,
            "unit": "iter/sec",
            "range": "stddev: 0.000045199291045281515",
            "extra": "mean: 7.823767250003666 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.21061444066529,
            "unit": "iter/sec",
            "range": "stddev: 0.0000929751035131795",
            "extra": "mean: 26.17073854053913 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.79326648264876,
            "unit": "iter/sec",
            "range": "stddev: 0.00004114110530922629",
            "extra": "mean: 8.210634535715197 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.6868865841097,
            "unit": "iter/sec",
            "range": "stddev: 0.00017196433633852047",
            "extra": "mean: 26.534428567565463 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.68616105949425,
            "unit": "iter/sec",
            "range": "stddev: 0.00004106691531853379",
            "extra": "mean: 8.87420416666813 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.597202856470947,
            "unit": "iter/sec",
            "range": "stddev: 0.0007117466454463359",
            "extra": "mean: 31.648371045451736 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.57713809034237,
            "unit": "iter/sec",
            "range": "stddev: 0.00011016341614006285",
            "extra": "mean: 12.410468076922871 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.775455754960706,
            "unit": "iter/sec",
            "range": "stddev: 0.0026465388922973124",
            "extra": "mean: 33.584708433334264 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.66775352836007,
            "unit": "iter/sec",
            "range": "stddev: 0.00011205557819990164",
            "extra": "mean: 12.24473499999897 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.230717615793964,
            "unit": "iter/sec",
            "range": "stddev: 0.0012232390101797354",
            "extra": "mean: 30.092639333335313 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 91.47206332864575,
            "unit": "iter/sec",
            "range": "stddev: 0.0003524052367515888",
            "extra": "mean: 10.932299585362431 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.457111923931347,
            "unit": "iter/sec",
            "range": "stddev: 0.00017915863966218225",
            "extra": "mean: 39.281753679997564 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.56930095875038,
            "unit": "iter/sec",
            "range": "stddev: 0.0001376171550992224",
            "extra": "mean: 13.060064379309441 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.41815642990041,
            "unit": "iter/sec",
            "range": "stddev: 0.0003569525554069321",
            "extra": "mean: 39.34195631999728 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.5960182138105,
            "unit": "iter/sec",
            "range": "stddev: 0.0009656046347224507",
            "extra": "mean: 13.587691620690794 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.621641504760984,
            "unit": "iter/sec",
            "range": "stddev: 0.00024532524810405766",
            "extra": "mean: 39.02950557692337 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.49936478245067,
            "unit": "iter/sec",
            "range": "stddev: 0.00020760196559998785",
            "extra": "mean: 13.422933241379308 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.96878017338647,
            "unit": "iter/sec",
            "range": "stddev: 0.0005960002943736103",
            "extra": "mean: 23.272710930234155 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.24081737491633,
            "unit": "iter/sec",
            "range": "stddev: 0.00010819582945549226",
            "extra": "mean: 10.076499029851357 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.18991115285911,
            "unit": "iter/sec",
            "range": "stddev: 0.00011869057017194363",
            "extra": "mean: 17.796789129628603 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 151.30347149793613,
            "unit": "iter/sec",
            "range": "stddev: 0.0002751895514404579",
            "extra": "mean: 6.609233681817014 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.89035668746787,
            "unit": "iter/sec",
            "range": "stddev: 0.0006561340544682192",
            "extra": "mean: 25.068715425003063 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 109.97062915255407,
            "unit": "iter/sec",
            "range": "stddev: 0.00010042605732558646",
            "extra": "mean: 9.093337081965535 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.95640093382283,
            "unit": "iter/sec",
            "range": "stddev: 0.00025154255190088106",
            "extra": "mean: 25.027279149997383 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.09266255726769,
            "unit": "iter/sec",
            "range": "stddev: 0.0002746393707983952",
            "extra": "mean: 9.795023216669088 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.675027758981937,
            "unit": "iter/sec",
            "range": "stddev: 0.0002562880638226732",
            "extra": "mean: 32.599807500001056 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 98.9505257760918,
            "unit": "iter/sec",
            "range": "stddev: 0.0002264435070668109",
            "extra": "mean: 10.10606050000007 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.0431007636967,
            "unit": "iter/sec",
            "range": "stddev: 0.00013389970837160583",
            "extra": "mean: 33.28551229999448 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 99.36452462875047,
            "unit": "iter/sec",
            "range": "stddev: 0.00037930525609185673",
            "extra": "mean: 10.063953948717996 msec\nrounds: 39"
          },
          {
            "name": "equator-float32-alpha",
            "value": 33.8766306610832,
            "unit": "iter/sec",
            "range": "stddev: 0.00019171309597976568",
            "extra": "mean: 29.518874235293424 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 123.48507631356584,
            "unit": "iter/sec",
            "range": "stddev: 0.00040777333379436726",
            "extra": "mean: 8.098144568180032 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.663270952380394,
            "unit": "iter/sec",
            "range": "stddev: 0.0004008987587796489",
            "extra": "mean: 46.16108076191137 msec\nrounds: 21"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 88.02152927738436,
            "unit": "iter/sec",
            "range": "stddev: 0.00027274461402091625",
            "extra": "mean: 11.360856920000515 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.2333575938595,
            "unit": "iter/sec",
            "range": "stddev: 0.0004322862388901783",
            "extra": "mean: 47.09570757142956 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 82.01856659761336,
            "unit": "iter/sec",
            "range": "stddev: 0.0008388602048096073",
            "extra": "mean: 12.192361333331311 msec\nrounds: 24"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.49097774112735,
            "unit": "iter/sec",
            "range": "stddev: 0.00024917798105073176",
            "extra": "mean: 46.531154238101365 msec\nrounds: 21"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 80.18184265781433,
            "unit": "iter/sec",
            "range": "stddev: 0.0008850198714225232",
            "extra": "mean: 12.471651521749386 msec\nrounds: 23"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.91949738395409,
            "unit": "iter/sec",
            "range": "stddev: 0.0002249026011053129",
            "extra": "mean: 22.768930875000137 msec\nrounds: 40"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.03832286336055,
            "unit": "iter/sec",
            "range": "stddev: 0.000106975281348474",
            "extra": "mean: 8.127549016663238 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.88135770770359,
            "unit": "iter/sec",
            "range": "stddev: 0.0002917561658930586",
            "extra": "mean: 20.884954977772296 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.45036289513422,
            "unit": "iter/sec",
            "range": "stddev: 0.000028481203378363115",
            "extra": "mean: 6.875197696969467 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.47491310870447,
            "unit": "iter/sec",
            "range": "stddev: 0.00025191847994139046",
            "extra": "mean: 24.110960700002693 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 139.3441217886928,
            "unit": "iter/sec",
            "range": "stddev: 0.00006040062571079152",
            "extra": "mean: 7.176477824564723 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.739652536141556,
            "unit": "iter/sec",
            "range": "stddev: 0.0005218728688783317",
            "extra": "mean: 23.958033649995514 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 139.75326213418214,
            "unit": "iter/sec",
            "range": "stddev: 0.00008077818094157775",
            "extra": "mean: 7.155468035085034 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.40419405508006,
            "unit": "iter/sec",
            "range": "stddev: 0.00035084271510625565",
            "extra": "mean: 29.936360636365105 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 115.00012222686323,
            "unit": "iter/sec",
            "range": "stddev: 0.00015253033889042883",
            "extra": "mean: 8.695642931816007 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.36797930280377,
            "unit": "iter/sec",
            "range": "stddev: 0.00023603506311602697",
            "extra": "mean: 30.894730580644502 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 111.6801855168309,
            "unit": "iter/sec",
            "range": "stddev: 0.00022205998660495947",
            "extra": "mean: 8.954139853656438 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.40332064738437,
            "unit": "iter/sec",
            "range": "stddev: 0.0003406595527676057",
            "extra": "mean: 28.245937999996077 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 133.53041433368114,
            "unit": "iter/sec",
            "range": "stddev: 0.00011878828667389544",
            "extra": "mean: 7.488930555559313 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.551891147210565,
            "unit": "iter/sec",
            "range": "stddev: 0.0006528539377739324",
            "extra": "mean: 37.66210076923489 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.80146316410976,
            "unit": "iter/sec",
            "range": "stddev: 0.00019719517117922284",
            "extra": "mean: 9.107346761904214 msec\nrounds: 21"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.9632211528783,
            "unit": "iter/sec",
            "range": "stddev: 0.0004000357245491758",
            "extra": "mean: 38.51602211111387 msec\nrounds: 18"
          },
          {
            "name": "dateline-int64-mask",
            "value": 92.96543234453287,
            "unit": "iter/sec",
            "range": "stddev: 0.0003758445120741849",
            "extra": "mean: 10.756686380954676 msec\nrounds: 21"
          },
          {
            "name": "equator-uint64-mask",
            "value": 25.7734383326025,
            "unit": "iter/sec",
            "range": "stddev: 0.00022715796527638312",
            "extra": "mean: 38.79963500000056 msec\nrounds: 18"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 104.28379609526395,
            "unit": "iter/sec",
            "range": "stddev: 0.00021808283949895644",
            "extra": "mean: 9.589217476188661 msec\nrounds: 21"
          },
          {
            "name": "equator-int8-none",
            "value": 44.37879250000774,
            "unit": "iter/sec",
            "range": "stddev: 0.00016421146091147206",
            "extra": "mean: 22.533285465119977 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 136.08365492787433,
            "unit": "iter/sec",
            "range": "stddev: 0.0000313271324756344",
            "extra": "mean: 7.34842109090919 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.70312626287738,
            "unit": "iter/sec",
            "range": "stddev: 0.00012914226473248025",
            "extra": "mean: 20.53256282979564 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.53290229308612,
            "unit": "iter/sec",
            "range": "stddev: 0.0000673192309630912",
            "extra": "mean: 5.933559479447854 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.340685133114896,
            "unit": "iter/sec",
            "range": "stddev: 0.000621078287423278",
            "extra": "mean: 23.073008581397335 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 166.85083467596766,
            "unit": "iter/sec",
            "range": "stddev: 0.00004959182593552581",
            "extra": "mean: 5.993377269835347 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 42.42750081343835,
            "unit": "iter/sec",
            "range": "stddev: 0.0016942830755241752",
            "extra": "mean: 23.56961830952963 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 165.7862068233072,
            "unit": "iter/sec",
            "range": "stddev: 0.00035340074275337305",
            "extra": "mean: 6.031864888891433 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.92366984312621,
            "unit": "iter/sec",
            "range": "stddev: 0.0003909570162546916",
            "extra": "mean: 29.47794282353049 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.09468673099312,
            "unit": "iter/sec",
            "range": "stddev: 0.00013710258500784873",
            "extra": "mean: 7.746252191492553 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.196446068348564,
            "unit": "iter/sec",
            "range": "stddev: 0.00029992303025327776",
            "extra": "mean: 31.059328656247942 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 121.40529710679142,
            "unit": "iter/sec",
            "range": "stddev: 0.00023238881293655123",
            "extra": "mean: 8.236872886364855 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.25900002870023,
            "unit": "iter/sec",
            "range": "stddev: 0.0005466217642750903",
            "extra": "mean: 28.361553055560762 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 149.38750938230964,
            "unit": "iter/sec",
            "range": "stddev: 0.00012607815292474726",
            "extra": "mean: 6.694000081632121 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.213255343739803,
            "unit": "iter/sec",
            "range": "stddev: 0.0007554321493171037",
            "extra": "mean: 38.1486384230724 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 118.00272434281591,
            "unit": "iter/sec",
            "range": "stddev: 0.0007899467156297455",
            "extra": "mean: 8.47438061764445 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.062311024196585,
            "unit": "iter/sec",
            "range": "stddev: 0.00024372330152152134",
            "extra": "mean: 38.36958276921747 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.66788572947472,
            "unit": "iter/sec",
            "range": "stddev: 0.00011383436468508776",
            "extra": "mean: 8.797559606061137 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.184492266680763,
            "unit": "iter/sec",
            "range": "stddev: 0.00034405212358861153",
            "extra": "mean: 38.19054384615583 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.21843597962453,
            "unit": "iter/sec",
            "range": "stddev: 0.0001971714861381927",
            "extra": "mean: 8.75515402941072 msec\nrounds: 34"
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
          "id": "83e8fc4ed765445d1aa0267cc3bccee15664b9b3",
          "message": "Bump version: 7.2.1 → 7.2.2",
          "timestamp": "2024-11-18T07:26:10Z",
          "tree_id": "e233c5d665bf30f68fe24f6f61448e857c16a200",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/83e8fc4ed765445d1aa0267cc3bccee15664b9b3"
        },
        "date": 1731915166679,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.56564606040824,
            "unit": "iter/sec",
            "range": "stddev: 0.00016504566607136354",
            "extra": "mean: 26.62006659999747 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 80.16307735152076,
            "unit": "iter/sec",
            "range": "stddev: 0.0002162739042736909",
            "extra": "mean: 12.47457099999953 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.594908347202136,
            "unit": "iter/sec",
            "range": "stddev: 0.0001766169342909452",
            "extra": "mean: 21.461572422216097 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 126.56968760079864,
            "unit": "iter/sec",
            "range": "stddev: 0.00006324946526366168",
            "extra": "mean: 7.900785875003535 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.6681686088164,
            "unit": "iter/sec",
            "range": "stddev: 0.0021136640940944665",
            "extra": "mean: 27.27161017143252 msec\nrounds: 35"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.05325479844294,
            "unit": "iter/sec",
            "range": "stddev: 0.00009606687630672845",
            "extra": "mean: 8.260827035712737 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.11517231389926,
            "unit": "iter/sec",
            "range": "stddev: 0.0002838652937004714",
            "extra": "mean: 26.943159297296596 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.71652548991602,
            "unit": "iter/sec",
            "range": "stddev: 0.0001468620218080518",
            "extra": "mean: 8.951227185187244 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.57568546608546,
            "unit": "iter/sec",
            "range": "stddev: 0.0003425761147722222",
            "extra": "mean: 31.66993796774646 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.77961874500342,
            "unit": "iter/sec",
            "range": "stddev: 0.00038923057411707133",
            "extra": "mean: 12.534529692304774 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.197906023650532,
            "unit": "iter/sec",
            "range": "stddev: 0.0005602461077172631",
            "extra": "mean: 33.114878866661 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.48419447129925,
            "unit": "iter/sec",
            "range": "stddev: 0.00019600911743623562",
            "extra": "mean: 12.272318656254555 msec\nrounds: 32"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.10030112828409,
            "unit": "iter/sec",
            "range": "stddev: 0.0004336109243307753",
            "extra": "mean: 30.211205515151754 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.96390782391734,
            "unit": "iter/sec",
            "range": "stddev: 0.00009115808523023328",
            "extra": "mean: 10.756862780490005 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 24.971295570657542,
            "unit": "iter/sec",
            "range": "stddev: 0.0003015410432628104",
            "extra": "mean: 40.045979879996594 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 72.34196138943703,
            "unit": "iter/sec",
            "range": "stddev: 0.0007783480804498846",
            "extra": "mean: 13.823235931034827 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 24.99853011143114,
            "unit": "iter/sec",
            "range": "stddev: 0.00047530185535265234",
            "extra": "mean: 40.00235195999494 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.19671864653392,
            "unit": "iter/sec",
            "range": "stddev: 0.00029073672419293857",
            "extra": "mean: 13.661814607140903 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.622536605600818,
            "unit": "iter/sec",
            "range": "stddev: 0.00038661559120619894",
            "extra": "mean: 39.02814211538332 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.60341570244556,
            "unit": "iter/sec",
            "range": "stddev: 0.0003532615335116066",
            "extra": "mean: 13.404212000003898 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.915037284593446,
            "unit": "iter/sec",
            "range": "stddev: 0.00014584337696972946",
            "extra": "mean: 22.771243333335992 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.36313006071549,
            "unit": "iter/sec",
            "range": "stddev: 0.000152237178997962",
            "extra": "mean: 10.06409519697048 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.39345702433789,
            "unit": "iter/sec",
            "range": "stddev: 0.0002680292913739614",
            "extra": "mean: 17.732553611111783 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 152.44848032619717,
            "unit": "iter/sec",
            "range": "stddev: 0.00010233203673517347",
            "extra": "mean: 6.55959310227481 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.11839790967463,
            "unit": "iter/sec",
            "range": "stddev: 0.0006654832081694148",
            "extra": "mean: 24.9262196923085 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 112.9998429728246,
            "unit": "iter/sec",
            "range": "stddev: 0.00011795049841363225",
            "extra": "mean: 8.849569819672144 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.23946032345928,
            "unit": "iter/sec",
            "range": "stddev: 0.00020839586339451541",
            "extra": "mean: 24.851227923079477 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 103.85284967878849,
            "unit": "iter/sec",
            "range": "stddev: 0.00033446489412671833",
            "extra": "mean: 9.629008766663105 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.270723379478376,
            "unit": "iter/sec",
            "range": "stddev: 0.000944856879927882",
            "extra": "mean: 31.978793322582895 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 105.782267670921,
            "unit": "iter/sec",
            "range": "stddev: 0.00020435190285799607",
            "extra": "mean: 9.453380249995291 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.445088994944413,
            "unit": "iter/sec",
            "range": "stddev: 0.0003288853044016558",
            "extra": "mean: 32.84601993333165 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 101.39112655938287,
            "unit": "iter/sec",
            "range": "stddev: 0.00044734663174283843",
            "extra": "mean: 9.862796024998488 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.60543493342124,
            "unit": "iter/sec",
            "range": "stddev: 0.00046676370836564465",
            "extra": "mean: 28.897194961541135 msec\nrounds: 26"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 124.81690919629459,
            "unit": "iter/sec",
            "range": "stddev: 0.00024788126734639224",
            "extra": "mean: 8.011735000001801 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 21.363292199235868,
            "unit": "iter/sec",
            "range": "stddev: 0.0025541498303858702",
            "extra": "mean: 46.809264727267475 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 91.72921876137241,
            "unit": "iter/sec",
            "range": "stddev: 0.00035751017298392884",
            "extra": "mean: 10.901651769229987 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.273044396357214,
            "unit": "iter/sec",
            "range": "stddev: 0.00037428601533955",
            "extra": "mean: 47.00784623808897 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 85.67755315247406,
            "unit": "iter/sec",
            "range": "stddev: 0.00040784400297177184",
            "extra": "mean: 11.67166851999582 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 21.335551754870753,
            "unit": "iter/sec",
            "range": "stddev: 0.0004401739281007047",
            "extra": "mean: 46.87012604544934 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.69158831907338,
            "unit": "iter/sec",
            "range": "stddev: 0.0009372061869016734",
            "extra": "mean: 11.403602320001482 msec\nrounds: 25"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.529838410772285,
            "unit": "iter/sec",
            "range": "stddev: 0.000754259822126422",
            "extra": "mean: 22.972747809523934 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.61791247459621,
            "unit": "iter/sec",
            "range": "stddev: 0.00009560434744994859",
            "extra": "mean: 8.08944254098695 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.422360799885205,
            "unit": "iter/sec",
            "range": "stddev: 0.00017522479015940503",
            "extra": "mean: 20.651615978260413 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 144.33753844087784,
            "unit": "iter/sec",
            "range": "stddev: 0.00008701979974603711",
            "extra": "mean: 6.928204615389159 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.179165189302374,
            "unit": "iter/sec",
            "range": "stddev: 0.0003826701756213312",
            "extra": "mean: 24.284125124998468 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 130.74815466955715,
            "unit": "iter/sec",
            "range": "stddev: 0.00032988070189939864",
            "extra": "mean: 7.648291500001076 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.19248407350061,
            "unit": "iter/sec",
            "range": "stddev: 0.0003731049915655774",
            "extra": "mean: 24.880273589740927 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 128.139884991158,
            "unit": "iter/sec",
            "range": "stddev: 0.0003340894948550465",
            "extra": "mean: 7.8039714181810185 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.969913001714076,
            "unit": "iter/sec",
            "range": "stddev: 0.0006592294710727183",
            "extra": "mean: 30.330683612905226 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 116.04946348751967,
            "unit": "iter/sec",
            "range": "stddev: 0.0007204987314974525",
            "extra": "mean: 8.617015279071438 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.20881980496362,
            "unit": "iter/sec",
            "range": "stddev: 0.0006053782425174576",
            "extra": "mean: 32.042224161291564 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 115.15850324535944,
            "unit": "iter/sec",
            "range": "stddev: 0.00020124224414393575",
            "extra": "mean: 8.683683547617637 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.09143620199752,
            "unit": "iter/sec",
            "range": "stddev: 0.00037179949247923905",
            "extra": "mean: 28.496981264707447 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 132.69882691344992,
            "unit": "iter/sec",
            "range": "stddev: 0.00021738354843622032",
            "extra": "mean: 7.535861644445656 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.402031951561085,
            "unit": "iter/sec",
            "range": "stddev: 0.0004769185949899511",
            "extra": "mean: 37.87587265384218 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 108.51393482716294,
            "unit": "iter/sec",
            "range": "stddev: 0.00022928870048951588",
            "extra": "mean: 9.215406312495844 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.80002838457137,
            "unit": "iter/sec",
            "range": "stddev: 0.000499446744344131",
            "extra": "mean: 38.75964728000099 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 100.44763844335189,
            "unit": "iter/sec",
            "range": "stddev: 0.0007130712239926489",
            "extra": "mean: 9.955435642859404 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.06383630372132,
            "unit": "iter/sec",
            "range": "stddev: 0.000992220725215552",
            "extra": "mean: 38.367337346161236 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 104.09852245916689,
            "unit": "iter/sec",
            "range": "stddev: 0.000339729214601581",
            "extra": "mean: 9.606284281241884 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.931952096507246,
            "unit": "iter/sec",
            "range": "stddev: 0.000709055652115787",
            "extra": "mean: 22.76247588095462 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-none",
            "value": 135.74979933093573,
            "unit": "iter/sec",
            "range": "stddev: 0.00004841168347004573",
            "extra": "mean: 7.366493393939863 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.81232950338794,
            "unit": "iter/sec",
            "range": "stddev: 0.00011944358633983194",
            "extra": "mean: 20.486627255324755 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.70116964871113,
            "unit": "iter/sec",
            "range": "stddev: 0.00004064372327392696",
            "extra": "mean: 5.927641178080237 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.34344588212995,
            "unit": "iter/sec",
            "range": "stddev: 0.00024143497439649934",
            "extra": "mean: 23.071538952381484 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 164.74267833005266,
            "unit": "iter/sec",
            "range": "stddev: 0.00015780726580931967",
            "extra": "mean: 6.070072492062781 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 43.35969163826189,
            "unit": "iter/sec",
            "range": "stddev: 0.00021544223169925233",
            "extra": "mean: 23.062894642856964 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 166.13173478680403,
            "unit": "iter/sec",
            "range": "stddev: 0.00006742586088949492",
            "extra": "mean: 6.019319555552072 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.37722509233535,
            "unit": "iter/sec",
            "range": "stddev: 0.0007661950400238001",
            "extra": "mean: 29.9605493636329 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.80448086829867,
            "unit": "iter/sec",
            "range": "stddev: 0.00018709564388905993",
            "extra": "mean: 7.703894297875688 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.532440131877955,
            "unit": "iter/sec",
            "range": "stddev: 0.00022234571294009098",
            "extra": "mean: 30.738548843746827 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 126.69705704820893,
            "unit": "iter/sec",
            "range": "stddev: 0.00015156044831155836",
            "extra": "mean: 7.892843159091647 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.55281180849711,
            "unit": "iter/sec",
            "range": "stddev: 0.0002963077858864569",
            "extra": "mean: 28.127170514288274 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 153.63475820722465,
            "unit": "iter/sec",
            "range": "stddev: 0.00016722402408576355",
            "extra": "mean: 6.50894375510512 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.3000149749245,
            "unit": "iter/sec",
            "range": "stddev: 0.001256175844634649",
            "extra": "mean: 38.022792038462356 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 118.77436813359671,
            "unit": "iter/sec",
            "range": "stddev: 0.0002313330415683871",
            "extra": "mean: 8.419324941179278 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 25.7774347924838,
            "unit": "iter/sec",
            "range": "stddev: 0.0009068893390825948",
            "extra": "mean: 38.79361961538471 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 111.11750392184194,
            "unit": "iter/sec",
            "range": "stddev: 0.00029385213384834825",
            "extra": "mean: 8.999482212121881 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.0368059152475,
            "unit": "iter/sec",
            "range": "stddev: 0.0005429871349887507",
            "extra": "mean: 38.407168807691065 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.4356576932204,
            "unit": "iter/sec",
            "range": "stddev: 0.00017217909507242227",
            "extra": "mean: 8.738534999998027 msec\nrounds: 33"
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
          "id": "7030d2145bd9a1099777c999015db3565f888c89",
          "message": "remove python 3.8 and add python 3.13 (#773)",
          "timestamp": "2024-12-20T16:59:46+01:00",
          "tree_id": "aeba0cb46d15cb8c01238bcb4713e1d187081654",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/7030d2145bd9a1099777c999015db3565f888c89"
        },
        "date": 1734710785721,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.61440159015153,
            "unit": "iter/sec",
            "range": "stddev: 0.00018057229578264603",
            "extra": "mean: 25.897073599997118 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.46286109818355,
            "unit": "iter/sec",
            "range": "stddev: 0.00006106428376742402",
            "extra": "mean: 12.126671166664474 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.23863678417445,
            "unit": "iter/sec",
            "range": "stddev: 0.00039191280070810476",
            "extra": "mean: 21.169112152173977 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.31889717324026,
            "unit": "iter/sec",
            "range": "stddev: 0.00010591524049780286",
            "extra": "mean: 7.673484212121927 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.7036697949836,
            "unit": "iter/sec",
            "range": "stddev: 0.00013577848088977006",
            "extra": "mean: 25.837343210529628 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.6741752390334,
            "unit": "iter/sec",
            "range": "stddev: 0.0002500773295829624",
            "extra": "mean: 8.218670872725976 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.611642371694664,
            "unit": "iter/sec",
            "range": "stddev: 0.0006813980416215884",
            "extra": "mean: 27.31371594444296 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.96321673108301,
            "unit": "iter/sec",
            "range": "stddev: 0.00006817142338236769",
            "extra": "mean: 8.698434407408387 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.60504137427625,
            "unit": "iter/sec",
            "range": "stddev: 0.0003284981197827799",
            "extra": "mean: 31.64052178124699 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 77.55774078843255,
            "unit": "iter/sec",
            "range": "stddev: 0.0002547106754614532",
            "extra": "mean: 12.893619512820392 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.253818616565344,
            "unit": "iter/sec",
            "range": "stddev: 0.0003345280425440836",
            "extra": "mean: 33.053678699999026 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 77.9875642083988,
            "unit": "iter/sec",
            "range": "stddev: 0.00035496100250249706",
            "extra": "mean: 12.822557162162349 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.455033994628664,
            "unit": "iter/sec",
            "range": "stddev: 0.0002501635076437206",
            "extra": "mean: 29.89086784848444 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 91.00332313508001,
            "unit": "iter/sec",
            "range": "stddev: 0.0006059223523264001",
            "extra": "mean: 10.988609707314298 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.047655957816303,
            "unit": "iter/sec",
            "range": "stddev: 0.0006540056769794985",
            "extra": "mean: 38.39117046153717 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.21021579520082,
            "unit": "iter/sec",
            "range": "stddev: 0.0008491060528932639",
            "extra": "mean: 13.475233689654221 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.150408599079565,
            "unit": "iter/sec",
            "range": "stddev: 0.00030243048600365937",
            "extra": "mean: 38.240320269228896 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.24388054350072,
            "unit": "iter/sec",
            "range": "stddev: 0.0003797160090311665",
            "extra": "mean: 13.469123551726037 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.27201195216641,
            "unit": "iter/sec",
            "range": "stddev: 0.0007389849689016138",
            "extra": "mean: 38.063320076920846 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 72.14173611865724,
            "unit": "iter/sec",
            "range": "stddev: 0.0005290207153639332",
            "extra": "mean: 13.861601533337382 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.413632213611415,
            "unit": "iter/sec",
            "range": "stddev: 0.00043663196346674875",
            "extra": "mean: 23.034239454547908 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 98.41067378736561,
            "unit": "iter/sec",
            "range": "stddev: 0.00022301737894865078",
            "extra": "mean: 10.161499373133896 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.640499545702696,
            "unit": "iter/sec",
            "range": "stddev: 0.00037748799877097497",
            "extra": "mean: 17.972520163637416 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 150.14329384514969,
            "unit": "iter/sec",
            "range": "stddev: 0.00035801635799621656",
            "extra": "mean: 6.660304129409536 msec\nrounds: 85"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.28903876135967,
            "unit": "iter/sec",
            "range": "stddev: 0.00048600893499177716",
            "extra": "mean: 24.8206467750002 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 107.59460945829149,
            "unit": "iter/sec",
            "range": "stddev: 0.00041791512280171334",
            "extra": "mean: 9.294145915252798 msec\nrounds: 59"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.181332890672856,
            "unit": "iter/sec",
            "range": "stddev: 0.0003927714903272292",
            "extra": "mean: 24.88717840000092 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 100.36156467725672,
            "unit": "iter/sec",
            "range": "stddev: 0.00029598288873749416",
            "extra": "mean: 9.963973790323076 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.634390257312916,
            "unit": "iter/sec",
            "range": "stddev: 0.0003089256701863601",
            "extra": "mean: 30.642521343750673 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 94.93434060948287,
            "unit": "iter/sec",
            "range": "stddev: 0.00042421448376299067",
            "extra": "mean: 10.533596099998732 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.125934878874762,
            "unit": "iter/sec",
            "range": "stddev: 0.00044524471786477047",
            "extra": "mean: 32.127549064516685 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 99.61841043361925,
            "unit": "iter/sec",
            "range": "stddev: 0.0003968318626576648",
            "extra": "mean: 10.038305124998459 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.16281029610336,
            "unit": "iter/sec",
            "range": "stddev: 0.00023473476223512097",
            "extra": "mean: 28.439137588238136 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 127.74282980730962,
            "unit": "iter/sec",
            "range": "stddev: 0.00028681935073417424",
            "extra": "mean: 7.828228022726787 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.17134138757247,
            "unit": "iter/sec",
            "range": "stddev: 0.0003058838587171165",
            "extra": "mean: 43.156759173913514 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 83.57049058224403,
            "unit": "iter/sec",
            "range": "stddev: 0.0002601164214683341",
            "extra": "mean: 11.965946269226126 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.533154397417412,
            "unit": "iter/sec",
            "range": "stddev: 0.0007701672661642696",
            "extra": "mean: 44.3790506363642 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 80.52922194075057,
            "unit": "iter/sec",
            "range": "stddev: 0.0018637931696361188",
            "extra": "mean: 12.417852499999945 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.738376078328482,
            "unit": "iter/sec",
            "range": "stddev: 0.0005562578015686064",
            "extra": "mean: 43.97851440908663 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 90.66483161051055,
            "unit": "iter/sec",
            "range": "stddev: 0.0002511984484323243",
            "extra": "mean: 11.029634999995661 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.69723827034817,
            "unit": "iter/sec",
            "range": "stddev: 0.0003330574388793938",
            "extra": "mean: 22.884741452380858 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 125.83150064487725,
            "unit": "iter/sec",
            "range": "stddev: 0.0006579540789250642",
            "extra": "mean: 7.94713561290355 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 50.08968296629133,
            "unit": "iter/sec",
            "range": "stddev: 0.00021292483659001986",
            "extra": "mean: 19.96419104255394 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.87353001836098,
            "unit": "iter/sec",
            "range": "stddev: 0.00046488769236776667",
            "extra": "mean: 6.855253313429316 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.533216151758225,
            "unit": "iter/sec",
            "range": "stddev: 0.0003841789069084708",
            "extra": "mean: 23.51103656097876 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 137.0274585457974,
            "unit": "iter/sec",
            "range": "stddev: 0.00028048227276865605",
            "extra": "mean: 7.297807392857537 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.39253276476712,
            "unit": "iter/sec",
            "range": "stddev: 0.0008239020254181159",
            "extra": "mean: 23.58906002500305 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 136.15688180697038,
            "unit": "iter/sec",
            "range": "stddev: 0.000339531994153181",
            "extra": "mean: 7.344469017862058 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.56729063561002,
            "unit": "iter/sec",
            "range": "stddev: 0.0011429731255953013",
            "extra": "mean: 29.79090599999588 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 122.08386965960072,
            "unit": "iter/sec",
            "range": "stddev: 0.00015662545682284355",
            "extra": "mean: 8.191090295452145 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.07928593349693,
            "unit": "iter/sec",
            "range": "stddev: 0.0003151752692713328",
            "extra": "mean: 30.230398625000987 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 111.54728934188238,
            "unit": "iter/sec",
            "range": "stddev: 0.0002540891999915637",
            "extra": "mean: 8.964807714287796 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.0646274042627,
            "unit": "iter/sec",
            "range": "stddev: 0.0009198927705911237",
            "extra": "mean: 27.7280003142859 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 132.74834523632148,
            "unit": "iter/sec",
            "range": "stddev: 0.00028978352591881625",
            "extra": "mean: 7.533050586956684 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.497103918453167,
            "unit": "iter/sec",
            "range": "stddev: 0.0002639631736449874",
            "extra": "mean: 36.36746629629257 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.99586966188902,
            "unit": "iter/sec",
            "range": "stddev: 0.00020357079811479794",
            "extra": "mean: 8.849881000006832 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.85076922750046,
            "unit": "iter/sec",
            "range": "stddev: 0.00037316209395882283",
            "extra": "mean: 37.242880884611814 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 103.97795521145,
            "unit": "iter/sec",
            "range": "stddev: 0.00043096262570358856",
            "extra": "mean: 9.617423212126031 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.05403253020251,
            "unit": "iter/sec",
            "range": "stddev: 0.0010139680730531805",
            "extra": "mean: 36.9630663703691 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 105.65176315148769,
            "unit": "iter/sec",
            "range": "stddev: 0.0004798066992636621",
            "extra": "mean: 9.46505737501191 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 45.14884742892571,
            "unit": "iter/sec",
            "range": "stddev: 0.00048576727841014543",
            "extra": "mean: 22.148959651167655 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.00642526556825,
            "unit": "iter/sec",
            "range": "stddev: 0.00006511171738682679",
            "extra": "mean: 7.142529338229806 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.145555374254045,
            "unit": "iter/sec",
            "range": "stddev: 0.0004032362639960431",
            "extra": "mean: 20.347720000003733 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 175.80878518356508,
            "unit": "iter/sec",
            "range": "stddev: 0.00009606748185559782",
            "extra": "mean: 5.687997894734795 msec\nrounds: 76"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.24877207522231,
            "unit": "iter/sec",
            "range": "stddev: 0.00043094010243989136",
            "extra": "mean: 22.59949718604651 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 163.60774715402778,
            "unit": "iter/sec",
            "range": "stddev: 0.0002611163846579378",
            "extra": "mean: 6.112180000000578 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.2280835397488,
            "unit": "iter/sec",
            "range": "stddev: 0.0003304735988806716",
            "extra": "mean: 22.610068534877325 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 163.55046371545012,
            "unit": "iter/sec",
            "range": "stddev: 0.00036060664790353255",
            "extra": "mean: 6.114320786884648 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.52135181147503,
            "unit": "iter/sec",
            "range": "stddev: 0.0003278487053204329",
            "extra": "mean: 28.967579411753977 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 125.15010623563592,
            "unit": "iter/sec",
            "range": "stddev: 0.00031558672839649635",
            "extra": "mean: 7.990404723406097 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 33.21881534296519,
            "unit": "iter/sec",
            "range": "stddev: 0.00037411782048778615",
            "extra": "mean: 30.10342150000156 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 125.31006623106414,
            "unit": "iter/sec",
            "range": "stddev: 0.00034763116145999684",
            "extra": "mean: 7.9802048636384955 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 37.19991333868246,
            "unit": "iter/sec",
            "range": "stddev: 0.0004854961725157114",
            "extra": "mean: 26.88178305405208 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 148.12996610923193,
            "unit": "iter/sec",
            "range": "stddev: 0.0003467219357943488",
            "extra": "mean: 6.750828520831457 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 27.288710908625855,
            "unit": "iter/sec",
            "range": "stddev: 0.0005812499125561493",
            "extra": "mean: 36.64519014285515 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 112.56061521547394,
            "unit": "iter/sec",
            "range": "stddev: 0.0008127854083014695",
            "extra": "mean: 8.884102117651965 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.932154509338474,
            "unit": "iter/sec",
            "range": "stddev: 0.0004094949050328178",
            "extra": "mean: 37.13033800000142 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 115.21009121364514,
            "unit": "iter/sec",
            "range": "stddev: 0.0002873507902891875",
            "extra": "mean: 8.679795228575975 msec\nrounds: 35"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.19651322005768,
            "unit": "iter/sec",
            "range": "stddev: 0.00032141356052121933",
            "extra": "mean: 36.76941937036586 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 107.58773820390115,
            "unit": "iter/sec",
            "range": "stddev: 0.00036546609726183314",
            "extra": "mean: 9.294739500005027 msec\nrounds: 34"
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
          "id": "127d1b22d9de1e20cc865d381232f21fc2979fb3",
          "message": "update changelog",
          "timestamp": "2024-12-20T17:01:56+01:00",
          "tree_id": "e44c89bc2c7e3742cf81501e761e3b2407df769b",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/127d1b22d9de1e20cc865d381232f21fc2979fb3"
        },
        "date": 1734710917011,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.629355027609115,
            "unit": "iter/sec",
            "range": "stddev: 0.0001854270013104903",
            "extra": "mean: 25.887048833336245 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.05815337460939,
            "unit": "iter/sec",
            "range": "stddev: 0.00010304485910900041",
            "extra": "mean: 12.186479452380928 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.93928583695062,
            "unit": "iter/sec",
            "range": "stddev: 0.00024226122575427635",
            "extra": "mean: 20.859718340426767 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.9275667005139,
            "unit": "iter/sec",
            "range": "stddev: 0.000049407788829127835",
            "extra": "mean: 7.6965960757583005 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.64450132242125,
            "unit": "iter/sec",
            "range": "stddev: 0.00013615719024809525",
            "extra": "mean: 25.876902684206915 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.75833483652936,
            "unit": "iter/sec",
            "range": "stddev: 0.00005988996356960209",
            "extra": "mean: 8.080263857144539 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.0525978490188,
            "unit": "iter/sec",
            "range": "stddev: 0.00019760447616956115",
            "extra": "mean: 26.279414718745286 msec\nrounds: 32"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.35395151623939,
            "unit": "iter/sec",
            "range": "stddev: 0.00006686752923445217",
            "extra": "mean: 8.744778704546908 msec\nrounds: 44"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.31149104541675,
            "unit": "iter/sec",
            "range": "stddev: 0.0002838716144367826",
            "extra": "mean: 30.948742000002685 msec\nrounds: 28"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.80159525055642,
            "unit": "iter/sec",
            "range": "stddev: 0.0003008040256772698",
            "extra": "mean: 12.37599328205236 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.883471104497584,
            "unit": "iter/sec",
            "range": "stddev: 0.00019971033195193463",
            "extra": "mean: 32.379780000000366 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.34625741374128,
            "unit": "iter/sec",
            "range": "stddev: 0.00016733080255750335",
            "extra": "mean: 12.143842736842197 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.61632654493052,
            "unit": "iter/sec",
            "range": "stddev: 0.0010313139209109272",
            "extra": "mean: 29.74745020588229 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 94.19732269522147,
            "unit": "iter/sec",
            "range": "stddev: 0.00008785859680963125",
            "extra": "mean: 10.616012975607944 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.090410237612005,
            "unit": "iter/sec",
            "range": "stddev: 0.0003135747427225359",
            "extra": "mean: 38.32825896153972 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.28711887198872,
            "unit": "iter/sec",
            "range": "stddev: 0.0002761703665473142",
            "extra": "mean: 12.93876670000221 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.436690667911595,
            "unit": "iter/sec",
            "range": "stddev: 0.00019023612880605037",
            "extra": "mean: 37.82621707692722 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.78486544275322,
            "unit": "iter/sec",
            "range": "stddev: 0.00033553687185315385",
            "extra": "mean: 13.371689500002997 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.429612505529743,
            "unit": "iter/sec",
            "range": "stddev: 0.00028408925890873994",
            "extra": "mean: 37.83634738461545 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.87850214242017,
            "unit": "iter/sec",
            "range": "stddev: 0.00022643542780325258",
            "extra": "mean: 13.35496800000063 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.458599465141646,
            "unit": "iter/sec",
            "range": "stddev: 0.0003168032504195595",
            "extra": "mean: 22.49283630232354 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.38104263472734,
            "unit": "iter/sec",
            "range": "stddev: 0.00011613341384418827",
            "extra": "mean: 9.76743324999899 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.299426262396196,
            "unit": "iter/sec",
            "range": "stddev: 0.000398607066612536",
            "extra": "mean: 17.452181727276184 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 154.13812438919499,
            "unit": "iter/sec",
            "range": "stddev: 0.00012979124500156635",
            "extra": "mean: 6.487687611113162 msec\nrounds: 90"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.41521193461238,
            "unit": "iter/sec",
            "range": "stddev: 0.0002895489866441635",
            "extra": "mean: 24.14571731707738 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 109.39056108304047,
            "unit": "iter/sec",
            "range": "stddev: 0.0002578880746428475",
            "extra": "mean: 9.141556548383374 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.80619597607464,
            "unit": "iter/sec",
            "range": "stddev: 0.0004162198922235211",
            "extra": "mean: 24.506082374998073 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 105.94639366404016,
            "unit": "iter/sec",
            "range": "stddev: 0.00015170663185915215",
            "extra": "mean: 9.43873562295132 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.60300797366912,
            "unit": "iter/sec",
            "range": "stddev: 0.0005561393216514505",
            "extra": "mean: 30.672016545455598 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 107.20465789330636,
            "unit": "iter/sec",
            "range": "stddev: 0.0001867577804010756",
            "extra": "mean: 9.327952904763086 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.097449767362324,
            "unit": "iter/sec",
            "range": "stddev: 0.0005454856775620027",
            "extra": "mean: 32.15697774193461 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 104.81620257453397,
            "unit": "iter/sec",
            "range": "stddev: 0.00024254695029219517",
            "extra": "mean: 9.540509725000845 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.97063787080147,
            "unit": "iter/sec",
            "range": "stddev: 0.0004448294837806452",
            "extra": "mean: 27.80045223528639 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 139.73302875097988,
            "unit": "iter/sec",
            "range": "stddev: 0.00019449872802490735",
            "extra": "mean: 7.156504148937567 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.25558567722443,
            "unit": "iter/sec",
            "range": "stddev: 0.00036950329095746567",
            "extra": "mean: 43.00042208695518 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 95.37722554628971,
            "unit": "iter/sec",
            "range": "stddev: 0.0003404547725269623",
            "extra": "mean: 10.484683259261585 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.513535961613016,
            "unit": "iter/sec",
            "range": "stddev: 0.0015008659309817813",
            "extra": "mean: 44.41772281817758 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.94530971161562,
            "unit": "iter/sec",
            "range": "stddev: 0.0002950958008257048",
            "extra": "mean: 11.242863769233772 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.815172756879015,
            "unit": "iter/sec",
            "range": "stddev: 0.0010963125747200724",
            "extra": "mean: 43.830481173914826 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.50108776746828,
            "unit": "iter/sec",
            "range": "stddev: 0.0002293418696602314",
            "extra": "mean: 10.69506274073454 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.160070289234945,
            "unit": "iter/sec",
            "range": "stddev: 0.000826761003442326",
            "extra": "mean: 22.14345534883668 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 124.94212772821497,
            "unit": "iter/sec",
            "range": "stddev: 0.0005817525472081636",
            "extra": "mean: 8.00370554097884 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.50661549003439,
            "unit": "iter/sec",
            "range": "stddev: 0.0006297078919065182",
            "extra": "mean: 20.19932063829527 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.0839127901173,
            "unit": "iter/sec",
            "range": "stddev: 0.000049911788836456724",
            "extra": "mean: 6.7076318382374085 msec\nrounds: 68"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.304792020522875,
            "unit": "iter/sec",
            "range": "stddev: 0.00032577159363152467",
            "extra": "mean: 23.637984073172625 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 143.12740052715213,
            "unit": "iter/sec",
            "range": "stddev: 0.00010834786904025868",
            "extra": "mean: 6.9867823793131345 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.38999856308613,
            "unit": "iter/sec",
            "range": "stddev: 0.0003414744187685785",
            "extra": "mean: 23.590470249999385 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 144.35263544933534,
            "unit": "iter/sec",
            "range": "stddev: 0.00005008625452440981",
            "extra": "mean: 6.927480034481105 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.30173046751919,
            "unit": "iter/sec",
            "range": "stddev: 0.0003671838964215432",
            "extra": "mean: 29.153048151518608 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 122.56340913383363,
            "unit": "iter/sec",
            "range": "stddev: 0.0001281044208294518",
            "extra": "mean: 8.15904197726783 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.85542975157097,
            "unit": "iter/sec",
            "range": "stddev: 0.00044515754183570934",
            "extra": "mean: 30.43636949999673 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.58777528174772,
            "unit": "iter/sec",
            "range": "stddev: 0.00022835847393282263",
            "extra": "mean: 8.504285395347749 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.95092280736977,
            "unit": "iter/sec",
            "range": "stddev: 0.0004495231524819066",
            "extra": "mean: 27.81569767647257 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.7973085828972,
            "unit": "iter/sec",
            "range": "stddev: 0.0001428145604349829",
            "extra": "mean: 7.363916195655323 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.607083718793458,
            "unit": "iter/sec",
            "range": "stddev: 0.00040474604640702",
            "extra": "mean: 36.22258729629064 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.54060477100543,
            "unit": "iter/sec",
            "range": "stddev: 0.00023883480989292854",
            "extra": "mean: 8.965344970587305 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.82482667008981,
            "unit": "iter/sec",
            "range": "stddev: 0.0009115162004336349",
            "extra": "mean: 37.27889884615802 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 105.01888363647423,
            "unit": "iter/sec",
            "range": "stddev: 0.00020726520159482847",
            "extra": "mean: 9.522097030297214 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.212749822363193,
            "unit": "iter/sec",
            "range": "stddev: 0.0003020432420352812",
            "extra": "mean: 36.747480740744884 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 109.31924402048085,
            "unit": "iter/sec",
            "range": "stddev: 0.0001796534721966196",
            "extra": "mean: 9.147520264708847 msec\nrounds: 34"
          },
          {
            "name": "equator-int8-none",
            "value": 45.49991126327694,
            "unit": "iter/sec",
            "range": "stddev: 0.00016369918629836793",
            "extra": "mean: 21.97806484091106 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.800543854463,
            "unit": "iter/sec",
            "range": "stddev: 0.000041168279627354396",
            "extra": "mean: 7.102245294120735 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.08776746607166,
            "unit": "iter/sec",
            "range": "stddev: 0.0006440817400383164",
            "extra": "mean: 19.964954530612246 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 175.80127712326262,
            "unit": "iter/sec",
            "range": "stddev: 0.00006716570014180717",
            "extra": "mean: 5.688240815786864 msec\nrounds: 76"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.50614620148382,
            "unit": "iter/sec",
            "range": "stddev: 0.00020814841513622231",
            "extra": "mean: 22.46880679070479 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 172.3316119518104,
            "unit": "iter/sec",
            "range": "stddev: 0.00011125844206466472",
            "extra": "mean: 5.802765892305545 msec\nrounds: 65"
          },
          {
            "name": "equator-int16-none",
            "value": 44.257255284065145,
            "unit": "iter/sec",
            "range": "stddev: 0.0004977172022120542",
            "extra": "mean: 22.595165325583366 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 172.44912550502727,
            "unit": "iter/sec",
            "range": "stddev: 0.0000927275591284278",
            "extra": "mean: 5.798811661534623 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.481297397021706,
            "unit": "iter/sec",
            "range": "stddev: 0.0010399061923031582",
            "extra": "mean: 29.001228941181726 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.0301321629647,
            "unit": "iter/sec",
            "range": "stddev: 0.00029841357857035523",
            "extra": "mean: 7.461008833328009 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.13880150557932,
            "unit": "iter/sec",
            "range": "stddev: 0.00031822966868708856",
            "extra": "mean: 30.176106393939374 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.68970360128029,
            "unit": "iter/sec",
            "range": "stddev: 0.00017192371844461146",
            "extra": "mean: 7.770629444437165 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.17641704378917,
            "unit": "iter/sec",
            "range": "stddev: 0.0008890766228412872",
            "extra": "mean: 26.898772918921292 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 146.50543683969403,
            "unit": "iter/sec",
            "range": "stddev: 0.00142646350827409",
            "extra": "mean: 6.825685254904213 msec\nrounds: 51"
          },
          {
            "name": "equator-float64-none",
            "value": 27.945411321742316,
            "unit": "iter/sec",
            "range": "stddev: 0.0003334080751502907",
            "extra": "mean: 35.78405014285733 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 124.0469331984316,
            "unit": "iter/sec",
            "range": "stddev: 0.000135651983373863",
            "extra": "mean: 8.061464916672712 msec\nrounds: 36"
          },
          {
            "name": "equator-int64-none",
            "value": 27.100975062269896,
            "unit": "iter/sec",
            "range": "stddev: 0.00045688079464427725",
            "extra": "mean: 36.89904137036769 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 114.44090447521279,
            "unit": "iter/sec",
            "range": "stddev: 0.0007870370177623658",
            "extra": "mean: 8.73813436363214 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.28331805050434,
            "unit": "iter/sec",
            "range": "stddev: 0.0003873277943420255",
            "extra": "mean: 36.65243348147366 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.60477565703891,
            "unit": "iter/sec",
            "range": "stddev: 0.00018555219482489506",
            "extra": "mean: 8.50305605714701 msec\nrounds: 35"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "42996815+MarcelCode@users.noreply.github.com",
            "name": "MarcelCode",
            "username": "MarcelCode"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ac4492d44dd1c838ec6f33d673bf6120732ce6a6",
          "message": "Fix issue #774: Use coverage array for calculation of valid_percent statistics (#775)",
          "timestamp": "2025-01-06T10:26:18+01:00",
          "tree_id": "dd29d7239dc25b398aa06c839fd7d176ed1f01a2",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ac4492d44dd1c838ec6f33d673bf6120732ce6a6"
        },
        "date": 1736155976319,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.14902657564096,
            "unit": "iter/sec",
            "range": "stddev: 0.0007455032977252197",
            "extra": "mean: 26.212988633333133 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.85234890204154,
            "unit": "iter/sec",
            "range": "stddev: 0.00020021084705896963",
            "extra": "mean: 12.217120380952906 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.19885081059332,
            "unit": "iter/sec",
            "range": "stddev: 0.00023780053367778654",
            "extra": "mean: 21.186956521737173 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.8701973351798,
            "unit": "iter/sec",
            "range": "stddev: 0.000041009750081371445",
            "extra": "mean: 7.699995999999269 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.146427340065465,
            "unit": "iter/sec",
            "range": "stddev: 0.0024936676429518335",
            "extra": "mean: 27.665251411764803 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.32238617512353,
            "unit": "iter/sec",
            "range": "stddev: 0.0004587264679346453",
            "extra": "mean: 8.175118482142299 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.05167043115371,
            "unit": "iter/sec",
            "range": "stddev: 0.00048321834451895275",
            "extra": "mean: 26.28005521621671 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.85482062048902,
            "unit": "iter/sec",
            "range": "stddev: 0.00007073305108412135",
            "extra": "mean: 8.783115150945505 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.751428220723398,
            "unit": "iter/sec",
            "range": "stddev: 0.0004856886828863347",
            "extra": "mean: 31.49464625806419 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.64278256784638,
            "unit": "iter/sec",
            "range": "stddev: 0.0001655121254175078",
            "extra": "mean: 12.400365763156548 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.55482465019875,
            "unit": "iter/sec",
            "range": "stddev: 0.00039944809274459857",
            "extra": "mean: 32.72805560000146 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.56311522905904,
            "unit": "iter/sec",
            "range": "stddev: 0.0005465643848023709",
            "extra": "mean: 12.412628249997226 msec\nrounds: 36"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.57210840953393,
            "unit": "iter/sec",
            "range": "stddev: 0.0005671632008887034",
            "extra": "mean: 29.78663084848184 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.03594640595081,
            "unit": "iter/sec",
            "range": "stddev: 0.0007568826771278013",
            "extra": "mean: 10.86531990000097 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.266369989769824,
            "unit": "iter/sec",
            "range": "stddev: 0.00014099256422850639",
            "extra": "mean: 38.071495999998405 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 75.3430095078493,
            "unit": "iter/sec",
            "range": "stddev: 0.0002359836608366295",
            "extra": "mean: 13.272631482763098 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.156811760538627,
            "unit": "iter/sec",
            "range": "stddev: 0.0002703593739177454",
            "extra": "mean: 38.23095907692566 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.885573906997,
            "unit": "iter/sec",
            "range": "stddev: 0.00018086820903363571",
            "extra": "mean: 13.353706833333945 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.475051108303315,
            "unit": "iter/sec",
            "range": "stddev: 0.00017162477344565932",
            "extra": "mean: 37.77140961538586 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.09709137499814,
            "unit": "iter/sec",
            "range": "stddev: 0.000229986703054277",
            "extra": "mean: 13.495806399998855 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.75710496637493,
            "unit": "iter/sec",
            "range": "stddev: 0.0004547907192387498",
            "extra": "mean: 22.342821340908422 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.43131882159442,
            "unit": "iter/sec",
            "range": "stddev: 0.00040338263743536153",
            "extra": "mean: 9.762639117648279 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.56879800289147,
            "unit": "iter/sec",
            "range": "stddev: 0.0006640933044815068",
            "extra": "mean: 17.370520745452662 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 158.15180399824584,
            "unit": "iter/sec",
            "range": "stddev: 0.00004141822744841224",
            "extra": "mean: 6.32303884444525 msec\nrounds: 90"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.62470289587935,
            "unit": "iter/sec",
            "range": "stddev: 0.00026460760825197676",
            "extra": "mean: 24.02419549999948 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 112.19062235813443,
            "unit": "iter/sec",
            "range": "stddev: 0.00026118615891532226",
            "extra": "mean: 8.91340095081926 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.292378013992355,
            "unit": "iter/sec",
            "range": "stddev: 0.0009147794586930681",
            "extra": "mean: 24.217544449998485 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.2430956247844,
            "unit": "iter/sec",
            "range": "stddev: 0.00018979291944201348",
            "extra": "mean: 9.41237634426307 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.898215030234915,
            "unit": "iter/sec",
            "range": "stddev: 0.00018744889627381422",
            "extra": "mean: 30.396785937503168 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 108.93891309731572,
            "unit": "iter/sec",
            "range": "stddev: 0.0004019264324231086",
            "extra": "mean: 9.17945637209263 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.68303626606508,
            "unit": "iter/sec",
            "range": "stddev: 0.0006085418323283816",
            "extra": "mean: 31.562631548387156 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.05427044183206,
            "unit": "iter/sec",
            "range": "stddev: 0.00010273231388423206",
            "extra": "mean: 9.254608780486112 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.80776623613097,
            "unit": "iter/sec",
            "range": "stddev: 0.0011787186456490883",
            "extra": "mean: 27.926902600000044 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 129.92527474923943,
            "unit": "iter/sec",
            "range": "stddev: 0.00029107822649808174",
            "extra": "mean: 7.696731847825889 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.811370767721275,
            "unit": "iter/sec",
            "range": "stddev: 0.0003892884286240625",
            "extra": "mean: 43.83778643478224 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 91.48275656473426,
            "unit": "iter/sec",
            "range": "stddev: 0.00019328345497415073",
            "extra": "mean: 10.931021730771615 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.332990425829625,
            "unit": "iter/sec",
            "range": "stddev: 0.0005101272160863074",
            "extra": "mean: 44.77680690909318 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 83.71334900787394,
            "unit": "iter/sec",
            "range": "stddev: 0.00032949323149524125",
            "extra": "mean: 11.945526153850823 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.60943036548922,
            "unit": "iter/sec",
            "range": "stddev: 0.0002255690438347965",
            "extra": "mean: 44.22933191304053 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 85.87679077440411,
            "unit": "iter/sec",
            "range": "stddev: 0.001003857989531714",
            "extra": "mean: 11.644589777777927 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.109329577533344,
            "unit": "iter/sec",
            "range": "stddev: 0.00038131493454867575",
            "extra": "mean: 22.670940809522985 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.5011738025056,
            "unit": "iter/sec",
            "range": "stddev: 0.0001120337574085316",
            "extra": "mean: 8.097089033332832 msec\nrounds: 60"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.33405758591214,
            "unit": "iter/sec",
            "range": "stddev: 0.0005059466740057251",
            "extra": "mean: 20.689345152174198 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 141.8040585465069,
            "unit": "iter/sec",
            "range": "stddev: 0.0005187719463632768",
            "extra": "mean: 7.0519843384597785 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.079171900919235,
            "unit": "iter/sec",
            "range": "stddev: 0.00027456139505384526",
            "extra": "mean: 23.76472622499861 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 141.78914198849992,
            "unit": "iter/sec",
            "range": "stddev: 0.00011116875157977158",
            "extra": "mean: 7.0527262241357445 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.49709828427871,
            "unit": "iter/sec",
            "range": "stddev: 0.0008528218799202901",
            "extra": "mean: 24.098070500000546 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 140.90547071724598,
            "unit": "iter/sec",
            "range": "stddev: 0.0004889983835113537",
            "extra": "mean: 7.096956526313255 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.65325006869331,
            "unit": "iter/sec",
            "range": "stddev: 0.00025044578815737223",
            "extra": "mean: 29.7148120303029 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 121.22076675576919,
            "unit": "iter/sec",
            "range": "stddev: 0.00015365189797833734",
            "extra": "mean: 8.24941160465319 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.27151478648752,
            "unit": "iter/sec",
            "range": "stddev: 0.0006307784589713435",
            "extra": "mean: 30.98707967742228 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 114.40975781212894,
            "unit": "iter/sec",
            "range": "stddev: 0.00024308072588054793",
            "extra": "mean: 8.74051321428448 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.59019228425583,
            "unit": "iter/sec",
            "range": "stddev: 0.0010004712670321375",
            "extra": "mean: 28.097628470593396 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 128.20049728172864,
            "unit": "iter/sec",
            "range": "stddev: 0.00019380586225059072",
            "extra": "mean: 7.800281755556979 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.222210274696696,
            "unit": "iter/sec",
            "range": "stddev: 0.0009466362289562539",
            "extra": "mean: 36.73470999999987 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 110.3020780507485,
            "unit": "iter/sec",
            "range": "stddev: 0.00015965372280938895",
            "extra": "mean: 9.066012333329871 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.69111323522308,
            "unit": "iter/sec",
            "range": "stddev: 0.00022250322415789202",
            "extra": "mean: 37.46565349999506 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 102.6941512116473,
            "unit": "iter/sec",
            "range": "stddev: 0.0002200812604769507",
            "extra": "mean: 9.737652906240513 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.90700386112511,
            "unit": "iter/sec",
            "range": "stddev: 0.0001970242844211148",
            "extra": "mean: 37.16504465384892 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 105.87057919861238,
            "unit": "iter/sec",
            "range": "stddev: 0.00017131875305508097",
            "extra": "mean: 9.44549475000045 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.99589343444026,
            "unit": "iter/sec",
            "range": "stddev: 0.00019895852985286474",
            "extra": "mean: 22.224250340912022 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.8220094289948,
            "unit": "iter/sec",
            "range": "stddev: 0.00007726568324422896",
            "extra": "mean: 7.2034687014920635 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.729830213102076,
            "unit": "iter/sec",
            "range": "stddev: 0.0001619252201848778",
            "extra": "mean: 20.10865502083566 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.96960069710352,
            "unit": "iter/sec",
            "range": "stddev: 0.0003337393401111757",
            "extra": "mean: 5.848993013510276 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.80731292285576,
            "unit": "iter/sec",
            "range": "stddev: 0.0005503529907194814",
            "extra": "mean: 22.827238953482265 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 169.49360324638332,
            "unit": "iter/sec",
            "range": "stddev: 0.00010449793971614883",
            "extra": "mean: 5.899927671880079 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.039067491021925,
            "unit": "iter/sec",
            "range": "stddev: 0.00029418898424606683",
            "extra": "mean: 22.70711113953233 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 170.19009310662335,
            "unit": "iter/sec",
            "range": "stddev: 0.00007039363236884238",
            "extra": "mean: 5.875782671870944 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.756086652050094,
            "unit": "iter/sec",
            "range": "stddev: 0.00030365400424880236",
            "extra": "mean: 29.62428703029969 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 133.879537157945,
            "unit": "iter/sec",
            "range": "stddev: 0.00010528780924202744",
            "extra": "mean: 7.469401382977932 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.63946958316306,
            "unit": "iter/sec",
            "range": "stddev: 0.0004044776302926738",
            "extra": "mean: 30.637752781247585 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 124.47890399170548,
            "unit": "iter/sec",
            "range": "stddev: 0.0002068032601779629",
            "extra": "mean: 8.033489755554355 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.483803324614584,
            "unit": "iter/sec",
            "range": "stddev: 0.0002640023103010551",
            "extra": "mean: 27.40942305555431 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 157.93101625650144,
            "unit": "iter/sec",
            "range": "stddev: 0.0001277427747043979",
            "extra": "mean: 6.331878459997142 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.390981277159064,
            "unit": "iter/sec",
            "range": "stddev: 0.00022080348691894553",
            "extra": "mean: 36.508367111107674 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 119.53580408467296,
            "unit": "iter/sec",
            "range": "stddev: 0.0001381086242010684",
            "extra": "mean: 8.365694342856907 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 26.710812654078868,
            "unit": "iter/sec",
            "range": "stddev: 0.00013962134599003186",
            "extra": "mean: 37.43802230769251 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 109.62273599795581,
            "unit": "iter/sec",
            "range": "stddev: 0.00021050553867969597",
            "extra": "mean: 9.122195235289944 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.798266162895473,
            "unit": "iter/sec",
            "range": "stddev: 0.0010161985423345714",
            "extra": "mean: 37.31584700000431 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.14039150657267,
            "unit": "iter/sec",
            "range": "stddev: 0.00015855364805942456",
            "extra": "mean: 8.761140441176915 msec\nrounds: 34"
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
          "id": "0b4aa5a14ad0d782945a67b905c64eb1403fc602",
          "message": "update changelog",
          "timestamp": "2025-01-06T10:27:48+01:00",
          "tree_id": "d49710ea5b63e072661a04e4ddb354831e2e7693",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/0b4aa5a14ad0d782945a67b905c64eb1403fc602"
        },
        "date": 1736156073141,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.73645604025034,
            "unit": "iter/sec",
            "range": "stddev: 0.00008050453890455806",
            "extra": "mean: 25.815474677418045 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.51010675137793,
            "unit": "iter/sec",
            "range": "stddev: 0.00008948319797075982",
            "extra": "mean: 12.119727380952636 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.28745410932124,
            "unit": "iter/sec",
            "range": "stddev: 0.00005874867033517615",
            "extra": "mean: 20.709312976741998 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.12697624729768,
            "unit": "iter/sec",
            "range": "stddev: 0.0001229635018246116",
            "extra": "mean: 7.684801636361444 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.86869818561683,
            "unit": "iter/sec",
            "range": "stddev: 0.00008827061299708645",
            "extra": "mean: 25.72764323684103 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 124.97152462442432,
            "unit": "iter/sec",
            "range": "stddev: 0.00003885503880367877",
            "extra": "mean: 8.00182283928511 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.39811439603795,
            "unit": "iter/sec",
            "range": "stddev: 0.0000921798996781038",
            "extra": "mean: 26.042945486489394 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 115.37572553703744,
            "unit": "iter/sec",
            "range": "stddev: 0.00003086384457740652",
            "extra": "mean: 8.667334444445023 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.45677197407336,
            "unit": "iter/sec",
            "range": "stddev: 0.0005743721123192112",
            "extra": "mean: 30.810211218749828 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.90372217070563,
            "unit": "iter/sec",
            "range": "stddev: 0.00007340746718280252",
            "extra": "mean: 12.062184589745165 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 31.183605420232933,
            "unit": "iter/sec",
            "range": "stddev: 0.0008111770361273243",
            "extra": "mean: 32.06813280645116 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 83.89139360135847,
            "unit": "iter/sec",
            "range": "stddev: 0.000060093275801204475",
            "extra": "mean: 11.920173894736763 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 34.31070414973913,
            "unit": "iter/sec",
            "range": "stddev: 0.0009523628889750367",
            "extra": "mean: 29.145423411766476 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 95.12451182554706,
            "unit": "iter/sec",
            "range": "stddev: 0.00010146412422499425",
            "extra": "mean: 10.512537523808197 msec\nrounds: 42"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.759656307660165,
            "unit": "iter/sec",
            "range": "stddev: 0.00016941773566048193",
            "extra": "mean: 37.369687730770366 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 78.21124786095494,
            "unit": "iter/sec",
            "range": "stddev: 0.0005009920989667787",
            "extra": "mean: 12.785884733329073 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.755827704583965,
            "unit": "iter/sec",
            "range": "stddev: 0.0008263103759083199",
            "extra": "mean: 37.375035115384385 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 76.62976647109741,
            "unit": "iter/sec",
            "range": "stddev: 0.00017494744769534608",
            "extra": "mean: 13.049759199999283 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 27.011374440950743,
            "unit": "iter/sec",
            "range": "stddev: 0.00012690212591696888",
            "extra": "mean: 37.021440807689686 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.1281650647951,
            "unit": "iter/sec",
            "range": "stddev: 0.00020569519113533107",
            "extra": "mean: 12.965432266668131 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.70024302898614,
            "unit": "iter/sec",
            "range": "stddev: 0.0007622434731755108",
            "extra": "mean: 22.371243023254795 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.90562319184392,
            "unit": "iter/sec",
            "range": "stddev: 0.000034051068255424096",
            "extra": "mean: 9.717641942031968 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 58.40224889957154,
            "unit": "iter/sec",
            "range": "stddev: 0.000053356418013689833",
            "extra": "mean: 17.122628303570966 msec\nrounds: 56"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 159.13948794669216,
            "unit": "iter/sec",
            "range": "stddev: 0.00003187469155774338",
            "extra": "mean: 6.283795511111458 msec\nrounds: 90"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 42.177359566193154,
            "unit": "iter/sec",
            "range": "stddev: 0.00009340841206142994",
            "extra": "mean: 23.709402634145455 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 117.81528048873011,
            "unit": "iter/sec",
            "range": "stddev: 0.00005765640716509107",
            "extra": "mean: 8.487863338708916 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.99753946915994,
            "unit": "iter/sec",
            "range": "stddev: 0.0001348687373566991",
            "extra": "mean: 23.810918749997967 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 110.2911618748242,
            "unit": "iter/sec",
            "range": "stddev: 0.00008417877922032134",
            "extra": "mean: 9.06690965079285 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 33.27166051289897,
            "unit": "iter/sec",
            "range": "stddev: 0.0009684179488445717",
            "extra": "mean: 30.055608424241814 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 112.13319441792692,
            "unit": "iter/sec",
            "range": "stddev: 0.00008826620225535871",
            "extra": "mean: 8.917965863640182 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-alpha",
            "value": 32.153850373898315,
            "unit": "iter/sec",
            "range": "stddev: 0.00013088269092377647",
            "extra": "mean: 31.10047438709781 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 109.49252397169316,
            "unit": "iter/sec",
            "range": "stddev: 0.0002183932566342091",
            "extra": "mean: 9.133043642856634 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-alpha",
            "value": 37.08920991731342,
            "unit": "iter/sec",
            "range": "stddev: 0.0003416547541323089",
            "extra": "mean: 26.962019472223787 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 144.34562529287797,
            "unit": "iter/sec",
            "range": "stddev: 0.0000814189975375759",
            "extra": "mean: 6.927816468084814 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.639030580581597,
            "unit": "iter/sec",
            "range": "stddev: 0.0005137379169405052",
            "extra": "mean: 42.302919173912954 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 98.1838029227689,
            "unit": "iter/sec",
            "range": "stddev: 0.00014614781438899578",
            "extra": "mean: 10.184979296295918 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 23.059365968736824,
            "unit": "iter/sec",
            "range": "stddev: 0.0001881928880641466",
            "extra": "mean: 43.366326782608375 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 92.28478359613759,
            "unit": "iter/sec",
            "range": "stddev: 0.00021804357929233858",
            "extra": "mean: 10.83602259258972 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 23.228679989843275,
            "unit": "iter/sec",
            "range": "stddev: 0.00039279136247294627",
            "extra": "mean: 43.05022930434486 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 96.46833671053167,
            "unit": "iter/sec",
            "range": "stddev: 0.00012468454934984864",
            "extra": "mean: 10.366095592594867 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.13612023791481,
            "unit": "iter/sec",
            "range": "stddev: 0.0006019974032597344",
            "extra": "mean: 22.155205071436107 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.27754310415234,
            "unit": "iter/sec",
            "range": "stddev: 0.00012610879550200476",
            "extra": "mean: 7.856845564513224 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 50.03583364134023,
            "unit": "iter/sec",
            "range": "stddev: 0.000546931757662468",
            "extra": "mean: 19.985676808506046 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 150.1619142131344,
            "unit": "iter/sec",
            "range": "stddev: 0.00006816756926970192",
            "extra": "mean: 6.659478238807186 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 43.15618555315133,
            "unit": "iter/sec",
            "range": "stddev: 0.00007419173089015676",
            "extra": "mean: 23.171649374998537 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 144.84812673916397,
            "unit": "iter/sec",
            "range": "stddev: 0.00012274829453097827",
            "extra": "mean: 6.90378275861831 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 43.09574328071361,
            "unit": "iter/sec",
            "range": "stddev: 0.00010591086071631928",
            "extra": "mean: 23.204147878046324 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-mask",
            "value": 145.64567750987936,
            "unit": "iter/sec",
            "range": "stddev: 0.000027783937695458788",
            "extra": "mean: 6.8659778793103445 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.91952096944555,
            "unit": "iter/sec",
            "range": "stddev: 0.00037416165486442476",
            "extra": "mean: 28.63727715151065 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 124.89057538785565,
            "unit": "iter/sec",
            "range": "stddev: 0.000047038361630744785",
            "extra": "mean: 8.007009311106433 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.65993526445753,
            "unit": "iter/sec",
            "range": "stddev: 0.00011352402334760132",
            "extra": "mean: 29.7089103749979 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.83681103320319,
            "unit": "iter/sec",
            "range": "stddev: 0.0003352698456687804",
            "extra": "mean: 8.414900999999054 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.79092842335649,
            "unit": "iter/sec",
            "range": "stddev: 0.0008305249114343593",
            "extra": "mean: 27.18061334285754 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 140.88037748520748,
            "unit": "iter/sec",
            "range": "stddev: 0.000039839231211413746",
            "extra": "mean: 7.098220617026673 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 28.09281175376791,
            "unit": "iter/sec",
            "range": "stddev: 0.0003493748900782901",
            "extra": "mean: 35.596294481483376 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.72133090263853,
            "unit": "iter/sec",
            "range": "stddev: 0.0002250661645457682",
            "extra": "mean: 8.871435352938976 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 27.629017377955,
            "unit": "iter/sec",
            "range": "stddev: 0.00027803100792299574",
            "extra": "mean: 36.193831518521286 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-mask",
            "value": 108.10528904802895,
            "unit": "iter/sec",
            "range": "stddev: 0.00012626495889780508",
            "extra": "mean: 9.250241212117944 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.83021104065527,
            "unit": "iter/sec",
            "range": "stddev: 0.00035643145288938516",
            "extra": "mean: 35.93217451851758 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 110.77115146360293,
            "unit": "iter/sec",
            "range": "stddev: 0.00011715794831582192",
            "extra": "mean: 9.027621242418691 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.78526071729853,
            "unit": "iter/sec",
            "range": "stddev: 0.00009152179567311474",
            "extra": "mean: 21.8410900000004 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 141.2933960068951,
            "unit": "iter/sec",
            "range": "stddev: 0.000027446827351233575",
            "extra": "mean: 7.077471617648712 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.6923699929103,
            "unit": "iter/sec",
            "range": "stddev: 0.00043102972376861805",
            "extra": "mean: 19.345214779998514 msec\nrounds: 50"
          },
          {
            "name": "dateline-uint8-none",
            "value": 176.33068730412523,
            "unit": "iter/sec",
            "range": "stddev: 0.00032515094621469754",
            "extra": "mean: 5.671162605265958 msec\nrounds: 76"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.91048127453879,
            "unit": "iter/sec",
            "range": "stddev: 0.0000817144375207045",
            "extra": "mean: 22.26651711628244 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 174.4321398752618,
            "unit": "iter/sec",
            "range": "stddev: 0.00023063994012038926",
            "extra": "mean: 5.732888450001876 msec\nrounds: 60"
          },
          {
            "name": "equator-int16-none",
            "value": 44.909765924905216,
            "unit": "iter/sec",
            "range": "stddev: 0.00009225932632174453",
            "extra": "mean: 22.266871790695276 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 175.45342360786472,
            "unit": "iter/sec",
            "range": "stddev: 0.000026897441727246107",
            "extra": "mean: 5.699518307690491 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 35.258052697359204,
            "unit": "iter/sec",
            "range": "stddev: 0.0001616363054509675",
            "extra": "mean: 28.36231508823229 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 137.70805822801802,
            "unit": "iter/sec",
            "range": "stddev: 0.00003307749835123237",
            "extra": "mean: 7.261739166666577 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.77490801595355,
            "unit": "iter/sec",
            "range": "stddev: 0.00024273274476944496",
            "extra": "mean: 29.607778636366703 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 134.1116688683083,
            "unit": "iter/sec",
            "range": "stddev: 0.0000522659907745899",
            "extra": "mean: 7.456472717388638 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 37.9960639672054,
            "unit": "iter/sec",
            "range": "stddev: 0.0006299834227322259",
            "extra": "mean: 26.318515540533493 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 165.86103390683107,
            "unit": "iter/sec",
            "range": "stddev: 0.000070743528866613",
            "extra": "mean: 6.029143653847768 msec\nrounds: 52"
          },
          {
            "name": "equator-float64-none",
            "value": 28.426992242151982,
            "unit": "iter/sec",
            "range": "stddev: 0.00017023963545667302",
            "extra": "mean: 35.17783349999247 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 126.39065744517352,
            "unit": "iter/sec",
            "range": "stddev: 0.00012755579916071046",
            "extra": "mean: 7.911977200006146 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.7530166048938,
            "unit": "iter/sec",
            "range": "stddev: 0.0004644069690294425",
            "extra": "mean: 36.0321191111047 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 119.2027070796236,
            "unit": "iter/sec",
            "range": "stddev: 0.00010633399749561099",
            "extra": "mean: 8.389071225807246 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.916513255946338,
            "unit": "iter/sec",
            "range": "stddev: 0.0008950419283212215",
            "extra": "mean: 35.821092370373144 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 121.46355434510549,
            "unit": "iter/sec",
            "range": "stddev: 0.00012226982223378512",
            "extra": "mean: 8.232922257146974 msec\nrounds: 35"
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
          "id": "acab661453fc96970cf307287894a4094f8a5699",
          "message": "Bump version: 7.2.2 → 7.3.0",
          "timestamp": "2025-01-07T10:44:31+01:00",
          "tree_id": "9c9eaebc93434695ce4728eeee4e1b7e0080add6",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/acab661453fc96970cf307287894a4094f8a5699"
        },
        "date": 1736243491489,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.6956916703099,
            "unit": "iter/sec",
            "range": "stddev: 0.0002743456638655287",
            "extra": "mean: 26.528230566667805 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.3036964541919,
            "unit": "iter/sec",
            "range": "stddev: 0.00007355700289071509",
            "extra": "mean: 12.150122571427568 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.12319039607426,
            "unit": "iter/sec",
            "range": "stddev: 0.0001036515019968626",
            "extra": "mean: 20.780002152176035 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.06558218813498,
            "unit": "iter/sec",
            "range": "stddev: 0.00009241130461207838",
            "extra": "mean: 7.68842904615256 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.11440021979981,
            "unit": "iter/sec",
            "range": "stddev: 0.0004901012674087331",
            "extra": "mean: 26.236802736843707 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.10050057882155,
            "unit": "iter/sec",
            "range": "stddev: 0.00046069665247217093",
            "extra": "mean: 8.257604181818579 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.578863574402845,
            "unit": "iter/sec",
            "range": "stddev: 0.0003323655030233406",
            "extra": "mean: 26.610703594590824 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.9603503704033,
            "unit": "iter/sec",
            "range": "stddev: 0.00007096883719976922",
            "extra": "mean: 8.774981796297729 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.38049077277296,
            "unit": "iter/sec",
            "range": "stddev: 0.00028108553418755995",
            "extra": "mean: 31.866933096777515 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.11207867310867,
            "unit": "iter/sec",
            "range": "stddev: 0.0003066859423940811",
            "extra": "mean: 12.640294842106258 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.06167067566707,
            "unit": "iter/sec",
            "range": "stddev: 0.0005811749228498087",
            "extra": "mean: 33.264950933330326 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.34020728869454,
            "unit": "iter/sec",
            "range": "stddev: 0.00035354522653138304",
            "extra": "mean: 12.447067710525062 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.82795530827752,
            "unit": "iter/sec",
            "range": "stddev: 0.00044355524780686535",
            "extra": "mean: 29.56134921212059 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 90.32094236113778,
            "unit": "iter/sec",
            "range": "stddev: 0.00019218502437159143",
            "extra": "mean: 11.071629390242812 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.19716388979947,
            "unit": "iter/sec",
            "range": "stddev: 0.0003658510843930812",
            "extra": "mean: 38.17207099999765 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.07494081561985,
            "unit": "iter/sec",
            "range": "stddev: 0.00030141329833401905",
            "extra": "mean: 13.144932999996211 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.028217841669225,
            "unit": "iter/sec",
            "range": "stddev: 0.0002258023482838243",
            "extra": "mean: 38.41984134615144 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.63348258575202,
            "unit": "iter/sec",
            "range": "stddev: 0.000245634547882951",
            "extra": "mean: 13.580778266672647 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.204165167171094,
            "unit": "iter/sec",
            "range": "stddev: 0.0002320717372249543",
            "extra": "mean: 38.16187211538464 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 75.36292563076793,
            "unit": "iter/sec",
            "range": "stddev: 0.0001068649179173886",
            "extra": "mean: 13.269123931034553 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.8963896476123,
            "unit": "iter/sec",
            "range": "stddev: 0.0006020714696657998",
            "extra": "mean: 23.311985186046115 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 95.84109854841323,
            "unit": "iter/sec",
            "range": "stddev: 0.0004370467039608371",
            "extra": "mean: 10.433937164178678 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.96398410857825,
            "unit": "iter/sec",
            "range": "stddev: 0.0003506438383860105",
            "extra": "mean: 17.868634907405 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 153.94140374402699,
            "unit": "iter/sec",
            "range": "stddev: 0.00011652053576116807",
            "extra": "mean: 6.4959781818203695 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.74787629377786,
            "unit": "iter/sec",
            "range": "stddev: 0.0002213050929628833",
            "extra": "mean: 24.54115627500073 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 110.8388244549663,
            "unit": "iter/sec",
            "range": "stddev: 0.0003222605176889684",
            "extra": "mean: 9.022109399999087 msec\nrounds: 60"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.26521841722286,
            "unit": "iter/sec",
            "range": "stddev: 0.00045202678411820126",
            "extra": "mean: 24.835330324999916 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.35301061725715,
            "unit": "iter/sec",
            "range": "stddev: 0.0001145550458692174",
            "extra": "mean: 9.31506246774274 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.20311114055371,
            "unit": "iter/sec",
            "range": "stddev: 0.00023793565926691346",
            "extra": "mean: 31.052900312500853 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 103.12342159014617,
            "unit": "iter/sec",
            "range": "stddev: 0.0003086518698692448",
            "extra": "mean: 9.697118119047689 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.79430108880154,
            "unit": "iter/sec",
            "range": "stddev: 0.0001553961150639797",
            "extra": "mean: 32.47354103333275 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 98.2761037307936,
            "unit": "iter/sec",
            "range": "stddev: 0.00042691819669497344",
            "extra": "mean: 10.175413574995673 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.8239785232903,
            "unit": "iter/sec",
            "range": "stddev: 0.000504935681036295",
            "extra": "mean: 27.914264166663354 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 137.68374745390327,
            "unit": "iter/sec",
            "range": "stddev: 0.00020879357022408532",
            "extra": "mean: 7.263021369568705 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.241067249567855,
            "unit": "iter/sec",
            "range": "stddev: 0.0006797360400167173",
            "extra": "mean: 43.02728395653147 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 92.89543169987819,
            "unit": "iter/sec",
            "range": "stddev: 0.00016656949837424856",
            "extra": "mean: 10.76479200000651 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.395058575111076,
            "unit": "iter/sec",
            "range": "stddev: 0.00038741667032680775",
            "extra": "mean: 44.65270750000885 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.53237027256442,
            "unit": "iter/sec",
            "range": "stddev: 0.00027016797476338126",
            "extra": "mean: 11.295303592587683 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.969392778793367,
            "unit": "iter/sec",
            "range": "stddev: 0.00020729891272977804",
            "extra": "mean: 43.53619660869991 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 90.49418087900388,
            "unit": "iter/sec",
            "range": "stddev: 0.00018674682641690318",
            "extra": "mean: 11.050434296289833 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.208260246649594,
            "unit": "iter/sec",
            "range": "stddev: 0.0003267132503883077",
            "extra": "mean: 22.11985142856964 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.25103036877898,
            "unit": "iter/sec",
            "range": "stddev: 0.00008865393751703925",
            "extra": "mean: 7.920727435483117 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.42473722841561,
            "unit": "iter/sec",
            "range": "stddev: 0.0006204301891597826",
            "extra": "mean: 20.232783340425595 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.00581727049936,
            "unit": "iter/sec",
            "range": "stddev: 0.00013102284219855957",
            "extra": "mean: 6.711147378794205 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.2389687460447,
            "unit": "iter/sec",
            "range": "stddev: 0.0004296921090208029",
            "extra": "mean: 23.67482042500484 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 137.90784327246593,
            "unit": "iter/sec",
            "range": "stddev: 0.000148343450659395",
            "extra": "mean: 7.2512191929815755 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.75017071028948,
            "unit": "iter/sec",
            "range": "stddev: 0.00043701184155875585",
            "extra": "mean: 23.95199787179664 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 142.8316192069207,
            "unit": "iter/sec",
            "range": "stddev: 0.00010415707989388757",
            "extra": "mean: 7.0012508823504715 msec\nrounds: 51"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.190203906692815,
            "unit": "iter/sec",
            "range": "stddev: 0.0003599580182890505",
            "extra": "mean: 29.248143787883276 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 112.56668418391963,
            "unit": "iter/sec",
            "range": "stddev: 0.0010847022328053185",
            "extra": "mean: 8.883623136363573 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.749494182016505,
            "unit": "iter/sec",
            "range": "stddev: 0.0008647968470171136",
            "extra": "mean: 30.53482274999908 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 116.88339217709341,
            "unit": "iter/sec",
            "range": "stddev: 0.00021740661071316137",
            "extra": "mean: 8.555535404763674 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.58681660593819,
            "unit": "iter/sec",
            "range": "stddev: 0.0003911065719345983",
            "extra": "mean: 28.100293742855747 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 117.64746083811161,
            "unit": "iter/sec",
            "range": "stddev: 0.0001337700639582953",
            "extra": "mean: 8.499970954545688 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.97871762277296,
            "unit": "iter/sec",
            "range": "stddev: 0.0008733071461780994",
            "extra": "mean: 37.06625400000079 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 108.8850673603195,
            "unit": "iter/sec",
            "range": "stddev: 0.00019814292508377483",
            "extra": "mean: 9.183995787878125 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.707906166532563,
            "unit": "iter/sec",
            "range": "stddev: 0.00023742485821916443",
            "extra": "mean: 37.44209649999037 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.08003908914169,
            "unit": "iter/sec",
            "range": "stddev: 0.00024162349408945072",
            "extra": "mean: 9.607990242428016 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.110752303092116,
            "unit": "iter/sec",
            "range": "stddev: 0.0002935193685477385",
            "extra": "mean: 36.885734074076026 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 109.75948687720135,
            "unit": "iter/sec",
            "range": "stddev: 0.00013815479234149074",
            "extra": "mean: 9.110829764709065 msec\nrounds: 34"
          },
          {
            "name": "equator-int8-none",
            "value": 44.83262807159459,
            "unit": "iter/sec",
            "range": "stddev: 0.00017922099026932833",
            "extra": "mean: 22.30518359091217 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.26233122079918,
            "unit": "iter/sec",
            "range": "stddev: 0.00009679083161367742",
            "extra": "mean: 7.232627941178293 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.91388781723626,
            "unit": "iter/sec",
            "range": "stddev: 0.0001867248575674853",
            "extra": "mean: 19.641006469387367 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 172.76320211238476,
            "unit": "iter/sec",
            "range": "stddev: 0.00017769264128557506",
            "extra": "mean: 5.788269653334434 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.068305263648384,
            "unit": "iter/sec",
            "range": "stddev: 0.0005770508708325395",
            "extra": "mean: 23.218930809521442 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 173.90613655472902,
            "unit": "iter/sec",
            "range": "stddev: 0.00004622126119847125",
            "extra": "mean: 5.750228369228912 msec\nrounds: 65"
          },
          {
            "name": "equator-int16-none",
            "value": 44.38113648491726,
            "unit": "iter/sec",
            "range": "stddev: 0.0005277686419085683",
            "extra": "mean: 22.532095372092275 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 175.12314700128448,
            "unit": "iter/sec",
            "range": "stddev: 0.00003253642622152523",
            "extra": "mean: 5.710267415378649 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.970266839171714,
            "unit": "iter/sec",
            "range": "stddev: 0.00019335184363217754",
            "extra": "mean: 28.595721176478317 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 133.23900973725512,
            "unit": "iter/sec",
            "range": "stddev: 0.00010264685067437693",
            "extra": "mean: 7.505309458333424 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.26366376556382,
            "unit": "iter/sec",
            "range": "stddev: 0.0007032608159055247",
            "extra": "mean: 30.06283393939453 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 133.66560277566316,
            "unit": "iter/sec",
            "range": "stddev: 0.00006179580629736065",
            "extra": "mean: 7.48135630434663 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 37.78240665358225,
            "unit": "iter/sec",
            "range": "stddev: 0.00041631310839478726",
            "extra": "mean: 26.46734521622082 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 163.00886805955886,
            "unit": "iter/sec",
            "range": "stddev: 0.00008297817826240892",
            "extra": "mean: 6.134635568628255 msec\nrounds: 51"
          },
          {
            "name": "equator-float64-none",
            "value": 27.533587416954155,
            "unit": "iter/sec",
            "range": "stddev: 0.0008377696255508832",
            "extra": "mean: 36.31927742856484 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 118.90480507459614,
            "unit": "iter/sec",
            "range": "stddev: 0.0003900426772359006",
            "extra": "mean: 8.41008905714651 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.05627494149367,
            "unit": "iter/sec",
            "range": "stddev: 0.00028599360342952934",
            "extra": "mean: 36.96000288888231 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 117.58742287684169,
            "unit": "iter/sec",
            "range": "stddev: 0.00013790462361054897",
            "extra": "mean: 8.504310882358368 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.31595151015715,
            "unit": "iter/sec",
            "range": "stddev: 0.000992954381756374",
            "extra": "mean: 36.60864603702934 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 116.73375693293004,
            "unit": "iter/sec",
            "range": "stddev: 0.00015286812101047024",
            "extra": "mean: 8.566502323527162 msec\nrounds: 34"
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
          "id": "b570b26ff2f5f8f86904f33d75d72bbba9328988",
          "message": "Xarray: add indexes options and better define band names (#764)\n\n* Xarray: add indexes options and better define band names\r\n\r\n* fix\r\n\r\n* Update rio_tiler/io/xarray.py\r\n\r\nCo-authored-by: Max Jones <14077947+maxrjones@users.noreply.github.com>\r\n\r\n* ds -> da\r\n\r\n---------\r\n\r\nCo-authored-by: Max Jones <14077947+maxrjones@users.noreply.github.com>",
          "timestamp": "2025-01-22T10:04:23+01:00",
          "tree_id": "a835e91b0e5e172b5d7e4ae1ad95e4d46aa40053",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/b570b26ff2f5f8f86904f33d75d72bbba9328988"
        },
        "date": 1737537044004,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 42.25270377227526,
            "unit": "iter/sec",
            "range": "stddev: 0.00008774492696407452",
            "extra": "mean: 23.667124484851662 msec\nrounds: 33"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 89.32183293506323,
            "unit": "iter/sec",
            "range": "stddev: 0.00009548893848831891",
            "extra": "mean: 11.195471108692963 msec\nrounds: 46"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 52.21589884616211,
            "unit": "iter/sec",
            "range": "stddev: 0.000615821604610978",
            "extra": "mean: 19.15125511764508 msec\nrounds: 51"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 141.53598280788302,
            "unit": "iter/sec",
            "range": "stddev: 0.00008045559651408765",
            "extra": "mean: 7.06534112500121 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 42.316508818031714,
            "unit": "iter/sec",
            "range": "stddev: 0.00014332429257732702",
            "extra": "mean: 23.631439074999605 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 135.4967174609442,
            "unit": "iter/sec",
            "range": "stddev: 0.000051819123958779364",
            "extra": "mean: 7.380252590165083 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-nodata",
            "value": 41.78760635465714,
            "unit": "iter/sec",
            "range": "stddev: 0.00009831616328322028",
            "extra": "mean: 23.930540349999063 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 124.59989205973578,
            "unit": "iter/sec",
            "range": "stddev: 0.00008093099975414328",
            "extra": "mean: 8.025689135593947 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 35.55944385769248,
            "unit": "iter/sec",
            "range": "stddev: 0.0002601353982062224",
            "extra": "mean: 28.12192462857297 msec\nrounds: 35"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 90.02778305539879,
            "unit": "iter/sec",
            "range": "stddev: 0.00007976178944502794",
            "extra": "mean: 11.107682162790212 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-nodata",
            "value": 33.97979285148073,
            "unit": "iter/sec",
            "range": "stddev: 0.0004085522918427312",
            "extra": "mean: 29.4292553333333 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 90.85669822284235,
            "unit": "iter/sec",
            "range": "stddev: 0.0000960373380516008",
            "extra": "mean: 11.006343170729368 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-nodata",
            "value": 37.4079279448806,
            "unit": "iter/sec",
            "range": "stddev: 0.0002846033832475398",
            "extra": "mean: 26.732301277779097 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 102.0063939103669,
            "unit": "iter/sec",
            "range": "stddev: 0.0004573798231897143",
            "extra": "mean: 9.803307044445672 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-nodata",
            "value": 28.895231603205797,
            "unit": "iter/sec",
            "range": "stddev: 0.0004669433252322385",
            "extra": "mean: 34.60778628571554 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 84.92013773138775,
            "unit": "iter/sec",
            "range": "stddev: 0.0002061467333211267",
            "extra": "mean: 11.775769878790305 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-nodata",
            "value": 29.065914156237234,
            "unit": "iter/sec",
            "range": "stddev: 0.00041915822362509683",
            "extra": "mean: 34.40456042857371 msec\nrounds: 28"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 82.8790652238089,
            "unit": "iter/sec",
            "range": "stddev: 0.00023390149453451242",
            "extra": "mean: 12.065773151513868 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 29.104230631911072,
            "unit": "iter/sec",
            "range": "stddev: 0.00040430539334835436",
            "extra": "mean: 34.35926593103475 msec\nrounds: 29"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 79.18035257555283,
            "unit": "iter/sec",
            "range": "stddev: 0.0012229481346604178",
            "extra": "mean: 12.629395645161008 msec\nrounds: 31"
          },
          {
            "name": "equator-int8-alpha",
            "value": 49.10736862136999,
            "unit": "iter/sec",
            "range": "stddev: 0.00011698894038473086",
            "extra": "mean: 20.363542744679485 msec\nrounds: 47"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 111.37896464394134,
            "unit": "iter/sec",
            "range": "stddev: 0.00006372102295175991",
            "extra": "mean: 8.978356040539804 msec\nrounds: 74"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 63.028592899800714,
            "unit": "iter/sec",
            "range": "stddev: 0.0005031369692887141",
            "extra": "mean: 15.86581508474643 msec\nrounds: 59"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 170.5754727938108,
            "unit": "iter/sec",
            "range": "stddev: 0.00016592781363542738",
            "extra": "mean: 5.862507567009858 msec\nrounds: 97"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 45.88026262905618,
            "unit": "iter/sec",
            "range": "stddev: 0.00015645167708178248",
            "extra": "mean: 21.795864772724627 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 122.46335837789522,
            "unit": "iter/sec",
            "range": "stddev: 0.0002789138230385391",
            "extra": "mean: 8.165707794116 msec\nrounds: 68"
          },
          {
            "name": "equator-int16-alpha",
            "value": 45.330961274473424,
            "unit": "iter/sec",
            "range": "stddev: 0.00054672021365614",
            "extra": "mean: 22.059977813951978 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 115.72651422410279,
            "unit": "iter/sec",
            "range": "stddev: 0.00013527881970467842",
            "extra": "mean: 8.641062134330893 msec\nrounds: 67"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 36.29732942046581,
            "unit": "iter/sec",
            "range": "stddev: 0.00037184311776275545",
            "extra": "mean: 27.550236228568433 msec\nrounds: 35"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 121.5565430165116,
            "unit": "iter/sec",
            "range": "stddev: 0.00015663862915416923",
            "extra": "mean: 8.226624212767925 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-alpha",
            "value": 34.835220427065806,
            "unit": "iter/sec",
            "range": "stddev: 0.0006739506222377589",
            "extra": "mean: 28.706578794117043 msec\nrounds: 34"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 118.26758767612613,
            "unit": "iter/sec",
            "range": "stddev: 0.0006284005207397298",
            "extra": "mean: 8.455402022221708 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-alpha",
            "value": 39.235583371722775,
            "unit": "iter/sec",
            "range": "stddev: 0.0011309262252985452",
            "extra": "mean: 25.487068473683088 msec\nrounds: 38"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 158.7565924686526,
            "unit": "iter/sec",
            "range": "stddev: 0.00009383845733759403",
            "extra": "mean: 6.29895101960856 msec\nrounds: 51"
          },
          {
            "name": "equator-float64-alpha",
            "value": 25.111970560157502,
            "unit": "iter/sec",
            "range": "stddev: 0.0009469911415482168",
            "extra": "mean: 39.82164591999776 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 104.23173774680919,
            "unit": "iter/sec",
            "range": "stddev: 0.0001260514608848254",
            "extra": "mean: 9.594006793104748 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-alpha",
            "value": 25.11270473902266,
            "unit": "iter/sec",
            "range": "stddev: 0.0004262511475060699",
            "extra": "mean: 39.820481719999634 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 97.82816151492561,
            "unit": "iter/sec",
            "range": "stddev: 0.0001978572237104712",
            "extra": "mean: 10.222005448271972 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 25.26476217628659,
            "unit": "iter/sec",
            "range": "stddev: 0.0008410791523587488",
            "extra": "mean: 39.580819839998185 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 98.59417992638289,
            "unit": "iter/sec",
            "range": "stddev: 0.001230346244530717",
            "extra": "mean: 10.142586517243389 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-mask",
            "value": 49.35804248587145,
            "unit": "iter/sec",
            "range": "stddev: 0.00028744514852859236",
            "extra": "mean: 20.260122760870146 msec\nrounds: 46"
          },
          {
            "name": "dateline-int8-mask",
            "value": 138.174193756003,
            "unit": "iter/sec",
            "range": "stddev: 0.00006446544917625942",
            "extra": "mean: 7.237241432838502 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-mask",
            "value": 54.158846284125865,
            "unit": "iter/sec",
            "range": "stddev: 0.0007607866772789209",
            "extra": "mean: 18.464204254903105 msec\nrounds: 51"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 162.43195363903246,
            "unit": "iter/sec",
            "range": "stddev: 0.000073758850438175",
            "extra": "mean: 6.156424136979041 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-mask",
            "value": 46.605834556466085,
            "unit": "iter/sec",
            "range": "stddev: 0.0004513231957680317",
            "extra": "mean: 21.45654099999933 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 157.52526114470334,
            "unit": "iter/sec",
            "range": "stddev: 0.00003796108605968844",
            "extra": "mean: 6.34818817460265 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-mask",
            "value": 46.374867442451716,
            "unit": "iter/sec",
            "range": "stddev: 0.0005733004485619404",
            "extra": "mean: 21.563403954543634 msec\nrounds: 44"
          },
          {
            "name": "dateline-int16-mask",
            "value": 153.90205503177486,
            "unit": "iter/sec",
            "range": "stddev: 0.0006058173632623675",
            "extra": "mean: 6.4976390327831455 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-mask",
            "value": 38.06523044832089,
            "unit": "iter/sec",
            "range": "stddev: 0.0003730846790732132",
            "extra": "mean: 26.270693444445214 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 134.5264079621919,
            "unit": "iter/sec",
            "range": "stddev: 0.00009560421667108333",
            "extra": "mean: 7.43348473469273 msec\nrounds: 49"
          },
          {
            "name": "equator-int32-mask",
            "value": 36.55330357557053,
            "unit": "iter/sec",
            "range": "stddev: 0.00018756981876069957",
            "extra": "mean: 27.357308428569077 msec\nrounds: 35"
          },
          {
            "name": "dateline-int32-mask",
            "value": 131.49420657393966,
            "unit": "iter/sec",
            "range": "stddev: 0.00008751586470622167",
            "extra": "mean: 7.604897782608364 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-mask",
            "value": 40.048499871565895,
            "unit": "iter/sec",
            "range": "stddev: 0.00037518359502352293",
            "extra": "mean: 24.969724289473117 msec\nrounds: 38"
          },
          {
            "name": "dateline-float32-mask",
            "value": 151.76409245566362,
            "unit": "iter/sec",
            "range": "stddev: 0.00008407841333790179",
            "extra": "mean: 6.589173919991254 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-mask",
            "value": 30.65607429404192,
            "unit": "iter/sec",
            "range": "stddev: 0.0003814220602559649",
            "extra": "mean: 32.619962699997515 msec\nrounds: 30"
          },
          {
            "name": "dateline-float64-mask",
            "value": 123.16178976092748,
            "unit": "iter/sec",
            "range": "stddev: 0.00012911609134885773",
            "extra": "mean: 8.11940133332851 msec\nrounds: 36"
          },
          {
            "name": "equator-int64-mask",
            "value": 29.92764080557951,
            "unit": "iter/sec",
            "range": "stddev: 0.0004490593793732948",
            "extra": "mean: 33.41392682758898 msec\nrounds: 29"
          },
          {
            "name": "dateline-int64-mask",
            "value": 117.42801987749068,
            "unit": "iter/sec",
            "range": "stddev: 0.00011476524170958154",
            "extra": "mean: 8.51585508333762 msec\nrounds: 36"
          },
          {
            "name": "equator-uint64-mask",
            "value": 30.02616969128706,
            "unit": "iter/sec",
            "range": "stddev: 0.0007997286826656149",
            "extra": "mean: 33.30428124137919 msec\nrounds: 29"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 118.75310689938934,
            "unit": "iter/sec",
            "range": "stddev: 0.00038484565642726875",
            "extra": "mean: 8.420832314284 msec\nrounds: 35"
          },
          {
            "name": "equator-int8-none",
            "value": 49.85480546118927,
            "unit": "iter/sec",
            "range": "stddev: 0.00033595154222277826",
            "extra": "mean: 20.058246958329324 msec\nrounds: 48"
          },
          {
            "name": "dateline-int8-none",
            "value": 152.30777025605954,
            "unit": "iter/sec",
            "range": "stddev: 0.00023543979227739174",
            "extra": "mean: 6.565653205472064 msec\nrounds: 73"
          },
          {
            "name": "equator-uint8-none",
            "value": 55.08163855147239,
            "unit": "iter/sec",
            "range": "stddev: 0.0006743486796894198",
            "extra": "mean: 18.15487023076711 msec\nrounds: 52"
          },
          {
            "name": "dateline-uint8-none",
            "value": 192.882261604999,
            "unit": "iter/sec",
            "range": "stddev: 0.00004246418623374103",
            "extra": "mean: 5.18450992682721 msec\nrounds: 82"
          },
          {
            "name": "equator-uint16-none",
            "value": 48.65298460263058,
            "unit": "iter/sec",
            "range": "stddev: 0.00022253526264516448",
            "extra": "mean: 20.553723644446915 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint16-none",
            "value": 189.63589910077388,
            "unit": "iter/sec",
            "range": "stddev: 0.00006114112762113462",
            "extra": "mean: 5.273263157144064 msec\nrounds: 70"
          },
          {
            "name": "equator-int16-none",
            "value": 48.144242192617355,
            "unit": "iter/sec",
            "range": "stddev: 0.0005039550121122906",
            "extra": "mean: 20.77091578260098 msec\nrounds: 46"
          },
          {
            "name": "dateline-int16-none",
            "value": 188.94113671134477,
            "unit": "iter/sec",
            "range": "stddev: 0.00006936083539725288",
            "extra": "mean: 5.292653666669488 msec\nrounds: 69"
          },
          {
            "name": "equator-uint32-none",
            "value": 38.26302448120963,
            "unit": "iter/sec",
            "range": "stddev: 0.0002258831048984509",
            "extra": "mean: 26.134891675672012 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint32-none",
            "value": 148.19670684685593,
            "unit": "iter/sec",
            "range": "stddev: 0.000109298797815293",
            "extra": "mean: 6.74778826923181 msec\nrounds: 52"
          },
          {
            "name": "equator-int32-none",
            "value": 36.629207665007584,
            "unit": "iter/sec",
            "range": "stddev: 0.00032484945164515",
            "extra": "mean: 27.300617833328527 msec\nrounds: 36"
          },
          {
            "name": "dateline-int32-none",
            "value": 144.99055630644594,
            "unit": "iter/sec",
            "range": "stddev: 0.000056650300691422324",
            "extra": "mean: 6.897000918366311 msec\nrounds: 49"
          },
          {
            "name": "equator-float32-none",
            "value": 41.287172566500324,
            "unit": "iter/sec",
            "range": "stddev: 0.0005123857622954161",
            "extra": "mean: 24.2205977749947 msec\nrounds: 40"
          },
          {
            "name": "dateline-float32-none",
            "value": 177.76192730336214,
            "unit": "iter/sec",
            "range": "stddev: 0.0005099695084576761",
            "extra": "mean: 5.625501563635929 msec\nrounds: 55"
          },
          {
            "name": "equator-float64-none",
            "value": 30.76718416769368,
            "unit": "iter/sec",
            "range": "stddev: 0.00041634016213603167",
            "extra": "mean: 32.502161866669134 msec\nrounds: 30"
          },
          {
            "name": "dateline-float64-none",
            "value": 136.81406114725374,
            "unit": "iter/sec",
            "range": "stddev: 0.00012161687533782399",
            "extra": "mean: 7.309190236840455 msec\nrounds: 38"
          },
          {
            "name": "equator-int64-none",
            "value": 29.90450373117412,
            "unit": "iter/sec",
            "range": "stddev: 0.0009344224571394352",
            "extra": "mean: 33.43977913793447 msec\nrounds: 29"
          },
          {
            "name": "dateline-int64-none",
            "value": 128.1255181293314,
            "unit": "iter/sec",
            "range": "stddev: 0.00011100732873475711",
            "extra": "mean: 7.804846486478893 msec\nrounds: 37"
          },
          {
            "name": "equator-uint64-none",
            "value": 29.98149611327725,
            "unit": "iter/sec",
            "range": "stddev: 0.0005519440575122497",
            "extra": "mean: 33.35390589654903 msec\nrounds: 29"
          },
          {
            "name": "dateline-uint64-none",
            "value": 127.9227736410481,
            "unit": "iter/sec",
            "range": "stddev: 0.0008975841513012039",
            "extra": "mean: 7.817216368416188 msec\nrounds: 38"
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
          "id": "4c1b2a6c4d4d469196d5e7f31d8c1772776519f8",
          "message": "make sure transform is an Affine object [backport 7.3.1]",
          "timestamp": "2025-01-23T09:29:07+01:00",
          "tree_id": "03587ec0d4002768f29d9c4d86a4401144fc9c09",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/4c1b2a6c4d4d469196d5e7f31d8c1772776519f8"
        },
        "date": 1737621356797,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.23483468657165,
            "unit": "iter/sec",
            "range": "stddev: 0.0006854677939919132",
            "extra": "mean: 26.15416041935202 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.27490888412994,
            "unit": "iter/sec",
            "range": "stddev: 0.00006818219455464471",
            "extra": "mean: 12.154373837208716 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.01224445328939,
            "unit": "iter/sec",
            "range": "stddev: 0.00007796145832192953",
            "extra": "mean: 20.828020255809733 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.8227800770702,
            "unit": "iter/sec",
            "range": "stddev: 0.00032673500992453616",
            "extra": "mean: 7.762602230767995 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.628035662679565,
            "unit": "iter/sec",
            "range": "stddev: 0.000655287073267176",
            "extra": "mean: 26.57592888889029 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.52880229538484,
            "unit": "iter/sec",
            "range": "stddev: 0.00005348912242821544",
            "extra": "mean: 8.095278035714923 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.05552669763514,
            "unit": "iter/sec",
            "range": "stddev: 0.00032666347265940845",
            "extra": "mean: 26.277392189191335 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.95950285727105,
            "unit": "iter/sec",
            "range": "stddev: 0.000045310099670670485",
            "extra": "mean: 8.775047055553175 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.2738915088944,
            "unit": "iter/sec",
            "range": "stddev: 0.0003431720801192386",
            "extra": "mean: 30.984797718750734 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.92758671434378,
            "unit": "iter/sec",
            "range": "stddev: 0.00015246529921335866",
            "extra": "mean: 12.20590084615444 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.997073039385196,
            "unit": "iter/sec",
            "range": "stddev: 0.0001525252322849669",
            "extra": "mean: 32.261110548385965 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 83.0832420250356,
            "unit": "iter/sec",
            "range": "stddev: 0.00012165895248083766",
            "extra": "mean: 12.036121552631135 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.81747433873252,
            "unit": "iter/sec",
            "range": "stddev: 0.0009948473911972854",
            "extra": "mean: 29.5705110909084 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.82442314863327,
            "unit": "iter/sec",
            "range": "stddev: 0.0001289393879928077",
            "extra": "mean: 10.658205682925821 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.998944000890134,
            "unit": "iter/sec",
            "range": "stddev: 0.0005427292167568832",
            "extra": "mean: 38.4631006538482 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.46006574108357,
            "unit": "iter/sec",
            "range": "stddev: 0.00013937848599259836",
            "extra": "mean: 13.078722733332407 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.536645947075932,
            "unit": "iter/sec",
            "range": "stddev: 0.0002020584023218405",
            "extra": "mean: 37.68373749999817 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.94025463142128,
            "unit": "iter/sec",
            "range": "stddev: 0.00026530188889238815",
            "extra": "mean: 13.343963199995793 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.567845590445685,
            "unit": "iter/sec",
            "range": "stddev: 0.00018173787661576575",
            "extra": "mean: 37.63948403703533 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 75.22646041998482,
            "unit": "iter/sec",
            "range": "stddev: 0.00019331278138331792",
            "extra": "mean: 13.29319490000008 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.648207232956786,
            "unit": "iter/sec",
            "range": "stddev: 0.00015370448278577005",
            "extra": "mean: 22.397315860464303 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.28796173670985,
            "unit": "iter/sec",
            "range": "stddev: 0.0000483915671064384",
            "extra": "mean: 9.681670382353836 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.70270975576591,
            "unit": "iter/sec",
            "range": "stddev: 0.00015464465197861647",
            "extra": "mean: 17.330208654543743 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 157.16077538843223,
            "unit": "iter/sec",
            "range": "stddev: 0.000041466068207030104",
            "extra": "mean: 6.36291083146186 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.598046658891356,
            "unit": "iter/sec",
            "range": "stddev: 0.00012005024431877951",
            "extra": "mean: 24.039590325000404 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 110.50991518932965,
            "unit": "iter/sec",
            "range": "stddev: 0.00024468548440604616",
            "extra": "mean: 9.048961790322283 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.79003281760946,
            "unit": "iter/sec",
            "range": "stddev: 0.00019689803343783625",
            "extra": "mean: 24.51579297500075 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.81418849920574,
            "unit": "iter/sec",
            "range": "stddev: 0.0002146161246705555",
            "extra": "mean: 9.726284033333835 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.24554729525507,
            "unit": "iter/sec",
            "range": "stddev: 0.0004781785210333126",
            "extra": "mean: 31.012033718750054 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 102.31196220685814,
            "unit": "iter/sec",
            "range": "stddev: 0.00034989847920693094",
            "extra": "mean: 9.774028162788655 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.972335943147876,
            "unit": "iter/sec",
            "range": "stddev: 0.0005921261499125305",
            "extra": "mean: 32.286876967742366 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 103.52498859257761,
            "unit": "iter/sec",
            "range": "stddev: 0.00022311609799859837",
            "extra": "mean: 9.659503600000363 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.823475777239175,
            "unit": "iter/sec",
            "range": "stddev: 0.00253954997359028",
            "extra": "mean: 28.71626044444437 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 138.14732638736578,
            "unit": "iter/sec",
            "range": "stddev: 0.0002580108226194378",
            "extra": "mean: 7.238648956520483 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.215563190302863,
            "unit": "iter/sec",
            "range": "stddev: 0.0006248815347648735",
            "extra": "mean: 43.0745526956546 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 93.43879301551343,
            "unit": "iter/sec",
            "range": "stddev: 0.00019568303956816492",
            "extra": "mean: 10.70219303703947 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.550966353176197,
            "unit": "iter/sec",
            "range": "stddev: 0.0003122221236227106",
            "extra": "mean: 44.34399769565328 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 90.63287897111587,
            "unit": "iter/sec",
            "range": "stddev: 0.00018971062514718933",
            "extra": "mean: 11.033523499994894 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.94221537331601,
            "unit": "iter/sec",
            "range": "stddev: 0.00020182618633183627",
            "extra": "mean: 43.587769695645676 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.5997071452063,
            "unit": "iter/sec",
            "range": "stddev: 0.0002275639325950073",
            "extra": "mean: 10.683794111114533 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.089367787188706,
            "unit": "iter/sec",
            "range": "stddev: 0.0003663287818907818",
            "extra": "mean: 22.178177452382272 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 125.0518983315847,
            "unit": "iter/sec",
            "range": "stddev: 0.00007229341426986939",
            "extra": "mean: 7.996679885245911 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.022884028263086,
            "unit": "iter/sec",
            "range": "stddev: 0.0012261728410941314",
            "extra": "mean: 20.39863667391481 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 147.77396127872646,
            "unit": "iter/sec",
            "range": "stddev: 0.00004045343045634688",
            "extra": "mean: 6.767092059702131 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.4559868363566,
            "unit": "iter/sec",
            "range": "stddev: 0.0003409993987403358",
            "extra": "mean: 23.553804175001858 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 140.1333943056607,
            "unit": "iter/sec",
            "range": "stddev: 0.00033194497009234085",
            "extra": "mean: 7.136057789471563 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.37588627311147,
            "unit": "iter/sec",
            "range": "stddev: 0.0002270778171700107",
            "extra": "mean: 23.59832650000584 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.46146706219446,
            "unit": "iter/sec",
            "range": "stddev: 0.00009183407178141919",
            "extra": "mean: 7.069062839284308 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.60443188922243,
            "unit": "iter/sec",
            "range": "stddev: 0.00013125445313757128",
            "extra": "mean: 28.89803257574792 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.9628613520332,
            "unit": "iter/sec",
            "range": "stddev: 0.00014167540842869978",
            "extra": "mean: 8.335913204549879 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.86712292971478,
            "unit": "iter/sec",
            "range": "stddev: 0.0011881693653937283",
            "extra": "mean: 31.38030383871087 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 119.18029089871987,
            "unit": "iter/sec",
            "range": "stddev: 0.00013493087075575546",
            "extra": "mean: 8.390649095241812 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.408009727188634,
            "unit": "iter/sec",
            "range": "stddev: 0.00045115122622850506",
            "extra": "mean: 27.46648354285688 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 136.8394372771566,
            "unit": "iter/sec",
            "range": "stddev: 0.00009041938346010543",
            "extra": "mean: 7.307834787237435 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.33681891302728,
            "unit": "iter/sec",
            "range": "stddev: 0.00026850491119082286",
            "extra": "mean: 36.5807010384611 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.97515458379164,
            "unit": "iter/sec",
            "range": "stddev: 0.000161313912129831",
            "extra": "mean: 8.93055252941575 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.84946664774095,
            "unit": "iter/sec",
            "range": "stddev: 0.0001850383436460924",
            "extra": "mean: 37.24468769230235 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.91074913539191,
            "unit": "iter/sec",
            "range": "stddev: 0.0001719289378716626",
            "extra": "mean: 9.53191172726692 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.09081934404164,
            "unit": "iter/sec",
            "range": "stddev: 0.00018167215666830657",
            "extra": "mean: 36.912873962962664 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 105.27634950825497,
            "unit": "iter/sec",
            "range": "stddev: 0.00030060307362922276",
            "extra": "mean: 9.498809606060549 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.3067251961122,
            "unit": "iter/sec",
            "range": "stddev: 0.00032197184691850445",
            "extra": "mean: 22.07177843182122 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.5747915686109,
            "unit": "iter/sec",
            "range": "stddev: 0.000041509942285137306",
            "extra": "mean: 7.216319712123702 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.014883427728684,
            "unit": "iter/sec",
            "range": "stddev: 0.00007304338510263604",
            "extra": "mean: 19.602122612250426 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 174.00855066890753,
            "unit": "iter/sec",
            "range": "stddev: 0.000043387066084734415",
            "extra": "mean: 5.746844026663591 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.19391051325548,
            "unit": "iter/sec",
            "range": "stddev: 0.00007822476416069811",
            "extra": "mean: 22.627551813955474 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 170.14891316751877,
            "unit": "iter/sec",
            "range": "stddev: 0.000041097068402457326",
            "extra": "mean: 5.877204746030072 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 44.21775089119464,
            "unit": "iter/sec",
            "range": "stddev: 0.0001014305206221147",
            "extra": "mean: 22.61535197619326 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.13987206395174,
            "unit": "iter/sec",
            "range": "stddev: 0.00004180661022897164",
            "extra": "mean: 5.843173703123483 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.71326597272202,
            "unit": "iter/sec",
            "range": "stddev: 0.0001716860591839118",
            "extra": "mean: 28.807430588231266 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.65768153189302,
            "unit": "iter/sec",
            "range": "stddev: 0.000060778334082330884",
            "extra": "mean: 7.426238062498906 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.20335036656509,
            "unit": "iter/sec",
            "range": "stddev: 0.00021456743695455273",
            "extra": "mean: 30.117442636360398 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 126.47666317392425,
            "unit": "iter/sec",
            "range": "stddev: 0.0001437256839448574",
            "extra": "mean: 7.906596955557335 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.38106455011379,
            "unit": "iter/sec",
            "range": "stddev: 0.0002009353300972411",
            "extra": "mean: 26.751512083327118 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 161.96913615231475,
            "unit": "iter/sec",
            "range": "stddev: 0.0000612676295413177",
            "extra": "mean: 6.174015764704742 msec\nrounds: 51"
          },
          {
            "name": "equator-float64-none",
            "value": 27.777440390466754,
            "unit": "iter/sec",
            "range": "stddev: 0.00033869079507202433",
            "extra": "mean: 36.000437259266015 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 123.12471993075457,
            "unit": "iter/sec",
            "range": "stddev: 0.00014637879414224476",
            "extra": "mean: 8.121845885719786 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 26.987565050840658,
            "unit": "iter/sec",
            "range": "stddev: 0.0006797961464627281",
            "extra": "mean: 37.0541024399995 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-none",
            "value": 110.77773132108075,
            "unit": "iter/sec",
            "range": "stddev: 0.00036278714299421206",
            "extra": "mean: 9.027085029405205 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.82406618060978,
            "unit": "iter/sec",
            "range": "stddev: 0.00037631916065479157",
            "extra": "mean: 37.27995574074696 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 115.87087498278566,
            "unit": "iter/sec",
            "range": "stddev: 0.00023034605848005287",
            "extra": "mean: 8.630296441176998 msec\nrounds: 34"
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
          "id": "3fbeaf3c1bec61da88789f845df8b0fceee06b7d",
          "message": "add tests for stac projection extension 2.0 (#783)\n\n* add tests for stac projection extension 2.0\r\n\r\n* skip if <3.10",
          "timestamp": "2025-01-27T17:15:05+01:00",
          "tree_id": "88f9fd79c6bd10854c7d6b4439c46c0542388b2c",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/3fbeaf3c1bec61da88789f845df8b0fceee06b7d"
        },
        "date": 1737994901559,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.645399548521866,
            "unit": "iter/sec",
            "range": "stddev: 0.00017398293413495438",
            "extra": "mean: 25.876301233331368 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.04660998646177,
            "unit": "iter/sec",
            "range": "stddev: 0.0006047266688130182",
            "extra": "mean: 12.33857899999818 msec\nrounds: 39"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.06432382421576,
            "unit": "iter/sec",
            "range": "stddev: 0.000201573169830705",
            "extra": "mean: 20.805452369563557 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.6867453606841,
            "unit": "iter/sec",
            "range": "stddev: 0.0004215788233617864",
            "extra": "mean: 7.710888242424507 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.88229939892211,
            "unit": "iter/sec",
            "range": "stddev: 0.0018680501501837368",
            "extra": "mean: 27.11327700000248 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 124.39001165180527,
            "unit": "iter/sec",
            "range": "stddev: 0.00007538079221644003",
            "extra": "mean: 8.039230696426156 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.34207015087854,
            "unit": "iter/sec",
            "range": "stddev: 0.00009725438490819126",
            "extra": "mean: 26.081012216214067 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.19096060405506,
            "unit": "iter/sec",
            "range": "stddev: 0.00017582397653728992",
            "extra": "mean: 8.834627735849208 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.39905416063964,
            "unit": "iter/sec",
            "range": "stddev: 0.00018110329053029015",
            "extra": "mean: 30.865098562502524 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.15334448372629,
            "unit": "iter/sec",
            "range": "stddev: 0.00007907596724150936",
            "extra": "mean: 12.172358974357879 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.99318593001112,
            "unit": "iter/sec",
            "range": "stddev: 0.00032541639710719086",
            "extra": "mean: 32.26515667857451 msec\nrounds: 28"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.99419267070205,
            "unit": "iter/sec",
            "range": "stddev: 0.0004432974733289352",
            "extra": "mean: 12.195985684207088 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.89826381876629,
            "unit": "iter/sec",
            "range": "stddev: 0.00036002496985714953",
            "extra": "mean: 29.50003591176235 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.13566441429698,
            "unit": "iter/sec",
            "range": "stddev: 0.000630980826760007",
            "extra": "mean: 10.737025459459685 msec\nrounds: 37"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.20950763881472,
            "unit": "iter/sec",
            "range": "stddev: 0.0005214754190085572",
            "extra": "mean: 38.15409330769189 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.58495858130027,
            "unit": "iter/sec",
            "range": "stddev: 0.00018257171220423642",
            "extra": "mean: 12.889096266670208 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.3648790371797,
            "unit": "iter/sec",
            "range": "stddev: 0.000603597202753404",
            "extra": "mean: 37.929246653845894 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.75554451420382,
            "unit": "iter/sec",
            "range": "stddev: 0.00014032916725309705",
            "extra": "mean: 13.200353933334933 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.458908737214553,
            "unit": "iter/sec",
            "range": "stddev: 0.0003919545953718739",
            "extra": "mean: 37.79445365384613 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.40069131012757,
            "unit": "iter/sec",
            "range": "stddev: 0.00019974101388044174",
            "extra": "mean: 13.088886799999955 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.87728865340701,
            "unit": "iter/sec",
            "range": "stddev: 0.0004107296717010839",
            "extra": "mean: 22.282986116276472 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.84264661759009,
            "unit": "iter/sec",
            "range": "stddev: 0.00037103319850723",
            "extra": "mean: 9.723592623188686 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 58.106127359403175,
            "unit": "iter/sec",
            "range": "stddev: 0.00025721338379920266",
            "extra": "mean: 17.209888964286183 msec\nrounds: 56"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 158.32330610065515,
            "unit": "iter/sec",
            "range": "stddev: 0.000055852441384496295",
            "extra": "mean: 6.316189477272809 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.90096014353366,
            "unit": "iter/sec",
            "range": "stddev: 0.00018048151165925736",
            "extra": "mean: 23.865801560977463 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.18795985606408,
            "unit": "iter/sec",
            "range": "stddev: 0.00022303991827697455",
            "extra": "mean: 8.834861952381278 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.646407593932125,
            "unit": "iter/sec",
            "range": "stddev: 0.0004895568596944745",
            "extra": "mean: 24.011674902439843 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.99297301724742,
            "unit": "iter/sec",
            "range": "stddev: 0.00007444345508695562",
            "extra": "mean: 9.346408196721466 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 33.020941570539236,
            "unit": "iter/sec",
            "range": "stddev: 0.00032351332078077194",
            "extra": "mean: 30.283812406251442 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 110.42428654893216,
            "unit": "iter/sec",
            "range": "stddev: 0.00018969238057915748",
            "extra": "mean: 9.055978818182098 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.74643084402198,
            "unit": "iter/sec",
            "range": "stddev: 0.00019635746928451544",
            "extra": "mean: 31.499603999997536 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.10282345218468,
            "unit": "iter/sec",
            "range": "stddev: 0.00011774725856764875",
            "extra": "mean: 9.250452190476906 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.09350398009975,
            "unit": "iter/sec",
            "range": "stddev: 0.00384730226360982",
            "extra": "mean: 28.49530216666491 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 140.6718240289666,
            "unit": "iter/sec",
            "range": "stddev: 0.0001890135136293468",
            "extra": "mean: 7.108744106382554 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.3614259762412,
            "unit": "iter/sec",
            "range": "stddev: 0.00022025664960210995",
            "extra": "mean: 42.80560617391292 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 97.3873028180318,
            "unit": "iter/sec",
            "range": "stddev: 0.0001099457170136918",
            "extra": "mean: 10.268279037037306 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.71542171915731,
            "unit": "iter/sec",
            "range": "stddev: 0.0002611359599008466",
            "extra": "mean: 44.02295552173872 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 91.55727666055962,
            "unit": "iter/sec",
            "range": "stddev: 0.0003103238687570958",
            "extra": "mean: 10.922124777776101 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.789345770793837,
            "unit": "iter/sec",
            "range": "stddev: 0.001804495687791921",
            "extra": "mean: 43.88015391304347 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.87266647722309,
            "unit": "iter/sec",
            "range": "stddev: 0.00013444792920562734",
            "extra": "mean: 10.652728185180893 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.40412618825102,
            "unit": "iter/sec",
            "range": "stddev: 0.00011107853767685025",
            "extra": "mean: 22.02443002325116 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.98207160406335,
            "unit": "iter/sec",
            "range": "stddev: 0.000048610363528153655",
            "extra": "mean: 7.875127467742467 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.86248182129403,
            "unit": "iter/sec",
            "range": "stddev: 0.0009456357088569576",
            "extra": "mean: 20.05515897872827 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.84689785596441,
            "unit": "iter/sec",
            "range": "stddev: 0.000053186283771621444",
            "extra": "mean: 6.7183126716397945 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.67088368785487,
            "unit": "iter/sec",
            "range": "stddev: 0.0008763622237825047",
            "extra": "mean: 23.435183750005706 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 143.58350493093553,
            "unit": "iter/sec",
            "range": "stddev: 0.0000983680036271159",
            "extra": "mean: 6.964588310342512 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.87503191295361,
            "unit": "iter/sec",
            "range": "stddev: 0.00011769839168612735",
            "extra": "mean: 23.32359780000246 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.1418243218871,
            "unit": "iter/sec",
            "range": "stddev: 0.00011031886950791347",
            "extra": "mean: 6.986078350875782 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.54759332216998,
            "unit": "iter/sec",
            "range": "stddev: 0.0002850656882446901",
            "extra": "mean: 28.945576343758717 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 123.38712475388692,
            "unit": "iter/sec",
            "range": "stddev: 0.00008961369235683374",
            "extra": "mean: 8.104573325577052 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.29682638073957,
            "unit": "iter/sec",
            "range": "stddev: 0.00018810929717458791",
            "extra": "mean: 30.03289228124295 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 120.27666945778962,
            "unit": "iter/sec",
            "range": "stddev: 0.00007064484846395774",
            "extra": "mean: 8.314164372093325 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.48722973698338,
            "unit": "iter/sec",
            "range": "stddev: 0.0003658461177792729",
            "extra": "mean: 27.40684911429168 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 137.1914647877599,
            "unit": "iter/sec",
            "range": "stddev: 0.00011255855174200858",
            "extra": "mean: 7.289083191487427 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.600654834738037,
            "unit": "iter/sec",
            "range": "stddev: 0.00024139998989878124",
            "extra": "mean: 36.23102444444199 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.20457574887337,
            "unit": "iter/sec",
            "range": "stddev: 0.00019488126105339566",
            "extra": "mean: 8.992435727269353 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.78290336849876,
            "unit": "iter/sec",
            "range": "stddev: 0.00013145327074246926",
            "extra": "mean: 37.33725153846352 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.38651065504615,
            "unit": "iter/sec",
            "range": "stddev: 0.00015689230034800306",
            "extra": "mean: 9.579781848485986 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.76585188198395,
            "unit": "iter/sec",
            "range": "stddev: 0.0011940633615238382",
            "extra": "mean: 37.361037653843496 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.59460647313273,
            "unit": "iter/sec",
            "range": "stddev: 0.00015895076237724948",
            "extra": "mean: 9.381337696969226 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 44.97770663105255,
            "unit": "iter/sec",
            "range": "stddev: 0.0009928897059703092",
            "extra": "mean: 22.233236749994745 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 137.6251164606274,
            "unit": "iter/sec",
            "range": "stddev: 0.0006137532199878721",
            "extra": "mean: 7.266115558827416 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.04214465509233,
            "unit": "iter/sec",
            "range": "stddev: 0.0007435783968216043",
            "extra": "mean: 19.59165326530285 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 172.97664159870303,
            "unit": "iter/sec",
            "range": "stddev: 0.00004484056879492304",
            "extra": "mean: 5.781127386667322 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.315782010826666,
            "unit": "iter/sec",
            "range": "stddev: 0.00019829971297306468",
            "extra": "mean: 22.565324465123794 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.5506066951687,
            "unit": "iter/sec",
            "range": "stddev: 0.00006475110265031988",
            "extra": "mean: 5.829183698411032 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 44.10143723276798,
            "unit": "iter/sec",
            "range": "stddev: 0.00012149723280930161",
            "extra": "mean: 22.674997976188088 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 170.85481517842211,
            "unit": "iter/sec",
            "range": "stddev: 0.0000859192618774715",
            "extra": "mean: 5.852922546875305 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.58986082751373,
            "unit": "iter/sec",
            "range": "stddev: 0.00027367349777734657",
            "extra": "mean: 28.91020594117489 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.66578242116145,
            "unit": "iter/sec",
            "range": "stddev: 0.0000995539825841551",
            "extra": "mean: 7.425791333336207 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.25732589257561,
            "unit": "iter/sec",
            "range": "stddev: 0.0005303679676123376",
            "extra": "mean: 30.0685630357082 msec\nrounds: 28"
          },
          {
            "name": "dateline-int32-none",
            "value": 131.91478709673893,
            "unit": "iter/sec",
            "range": "stddev: 0.00007347961413201933",
            "extra": "mean: 7.580651282609097 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 37.03607254207612,
            "unit": "iter/sec",
            "range": "stddev: 0.0009396867111355143",
            "extra": "mean: 27.00070313513711 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 163.85582163711567,
            "unit": "iter/sec",
            "range": "stddev: 0.00005171565552218504",
            "extra": "mean: 6.10292627999911 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.58378177836074,
            "unit": "iter/sec",
            "range": "stddev: 0.0012451806907175953",
            "extra": "mean: 36.25318703704697 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 123.01055382753373,
            "unit": "iter/sec",
            "range": "stddev: 0.0001412183714637117",
            "extra": "mean: 8.129383771428625 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.02508546806074,
            "unit": "iter/sec",
            "range": "stddev: 0.0006742807926598758",
            "extra": "mean: 37.0026581851827 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.75527113483687,
            "unit": "iter/sec",
            "range": "stddev: 0.0007110234881008325",
            "extra": "mean: 8.790801428574468 msec\nrounds: 35"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.339699290502804,
            "unit": "iter/sec",
            "range": "stddev: 0.00035588412438461686",
            "extra": "mean: 36.57684707407801 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 112.65518307791058,
            "unit": "iter/sec",
            "range": "stddev: 0.000321740354487527",
            "extra": "mean: 8.876644400004352 msec\nrounds: 35"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "emmanuel.mathot@gmail.com",
            "name": "Emmanuel Mathot",
            "username": "emmanuelmathot"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8a479910c6da7fa6baa9f73e4811c343f79f0e53",
          "message": "Reproject method for ImageData (#782)\n\n* Add reproject method to ImageData class with tests\r\n\r\n* Add reproject method for ImageData objects in CHANGES.md\r\n\r\n* Remove unused rasterio import and clean up test cases for reproject method\r\n\r\n* lint\r\n\r\n* fix and update tests\r\n\r\n* relaxe rasterio version limit\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2025-01-28T11:09:03+01:00",
          "tree_id": "c268076a4fbedfebe961e0ced9738e56f45606b4",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/8a479910c6da7fa6baa9f73e4811c343f79f0e53"
        },
        "date": 1738059343817,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.67721075759655,
            "unit": "iter/sec",
            "range": "stddev: 0.0010636615968847355",
            "extra": "mean: 26.541242833332035 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.13999090745068,
            "unit": "iter/sec",
            "range": "stddev: 0.00036047524709452433",
            "extra": "mean: 12.324379000000295 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.23403546590573,
            "unit": "iter/sec",
            "range": "stddev: 0.0005788160999567925",
            "extra": "mean: 21.171174347824163 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 124.92017840830205,
            "unit": "iter/sec",
            "range": "stddev: 0.0005206167721130725",
            "extra": "mean: 8.005111846154241 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.18340027287243,
            "unit": "iter/sec",
            "range": "stddev: 0.000459068813108198",
            "extra": "mean: 26.893721194442815 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 120.0784571196363,
            "unit": "iter/sec",
            "range": "stddev: 0.00043132868711302373",
            "extra": "mean: 8.32788848214199 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.98819006031309,
            "unit": "iter/sec",
            "range": "stddev: 0.0007343282526887992",
            "extra": "mean: 27.035656472225217 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.7176341097896,
            "unit": "iter/sec",
            "range": "stddev: 0.00012825355896220242",
            "extra": "mean: 8.951138358490999 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.23071610321381,
            "unit": "iter/sec",
            "range": "stddev: 0.0006044975237464704",
            "extra": "mean: 32.01975890322587 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 78.72073176140545,
            "unit": "iter/sec",
            "range": "stddev: 0.0003696983740075265",
            "extra": "mean: 12.703133947368508 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.22383290087468,
            "unit": "iter/sec",
            "range": "stddev: 0.0004823465656570233",
            "extra": "mean: 33.08647196666641 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 78.08798916208751,
            "unit": "iter/sec",
            "range": "stddev: 0.0010391186457481055",
            "extra": "mean: 12.806066729728391 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.68907786854248,
            "unit": "iter/sec",
            "range": "stddev: 0.0017625205989079055",
            "extra": "mean: 30.591257545454496 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 90.14214657066451,
            "unit": "iter/sec",
            "range": "stddev: 0.00036189314016624256",
            "extra": "mean: 11.093589825000194 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.028161195030993,
            "unit": "iter/sec",
            "range": "stddev: 0.00033524402666418947",
            "extra": "mean: 38.41992496154161 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 75.11371932192372,
            "unit": "iter/sec",
            "range": "stddev: 0.0003077890401978594",
            "extra": "mean: 13.313147172411766 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.981704956471514,
            "unit": "iter/sec",
            "range": "stddev: 0.00022456821153919048",
            "extra": "mean: 38.488621192310184 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 72.51454879335222,
            "unit": "iter/sec",
            "range": "stddev: 0.000376263393712343",
            "extra": "mean: 13.790336099997564 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.949232014264624,
            "unit": "iter/sec",
            "range": "stddev: 0.0011563248894237038",
            "extra": "mean: 38.53678596153779 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 73.03332291928137,
            "unit": "iter/sec",
            "range": "stddev: 0.00034525644752774127",
            "extra": "mean: 13.692379862069675 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.03479775032829,
            "unit": "iter/sec",
            "range": "stddev: 0.0003625018087176383",
            "extra": "mean: 22.70931288636485 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 101.12014697778044,
            "unit": "iter/sec",
            "range": "stddev: 0.0001226738995938276",
            "extra": "mean: 9.88922613235258 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.09061590174083,
            "unit": "iter/sec",
            "range": "stddev: 0.0005352275618435699",
            "extra": "mean: 17.51601351999966 msec\nrounds: 50"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.44706039868086,
            "unit": "iter/sec",
            "range": "stddev: 0.00009547726756018906",
            "extra": "mean: 6.391938573033309 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.960585700989334,
            "unit": "iter/sec",
            "range": "stddev: 0.0004297860240244085",
            "extra": "mean: 24.41371339999776 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 109.0761274712667,
            "unit": "iter/sec",
            "range": "stddev: 0.00023292130470817872",
            "extra": "mean: 9.167908901637752 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.158207434641604,
            "unit": "iter/sec",
            "range": "stddev: 0.0009180307113500811",
            "extra": "mean: 24.901509900000462 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 104.75393320840166,
            "unit": "iter/sec",
            "range": "stddev: 0.00012429259539169848",
            "extra": "mean: 9.546180934424296 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.91389583136458,
            "unit": "iter/sec",
            "range": "stddev: 0.0003575624616002653",
            "extra": "mean: 31.334312967745305 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 103.66311844100787,
            "unit": "iter/sec",
            "range": "stddev: 0.0003596673841706187",
            "extra": "mean: 9.646632428572707 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.109175255154028,
            "unit": "iter/sec",
            "range": "stddev: 0.00017909484207912025",
            "extra": "mean: 32.14485732257799 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 96.88850064802753,
            "unit": "iter/sec",
            "range": "stddev: 0.0008223201960905994",
            "extra": "mean: 10.32114227500287 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.993283284229406,
            "unit": "iter/sec",
            "range": "stddev: 0.0008841693285839993",
            "extra": "mean: 28.576912657140547 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 123.76147553057385,
            "unit": "iter/sec",
            "range": "stddev: 0.0004116024385846768",
            "extra": "mean: 8.080058804348704 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.14612435315898,
            "unit": "iter/sec",
            "range": "stddev: 0.0003586919944829053",
            "extra": "mean: 43.203777217394936 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 89.52301985817289,
            "unit": "iter/sec",
            "range": "stddev: 0.0004830841720416381",
            "extra": "mean: 11.170311296292876 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.463785596503516,
            "unit": "iter/sec",
            "range": "stddev: 0.0011619324957056277",
            "extra": "mean: 44.51609439130553 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 83.91370390857794,
            "unit": "iter/sec",
            "range": "stddev: 0.0006352630778231576",
            "extra": "mean: 11.917004653846256 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.749607176597447,
            "unit": "iter/sec",
            "range": "stddev: 0.0012759178989777433",
            "extra": "mean: 43.9568029565232 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.50933781354966,
            "unit": "iter/sec",
            "range": "stddev: 0.00045398533508742706",
            "extra": "mean: 11.427351925923993 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.963547931438185,
            "unit": "iter/sec",
            "range": "stddev: 0.0001851238608491185",
            "extra": "mean: 22.24023783721051 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 125.90781547421471,
            "unit": "iter/sec",
            "range": "stddev: 0.00016123377904725855",
            "extra": "mean: 7.942318721309202 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.92209704292571,
            "unit": "iter/sec",
            "range": "stddev: 0.0011455778738724309",
            "extra": "mean: 20.4406609782604 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.00343610819382,
            "unit": "iter/sec",
            "range": "stddev: 0.0000819697654038327",
            "extra": "mean: 6.711254626865676 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.62117380319813,
            "unit": "iter/sec",
            "range": "stddev: 0.0002553390869451596",
            "extra": "mean: 23.462516649998122 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 140.97040415401727,
            "unit": "iter/sec",
            "range": "stddev: 0.0005347967292664235",
            "extra": "mean: 7.09368754385814 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.53383314335102,
            "unit": "iter/sec",
            "range": "stddev: 0.0002807964150261877",
            "extra": "mean: 23.510695512198907 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.3999983855239,
            "unit": "iter/sec",
            "range": "stddev: 0.00011205738373481903",
            "extra": "mean: 6.973500775861579 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.77735018063784,
            "unit": "iter/sec",
            "range": "stddev: 0.0007652706011231537",
            "extra": "mean: 29.605637939391382 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 120.28516308334437,
            "unit": "iter/sec",
            "range": "stddev: 0.0002492298206916871",
            "extra": "mean: 8.313577288888988 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.80157457070485,
            "unit": "iter/sec",
            "range": "stddev: 0.00020771039402183987",
            "extra": "mean: 30.48634137499917 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.45318638288302,
            "unit": "iter/sec",
            "range": "stddev: 0.0002231433946906236",
            "extra": "mean: 8.514030404761623 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.09300758037069,
            "unit": "iter/sec",
            "range": "stddev: 0.000269296887322112",
            "extra": "mean: 27.706197599998664 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 131.4891072436644,
            "unit": "iter/sec",
            "range": "stddev: 0.00041605431870335983",
            "extra": "mean: 7.605192711110931 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.436625302731713,
            "unit": "iter/sec",
            "range": "stddev: 0.00017746279077647932",
            "extra": "mean: 36.447631185182075 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 110.72168629587384,
            "unit": "iter/sec",
            "range": "stddev: 0.00025902414852648994",
            "extra": "mean: 9.031654352949156 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.85846800024359,
            "unit": "iter/sec",
            "range": "stddev: 0.00029724835711835665",
            "extra": "mean: 37.23220549999094 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.13741726097498,
            "unit": "iter/sec",
            "range": "stddev: 0.000356140218012196",
            "extra": "mean: 9.602696382357328 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.115610142522108,
            "unit": "iter/sec",
            "range": "stddev: 0.00018613121028540833",
            "extra": "mean: 36.879125888885014 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.04463412218846,
            "unit": "iter/sec",
            "range": "stddev: 0.0003058842366136846",
            "extra": "mean: 9.429991515155438 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 44.92678191477299,
            "unit": "iter/sec",
            "range": "stddev: 0.0004949326885814337",
            "extra": "mean: 22.258438227269874 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 140.3640415728187,
            "unit": "iter/sec",
            "range": "stddev: 0.00007363044586906581",
            "extra": "mean: 7.124331764707811 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.76406858619335,
            "unit": "iter/sec",
            "range": "stddev: 0.0004029988215289798",
            "extra": "mean: 20.506902499992208 msec\nrounds: 48"
          },
          {
            "name": "dateline-uint8-none",
            "value": 174.32623444997063,
            "unit": "iter/sec",
            "range": "stddev: 0.00008137185603604126",
            "extra": "mean: 5.736371253329556 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.53219356000221,
            "unit": "iter/sec",
            "range": "stddev: 0.00043179448139961455",
            "extra": "mean: 22.97150495349284 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.40135891986043,
            "unit": "iter/sec",
            "range": "stddev: 0.0002032903176127453",
            "extra": "mean: 5.8342594615457815 msec\nrounds: 65"
          },
          {
            "name": "equator-int16-none",
            "value": 42.982964474750396,
            "unit": "iter/sec",
            "range": "stddev: 0.00029043802171563484",
            "extra": "mean: 23.26503097727084 msec\nrounds: 44"
          },
          {
            "name": "dateline-int16-none",
            "value": 169.68636846977506,
            "unit": "iter/sec",
            "range": "stddev: 0.00012783090790403082",
            "extra": "mean: 5.893225301584095 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.98517519079547,
            "unit": "iter/sec",
            "range": "stddev: 0.00029022582431903764",
            "extra": "mean: 29.424594529406452 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.16814011101062,
            "unit": "iter/sec",
            "range": "stddev: 0.0003224397952095947",
            "extra": "mean: 7.741847170212197 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.75782549086882,
            "unit": "iter/sec",
            "range": "stddev: 0.00038011441210350266",
            "extra": "mean: 30.527056818186793 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.050920968311,
            "unit": "iter/sec",
            "range": "stddev: 0.0002756926574884465",
            "extra": "mean: 7.8093932666635935 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.75244579639886,
            "unit": "iter/sec",
            "range": "stddev: 0.0002757236383060549",
            "extra": "mean: 27.20907352778094 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 153.64836254543053,
            "unit": "iter/sec",
            "range": "stddev: 0.00027455887024038",
            "extra": "mean: 6.508367440000029 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.525058690557092,
            "unit": "iter/sec",
            "range": "stddev: 0.00021805319578127304",
            "extra": "mean: 36.33053107142205 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 121.73752736009745,
            "unit": "iter/sec",
            "range": "stddev: 0.00023132829044110936",
            "extra": "mean: 8.21439388235657 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.886545044477433,
            "unit": "iter/sec",
            "range": "stddev: 0.00018909364892883275",
            "extra": "mean: 37.19332470370352 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 111.39231372657592,
            "unit": "iter/sec",
            "range": "stddev: 0.0006374191922130438",
            "extra": "mean: 8.977280088234854 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.192515723727293,
            "unit": "iter/sec",
            "range": "stddev: 0.0002850521154769096",
            "extra": "mean: 36.77482474074412 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.70796297280494,
            "unit": "iter/sec",
            "range": "stddev: 0.00033401027873208264",
            "extra": "mean: 8.71779058823563 msec\nrounds: 34"
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
          "id": "3fc6e4827ba52b25666d2ea38a830393c34b21a6",
          "message": "remove useless <3.9 dependencies",
          "timestamp": "2025-01-28T13:10:19+01:00",
          "tree_id": "2cade700b67e8fd38aa628c132e1e615e9b9b82d",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/3fc6e4827ba52b25666d2ea38a830393c34b21a6"
        },
        "date": 1738066620060,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.23067354030278,
            "unit": "iter/sec",
            "range": "stddev: 0.00038898886616518997",
            "extra": "mean: 26.859573166665502 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 78.7150759410935,
            "unit": "iter/sec",
            "range": "stddev: 0.0002545640741988146",
            "extra": "mean: 12.704046690475797 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.11100793972131,
            "unit": "iter/sec",
            "range": "stddev: 0.0005155892956009366",
            "extra": "mean: 21.686795511112045 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 126.6331623243342,
            "unit": "iter/sec",
            "range": "stddev: 0.000070712714662241",
            "extra": "mean: 7.8968256153849286 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.11056272019209,
            "unit": "iter/sec",
            "range": "stddev: 0.00014279212559007858",
            "extra": "mean: 26.946505972971778 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.36722838332118,
            "unit": "iter/sec",
            "range": "stddev: 0.00006581392922853766",
            "extra": "mean: 8.172122660713146 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.70328645271976,
            "unit": "iter/sec",
            "range": "stddev: 0.0004047082602495177",
            "extra": "mean: 26.522886837835966 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 110.8910214113299,
            "unit": "iter/sec",
            "range": "stddev: 0.00018921087283750988",
            "extra": "mean: 9.017862648146089 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.846914291039724,
            "unit": "iter/sec",
            "range": "stddev: 0.0006096108920784061",
            "extra": "mean: 31.400216387097654 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 77.2319154712076,
            "unit": "iter/sec",
            "range": "stddev: 0.00037046310644113165",
            "extra": "mean: 12.94801500000093 msec\nrounds: 37"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.361563932779404,
            "unit": "iter/sec",
            "range": "stddev: 0.0005208445760084962",
            "extra": "mean: 32.93637976666825 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.3571085541535,
            "unit": "iter/sec",
            "range": "stddev: 0.00013224300938097445",
            "extra": "mean: 12.444449756751633 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.21938443572434,
            "unit": "iter/sec",
            "range": "stddev: 0.0007126694840095128",
            "extra": "mean: 30.102905787880687 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.91749101352566,
            "unit": "iter/sec",
            "range": "stddev: 0.0006113570185112539",
            "extra": "mean: 10.762236357140052 msec\nrounds: 42"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.97009522758266,
            "unit": "iter/sec",
            "range": "stddev: 0.0005888586601149211",
            "extra": "mean: 38.50582723077222 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 71.82366696019403,
            "unit": "iter/sec",
            "range": "stddev: 0.0002824656782532692",
            "extra": "mean: 13.9229872592584 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.867718849265717,
            "unit": "iter/sec",
            "range": "stddev: 0.001091722141259221",
            "extra": "mean: 38.658221307689296 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.30923574041861,
            "unit": "iter/sec",
            "range": "stddev: 0.000300314038313801",
            "extra": "mean: 13.640846066666274 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.289868222408327,
            "unit": "iter/sec",
            "range": "stddev: 0.00027267267472086783",
            "extra": "mean: 38.03746719230962 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 72.77742846702841,
            "unit": "iter/sec",
            "range": "stddev: 0.00021825125277305952",
            "extra": "mean: 13.740523965518332 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 43.50958548345079,
            "unit": "iter/sec",
            "range": "stddev: 0.0003215713092836802",
            "extra": "mean: 22.983441209302203 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 99.37848871154142,
            "unit": "iter/sec",
            "range": "stddev: 0.00018024517602128478",
            "extra": "mean: 10.062539820892486 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.503254083017296,
            "unit": "iter/sec",
            "range": "stddev: 0.00015782990851826703",
            "extra": "mean: 17.39032018181619 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 153.91579291737432,
            "unit": "iter/sec",
            "range": "stddev: 0.00016908389270855686",
            "extra": "mean: 6.497059080459819 msec\nrounds: 87"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.8984226058831,
            "unit": "iter/sec",
            "range": "stddev: 0.0007197045587763346",
            "extra": "mean: 25.063647500002872 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 111.10772708139794,
            "unit": "iter/sec",
            "range": "stddev: 0.00011984518174127745",
            "extra": "mean: 9.000274114755278 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.39495410995368,
            "unit": "iter/sec",
            "range": "stddev: 0.0008352784433216824",
            "extra": "mean: 24.75556717499998 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.19092628134979,
            "unit": "iter/sec",
            "range": "stddev: 0.0002624846297085645",
            "extra": "mean: 9.78560461666452 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.11007159147223,
            "unit": "iter/sec",
            "range": "stddev: 0.00044174768235162674",
            "extra": "mean: 31.142876687499488 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 108.0294138065834,
            "unit": "iter/sec",
            "range": "stddev: 0.0008500050693267718",
            "extra": "mean: 9.256738186050022 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.822896604284843,
            "unit": "iter/sec",
            "range": "stddev: 0.000858055993127348",
            "extra": "mean: 31.423915064518464 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.79958787966763,
            "unit": "iter/sec",
            "range": "stddev: 0.00011690610797698983",
            "extra": "mean: 9.19121128570818 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.27196604066572,
            "unit": "iter/sec",
            "range": "stddev: 0.0003318264864938775",
            "extra": "mean: 27.56950088889217 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 141.73723346355573,
            "unit": "iter/sec",
            "range": "stddev: 0.0000883010811235427",
            "extra": "mean: 7.055309148933866 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.92830884154989,
            "unit": "iter/sec",
            "range": "stddev: 0.0016483230386559798",
            "extra": "mean: 43.614206652164185 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 97.54646964784266,
            "unit": "iter/sec",
            "range": "stddev: 0.00018021059369220871",
            "extra": "mean: 10.25152425925971 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.786614030585174,
            "unit": "iter/sec",
            "range": "stddev: 0.005650827383226479",
            "extra": "mean: 45.89974369565405 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 91.74314015224903,
            "unit": "iter/sec",
            "range": "stddev: 0.00011599301257319822",
            "extra": "mean: 10.899997518511858 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 23.132564003325893,
            "unit": "iter/sec",
            "range": "stddev: 0.00019209403689395937",
            "extra": "mean: 43.2291033478271 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 94.66659782882462,
            "unit": "iter/sec",
            "range": "stddev: 0.00024581190399443044",
            "extra": "mean: 10.563387962966535 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.61752646075629,
            "unit": "iter/sec",
            "range": "stddev: 0.00009636390833362923",
            "extra": "mean: 21.921399023252107 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.71579548422196,
            "unit": "iter/sec",
            "range": "stddev: 0.00019820223657754648",
            "extra": "mean: 7.891675983871445 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 50.34918266935874,
            "unit": "iter/sec",
            "range": "stddev: 0.00006519831952339926",
            "extra": "mean: 19.861295595739136 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.22112993667992,
            "unit": "iter/sec",
            "range": "stddev: 0.00006621955135520685",
            "extra": "mean: 6.701463796878748 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.27968135641564,
            "unit": "iter/sec",
            "range": "stddev: 0.0018399566627859793",
            "extra": "mean: 23.652023097573732 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 138.6210107564163,
            "unit": "iter/sec",
            "range": "stddev: 0.0007975207519770267",
            "extra": "mean: 7.213913637934669 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.99496067182482,
            "unit": "iter/sec",
            "range": "stddev: 0.0005369056444608952",
            "extra": "mean: 23.258539707313037 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-mask",
            "value": 144.92691697896967,
            "unit": "iter/sec",
            "range": "stddev: 0.00004186265833470957",
            "extra": "mean: 6.900029482757231 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.364039160166065,
            "unit": "iter/sec",
            "range": "stddev: 0.0003975264552795171",
            "extra": "mean: 29.100187999994336 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 120.12729072126727,
            "unit": "iter/sec",
            "range": "stddev: 0.0007297804322343921",
            "extra": "mean: 8.324503066670431 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.171211132077914,
            "unit": "iter/sec",
            "range": "stddev: 0.0026497646972923786",
            "extra": "mean: 31.083691437494565 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.35013504320419,
            "unit": "iter/sec",
            "range": "stddev: 0.00010193279753600174",
            "extra": "mean: 8.449504511633604 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.07441066627512,
            "unit": "iter/sec",
            "range": "stddev: 0.0007923987584464154",
            "extra": "mean: 27.72048057142261 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.72570585666224,
            "unit": "iter/sec",
            "range": "stddev: 0.00013027184797464338",
            "extra": "mean: 7.36780106383152 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.69951308852263,
            "unit": "iter/sec",
            "range": "stddev: 0.00033243804246292446",
            "extra": "mean: 36.101717629626954 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 106.8198239375161,
            "unit": "iter/sec",
            "range": "stddev: 0.00021279137476912723",
            "extra": "mean: 9.361558212124995 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 27.289145739547497,
            "unit": "iter/sec",
            "range": "stddev: 0.00039524011368132324",
            "extra": "mean: 36.64460623077686 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 106.40512237527778,
            "unit": "iter/sec",
            "range": "stddev: 0.00016887641414923353",
            "extra": "mean: 9.398043794105353 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.11808061093985,
            "unit": "iter/sec",
            "range": "stddev: 0.0010852898722661147",
            "extra": "mean: 36.87576618518439 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 109.06363633160936,
            "unit": "iter/sec",
            "range": "stddev: 0.0001516603044492431",
            "extra": "mean: 9.16895890908577 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.25217580765092,
            "unit": "iter/sec",
            "range": "stddev: 0.0005787702274913396",
            "extra": "mean: 22.098384931823034 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 139.38657154649562,
            "unit": "iter/sec",
            "range": "stddev: 0.00005145287803201165",
            "extra": "mean: 7.174292249999326 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.868156938331445,
            "unit": "iter/sec",
            "range": "stddev: 0.0002221847162310869",
            "extra": "mean: 20.052876653064036 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.42591847722503,
            "unit": "iter/sec",
            "range": "stddev: 0.0003861722423428402",
            "extra": "mean: 5.902284662157073 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.155933911855065,
            "unit": "iter/sec",
            "range": "stddev: 0.0006611067747895216",
            "extra": "mean: 23.171784488373614 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 164.9156165315824,
            "unit": "iter/sec",
            "range": "stddev: 0.0001590418727944916",
            "extra": "mean: 6.063707131146635 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-none",
            "value": 42.69144590971935,
            "unit": "iter/sec",
            "range": "stddev: 0.00025248725631852074",
            "extra": "mean: 23.423896255814913 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 161.78979005382857,
            "unit": "iter/sec",
            "range": "stddev: 0.00019280099391210192",
            "extra": "mean: 6.180859741936083 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.39077213956892,
            "unit": "iter/sec",
            "range": "stddev: 0.0002320720543200202",
            "extra": "mean: 29.948393999999013 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 131.3531159863949,
            "unit": "iter/sec",
            "range": "stddev: 0.0001231152045818284",
            "extra": "mean: 7.613066446810264 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.179332322006736,
            "unit": "iter/sec",
            "range": "stddev: 0.002407235209851471",
            "extra": "mean: 31.07584675758241 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.687925634024,
            "unit": "iter/sec",
            "range": "stddev: 0.00010437372916779346",
            "extra": "mean: 7.7707368043518175 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 36.248863413207644,
            "unit": "iter/sec",
            "range": "stddev: 0.00046749992636890874",
            "extra": "mean: 27.587071864869557 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 158.2176866204749,
            "unit": "iter/sec",
            "range": "stddev: 0.00011024555475798637",
            "extra": "mean: 6.320405899997468 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.54718569735847,
            "unit": "iter/sec",
            "range": "stddev: 0.0001310416562904099",
            "extra": "mean: 36.30134892857281 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 122.07755233937215,
            "unit": "iter/sec",
            "range": "stddev: 0.00015384301540508159",
            "extra": "mean: 8.191514171418085 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 26.823475832135447,
            "unit": "iter/sec",
            "range": "stddev: 0.0011256920858166873",
            "extra": "mean: 37.28077622222119 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 114.08314059186311,
            "unit": "iter/sec",
            "range": "stddev: 0.00010768380339270605",
            "extra": "mean: 8.765537088232337 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.847820032038076,
            "unit": "iter/sec",
            "range": "stddev: 0.001116383046614287",
            "extra": "mean: 37.24697196296305 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 118.15899428353467,
            "unit": "iter/sec",
            "range": "stddev: 0.0002040161918267086",
            "extra": "mean: 8.463172914288666 msec\nrounds: 35"
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
          "id": "7db311c4dd0a839d6fb7634d5891979fea456935",
          "message": "Bump version: 7.3.0 → 7.4.0",
          "timestamp": "2025-01-28T13:11:51+01:00",
          "tree_id": "51d66fef7bed5080361c5f2571145f681a05d207",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/7db311c4dd0a839d6fb7634d5891979fea456935"
        },
        "date": 1738066818910,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 36.44355541270613,
            "unit": "iter/sec",
            "range": "stddev: 0.00022382001331920314",
            "extra": "mean: 27.439693758621246 msec\nrounds: 29"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 78.68367976448545,
            "unit": "iter/sec",
            "range": "stddev: 0.00016955155281236697",
            "extra": "mean: 12.709115829269575 msec\nrounds: 41"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.074748717892064,
            "unit": "iter/sec",
            "range": "stddev: 0.0002096937298193541",
            "extra": "mean: 22.18537048888878 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 121.8079016534489,
            "unit": "iter/sec",
            "range": "stddev: 0.0001761533188004888",
            "extra": "mean: 8.209648031250572 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 36.98150185482799,
            "unit": "iter/sec",
            "range": "stddev: 0.00019723348121618946",
            "extra": "mean: 27.040545944443533 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 114.04073535481862,
            "unit": "iter/sec",
            "range": "stddev: 0.00025314631708133525",
            "extra": "mean: 8.768796490908864 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.634499418808936,
            "unit": "iter/sec",
            "range": "stddev: 0.0002174057455032949",
            "extra": "mean: 27.296674333335602 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 105.14760328915,
            "unit": "iter/sec",
            "range": "stddev: 0.0003148425683686571",
            "extra": "mean: 9.51044026414997 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.180627912007303,
            "unit": "iter/sec",
            "range": "stddev: 0.0003086259670855061",
            "extra": "mean: 32.07119506451348 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 74.54751634071063,
            "unit": "iter/sec",
            "range": "stddev: 0.00027616176902243365",
            "extra": "mean: 13.414263131579299 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 29.85774034777725,
            "unit": "iter/sec",
            "range": "stddev: 0.0002520898390478626",
            "extra": "mean: 33.492152733334514 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 73.22797662813954,
            "unit": "iter/sec",
            "range": "stddev: 0.00029879516138281534",
            "extra": "mean: 13.655982945945919 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.93305438994969,
            "unit": "iter/sec",
            "range": "stddev: 0.00014005981324966718",
            "extra": "mean: 30.364629656251196 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 81.53232686744063,
            "unit": "iter/sec",
            "range": "stddev: 0.0002877670195908729",
            "extra": "mean: 12.26507372500052 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.46414487417327,
            "unit": "iter/sec",
            "range": "stddev: 0.00017261888914269651",
            "extra": "mean: 39.270904440001004 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 73.08891060819963,
            "unit": "iter/sec",
            "range": "stddev: 0.0007700127060159932",
            "extra": "mean: 13.681966137935746 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.431095313935433,
            "unit": "iter/sec",
            "range": "stddev: 0.00033974760940071907",
            "extra": "mean: 39.321939840004916 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 71.82897248205516,
            "unit": "iter/sec",
            "range": "stddev: 0.00022575320058150844",
            "extra": "mean: 13.921958862070971 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.573621260582076,
            "unit": "iter/sec",
            "range": "stddev: 0.00021571434079471468",
            "extra": "mean: 39.10279228000263 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 65.04244621256937,
            "unit": "iter/sec",
            "range": "stddev: 0.002624674468248851",
            "extra": "mean: 15.374575500002509 msec\nrounds: 28"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.61076409240688,
            "unit": "iter/sec",
            "range": "stddev: 0.00013985277725531685",
            "extra": "mean: 23.468248488371913 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 94.71052311905139,
            "unit": "iter/sec",
            "range": "stddev: 0.0004728955881174976",
            "extra": "mean: 10.558488825396912 msec\nrounds: 63"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.39571184454286,
            "unit": "iter/sec",
            "range": "stddev: 0.0002907222510950044",
            "extra": "mean: 18.05193879999778 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 144.94075546624427,
            "unit": "iter/sec",
            "range": "stddev: 0.00026587436167096155",
            "extra": "mean: 6.8993706896532165 msec\nrounds: 87"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.0324630849302,
            "unit": "iter/sec",
            "range": "stddev: 0.00020605622371284903",
            "extra": "mean: 24.979727025001353 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 105.50040939880238,
            "unit": "iter/sec",
            "range": "stddev: 0.0003859547614473175",
            "extra": "mean: 9.478636203390428 msec\nrounds: 59"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.703325712748885,
            "unit": "iter/sec",
            "range": "stddev: 0.00013039676944269827",
            "extra": "mean: 25.186806950000573 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 95.91993207371661,
            "unit": "iter/sec",
            "range": "stddev: 0.0003196618662661116",
            "extra": "mean: 10.425361844829892 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 30.856618304869947,
            "unit": "iter/sec",
            "range": "stddev: 0.00025894121019169066",
            "extra": "mean: 32.407958322580505 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 94.79598297794799,
            "unit": "iter/sec",
            "range": "stddev: 0.00021611293544967036",
            "extra": "mean: 10.54897020512595 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.850697321120336,
            "unit": "iter/sec",
            "range": "stddev: 0.0001052183976669638",
            "extra": "mean: 32.414178181813796 msec\nrounds: 22"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 88.42857482180051,
            "unit": "iter/sec",
            "range": "stddev: 0.0003233781267875588",
            "extra": "mean: 11.308561763153822 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.75739712189092,
            "unit": "iter/sec",
            "range": "stddev: 0.00020756212119056234",
            "extra": "mean: 28.770854057140532 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 115.10507767271689,
            "unit": "iter/sec",
            "range": "stddev: 0.0001637770536321716",
            "extra": "mean: 8.687714045451079 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.234082977676497,
            "unit": "iter/sec",
            "range": "stddev: 0.0007608494866935516",
            "extra": "mean: 44.97599478260569 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 82.99266943945901,
            "unit": "iter/sec",
            "range": "stddev: 0.0003970759395384209",
            "extra": "mean: 12.049256961537717 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.987405877759603,
            "unit": "iter/sec",
            "range": "stddev: 0.0003173941534495987",
            "extra": "mean: 45.48058127273242 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 81.42723553870252,
            "unit": "iter/sec",
            "range": "stddev: 0.0006918303357403295",
            "extra": "mean: 12.280903230770964 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.235429057356342,
            "unit": "iter/sec",
            "range": "stddev: 0.0010569428948340946",
            "extra": "mean: 44.97327204348059 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 88.83871035549392,
            "unit": "iter/sec",
            "range": "stddev: 0.0003625689151082041",
            "extra": "mean: 11.25635430769351 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.75651690301631,
            "unit": "iter/sec",
            "range": "stddev: 0.0003105299095800669",
            "extra": "mean: 22.343114906973607 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 125.88248954876256,
            "unit": "iter/sec",
            "range": "stddev: 0.00020900805288894477",
            "extra": "mean: 7.943916612902975 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.390157552808695,
            "unit": "iter/sec",
            "range": "stddev: 0.00029239759335817635",
            "extra": "mean: 20.246948978261205 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 149.2435004004974,
            "unit": "iter/sec",
            "range": "stddev: 0.00006127680052575632",
            "extra": "mean: 6.700459298505352 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.17637731618022,
            "unit": "iter/sec",
            "range": "stddev: 0.0008176923624257171",
            "extra": "mean: 23.70995480487528 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 141.47842953343206,
            "unit": "iter/sec",
            "range": "stddev: 0.00009240973599534962",
            "extra": "mean: 7.068215298245836 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.82832136452242,
            "unit": "iter/sec",
            "range": "stddev: 0.0007534655309271519",
            "extra": "mean: 23.907246750001576 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 140.39567728512085,
            "unit": "iter/sec",
            "range": "stddev: 0.00010156697009067603",
            "extra": "mean: 7.12272642105043 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.89854813751375,
            "unit": "iter/sec",
            "range": "stddev: 0.00031992771271228737",
            "extra": "mean: 29.499788484845237 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 112.31038080123407,
            "unit": "iter/sec",
            "range": "stddev: 0.00025991990714810246",
            "extra": "mean: 8.903896441859557 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.67048265935094,
            "unit": "iter/sec",
            "range": "stddev: 0.0004162487819261134",
            "extra": "mean: 30.608669312504944 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 114.05808414452102,
            "unit": "iter/sec",
            "range": "stddev: 0.00009954269560967204",
            "extra": "mean: 8.767462714286149 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.362991916971225,
            "unit": "iter/sec",
            "range": "stddev: 0.00040126188873382024",
            "extra": "mean: 27.500487371427848 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 129.895547410982,
            "unit": "iter/sec",
            "range": "stddev: 0.00017509127691433946",
            "extra": "mean: 7.698493288888939 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.06690908965536,
            "unit": "iter/sec",
            "range": "stddev: 0.00032333183735843693",
            "extra": "mean: 38.362814576924634 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.04490713998912,
            "unit": "iter/sec",
            "range": "stddev: 0.0001584816357971056",
            "extra": "mean: 9.005365718747882 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.458290074883593,
            "unit": "iter/sec",
            "range": "stddev: 0.0010660266174781215",
            "extra": "mean: 37.795337384606086 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.2995783490382,
            "unit": "iter/sec",
            "range": "stddev: 0.0003080645579980046",
            "extra": "mean: 9.587766468753145 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.881448752931128,
            "unit": "iter/sec",
            "range": "stddev: 0.00022449660319398814",
            "extra": "mean: 37.2003759615434 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 94.00981835015392,
            "unit": "iter/sec",
            "range": "stddev: 0.00026420709066674194",
            "extra": "mean: 10.637186812502364 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.47965217447574,
            "unit": "iter/sec",
            "range": "stddev: 0.0008775687172578914",
            "extra": "mean: 22.9992640232536 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.14382276496,
            "unit": "iter/sec",
            "range": "stddev: 0.000527296943425862",
            "extra": "mean: 7.238832544119004 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.51911324015756,
            "unit": "iter/sec",
            "range": "stddev: 0.0005648588722529854",
            "extra": "mean: 19.794488379995983 msec\nrounds: 50"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.76757192841285,
            "unit": "iter/sec",
            "range": "stddev: 0.00008054671173390429",
            "extra": "mean: 5.890406445947624 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.45362499285759,
            "unit": "iter/sec",
            "range": "stddev: 0.0007579246516676405",
            "extra": "mean: 23.013039767438702 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.3243960997279,
            "unit": "iter/sec",
            "range": "stddev: 0.00010451676153173437",
            "extra": "mean: 5.8368803437538475 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.83284500724039,
            "unit": "iter/sec",
            "range": "stddev: 0.00040189183160578194",
            "extra": "mean: 22.81394237209148 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 170.6373388570871,
            "unit": "iter/sec",
            "range": "stddev: 0.00009351573963368846",
            "extra": "mean: 5.860382063491533 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.66914299483775,
            "unit": "iter/sec",
            "range": "stddev: 0.0006947318229817952",
            "extra": "mean: 29.70078567646711 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 130.42410798062318,
            "unit": "iter/sec",
            "range": "stddev: 0.00019302166691016124",
            "extra": "mean: 7.667294148935777 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.73096798980488,
            "unit": "iter/sec",
            "range": "stddev: 0.00023726090060353675",
            "extra": "mean: 30.552105892849927 msec\nrounds: 28"
          },
          {
            "name": "dateline-int32-none",
            "value": 122.30457832012608,
            "unit": "iter/sec",
            "range": "stddev: 0.0006333634911009229",
            "extra": "mean: 8.176308800007064 msec\nrounds: 25"
          },
          {
            "name": "equator-float32-none",
            "value": 35.90737799568553,
            "unit": "iter/sec",
            "range": "stddev: 0.0008311556117915493",
            "extra": "mean: 27.84942972221908 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 149.00263036767782,
            "unit": "iter/sec",
            "range": "stddev: 0.00024613865031962245",
            "extra": "mean: 6.711290918371087 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 27.220957850176088,
            "unit": "iter/sec",
            "range": "stddev: 0.0009845227118849718",
            "extra": "mean: 36.73640014815023 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 121.69286132743485,
            "unit": "iter/sec",
            "range": "stddev: 0.00012694914652461195",
            "extra": "mean: 8.217408885713796 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 26.71345470874331,
            "unit": "iter/sec",
            "range": "stddev: 0.0005127117116776004",
            "extra": "mean: 37.43431955555715 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.8147800964589,
            "unit": "iter/sec",
            "range": "stddev: 0.0001566296530664025",
            "extra": "mean: 8.786205088236276 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.26352748453431,
            "unit": "iter/sec",
            "range": "stddev: 0.00028022487778247125",
            "extra": "mean: 36.679039444447035 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.48811734409024,
            "unit": "iter/sec",
            "range": "stddev: 0.0001358448629428267",
            "extra": "mean: 8.511499057145295 msec\nrounds: 35"
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
          "id": "ffac76681c0d62961675564c067788aa2fb2c6f3",
          "message": "add experimental features (#786)",
          "timestamp": "2025-02-26T18:03:15+01:00",
          "tree_id": "b2594f54a7d4cba541cf9f39f3c48cad421637a2",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ffac76681c0d62961675564c067788aa2fb2c6f3"
        },
        "date": 1740589794362,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.189343621116784,
            "unit": "iter/sec",
            "range": "stddev: 0.000225437579608642",
            "extra": "mean: 26.185315199998627 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.13035133723477,
            "unit": "iter/sec",
            "range": "stddev: 0.00008024216931490789",
            "extra": "mean: 12.175766738095495 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.507935753988676,
            "unit": "iter/sec",
            "range": "stddev: 0.00012480875752043718",
            "extra": "mean: 21.04911493478312 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.946546175368,
            "unit": "iter/sec",
            "range": "stddev: 0.00008811543176199762",
            "extra": "mean: 7.755151492309026 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.96424855820393,
            "unit": "iter/sec",
            "range": "stddev: 0.00020607504656645768",
            "extra": "mean: 26.340571405407253 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.4520411934291,
            "unit": "iter/sec",
            "range": "stddev: 0.00008875955586095337",
            "extra": "mean: 8.100311589284814 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.74592589068484,
            "unit": "iter/sec",
            "range": "stddev: 0.0001792175918422167",
            "extra": "mean: 26.49292543243153 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.0907924680412,
            "unit": "iter/sec",
            "range": "stddev: 0.0006372289709863653",
            "extra": "mean: 9.001646111109359 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.64772922098145,
            "unit": "iter/sec",
            "range": "stddev: 0.0005332706309023715",
            "extra": "mean: 31.597843656252955 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 77.50390017014344,
            "unit": "iter/sec",
            "range": "stddev: 0.0019922345342516887",
            "extra": "mean: 12.9025764871795 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.05304356178213,
            "unit": "iter/sec",
            "range": "stddev: 0.00048118078302827205",
            "extra": "mean: 33.274500066664814 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.59720236348281,
            "unit": "iter/sec",
            "range": "stddev: 0.0001473779712892973",
            "extra": "mean: 12.255322131577516 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.939707718965366,
            "unit": "iter/sec",
            "range": "stddev: 0.00017983316782157596",
            "extra": "mean: 30.358496454546252 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 90.04061701487115,
            "unit": "iter/sec",
            "range": "stddev: 0.00020812915803711075",
            "extra": "mean: 11.106098926830315 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.067764143466675,
            "unit": "iter/sec",
            "range": "stddev: 0.00024551152981264906",
            "extra": "mean: 38.3615562307682 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.43005193874102,
            "unit": "iter/sec",
            "range": "stddev: 0.0002071337158948175",
            "extra": "mean: 13.083858699998057 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.053539789786004,
            "unit": "iter/sec",
            "range": "stddev: 0.00036133604433847514",
            "extra": "mean: 38.38250034615406 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.23606835646099,
            "unit": "iter/sec",
            "range": "stddev: 0.00017544709283597655",
            "extra": "mean: 13.470540966667006 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.09693953501815,
            "unit": "iter/sec",
            "range": "stddev: 0.0007791566042871665",
            "extra": "mean: 38.31866946153403 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 75.67557095705443,
            "unit": "iter/sec",
            "range": "stddev: 0.00020722383353549684",
            "extra": "mean: 13.214303999998833 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.19354842025059,
            "unit": "iter/sec",
            "range": "stddev: 0.0002293388154526573",
            "extra": "mean: 22.627737209302136 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 101.07584587253388,
            "unit": "iter/sec",
            "range": "stddev: 0.0001131071730380634",
            "extra": "mean: 9.89356053731268 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.39185736578532,
            "unit": "iter/sec",
            "range": "stddev: 0.00010421759195613164",
            "extra": "mean: 17.424074527271863 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 154.764247015769,
            "unit": "iter/sec",
            "range": "stddev: 0.00029788532389264964",
            "extra": "mean: 6.461440670454783 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.20588933715415,
            "unit": "iter/sec",
            "range": "stddev: 0.000126449925871589",
            "extra": "mean: 24.26837561538392 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.35325019513348,
            "unit": "iter/sec",
            "range": "stddev: 0.000527347321845773",
            "extra": "mean: 8.8219790634899 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.30479875302603,
            "unit": "iter/sec",
            "range": "stddev: 0.00034726849254126973",
            "extra": "mean: 24.810941399996977 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 105.91017556441444,
            "unit": "iter/sec",
            "range": "stddev: 0.0005144970178451397",
            "extra": "mean: 9.441963387094956 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.945133370917407,
            "unit": "iter/sec",
            "range": "stddev: 0.0003381904146855925",
            "extra": "mean: 31.303672718749453 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 104.90504624642406,
            "unit": "iter/sec",
            "range": "stddev: 0.0004600524989111444",
            "extra": "mean: 9.532429904763399 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.83084514986158,
            "unit": "iter/sec",
            "range": "stddev: 0.00021794653458890133",
            "extra": "mean: 32.4350498709728 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 102.17313307671867,
            "unit": "iter/sec",
            "range": "stddev: 0.0005740744817977105",
            "extra": "mean: 9.787308756100595 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.259027163972604,
            "unit": "iter/sec",
            "range": "stddev: 0.0003824380047141452",
            "extra": "mean: 28.361531228569806 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 120.43795153411942,
            "unit": "iter/sec",
            "range": "stddev: 0.002081740155801391",
            "extra": "mean: 8.303030624999508 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.013260931349908,
            "unit": "iter/sec",
            "range": "stddev: 0.00034708810525888983",
            "extra": "mean: 43.45320739129786 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 90.0352366057856,
            "unit": "iter/sec",
            "range": "stddev: 0.0007273906988595073",
            "extra": "mean: 11.10676261537964 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.35092269571643,
            "unit": "iter/sec",
            "range": "stddev: 0.0007058623290499784",
            "extra": "mean: 44.74088222727604 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 84.9157681094737,
            "unit": "iter/sec",
            "range": "stddev: 0.0011349070825229643",
            "extra": "mean: 11.776375840006494 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.617105810570326,
            "unit": "iter/sec",
            "range": "stddev: 0.0011270226773958628",
            "extra": "mean: 44.21432204347915 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 88.38802226541176,
            "unit": "iter/sec",
            "range": "stddev: 0.0006527518242027206",
            "extra": "mean: 11.313750148150136 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.93844667292992,
            "unit": "iter/sec",
            "range": "stddev: 0.00024743224589883586",
            "extra": "mean: 22.75911134145966 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.18724358105585,
            "unit": "iter/sec",
            "range": "stddev: 0.0002321401218029025",
            "extra": "mean: 8.117723645159826 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.615444557096524,
            "unit": "iter/sec",
            "range": "stddev: 0.0005599759775440088",
            "extra": "mean: 20.569594891301417 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.70593886497608,
            "unit": "iter/sec",
            "range": "stddev: 0.00021309901836451514",
            "extra": "mean: 6.863138234376898 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.40363013759126,
            "unit": "iter/sec",
            "range": "stddev: 0.0006859483248618657",
            "extra": "mean: 24.152471575000334 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 138.47080670962495,
            "unit": "iter/sec",
            "range": "stddev: 0.0003495648431209199",
            "extra": "mean: 7.221738818182902 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.24838207733733,
            "unit": "iter/sec",
            "range": "stddev: 0.001021234415385104",
            "extra": "mean: 24.24337512499477 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 139.06611143398558,
            "unit": "iter/sec",
            "range": "stddev: 0.0005607188199507087",
            "extra": "mean: 7.190824491232705 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.67804262538315,
            "unit": "iter/sec",
            "range": "stddev: 0.0004176987240671621",
            "extra": "mean: 29.692937060608735 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 118.74238890970537,
            "unit": "iter/sec",
            "range": "stddev: 0.0005078852995620369",
            "extra": "mean: 8.421592400001526 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.58530135383125,
            "unit": "iter/sec",
            "range": "stddev: 0.0006335695386062383",
            "extra": "mean: 30.688683500004643 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 115.50091909864614,
            "unit": "iter/sec",
            "range": "stddev: 0.0006747211577816268",
            "extra": "mean: 8.657939761898584 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.49012964536188,
            "unit": "iter/sec",
            "range": "stddev: 0.0008842752979245864",
            "extra": "mean: 28.176848323536273 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 130.83193705076923,
            "unit": "iter/sec",
            "range": "stddev: 0.0005884942055328964",
            "extra": "mean: 7.643393673915804 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.333590509345907,
            "unit": "iter/sec",
            "range": "stddev: 0.000363079238175818",
            "extra": "mean: 36.58502162963478 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.91345899979767,
            "unit": "iter/sec",
            "range": "stddev: 0.0006490485212187371",
            "extra": "mean: 9.098066870972016 msec\nrounds: 31"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.523914604618277,
            "unit": "iter/sec",
            "range": "stddev: 0.0006310782222949727",
            "extra": "mean: 37.70182549999171 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 100.83006300234747,
            "unit": "iter/sec",
            "range": "stddev: 0.0006809628028076615",
            "extra": "mean: 9.917677032262873 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.779931383923277,
            "unit": "iter/sec",
            "range": "stddev: 0.001010225004540811",
            "extra": "mean: 37.34139515384746 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 103.90050558106783,
            "unit": "iter/sec",
            "range": "stddev: 0.0007248007480613979",
            "extra": "mean: 9.624592242429035 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 44.57625113594743,
            "unit": "iter/sec",
            "range": "stddev: 0.0006073739280109727",
            "extra": "mean: 22.433470166664023 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-none",
            "value": 133.5003211141793,
            "unit": "iter/sec",
            "range": "stddev: 0.0005221695336922491",
            "extra": "mean: 7.490618686562757 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.986151600465995,
            "unit": "iter/sec",
            "range": "stddev: 0.0006392499732676296",
            "extra": "mean: 20.413932659092314 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.34920628809706,
            "unit": "iter/sec",
            "range": "stddev: 0.00024054266640554552",
            "extra": "mean: 5.940033945207283 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.49269996220722,
            "unit": "iter/sec",
            "range": "stddev: 0.0005230027875058807",
            "extra": "mean: 22.992364255816387 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 168.2871292912493,
            "unit": "iter/sec",
            "range": "stddev: 0.00037415256218940987",
            "extra": "mean: 5.9422250781242525 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.41732717514514,
            "unit": "iter/sec",
            "range": "stddev: 0.0007951597666230448",
            "extra": "mean: 23.032279162786974 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 169.90682075310625,
            "unit": "iter/sec",
            "range": "stddev: 0.0002653669786373586",
            "extra": "mean: 5.885578904763998 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.76972656466674,
            "unit": "iter/sec",
            "range": "stddev: 0.0007145304221204007",
            "extra": "mean: 29.61232149999994 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 128.56435264728833,
            "unit": "iter/sec",
            "range": "stddev: 0.0008654523116062969",
            "extra": "mean: 7.778205851068717 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.37823502986522,
            "unit": "iter/sec",
            "range": "stddev: 0.00036765679507829536",
            "extra": "mean: 30.88494475000303 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 126.5170423081523,
            "unit": "iter/sec",
            "range": "stddev: 0.0008054474656518859",
            "extra": "mean: 7.904073488884934 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.3822511865302,
            "unit": "iter/sec",
            "range": "stddev: 0.0011734335459920421",
            "extra": "mean: 27.485929742858517 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 150.18172086165112,
            "unit": "iter/sec",
            "range": "stddev: 0.0011403364845377552",
            "extra": "mean: 6.658599956523403 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-none",
            "value": 27.020229289101955,
            "unit": "iter/sec",
            "range": "stddev: 0.0011620463882096527",
            "extra": "mean: 37.009308444444954 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 118.12410444994725,
            "unit": "iter/sec",
            "range": "stddev: 0.0006635875918571505",
            "extra": "mean: 8.46567264705681 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.534796652361457,
            "unit": "iter/sec",
            "range": "stddev: 0.0008415885851262715",
            "extra": "mean: 37.686363800003164 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-none",
            "value": 102.87839995524807,
            "unit": "iter/sec",
            "range": "stddev: 0.001197818528655549",
            "extra": "mean: 9.720213382352354 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.920288541061456,
            "unit": "iter/sec",
            "range": "stddev: 0.0005037945594723313",
            "extra": "mean: 37.14670437037486 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 112.75186915211262,
            "unit": "iter/sec",
            "range": "stddev: 0.001418079111582436",
            "extra": "mean: 8.869032571432658 msec\nrounds: 35"
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
          "id": "69d77a24ef44e2cd81569ca45d0bfc5ac83db0b4",
          "message": "Bump version: 7.4.0 → 7.5.0",
          "timestamp": "2025-02-26T18:03:53+01:00",
          "tree_id": "8dc6d36325d491467f352f3a8e55ef1becf367c7",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/69d77a24ef44e2cd81569ca45d0bfc5ac83db0b4"
        },
        "date": 1740589838051,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 35.32816798927062,
            "unit": "iter/sec",
            "range": "stddev: 0.001300343533073902",
            "extra": "mean: 28.306024821431613 msec\nrounds: 28"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 77.68282858108995,
            "unit": "iter/sec",
            "range": "stddev: 0.0010182537667411465",
            "extra": "mean: 12.872857725000841 msec\nrounds: 40"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 45.86532857321918,
            "unit": "iter/sec",
            "range": "stddev: 0.0002605793910675237",
            "extra": "mean: 21.802961651165432 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 113.58833551455265,
            "unit": "iter/sec",
            "range": "stddev: 0.00019975806904524136",
            "extra": "mean: 8.803720870369498 msec\nrounds: 54"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 35.475348324957274,
            "unit": "iter/sec",
            "range": "stddev: 0.00022749006735483122",
            "extra": "mean: 28.188588617648318 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 111.92437434180795,
            "unit": "iter/sec",
            "range": "stddev: 0.0003442918669108123",
            "extra": "mean: 8.934604333333874 msec\nrounds: 51"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.67654606021712,
            "unit": "iter/sec",
            "range": "stddev: 0.00033514506575084657",
            "extra": "mean: 27.26538094285534 msec\nrounds: 35"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 111.69562184390354,
            "unit": "iter/sec",
            "range": "stddev: 0.00011260358164809248",
            "extra": "mean: 8.952902392159258 msec\nrounds: 51"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.899349026259994,
            "unit": "iter/sec",
            "range": "stddev: 0.00029718915340994117",
            "extra": "mean: 32.36314134482717 msec\nrounds: 29"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 78.33989237708516,
            "unit": "iter/sec",
            "range": "stddev: 0.0002679026854823668",
            "extra": "mean: 12.764888611112072 msec\nrounds: 36"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.33208726992341,
            "unit": "iter/sec",
            "range": "stddev: 0.00025802215025667034",
            "extra": "mean: 32.968387275859406 msec\nrounds: 29"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 79.48965275903431,
            "unit": "iter/sec",
            "range": "stddev: 0.00022240092301295013",
            "extra": "mean: 12.580253722222304 msec\nrounds: 36"
          },
          {
            "name": "equator-float32-nodata",
            "value": 31.88101917564857,
            "unit": "iter/sec",
            "range": "stddev: 0.002034275907770166",
            "extra": "mean: 31.366625843750384 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 90.62012413466694,
            "unit": "iter/sec",
            "range": "stddev: 0.00035627355510199946",
            "extra": "mean: 11.035076474999528 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.35338228773856,
            "unit": "iter/sec",
            "range": "stddev: 0.0010250239890271958",
            "extra": "mean: 39.442469200001824 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 69.87358369339405,
            "unit": "iter/sec",
            "range": "stddev: 0.0005848629616752535",
            "extra": "mean: 14.311560208332944 msec\nrounds: 24"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.226025458386108,
            "unit": "iter/sec",
            "range": "stddev: 0.0006064550638355327",
            "extra": "mean: 39.64159957142838 msec\nrounds: 21"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 71.85038616669704,
            "unit": "iter/sec",
            "range": "stddev: 0.00024066676324586682",
            "extra": "mean: 13.917809678572114 msec\nrounds: 28"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.314669980160854,
            "unit": "iter/sec",
            "range": "stddev: 0.00041045716828897307",
            "extra": "mean: 39.502786359992115 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 69.4642856800928,
            "unit": "iter/sec",
            "range": "stddev: 0.0007429493732760235",
            "extra": "mean: 14.395886896546346 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.17726771288337,
            "unit": "iter/sec",
            "range": "stddev: 0.0006673963011332963",
            "extra": "mean: 23.709454268289225 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 96.03342052863741,
            "unit": "iter/sec",
            "range": "stddev: 0.00029704449873534404",
            "extra": "mean: 10.41304156922951 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 55.5241417743662,
            "unit": "iter/sec",
            "range": "stddev: 0.00023398053689856763",
            "extra": "mean: 18.010183823528624 msec\nrounds: 51"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 152.0882702713945,
            "unit": "iter/sec",
            "range": "stddev: 0.00010546650887701309",
            "extra": "mean: 6.575129023530521 msec\nrounds: 85"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 38.93090232954423,
            "unit": "iter/sec",
            "range": "stddev: 0.00035975138650130763",
            "extra": "mean: 25.68653537837758 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 103.28126571694371,
            "unit": "iter/sec",
            "range": "stddev: 0.0007080554565407006",
            "extra": "mean: 9.682298072727297 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.71931011592846,
            "unit": "iter/sec",
            "range": "stddev: 0.0008319866169839813",
            "extra": "mean: 25.176670921053443 msec\nrounds: 38"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.12484536599496,
            "unit": "iter/sec",
            "range": "stddev: 0.0005430147878766431",
            "extra": "mean: 9.791936491225036 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.16220953404866,
            "unit": "iter/sec",
            "range": "stddev: 0.0003753263771165645",
            "extra": "mean: 31.092391178577014 msec\nrounds: 28"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 103.55053571744855,
            "unit": "iter/sec",
            "range": "stddev: 0.0003639317365517241",
            "extra": "mean: 9.657120487803496 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.217966139311578,
            "unit": "iter/sec",
            "range": "stddev: 0.0006510473176254232",
            "extra": "mean: 32.032836333329826 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 103.2711349405263,
            "unit": "iter/sec",
            "range": "stddev: 0.0002198123522609864",
            "extra": "mean: 9.683247894737466 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.43497913166889,
            "unit": "iter/sec",
            "range": "stddev: 0.0004800154561037815",
            "extra": "mean: 28.220702382360983 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 125.6826761453853,
            "unit": "iter/sec",
            "range": "stddev: 0.0007218798323441509",
            "extra": "mean: 7.956546046515077 msec\nrounds: 43"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.385850442824324,
            "unit": "iter/sec",
            "range": "stddev: 0.001426243886338359",
            "extra": "mean: 44.67107481818031 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 85.38932964283137,
            "unit": "iter/sec",
            "range": "stddev: 0.00029155046885552375",
            "extra": "mean: 11.711065119995965 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.039595411453732,
            "unit": "iter/sec",
            "range": "stddev: 0.00040518372616031616",
            "extra": "mean: 45.372883727271656 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.22628415807287,
            "unit": "iter/sec",
            "range": "stddev: 0.0002671765615885438",
            "extra": "mean: 11.334490730770487 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.410032373347384,
            "unit": "iter/sec",
            "range": "stddev: 0.00037694394621609276",
            "extra": "mean: 44.62287172727677 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 88.98672896074712,
            "unit": "iter/sec",
            "range": "stddev: 0.0005968737303256674",
            "extra": "mean: 11.237630730770084 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.32143479484368,
            "unit": "iter/sec",
            "range": "stddev: 0.0008131401722339744",
            "extra": "mean: 23.08326131707495 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 124.83201524971696,
            "unit": "iter/sec",
            "range": "stddev: 0.00009287734314382199",
            "extra": "mean: 8.010765491525358 msec\nrounds: 59"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.47704692631156,
            "unit": "iter/sec",
            "range": "stddev: 0.0009724500183541974",
            "extra": "mean: 21.06280960465139 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 143.5963547232631,
            "unit": "iter/sec",
            "range": "stddev: 0.00040654436749209313",
            "extra": "mean: 6.9639650806400075 msec\nrounds: 62"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.74262404270686,
            "unit": "iter/sec",
            "range": "stddev: 0.0007095927947921733",
            "extra": "mean: 24.54431994737966 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 137.74941598004173,
            "unit": "iter/sec",
            "range": "stddev: 0.0001881622661281377",
            "extra": "mean: 7.259558909091043 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.057304197004015,
            "unit": "iter/sec",
            "range": "stddev: 0.00026853168060096363",
            "extra": "mean: 24.356202131580055 msec\nrounds: 38"
          },
          {
            "name": "dateline-int16-mask",
            "value": 140.77481784016106,
            "unit": "iter/sec",
            "range": "stddev: 0.00012613101276991517",
            "extra": "mean: 7.103543200002026 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.820433108937024,
            "unit": "iter/sec",
            "range": "stddev: 0.00048739179978091754",
            "extra": "mean: 30.468824000000758 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 120.48899252724655,
            "unit": "iter/sec",
            "range": "stddev: 0.00015933878413551528",
            "extra": "mean: 8.299513333335133 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.48922155455253,
            "unit": "iter/sec",
            "range": "stddev: 0.0004829437776443168",
            "extra": "mean: 30.7794385999955 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.17633906810013,
            "unit": "iter/sec",
            "range": "stddev: 0.00015945490643520596",
            "extra": "mean: 8.53414612500245 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.58863370560005,
            "unit": "iter/sec",
            "range": "stddev: 0.0004801277842584207",
            "extra": "mean: 28.911231606066462 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-mask",
            "value": 133.63289779535143,
            "unit": "iter/sec",
            "range": "stddev: 0.00012456520591848426",
            "extra": "mean: 7.483187272728483 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.068467528340413,
            "unit": "iter/sec",
            "range": "stddev: 0.00041763063895309936",
            "extra": "mean: 36.943354807693126 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 103.40525025232944,
            "unit": "iter/sec",
            "range": "stddev: 0.00019311374280754002",
            "extra": "mean: 9.670688843746333 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 25.940455951597006,
            "unit": "iter/sec",
            "range": "stddev: 0.0009199682838203735",
            "extra": "mean: 38.54982355999937 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-mask",
            "value": 99.24170247483991,
            "unit": "iter/sec",
            "range": "stddev: 0.00023879265125836845",
            "extra": "mean: 10.076409161295105 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.24838055063727,
            "unit": "iter/sec",
            "range": "stddev: 0.0006418929151068273",
            "extra": "mean: 38.097588461537356 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 98.81166635681434,
            "unit": "iter/sec",
            "range": "stddev: 0.0003240387189527752",
            "extra": "mean: 10.12026248387458 msec\nrounds: 31"
          },
          {
            "name": "equator-int8-none",
            "value": 43.4254784749082,
            "unit": "iter/sec",
            "range": "stddev: 0.0003338205989063255",
            "extra": "mean: 23.027955825007496 msec\nrounds: 40"
          },
          {
            "name": "dateline-int8-none",
            "value": 134.00460331316745,
            "unit": "iter/sec",
            "range": "stddev: 0.00016943650695811491",
            "extra": "mean: 7.462430209677274 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-none",
            "value": 47.05779421819706,
            "unit": "iter/sec",
            "range": "stddev: 0.0005933223053255756",
            "extra": "mean: 21.25046480851208 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.09828830961362,
            "unit": "iter/sec",
            "range": "stddev: 0.00009712067673463729",
            "extra": "mean: 5.913720416666972 msec\nrounds: 72"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.648222795721104,
            "unit": "iter/sec",
            "range": "stddev: 0.0003373578276703712",
            "extra": "mean: 23.447635902435074 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-none",
            "value": 167.35145731927287,
            "unit": "iter/sec",
            "range": "stddev: 0.00010576686232570293",
            "extra": "mean: 5.975448412691152 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 40.98668131437089,
            "unit": "iter/sec",
            "range": "stddev: 0.00022931374245893928",
            "extra": "mean: 24.398169550003956 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-none",
            "value": 164.84079365378165,
            "unit": "iter/sec",
            "range": "stddev: 0.0003101719189350093",
            "extra": "mean: 6.066459508198678 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-none",
            "value": 32.24853455403614,
            "unit": "iter/sec",
            "range": "stddev: 0.0005272918665268428",
            "extra": "mean: 31.009160999994734 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-none",
            "value": 122.06950188215667,
            "unit": "iter/sec",
            "range": "stddev: 0.00026457042389218426",
            "extra": "mean: 8.192054400003851 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-none",
            "value": 31.942385334102557,
            "unit": "iter/sec",
            "range": "stddev: 0.00023781540745258372",
            "extra": "mean: 31.306365806450057 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-none",
            "value": 119.96142486948118,
            "unit": "iter/sec",
            "range": "stddev: 0.00025679354224693654",
            "extra": "mean: 8.336013023253154 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-none",
            "value": 34.8904483186937,
            "unit": "iter/sec",
            "range": "stddev: 0.00032268645540005727",
            "extra": "mean: 28.661139314286693 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 138.1511974205224,
            "unit": "iter/sec",
            "range": "stddev: 0.00039937378330269827",
            "extra": "mean: 7.238446127658752 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-none",
            "value": 26.796178036802225,
            "unit": "iter/sec",
            "range": "stddev: 0.0006990534487558834",
            "extra": "mean: 37.318754884617746 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-none",
            "value": 109.91802057551513,
            "unit": "iter/sec",
            "range": "stddev: 0.00043501351078611413",
            "extra": "mean: 9.097689303029131 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-none",
            "value": 26.2108294540025,
            "unit": "iter/sec",
            "range": "stddev: 0.00031853499527302685",
            "extra": "mean: 38.15216919231436 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.5419268843595,
            "unit": "iter/sec",
            "range": "stddev: 0.00021072346282379481",
            "extra": "mean: 8.807319264701952 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.51506121561361,
            "unit": "iter/sec",
            "range": "stddev: 0.0005310339145750361",
            "extra": "mean: 37.71441415383728 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 109.1576995862997,
            "unit": "iter/sec",
            "range": "stddev: 0.00028333113188978105",
            "extra": "mean: 9.161057843742881 msec\nrounds: 32"
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
          "id": "ee3d17fc168db938bf8779a5e0283da9ac64b361",
          "message": "set GDAL_MEM_ENABLE_OPEN=True when opening a mem array (#787)",
          "timestamp": "2025-03-03T10:59:14+01:00",
          "tree_id": "59c59965dd29147772c23346a75177b54c5a18ad",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ee3d17fc168db938bf8779a5e0283da9ac64b361"
        },
        "date": 1740996352563,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.59461898060524,
            "unit": "iter/sec",
            "range": "stddev: 0.00009547415220207634",
            "extra": "mean: 25.910347774194243 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.21199124793627,
            "unit": "iter/sec",
            "range": "stddev: 0.0000764975162467874",
            "extra": "mean: 12.163675697675096 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.46698864418981,
            "unit": "iter/sec",
            "range": "stddev: 0.0005719444599943084",
            "extra": "mean: 21.067272826088683 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.0884352615023,
            "unit": "iter/sec",
            "range": "stddev: 0.00003179575784805161",
            "extra": "mean: 7.687078393938795 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.525627871168474,
            "unit": "iter/sec",
            "range": "stddev: 0.0002439336004337588",
            "extra": "mean: 25.9567476315778 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.40900325502615,
            "unit": "iter/sec",
            "range": "stddev: 0.0005239404576222126",
            "extra": "mean: 8.236621446429686 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.3508808606111,
            "unit": "iter/sec",
            "range": "stddev: 0.000589417223613685",
            "extra": "mean: 26.773130297298138 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.31320862693474,
            "unit": "iter/sec",
            "range": "stddev: 0.0003597998599240705",
            "extra": "mean: 8.903672259258933 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.852848503887913,
            "unit": "iter/sec",
            "range": "stddev: 0.000576665811202294",
            "extra": "mean: 31.394366499998938 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 80.5765590372768,
            "unit": "iter/sec",
            "range": "stddev: 0.00039910044315412006",
            "extra": "mean: 12.410557263153596 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.414243609920636,
            "unit": "iter/sec",
            "range": "stddev: 0.0005750194114427835",
            "extra": "mean: 32.8793315666682 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.49074974374427,
            "unit": "iter/sec",
            "range": "stddev: 0.000547915869784659",
            "extra": "mean: 12.27133144736794 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.934570142427596,
            "unit": "iter/sec",
            "range": "stddev: 0.00045629813669519043",
            "extra": "mean: 29.468474060607694 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 92.89493262629436,
            "unit": "iter/sec",
            "range": "stddev: 0.00015935148289271137",
            "extra": "mean: 10.76484983333682 msec\nrounds: 42"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.685621560527995,
            "unit": "iter/sec",
            "range": "stddev: 0.001040976005804697",
            "extra": "mean: 38.932287375001096 msec\nrounds: 16"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.48448846636106,
            "unit": "iter/sec",
            "range": "stddev: 0.00018884481915826032",
            "extra": "mean: 12.90580888888668 msec\nrounds: 18"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.321279751637075,
            "unit": "iter/sec",
            "range": "stddev: 0.000278782442111007",
            "extra": "mean: 37.99207369230609 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.38302922029466,
            "unit": "iter/sec",
            "range": "stddev: 0.00034189461215075427",
            "extra": "mean: 13.443926800001313 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.352789243221075,
            "unit": "iter/sec",
            "range": "stddev: 0.0006457871066160132",
            "extra": "mean: 37.94664734615284 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.3459598031163,
            "unit": "iter/sec",
            "range": "stddev: 0.00021967626301029017",
            "extra": "mean: 13.098270066665425 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.681940202154955,
            "unit": "iter/sec",
            "range": "stddev: 0.0002061658338193097",
            "extra": "mean: 22.380406837207378 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.10252568958131,
            "unit": "iter/sec",
            "range": "stddev: 0.00031297553212151233",
            "extra": "mean: 9.794077014708376 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.726361138803654,
            "unit": "iter/sec",
            "range": "stddev: 0.00033086281601329076",
            "extra": "mean: 17.32310820000397 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.77530047057533,
            "unit": "iter/sec",
            "range": "stddev: 0.00010685455709734935",
            "extra": "mean: 6.378555786520001 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.4141820857966,
            "unit": "iter/sec",
            "range": "stddev: 0.0003413811583447311",
            "extra": "mean: 24.14631774999994 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.68675389554735,
            "unit": "iter/sec",
            "range": "stddev: 0.00005584844496576317",
            "extra": "mean: 8.796099507940703 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.39550677936113,
            "unit": "iter/sec",
            "range": "stddev: 0.00026909682381457106",
            "extra": "mean: 24.157211199998585 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.05261730203844,
            "unit": "iter/sec",
            "range": "stddev: 0.00006477242870517011",
            "extra": "mean: 9.341200852461162 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.91112575964734,
            "unit": "iter/sec",
            "range": "stddev: 0.002949269787557451",
            "extra": "mean: 31.337032968750123 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 109.976645180691,
            "unit": "iter/sec",
            "range": "stddev: 0.00013120894958622585",
            "extra": "mean: 9.092839651155076 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.439607359544794,
            "unit": "iter/sec",
            "range": "stddev: 0.00042882304507559034",
            "extra": "mean: 31.80701300000201 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 107.74467827677798,
            "unit": "iter/sec",
            "range": "stddev: 0.00018706866545884464",
            "extra": "mean: 9.281200853662284 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.47078868279381,
            "unit": "iter/sec",
            "range": "stddev: 0.00017051351975941204",
            "extra": "mean: 27.419204138894315 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 143.80078634559084,
            "unit": "iter/sec",
            "range": "stddev: 0.00013905865737624774",
            "extra": "mean: 6.954064893614273 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.70531135140808,
            "unit": "iter/sec",
            "range": "stddev: 0.003019959151520117",
            "extra": "mean: 44.04255834782836 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 82.58240779365055,
            "unit": "iter/sec",
            "range": "stddev: 0.0002414401823654837",
            "extra": "mean: 12.109116538460704 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.325596136844123,
            "unit": "iter/sec",
            "range": "stddev: 0.0003873200090124453",
            "extra": "mean: 44.79163709092146 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 73.36649830142393,
            "unit": "iter/sec",
            "range": "stddev: 0.00163644559191684",
            "extra": "mean: 13.630199384622825 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.2487934618348,
            "unit": "iter/sec",
            "range": "stddev: 0.0012414971855554727",
            "extra": "mean: 44.946257500002545 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 82.10365608684664,
            "unit": "iter/sec",
            "range": "stddev: 0.00017195400409019133",
            "extra": "mean: 12.179725576924756 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 42.02862681097046,
            "unit": "iter/sec",
            "range": "stddev: 0.0006732745126312616",
            "extra": "mean: 23.793306512193173 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 116.89831381825384,
            "unit": "iter/sec",
            "range": "stddev: 0.00014039759767389953",
            "extra": "mean: 8.554443322037452 msec\nrounds: 59"
          },
          {
            "name": "equator-uint8-mask",
            "value": 46.770912746568065,
            "unit": "iter/sec",
            "range": "stddev: 0.00022587052546195068",
            "extra": "mean: 21.380810022215734 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 139.0214633804597,
            "unit": "iter/sec",
            "range": "stddev: 0.00015479313195239467",
            "extra": "mean: 7.193133892306273 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.20955608123105,
            "unit": "iter/sec",
            "range": "stddev: 0.00012645704788909377",
            "extra": "mean: 24.86971002564185 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 131.30919837953607,
            "unit": "iter/sec",
            "range": "stddev: 0.00017024586403759334",
            "extra": "mean: 7.615612709092932 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.30489780574766,
            "unit": "iter/sec",
            "range": "stddev: 0.000587115900188997",
            "extra": "mean: 24.810880424993798 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 133.45272709867737,
            "unit": "iter/sec",
            "range": "stddev: 0.00014049486308088127",
            "extra": "mean: 7.493290109092951 msec\nrounds: 55"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.892976418659735,
            "unit": "iter/sec",
            "range": "stddev: 0.000211354563859705",
            "extra": "mean: 30.401627000003373 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 104.17970256542364,
            "unit": "iter/sec",
            "range": "stddev: 0.0003664473489920715",
            "extra": "mean: 9.598798761899053 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.00462435849469,
            "unit": "iter/sec",
            "range": "stddev: 0.0007716873316033977",
            "extra": "mean: 31.24548467742223 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 105.92663118485652,
            "unit": "iter/sec",
            "range": "stddev: 0.0008425238201166614",
            "extra": "mean: 9.440496585366363 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.48563100094897,
            "unit": "iter/sec",
            "range": "stddev: 0.000766327360176713",
            "extra": "mean: 28.997584529408268 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 121.08113767573302,
            "unit": "iter/sec",
            "range": "stddev: 0.00027865730597118055",
            "extra": "mean: 8.258924711114762 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.863742803463637,
            "unit": "iter/sec",
            "range": "stddev: 0.00017094922309132525",
            "extra": "mean: 37.22489480769845 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 100.53720389756856,
            "unit": "iter/sec",
            "range": "stddev: 0.00029530724693202764",
            "extra": "mean: 9.946566656248379 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.291800122080424,
            "unit": "iter/sec",
            "range": "stddev: 0.0010435174115473944",
            "extra": "mean: 38.034672230760584 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 94.83657580469908,
            "unit": "iter/sec",
            "range": "stddev: 0.0003261403070864583",
            "extra": "mean: 10.544454937505776 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.25862283054957,
            "unit": "iter/sec",
            "range": "stddev: 0.00034891957950569847",
            "extra": "mean: 38.082728346156415 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 97.57867066868519,
            "unit": "iter/sec",
            "range": "stddev: 0.00030382488756025756",
            "extra": "mean: 10.248141250000842 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.047551918619625,
            "unit": "iter/sec",
            "range": "stddev: 0.00020038216859236146",
            "extra": "mean: 23.23012472092434 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 127.67471111796273,
            "unit": "iter/sec",
            "range": "stddev: 0.0005469503290283874",
            "extra": "mean: 7.832404641793692 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 46.770533026058544,
            "unit": "iter/sec",
            "range": "stddev: 0.00024092260776331715",
            "extra": "mean: 21.380983608693164 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.32568650315,
            "unit": "iter/sec",
            "range": "stddev: 0.00007576734573272276",
            "extra": "mean: 5.940863933332518 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.22056619088519,
            "unit": "iter/sec",
            "range": "stddev: 0.0005657171098666947",
            "extra": "mean: 23.68513949999765 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 154.62205629377013,
            "unit": "iter/sec",
            "range": "stddev: 0.00023172301722610786",
            "extra": "mean: 6.467382622955655 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-none",
            "value": 42.10399307353234,
            "unit": "iter/sec",
            "range": "stddev: 0.00034580259885257634",
            "extra": "mean: 23.750716428571376 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 168.05869913045956,
            "unit": "iter/sec",
            "range": "stddev: 0.00018177231024362015",
            "extra": "mean: 5.950301919353346 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-none",
            "value": 32.52983625738293,
            "unit": "iter/sec",
            "range": "stddev: 0.0014917061068998125",
            "extra": "mean: 30.741009333332908 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 128.12603330811424,
            "unit": "iter/sec",
            "range": "stddev: 0.000301733253478133",
            "extra": "mean: 7.804815104165641 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 31.729182511364083,
            "unit": "iter/sec",
            "range": "stddev: 0.00038346624600859387",
            "extra": "mean: 31.51672753125112 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 114.71337887223594,
            "unit": "iter/sec",
            "range": "stddev: 0.0002984137122681762",
            "extra": "mean: 8.717379000001106 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.549695280461435,
            "unit": "iter/sec",
            "range": "stddev: 0.00020593896147992987",
            "extra": "mean: 28.129636333327806 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 147.43211660440406,
            "unit": "iter/sec",
            "range": "stddev: 0.00024429666998202604",
            "extra": "mean: 6.782782632655551 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 26.946998113251905,
            "unit": "iter/sec",
            "range": "stddev: 0.00017418243853503345",
            "extra": "mean: 37.109884959995725 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-none",
            "value": 112.00548995561333,
            "unit": "iter/sec",
            "range": "stddev: 0.0002554621760297703",
            "extra": "mean: 8.92813379412286 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.542133310262017,
            "unit": "iter/sec",
            "range": "stddev: 0.0002458758566850688",
            "extra": "mean: 37.67594670370255 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 104.05646600792194,
            "unit": "iter/sec",
            "range": "stddev: 0.00025829037688870676",
            "extra": "mean: 9.61016684848656 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.72829026132224,
            "unit": "iter/sec",
            "range": "stddev: 0.00023815190731674848",
            "extra": "mean: 37.413541615382414 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 102.3050908752465,
            "unit": "iter/sec",
            "range": "stddev: 0.00030541426322836185",
            "extra": "mean: 9.774684636363073 msec\nrounds: 33"
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
          "id": "a3aa6b2400b22b450ab0abe416b9c9ad6a8697f5",
          "message": "avoid ZeroDivisionError in statistics (#795)",
          "timestamp": "2025-03-19T17:02:11+01:00",
          "tree_id": "07b522a5984676dafbb8862654ed4f27ad27fd4c",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/a3aa6b2400b22b450ab0abe416b9c9ad6a8697f5"
        },
        "date": 1742400521805,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.38857459330326,
            "unit": "iter/sec",
            "range": "stddev: 0.0004079599953515271",
            "extra": "mean: 26.04941732258134 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.5715160464539,
            "unit": "iter/sec",
            "range": "stddev: 0.0012650813546789352",
            "extra": "mean: 12.567311139531379 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.92120255081188,
            "unit": "iter/sec",
            "range": "stddev: 0.00038534338679887994",
            "extra": "mean: 20.867589851061826 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.38240682300705,
            "unit": "iter/sec",
            "range": "stddev: 0.00045145285339455725",
            "extra": "mean: 7.729026106060798 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.26670632270146,
            "unit": "iter/sec",
            "range": "stddev: 0.0008226234486704315",
            "extra": "mean: 26.13237710000552 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.82421692167011,
            "unit": "iter/sec",
            "range": "stddev: 0.00012304855771898688",
            "extra": "mean: 8.075964660714062 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.039847299335925,
            "unit": "iter/sec",
            "range": "stddev: 0.00036446470284381174",
            "extra": "mean: 26.288223297296394 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.75578979789418,
            "unit": "iter/sec",
            "range": "stddev: 0.0001705837054346104",
            "extra": "mean: 8.868724185183046 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.0674879026882,
            "unit": "iter/sec",
            "range": "stddev: 0.0005227035570768358",
            "extra": "mean: 31.18423254838651 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.01722492637079,
            "unit": "iter/sec",
            "range": "stddev: 0.0004011963046174613",
            "extra": "mean: 12.65546848717874 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.27234368690388,
            "unit": "iter/sec",
            "range": "stddev: 0.00019678445959884293",
            "extra": "mean: 33.03345160000314 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 78.13286591409194,
            "unit": "iter/sec",
            "range": "stddev: 0.00026760578230196867",
            "extra": "mean: 12.79871137837837 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 34.15803275336865,
            "unit": "iter/sec",
            "range": "stddev: 0.0003890396148877472",
            "extra": "mean: 29.275690647066913 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 89.55497892100743,
            "unit": "iter/sec",
            "range": "stddev: 0.0009069173895025327",
            "extra": "mean: 11.166324999998679 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.035270180466544,
            "unit": "iter/sec",
            "range": "stddev: 0.0008242067881051628",
            "extra": "mean: 38.40943431999676 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.70858529478771,
            "unit": "iter/sec",
            "range": "stddev: 0.0003249012262052794",
            "extra": "mean: 13.036350444439096 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.233342854322462,
            "unit": "iter/sec",
            "range": "stddev: 0.0004636608281224503",
            "extra": "mean: 38.119427080000605 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 72.58559729147747,
            "unit": "iter/sec",
            "range": "stddev: 0.0007506299857146131",
            "extra": "mean: 13.776837793100498 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.345613561535096,
            "unit": "iter/sec",
            "range": "stddev: 0.00033507665599209107",
            "extra": "mean: 37.95698276923076 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.83736279802507,
            "unit": "iter/sec",
            "range": "stddev: 0.00023783922151502456",
            "extra": "mean: 13.362309448274543 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.5465172520792,
            "unit": "iter/sec",
            "range": "stddev: 0.000333693757583937",
            "extra": "mean: 22.44844404650568 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 102.30742850268291,
            "unit": "iter/sec",
            "range": "stddev: 0.00019746232313864106",
            "extra": "mean: 9.774461294115861 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.97181305255945,
            "unit": "iter/sec",
            "range": "stddev: 0.0002511006012656514",
            "extra": "mean: 17.249762381821007 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 153.78731989500974,
            "unit": "iter/sec",
            "range": "stddev: 0.0002792870617232594",
            "extra": "mean: 6.502486685395764 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.74672245564096,
            "unit": "iter/sec",
            "range": "stddev: 0.0003428768345433737",
            "extra": "mean: 23.953976292691607 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 112.04438582681023,
            "unit": "iter/sec",
            "range": "stddev: 0.00031689604282118827",
            "extra": "mean: 8.92503441935703 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.58065046425383,
            "unit": "iter/sec",
            "range": "stddev: 0.0002583160950669165",
            "extra": "mean: 24.04964782500656 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 104.95642992761853,
            "unit": "iter/sec",
            "range": "stddev: 0.0002736759949486382",
            "extra": "mean: 9.527763098360277 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.6737511772695,
            "unit": "iter/sec",
            "range": "stddev: 0.0005663071843285387",
            "extra": "mean: 30.605607375001398 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 109.117401134957,
            "unit": "iter/sec",
            "range": "stddev: 0.00027799744413036875",
            "extra": "mean: 9.164441139531855 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.015671071009955,
            "unit": "iter/sec",
            "range": "stddev: 0.001469392278572327",
            "extra": "mean: 32.24176570967991 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 102.8826361749323,
            "unit": "iter/sec",
            "range": "stddev: 0.000372892329585191",
            "extra": "mean: 9.71981315000221 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.31026837475139,
            "unit": "iter/sec",
            "range": "stddev: 0.00042581917316453655",
            "extra": "mean: 27.540418861110854 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 132.3520321880571,
            "unit": "iter/sec",
            "range": "stddev: 0.0004161570163309011",
            "extra": "mean: 7.555607446806063 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.147473246475446,
            "unit": "iter/sec",
            "range": "stddev: 0.000371815375002303",
            "extra": "mean: 43.201259565221235 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 86.73537168200878,
            "unit": "iter/sec",
            "range": "stddev: 0.0003320373298763202",
            "extra": "mean: 11.529321666669315 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 21.64084873410016,
            "unit": "iter/sec",
            "range": "stddev: 0.003916941028534175",
            "extra": "mean: 46.20890854545223 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 86.19011148474121,
            "unit": "iter/sec",
            "range": "stddev: 0.0003839280931480572",
            "extra": "mean: 11.602259038463322 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.780863131012598,
            "unit": "iter/sec",
            "range": "stddev: 0.00046149219539407644",
            "extra": "mean: 43.89649304545691 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 86.15643644338137,
            "unit": "iter/sec",
            "range": "stddev: 0.0012783435197237188",
            "extra": "mean: 11.606793888894892 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.30845789393004,
            "unit": "iter/sec",
            "range": "stddev: 0.00021179225645889121",
            "extra": "mean: 22.070934357136213 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.41078686372343,
            "unit": "iter/sec",
            "range": "stddev: 0.00009265570134991613",
            "extra": "mean: 7.910717311474736 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.59118917602977,
            "unit": "iter/sec",
            "range": "stddev: 0.00029565063665649147",
            "extra": "mean: 20.16487236170889 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.8494054263928,
            "unit": "iter/sec",
            "range": "stddev: 0.0000871712212439964",
            "extra": "mean: 6.718199492536823 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.41206293989529,
            "unit": "iter/sec",
            "range": "stddev: 0.0003850865473511569",
            "extra": "mean: 23.57819758537001 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 128.29069977545575,
            "unit": "iter/sec",
            "range": "stddev: 0.0005772511271793995",
            "extra": "mean: 7.794797298247471 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.020610384198655,
            "unit": "iter/sec",
            "range": "stddev: 0.0002460001671402966",
            "extra": "mean: 24.377989275001255 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 131.36376327679997,
            "unit": "iter/sec",
            "range": "stddev: 0.0006039864050816537",
            "extra": "mean: 7.6124493928578625 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.24144083279673,
            "unit": "iter/sec",
            "range": "stddev: 0.00024641894612523305",
            "extra": "mean: 30.082931875003993 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.70289167712201,
            "unit": "iter/sec",
            "range": "stddev: 0.00029126334796569954",
            "extra": "mean: 8.354017066666428 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.45806680475888,
            "unit": "iter/sec",
            "range": "stddev: 0.0003868658870344609",
            "extra": "mean: 30.808982125003936 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 113.87165587478286,
            "unit": "iter/sec",
            "range": "stddev: 0.000850814727153577",
            "extra": "mean: 8.781816619050785 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.990022426430016,
            "unit": "iter/sec",
            "range": "stddev: 0.00027251616637404116",
            "extra": "mean: 27.785478657152193 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 132.70048357320923,
            "unit": "iter/sec",
            "range": "stddev: 0.00023209740660233037",
            "extra": "mean: 7.535767565220003 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.407255732117324,
            "unit": "iter/sec",
            "range": "stddev: 0.0002906521097151374",
            "extra": "mean: 36.48668840741123 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 108.11423865478697,
            "unit": "iter/sec",
            "range": "stddev: 0.00039974036274239666",
            "extra": "mean: 9.249475484843762 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.51854454824388,
            "unit": "iter/sec",
            "range": "stddev: 0.0001829407533257263",
            "extra": "mean: 37.709460192309926 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 105.80348585588679,
            "unit": "iter/sec",
            "range": "stddev: 0.0002923268709678242",
            "extra": "mean: 9.451484437498436 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.911778454782556,
            "unit": "iter/sec",
            "range": "stddev: 0.0009032583932648516",
            "extra": "mean: 37.15845096154497 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 101.58308089098519,
            "unit": "iter/sec",
            "range": "stddev: 0.0008813407116129881",
            "extra": "mean: 9.844158999992914 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 45.15516579838006,
            "unit": "iter/sec",
            "range": "stddev: 0.0003514574343004606",
            "extra": "mean: 22.145860441860563 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 139.89335215679748,
            "unit": "iter/sec",
            "range": "stddev: 0.00010468546057724661",
            "extra": "mean: 7.148302507464145 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.508930369573214,
            "unit": "iter/sec",
            "range": "stddev: 0.000299290551346701",
            "extra": "mean: 19.41410921999477 msec\nrounds: 50"
          },
          {
            "name": "dateline-uint8-none",
            "value": 176.76316917754554,
            "unit": "iter/sec",
            "range": "stddev: 0.00007243707058502707",
            "extra": "mean: 5.657287118424392 msec\nrounds: 76"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.11529256350922,
            "unit": "iter/sec",
            "range": "stddev: 0.0005727998372447177",
            "extra": "mean: 22.66787641859976 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 170.60235503806157,
            "unit": "iter/sec",
            "range": "stddev: 0.0001838887871982653",
            "extra": "mean: 5.861583796876069 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.22003760312878,
            "unit": "iter/sec",
            "range": "stddev: 0.00034894992093951387",
            "extra": "mean: 22.61418248837593 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 167.27660391611263,
            "unit": "iter/sec",
            "range": "stddev: 0.00037996555020383975",
            "extra": "mean: 5.978122323080453 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.40827802935305,
            "unit": "iter/sec",
            "range": "stddev: 0.000973290718432373",
            "extra": "mean: 29.062773764700427 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 132.60177816336292,
            "unit": "iter/sec",
            "range": "stddev: 0.0006869457007242252",
            "extra": "mean: 7.541376999997833 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.2257946592109,
            "unit": "iter/sec",
            "range": "stddev: 0.00029334658971346794",
            "extra": "mean: 30.097098060611135 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 122.9857739336804,
            "unit": "iter/sec",
            "range": "stddev: 0.00030932133892004176",
            "extra": "mean: 8.131021727271042 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 36.76208091509681,
            "unit": "iter/sec",
            "range": "stddev: 0.0004326453963444277",
            "extra": "mean: 27.20194219444573 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 159.46826086614246,
            "unit": "iter/sec",
            "range": "stddev: 0.00018930045280177987",
            "extra": "mean: 6.27084032000198 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.60174608032476,
            "unit": "iter/sec",
            "range": "stddev: 0.00028931096317179653",
            "extra": "mean: 36.229592037035154 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 119.46922913632065,
            "unit": "iter/sec",
            "range": "stddev: 0.0002370411084786256",
            "extra": "mean: 8.370356176475765 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.899413570269783,
            "unit": "iter/sec",
            "range": "stddev: 0.0004199041515565132",
            "extra": "mean: 37.17553162962767 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 115.65704726029907,
            "unit": "iter/sec",
            "range": "stddev: 0.00014862645654162488",
            "extra": "mean: 8.646252205880621 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.141109147189532,
            "unit": "iter/sec",
            "range": "stddev: 0.00036269800856765847",
            "extra": "mean: 36.844478041662875 msec\nrounds: 24"
          },
          {
            "name": "dateline-uint64-none",
            "value": 112.02215457682196,
            "unit": "iter/sec",
            "range": "stddev: 0.0003633896342209924",
            "extra": "mean: 8.926805628561851 msec\nrounds: 35"
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
          "id": "ce62e555562fd7a38bde4671ab680dfb2b5bdd15",
          "message": "Bump version: 7.5.0 → 7.5.1",
          "timestamp": "2025-03-19T17:04:45+01:00",
          "tree_id": "60291dfefbbcae4e60f1e18d974afb1dd21e0e1f",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ce62e555562fd7a38bde4671ab680dfb2b5bdd15"
        },
        "date": 1742400692773,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.585728583595575,
            "unit": "iter/sec",
            "range": "stddev: 0.0008958075756799823",
            "extra": "mean: 26.605843166665483 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.11717806869875,
            "unit": "iter/sec",
            "range": "stddev: 0.00015207144047686412",
            "extra": "mean: 12.327845023813481 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.66954485866618,
            "unit": "iter/sec",
            "range": "stddev: 0.00029221097577366553",
            "extra": "mean: 21.427249891302672 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.27408071012252,
            "unit": "iter/sec",
            "range": "stddev: 0.00010158217205503744",
            "extra": "mean: 7.795807184616112 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.189950443575725,
            "unit": "iter/sec",
            "range": "stddev: 0.00031337617810947257",
            "extra": "mean: 26.88898447222164 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 117.67361832551667,
            "unit": "iter/sec",
            "range": "stddev: 0.00016424805148173064",
            "extra": "mean: 8.498081509091806 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.73358628596949,
            "unit": "iter/sec",
            "range": "stddev: 0.00028587926238472566",
            "extra": "mean: 27.22304302702819 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.98665352478558,
            "unit": "iter/sec",
            "range": "stddev: 0.00029135624555574126",
            "extra": "mean: 8.850602870370283 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.550552471138662,
            "unit": "iter/sec",
            "range": "stddev: 0.0005338093240012253",
            "extra": "mean: 31.69516606451709 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.42224042752343,
            "unit": "iter/sec",
            "range": "stddev: 0.0003920954188198278",
            "extra": "mean: 12.590931641025001 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.69359400936624,
            "unit": "iter/sec",
            "range": "stddev: 0.0003329368986801419",
            "extra": "mean: 32.580088199995316 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.83790957068827,
            "unit": "iter/sec",
            "range": "stddev: 0.00022314692726974232",
            "extra": "mean: 12.219275947368141 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.04792616861998,
            "unit": "iter/sec",
            "range": "stddev: 0.0007094685652109295",
            "extra": "mean: 30.25908478788393 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 86.87269563112703,
            "unit": "iter/sec",
            "range": "stddev: 0.00012039731642657672",
            "extra": "mean: 11.511096700004941 msec\nrounds: 40"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.667190532053592,
            "unit": "iter/sec",
            "range": "stddev: 0.00021291624284169476",
            "extra": "mean: 38.96024376922688 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 71.55750218501147,
            "unit": "iter/sec",
            "range": "stddev: 0.00016166196930836397",
            "extra": "mean: 13.974775103447664 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.7603123208276,
            "unit": "iter/sec",
            "range": "stddev: 0.0003307819724552687",
            "extra": "mean: 38.81940512000256 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 69.62314702283479,
            "unit": "iter/sec",
            "range": "stddev: 0.00018524847162293003",
            "extra": "mean: 14.363039344832016 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.874722356758294,
            "unit": "iter/sec",
            "range": "stddev: 0.00010755169230523286",
            "extra": "mean: 38.64775769231808 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 70.13253920535448,
            "unit": "iter/sec",
            "range": "stddev: 0.00021526686211967235",
            "extra": "mean: 14.258716586204143 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.02775205943857,
            "unit": "iter/sec",
            "range": "stddev: 0.0007205698702249695",
            "extra": "mean: 23.793801738092736 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 96.12664584218045,
            "unit": "iter/sec",
            "range": "stddev: 0.0002065973080285232",
            "extra": "mean: 10.402942818183709 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 54.759857695789535,
            "unit": "iter/sec",
            "range": "stddev: 0.0001368474818285076",
            "extra": "mean: 18.261552204086346 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 152.43746802364905,
            "unit": "iter/sec",
            "range": "stddev: 0.00011472419474681107",
            "extra": "mean: 6.560066976741314 msec\nrounds: 86"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.5302147719449,
            "unit": "iter/sec",
            "range": "stddev: 0.00020973295782325137",
            "extra": "mean: 25.297105157893373 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 105.02768821307178,
            "unit": "iter/sec",
            "range": "stddev: 0.00026495606316694666",
            "extra": "mean: 9.521298783338732 msec\nrounds: 60"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.33515669737704,
            "unit": "iter/sec",
            "range": "stddev: 0.00038015769418541873",
            "extra": "mean: 25.422550307691605 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 96.86492473618755,
            "unit": "iter/sec",
            "range": "stddev: 0.00020936467397934705",
            "extra": "mean: 10.323654333325592 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.783059767395233,
            "unit": "iter/sec",
            "range": "stddev: 0.00013844730408147518",
            "extra": "mean: 31.463301750005 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 97.64639907282984,
            "unit": "iter/sec",
            "range": "stddev: 0.0005176905981602242",
            "extra": "mean: 10.24103304878808 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.47788705147384,
            "unit": "iter/sec",
            "range": "stddev: 0.0006944696290681198",
            "extra": "mean: 32.81067346667139 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 86.20821052504728,
            "unit": "iter/sec",
            "range": "stddev: 0.0023341693996440102",
            "extra": "mean: 11.599823194444525 msec\nrounds: 36"
          },
          {
            "name": "equator-float32-alpha",
            "value": 34.834204692016264,
            "unit": "iter/sec",
            "range": "stddev: 0.00016090795187799457",
            "extra": "mean: 28.70741585293585 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 120.0882703525619,
            "unit": "iter/sec",
            "range": "stddev: 0.00023626439430382874",
            "extra": "mean: 8.327207953484079 msec\nrounds: 43"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.77725588584851,
            "unit": "iter/sec",
            "range": "stddev: 0.00023016782731114053",
            "extra": "mean: 43.903444954547794 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 83.6725964802443,
            "unit": "iter/sec",
            "range": "stddev: 0.0002577313069861376",
            "extra": "mean: 11.951344192313993 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.308142827499882,
            "unit": "iter/sec",
            "range": "stddev: 0.00031317820820248287",
            "extra": "mean: 44.82668090000175 msec\nrounds: 20"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 78.84373754037676,
            "unit": "iter/sec",
            "range": "stddev: 0.00021725962175820894",
            "extra": "mean: 12.683315519991538 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.312304342133544,
            "unit": "iter/sec",
            "range": "stddev: 0.0005615765224352257",
            "extra": "mean: 44.818320181822074 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 82.75361139620333,
            "unit": "iter/sec",
            "range": "stddev: 0.0002619470090966127",
            "extra": "mean: 12.08406476923712 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 42.48378524217382,
            "unit": "iter/sec",
            "range": "stddev: 0.00024022409101662767",
            "extra": "mean: 23.538392219516634 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 120.36935471142984,
            "unit": "iter/sec",
            "range": "stddev: 0.00015406926133229985",
            "extra": "mean: 8.307762406780133 msec\nrounds: 59"
          },
          {
            "name": "equator-uint8-mask",
            "value": 46.94494860914049,
            "unit": "iter/sec",
            "range": "stddev: 0.00019439562232079327",
            "extra": "mean: 21.301546377777765 msec\nrounds: 45"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 140.86742475606732,
            "unit": "iter/sec",
            "range": "stddev: 0.00024240396834219745",
            "extra": "mean: 7.098873296872199 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.35289934883075,
            "unit": "iter/sec",
            "range": "stddev: 0.000564382342443308",
            "extra": "mean: 24.781366794873822 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 132.92476848577334,
            "unit": "iter/sec",
            "range": "stddev: 0.0006394148590057099",
            "extra": "mean: 7.523052410710258 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.73083023204124,
            "unit": "iter/sec",
            "range": "stddev: 0.00018576405834295185",
            "extra": "mean: 24.551426875000004 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 135.11916226481634,
            "unit": "iter/sec",
            "range": "stddev: 0.00012666818716282476",
            "extra": "mean: 7.400874777776726 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.93265882583109,
            "unit": "iter/sec",
            "range": "stddev: 0.00030233202712803554",
            "extra": "mean: 30.36499437499529 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 110.11398290169129,
            "unit": "iter/sec",
            "range": "stddev: 0.00027508035587891133",
            "extra": "mean: 9.081498767443463 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.09563638235608,
            "unit": "iter/sec",
            "range": "stddev: 0.00015423365942812583",
            "extra": "mean: 31.15688338710521 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 108.75414847007622,
            "unit": "iter/sec",
            "range": "stddev: 0.00023231347813640037",
            "extra": "mean: 9.195051536587139 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.69067807934151,
            "unit": "iter/sec",
            "range": "stddev: 0.0005427651888523805",
            "extra": "mean: 28.826187764704013 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 127.07312107669412,
            "unit": "iter/sec",
            "range": "stddev: 0.0003682655474152832",
            "extra": "mean: 7.869484840908698 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.93414030448566,
            "unit": "iter/sec",
            "range": "stddev: 0.00031716318414732453",
            "extra": "mean: 37.127600461539814 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 93.56022404959451,
            "unit": "iter/sec",
            "range": "stddev: 0.00018537055524728616",
            "extra": "mean: 10.6883027500011 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.403331188056967,
            "unit": "iter/sec",
            "range": "stddev: 0.00020639959308822552",
            "extra": "mean: 37.87400888461871 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 94.5984237933861,
            "unit": "iter/sec",
            "range": "stddev: 0.0004898054463973759",
            "extra": "mean: 10.571000656248941 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.26790441328432,
            "unit": "iter/sec",
            "range": "stddev: 0.0011654682823046675",
            "extra": "mean: 38.06927207692577 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 100.08943021864631,
            "unit": "iter/sec",
            "range": "stddev: 0.00021856070766183505",
            "extra": "mean: 9.99106496875335 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 43.14800655095748,
            "unit": "iter/sec",
            "range": "stddev: 0.0007541116464955328",
            "extra": "mean: 23.17604172093112 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 133.49518768086523,
            "unit": "iter/sec",
            "range": "stddev: 0.00022709859245185782",
            "extra": "mean: 7.490906731339325 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 47.40375795308528,
            "unit": "iter/sec",
            "range": "stddev: 0.00017804417746117795",
            "extra": "mean: 21.095373936169437 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 172.1457016981592,
            "unit": "iter/sec",
            "range": "stddev: 0.00007116634040378555",
            "extra": "mean: 5.809032639998198 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 41.242229346613136,
            "unit": "iter/sec",
            "range": "stddev: 0.002495377804689868",
            "extra": "mean: 24.2469918780499 msec\nrounds: 41"
          },
          {
            "name": "dateline-uint16-none",
            "value": 163.55732763784542,
            "unit": "iter/sec",
            "range": "stddev: 0.00011137544700333404",
            "extra": "mean: 6.114064190472936 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 42.02014576050817,
            "unit": "iter/sec",
            "range": "stddev: 0.00023394909046169012",
            "extra": "mean: 23.79810878571085 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 162.40473715128692,
            "unit": "iter/sec",
            "range": "stddev: 0.00020246583166313434",
            "extra": "mean: 6.15745585714324 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.20757410344835,
            "unit": "iter/sec",
            "range": "stddev: 0.0002260881617891781",
            "extra": "mean: 30.113611939396613 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 124.08539721390626,
            "unit": "iter/sec",
            "range": "stddev: 0.00025970718716363417",
            "extra": "mean: 8.058966022215627 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-none",
            "value": 31.99665548560236,
            "unit": "iter/sec",
            "range": "stddev: 0.000422550388879087",
            "extra": "mean: 31.253266468739938 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 117.09098528133461,
            "unit": "iter/sec",
            "range": "stddev: 0.00024421634691263215",
            "extra": "mean: 8.540367113636453 msec\nrounds: 44"
          },
          {
            "name": "equator-float32-none",
            "value": 35.6614906604262,
            "unit": "iter/sec",
            "range": "stddev: 0.0004604372007930088",
            "extra": "mean: 28.041452600008856 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 145.49165376224576,
            "unit": "iter/sec",
            "range": "stddev: 0.000300849213850685",
            "extra": "mean: 6.8732464999961 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 27.002337565359653,
            "unit": "iter/sec",
            "range": "stddev: 0.0003366183534690431",
            "extra": "mean: 37.03383077777921 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 110.9039740191774,
            "unit": "iter/sec",
            "range": "stddev: 0.00019144345408416728",
            "extra": "mean: 9.01680944117549 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.584851717338662,
            "unit": "iter/sec",
            "range": "stddev: 0.0002233030357018026",
            "extra": "mean: 37.615406346156114 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 106.49008158642307,
            "unit": "iter/sec",
            "range": "stddev: 0.0001828417285195125",
            "extra": "mean: 9.390545909089573 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.70066884107119,
            "unit": "iter/sec",
            "range": "stddev: 0.00019746651157507842",
            "extra": "mean: 37.45224533333755 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 105.80636405525995,
            "unit": "iter/sec",
            "range": "stddev: 0.0002730335877296291",
            "extra": "mean: 9.451227333336261 msec\nrounds: 33"
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
          "id": "5333bac9d844557daf5e054b192faa8121586114",
          "message": "add interpolate=True/False to point methods (#794)\n\n* add interpolate=True/False to point methods\n\n* add buffer and warnings\n\n* update changelog\n\n* remove buffer\n\n* add pixel_location to PointData model\n\n* update changelog",
          "timestamp": "2025-03-31T09:07:00+02:00",
          "tree_id": "dace1bd907330d3cef2ef1b1cf111a390fd88f78",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/5333bac9d844557daf5e054b192faa8121586114"
        },
        "date": 1743405195896,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.67272181628989,
            "unit": "iter/sec",
            "range": "stddev: 0.00006609909373513454",
            "extra": "mean: 25.858019633331725 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.22294591162353,
            "unit": "iter/sec",
            "range": "stddev: 0.00007344606989101016",
            "extra": "mean: 12.162055116279092 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.92019963329213,
            "unit": "iter/sec",
            "range": "stddev: 0.00013946397091295771",
            "extra": "mean: 20.868026586960607 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.10556721698063,
            "unit": "iter/sec",
            "range": "stddev: 0.00020497987927492697",
            "extra": "mean: 7.745599369230568 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.73836892324289,
            "unit": "iter/sec",
            "range": "stddev: 0.0000913083301587177",
            "extra": "mean: 25.814199921050456 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.87265282765516,
            "unit": "iter/sec",
            "range": "stddev: 0.0004687900162388435",
            "extra": "mean: 8.138507446426095 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.16130687879684,
            "unit": "iter/sec",
            "range": "stddev: 0.00019194430578256742",
            "extra": "mean: 26.204553297298613 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.54765847718073,
            "unit": "iter/sec",
            "range": "stddev: 0.0000428199965248801",
            "extra": "mean: 8.729990759254255 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.272721471884935,
            "unit": "iter/sec",
            "range": "stddev: 0.0002749101384257519",
            "extra": "mean: 30.985921062503863 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.30237075164435,
            "unit": "iter/sec",
            "range": "stddev: 0.0001322042927504737",
            "extra": "mean: 12.150318282052899 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.97574664087241,
            "unit": "iter/sec",
            "range": "stddev: 0.00040347949866909245",
            "extra": "mean: 32.283321903224206 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 83.36043754090878,
            "unit": "iter/sec",
            "range": "stddev: 0.00014201962215886006",
            "extra": "mean: 11.99609826315096 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 34.2726773865373,
            "unit": "iter/sec",
            "range": "stddev: 0.00013137305469235075",
            "extra": "mean: 29.177761303025928 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 94.75877191254524,
            "unit": "iter/sec",
            "range": "stddev: 0.00012150756808522205",
            "extra": "mean: 10.553112707316636 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.62548387016594,
            "unit": "iter/sec",
            "range": "stddev: 0.0005409089669196527",
            "extra": "mean: 37.55800288461641 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 78.06020169806611,
            "unit": "iter/sec",
            "range": "stddev: 0.00016980304544800086",
            "extra": "mean: 12.810625366662029 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.412069459990743,
            "unit": "iter/sec",
            "range": "stddev: 0.001330249502684533",
            "extra": "mean: 37.861478500002036 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.92096457523091,
            "unit": "iter/sec",
            "range": "stddev: 0.00014117608044048497",
            "extra": "mean: 13.17159240000289 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.94343323293242,
            "unit": "iter/sec",
            "range": "stddev: 0.00016599701076528247",
            "extra": "mean: 37.11479496153148 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.85954265729625,
            "unit": "iter/sec",
            "range": "stddev: 0.00021794695314465113",
            "extra": "mean: 13.010746166664452 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.88597968447708,
            "unit": "iter/sec",
            "range": "stddev: 0.00010731201684244246",
            "extra": "mean: 22.278671581403177 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 101.85167717256022,
            "unit": "iter/sec",
            "range": "stddev: 0.00007572886173461124",
            "extra": "mean: 9.818198656716959 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.226027173395025,
            "unit": "iter/sec",
            "range": "stddev: 0.0011568190266348368",
            "extra": "mean: 17.474566196426622 msec\nrounds: 56"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.7081973264267,
            "unit": "iter/sec",
            "range": "stddev: 0.00024169790628447404",
            "extra": "mean: 6.3812871123581205 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.823753732856694,
            "unit": "iter/sec",
            "range": "stddev: 0.00008316432592414502",
            "extra": "mean: 23.90985769444222 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.19939111812029,
            "unit": "iter/sec",
            "range": "stddev: 0.00008575811849231137",
            "extra": "mean: 8.833969777774945 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.42984783039129,
            "unit": "iter/sec",
            "range": "stddev: 0.000528883972738044",
            "extra": "mean: 24.13718737500261 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.26035431102592,
            "unit": "iter/sec",
            "range": "stddev: 0.00010983875591740349",
            "extra": "mean: 9.410847596771442 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 33.154638305718244,
            "unit": "iter/sec",
            "range": "stddev: 0.00020876599209804418",
            "extra": "mean: 30.16169233333268 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 109.56046979166572,
            "unit": "iter/sec",
            "range": "stddev: 0.00024549149717445533",
            "extra": "mean: 9.127379627903624 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.759534117628792,
            "unit": "iter/sec",
            "range": "stddev: 0.0002232612628932132",
            "extra": "mean: 31.486607967745 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.40860962777019,
            "unit": "iter/sec",
            "range": "stddev: 0.0004274986192416228",
            "extra": "mean: 9.224359609754075 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.73973835608759,
            "unit": "iter/sec",
            "range": "stddev: 0.0005976330534968542",
            "extra": "mean: 27.218484527783932 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 137.66603994594576,
            "unit": "iter/sec",
            "range": "stddev: 0.00019021162381132123",
            "extra": "mean: 7.263955586959919 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.428110269646975,
            "unit": "iter/sec",
            "range": "stddev: 0.00021769907115242682",
            "extra": "mean: 42.68376700000346 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 97.70287266027884,
            "unit": "iter/sec",
            "range": "stddev: 0.00017018768465535956",
            "extra": "mean: 10.23511359258683 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.651738334631922,
            "unit": "iter/sec",
            "range": "stddev: 0.0002826985458229395",
            "extra": "mean: 44.14672221739001 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 91.55160127988916,
            "unit": "iter/sec",
            "range": "stddev: 0.00041281258488818756",
            "extra": "mean: 10.922801851852117 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.982570822672283,
            "unit": "iter/sec",
            "range": "stddev: 0.0001817986893273253",
            "extra": "mean: 43.51123326088051 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 93.52316864697353,
            "unit": "iter/sec",
            "range": "stddev: 0.00020235409781744525",
            "extra": "mean: 10.692537629630031 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.09226061722471,
            "unit": "iter/sec",
            "range": "stddev: 0.00011261320656711758",
            "extra": "mean: 22.176754642857976 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.08301459886981,
            "unit": "iter/sec",
            "range": "stddev: 0.00004766574067888754",
            "extra": "mean: 7.931282442615104 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.724402078302525,
            "unit": "iter/sec",
            "range": "stddev: 0.0001144272656864264",
            "extra": "mean: 20.11085017020958 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 147.45831662820657,
            "unit": "iter/sec",
            "range": "stddev: 0.00019350049792065828",
            "extra": "mean: 6.781577484851844 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.38800637549102,
            "unit": "iter/sec",
            "range": "stddev: 0.0009999857797547299",
            "extra": "mean: 23.591578974995286 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 143.3355503224302,
            "unit": "iter/sec",
            "range": "stddev: 0.00003665984391843618",
            "extra": "mean: 6.9766362758612335 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.79842642725131,
            "unit": "iter/sec",
            "range": "stddev: 0.00012067305370587796",
            "extra": "mean: 23.365345025004558 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 142.9424795174483,
            "unit": "iter/sec",
            "range": "stddev: 0.00006044224127911303",
            "extra": "mean: 6.995820999998358 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.44873529308262,
            "unit": "iter/sec",
            "range": "stddev: 0.0002235117996824895",
            "extra": "mean: 29.02864187878625 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 120.68353966130044,
            "unit": "iter/sec",
            "range": "stddev: 0.0003133552961572556",
            "extra": "mean: 8.286134155548552 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.392274558909676,
            "unit": "iter/sec",
            "range": "stddev: 0.00014551073378141536",
            "extra": "mean: 29.947046531251686 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.39717179889368,
            "unit": "iter/sec",
            "range": "stddev: 0.00013831529479707753",
            "extra": "mean: 8.446147697671137 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.51473821664349,
            "unit": "iter/sec",
            "range": "stddev: 0.00019701744077274864",
            "extra": "mean: 27.386202088235102 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.49744042577203,
            "unit": "iter/sec",
            "range": "stddev: 0.00004985530919069824",
            "extra": "mean: 7.220350043479336 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.831517173253673,
            "unit": "iter/sec",
            "range": "stddev: 0.00035866162372385655",
            "extra": "mean: 35.93048822221623 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 111.17448310971405,
            "unit": "iter/sec",
            "range": "stddev: 0.0002995106311387269",
            "extra": "mean: 8.994869794115763 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 27.269136505885616,
            "unit": "iter/sec",
            "range": "stddev: 0.00025109786983025056",
            "extra": "mean: 36.671494888888965 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-mask",
            "value": 106.52228253439573,
            "unit": "iter/sec",
            "range": "stddev: 0.00014254938346147024",
            "extra": "mean: 9.387707212123463 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.38282473230524,
            "unit": "iter/sec",
            "range": "stddev: 0.001240395515730337",
            "extra": "mean: 36.51924188888508 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 107.17180640511756,
            "unit": "iter/sec",
            "range": "stddev: 0.0006307183153870132",
            "extra": "mean: 9.330812212121574 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.4491619388538,
            "unit": "iter/sec",
            "range": "stddev: 0.0006539983487823539",
            "extra": "mean: 22.00260593023422 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 139.58327921065546,
            "unit": "iter/sec",
            "range": "stddev: 0.00003614862277886283",
            "extra": "mean: 7.164181882350149 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.80481588512879,
            "unit": "iter/sec",
            "range": "stddev: 0.0009043860358054027",
            "extra": "mean: 19.683173387755797 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 168.47495567731255,
            "unit": "iter/sec",
            "range": "stddev: 0.00006932122003387047",
            "extra": "mean: 5.935600315072014 msec\nrounds: 73"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.66261192000052,
            "unit": "iter/sec",
            "range": "stddev: 0.00010204222812613388",
            "extra": "mean: 22.3900922272794 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint16-none",
            "value": 173.54470003975953,
            "unit": "iter/sec",
            "range": "stddev: 0.00003848795883965734",
            "extra": "mean: 5.762204203129784 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.5962401818374,
            "unit": "iter/sec",
            "range": "stddev: 0.00017429298156405908",
            "extra": "mean: 22.42341497674657 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 173.60209669236335,
            "unit": "iter/sec",
            "range": "stddev: 0.00003423506494040524",
            "extra": "mean: 5.760299092309231 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.776924491844305,
            "unit": "iter/sec",
            "range": "stddev: 0.00026505012272543443",
            "extra": "mean: 28.75469911764379 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 135.5430108428622,
            "unit": "iter/sec",
            "range": "stddev: 0.00011598993957591069",
            "extra": "mean: 7.377731937497837 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.519662024283846,
            "unit": "iter/sec",
            "range": "stddev: 0.00017471145187096637",
            "extra": "mean: 29.83323636364634 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 132.25665262539903,
            "unit": "iter/sec",
            "range": "stddev: 0.00006832508383267989",
            "extra": "mean: 7.561056326084247 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 37.48801476927617,
            "unit": "iter/sec",
            "range": "stddev: 0.00017544277811774636",
            "extra": "mean: 26.675192222223625 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 163.73435733934025,
            "unit": "iter/sec",
            "range": "stddev: 0.000056269045165787234",
            "extra": "mean: 6.107453660000601 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 28.071852207620577,
            "unit": "iter/sec",
            "range": "stddev: 0.00017716120652322442",
            "extra": "mean: 35.62287207142439 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 124.79121582793591,
            "unit": "iter/sec",
            "range": "stddev: 0.00010802469491408391",
            "extra": "mean: 8.013384542857693 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.38968846339125,
            "unit": "iter/sec",
            "range": "stddev: 0.00021421302023928607",
            "extra": "mean: 36.51009033332339 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 115.03521689776117,
            "unit": "iter/sec",
            "range": "stddev: 0.0008531876995679785",
            "extra": "mean: 8.692990085712283 msec\nrounds: 35"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.50196111901708,
            "unit": "iter/sec",
            "range": "stddev: 0.0009950954888183752",
            "extra": "mean: 36.36104333332502 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.74285084510124,
            "unit": "iter/sec",
            "range": "stddev: 0.000694083464790707",
            "extra": "mean: 8.493084657136155 msec\nrounds: 35"
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
          "id": "661ce7d8c02117f4ce8404f7c1fb97cad94f89f0",
          "message": "add out-dtype to reader methods (#797)",
          "timestamp": "2025-03-31T21:16:08+02:00",
          "tree_id": "a8fa81f96bd14fd67eb2b405d5835c11b3170224",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/661ce7d8c02117f4ce8404f7c1fb97cad94f89f0"
        },
        "date": 1743448935019,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.25808415346719,
            "unit": "iter/sec",
            "range": "stddev: 0.00025654639952529075",
            "extra": "mean: 26.13826651613379 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.43983329437806,
            "unit": "iter/sec",
            "range": "stddev: 0.00034919828978223786",
            "extra": "mean: 12.279003523807948 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.31804421627621,
            "unit": "iter/sec",
            "range": "stddev: 0.00028299848930944145",
            "extra": "mean: 21.13358691304543 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.0698165078076,
            "unit": "iter/sec",
            "range": "stddev: 0.00021486323956592843",
            "extra": "mean: 7.808241061538778 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.12642120936654,
            "unit": "iter/sec",
            "range": "stddev: 0.00035622459989192437",
            "extra": "mean: 26.22853045945811 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.07764324717604,
            "unit": "iter/sec",
            "range": "stddev: 0.0003694503233688308",
            "extra": "mean: 8.191508071426767 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.232732090552666,
            "unit": "iter/sec",
            "range": "stddev: 0.000806296531839606",
            "extra": "mean: 26.858088135136803 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.88190110713244,
            "unit": "iter/sec",
            "range": "stddev: 0.00010440191435107756",
            "extra": "mean: 8.858816074074916 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.82092559818425,
            "unit": "iter/sec",
            "range": "stddev: 0.002023999206372472",
            "extra": "mean: 32.44548891999898 msec\nrounds: 25"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.08357944724857,
            "unit": "iter/sec",
            "range": "stddev: 0.00018796817145183477",
            "extra": "mean: 12.332953315789185 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.60178199256443,
            "unit": "iter/sec",
            "range": "stddev: 0.00039621760327690747",
            "extra": "mean: 32.677835566666616 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.77107594663215,
            "unit": "iter/sec",
            "range": "stddev: 0.00017787876024170067",
            "extra": "mean: 12.229263078947982 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.82916040063933,
            "unit": "iter/sec",
            "range": "stddev: 0.00028257306211599333",
            "extra": "mean: 29.560296151514926 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.11675857396703,
            "unit": "iter/sec",
            "range": "stddev: 0.0001509321435006397",
            "extra": "mean: 10.739205437500843 msec\nrounds: 32"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.885490253226205,
            "unit": "iter/sec",
            "range": "stddev: 0.0005049732071444",
            "extra": "mean: 38.631680923074896 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.9738059506739,
            "unit": "iter/sec",
            "range": "stddev: 0.00015940744708070912",
            "extra": "mean: 12.991432444445017 msec\nrounds: 18"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.95290140121418,
            "unit": "iter/sec",
            "range": "stddev: 0.000678718452158915",
            "extra": "mean: 38.531337384621516 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.9727895631815,
            "unit": "iter/sec",
            "range": "stddev: 0.00024078928440687613",
            "extra": "mean: 13.33817250000114 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.21024635608357,
            "unit": "iter/sec",
            "range": "stddev: 0.00054081885949844",
            "extra": "mean: 38.15301796153829 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.00655761745848,
            "unit": "iter/sec",
            "range": "stddev: 0.0006101183011533926",
            "extra": "mean: 13.512316100000513 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.031853957958674,
            "unit": "iter/sec",
            "range": "stddev: 0.000609380239129719",
            "extra": "mean: 22.710831139538058 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 101.29350643599471,
            "unit": "iter/sec",
            "range": "stddev: 0.00008278563334617761",
            "extra": "mean: 9.872301149253623 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 56.973848675089585,
            "unit": "iter/sec",
            "range": "stddev: 0.0004004200837301365",
            "extra": "mean: 17.551912381815722 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 155.35045411850652,
            "unit": "iter/sec",
            "range": "stddev: 0.00010414310062537923",
            "extra": "mean: 6.437058749999961 msec\nrounds: 88"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.49235041646698,
            "unit": "iter/sec",
            "range": "stddev: 0.0010080526587387703",
            "extra": "mean: 24.696022575002985 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 106.7427694493461,
            "unit": "iter/sec",
            "range": "stddev: 0.0004099546286882189",
            "extra": "mean: 9.368316047622708 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.5025956154237,
            "unit": "iter/sec",
            "range": "stddev: 0.0004075605622780037",
            "extra": "mean: 24.68977567499877 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 104.40200341783594,
            "unit": "iter/sec",
            "range": "stddev: 0.00017225307062241339",
            "extra": "mean: 9.578360254235898 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.17628993486678,
            "unit": "iter/sec",
            "range": "stddev: 0.0005990157041922729",
            "extra": "mean: 31.078785093752614 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 106.87461554302149,
            "unit": "iter/sec",
            "range": "stddev: 0.00030605162245132096",
            "extra": "mean: 9.3567588048769 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.308220666157094,
            "unit": "iter/sec",
            "range": "stddev: 0.00031070207514126435",
            "extra": "mean: 31.940492903225223 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 106.53050939846221,
            "unit": "iter/sec",
            "range": "stddev: 0.0001946730470357177",
            "extra": "mean: 9.386982242426367 msec\nrounds: 33"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.79311995140618,
            "unit": "iter/sec",
            "range": "stddev: 0.0005077849011327767",
            "extra": "mean: 27.938330085715638 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 131.62040290098986,
            "unit": "iter/sec",
            "range": "stddev: 0.0003640662198058109",
            "extra": "mean: 7.597606282608329 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.251941364991204,
            "unit": "iter/sec",
            "range": "stddev: 0.00025874528260432677",
            "extra": "mean: 43.00716160869169 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 90.36862931447645,
            "unit": "iter/sec",
            "range": "stddev: 0.0004919846700132761",
            "extra": "mean: 11.065786961535853 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.539000182574455,
            "unit": "iter/sec",
            "range": "stddev: 0.00047716158573473094",
            "extra": "mean: 44.36754034782468 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 85.72038165799012,
            "unit": "iter/sec",
            "range": "stddev: 0.0005091237743525107",
            "extra": "mean: 11.665837000001138 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.81318619459904,
            "unit": "iter/sec",
            "range": "stddev: 0.00031332030631898994",
            "extra": "mean: 43.8342979130529 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.34603696037664,
            "unit": "iter/sec",
            "range": "stddev: 0.0003921565204613154",
            "extra": "mean: 11.448716333331033 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.85515792120117,
            "unit": "iter/sec",
            "range": "stddev: 0.00019873315444881125",
            "extra": "mean: 22.29398014285759 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.78517652024982,
            "unit": "iter/sec",
            "range": "stddev: 0.0006892768735864828",
            "extra": "mean: 8.078511725807585 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.187632598817544,
            "unit": "iter/sec",
            "range": "stddev: 0.00029075593708513666",
            "extra": "mean: 20.33031368181846 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.1879704121774,
            "unit": "iter/sec",
            "range": "stddev: 0.0005789865884868198",
            "extra": "mean: 6.887622970147439 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.86648037534759,
            "unit": "iter/sec",
            "range": "stddev: 0.000341121848496844",
            "extra": "mean: 23.885456599997212 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.43812672573213,
            "unit": "iter/sec",
            "range": "stddev: 0.0001085899956328508",
            "extra": "mean: 7.020592189656655 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.86075339571165,
            "unit": "iter/sec",
            "range": "stddev: 0.0010319193349255628",
            "extra": "mean: 23.88872437499998 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.24006980491674,
            "unit": "iter/sec",
            "range": "stddev: 0.00016658902579023667",
            "extra": "mean: 7.0801437678501395 msec\nrounds: 56"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.050904905891095,
            "unit": "iter/sec",
            "range": "stddev: 0.00036932667469461507",
            "extra": "mean: 29.36779515151715 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 117.34420816868214,
            "unit": "iter/sec",
            "range": "stddev: 0.0003703837905917917",
            "extra": "mean: 8.521937431820252 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.39378041440799,
            "unit": "iter/sec",
            "range": "stddev: 0.0022355209434059453",
            "extra": "mean: 30.87012343749862 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 117.88462606381977,
            "unit": "iter/sec",
            "range": "stddev: 0.00015238364102460893",
            "extra": "mean: 8.482870357145853 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.447230332068344,
            "unit": "iter/sec",
            "range": "stddev: 0.0004793127025563118",
            "extra": "mean: 28.21094880000601 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.1453544107916,
            "unit": "iter/sec",
            "range": "stddev: 0.00013525762020400202",
            "extra": "mean: 7.399440434780851 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.963249244763766,
            "unit": "iter/sec",
            "range": "stddev: 0.0014471996479935305",
            "extra": "mean: 37.087518307690566 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 109.20230808015582,
            "unit": "iter/sec",
            "range": "stddev: 0.0002924180229341933",
            "extra": "mean: 9.157315606058326 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.72044209078,
            "unit": "iter/sec",
            "range": "stddev: 0.00021921279193025918",
            "extra": "mean: 37.424530500004494 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 96.94806491864838,
            "unit": "iter/sec",
            "range": "stddev: 0.00046390265019280685",
            "extra": "mean: 10.314801031244158 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.805692728675524,
            "unit": "iter/sec",
            "range": "stddev: 0.0002778850667862111",
            "extra": "mean: 37.305508576924225 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 105.12409289776163,
            "unit": "iter/sec",
            "range": "stddev: 0.00040347858202140853",
            "extra": "mean: 9.512567218749268 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 45.17402405197739,
            "unit": "iter/sec",
            "range": "stddev: 0.00017497326081087345",
            "extra": "mean: 22.13661547727952 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.27047847326875,
            "unit": "iter/sec",
            "range": "stddev: 0.0001364253130920737",
            "extra": "mean: 7.232201776124798 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.109398465588626,
            "unit": "iter/sec",
            "range": "stddev: 0.0002891801292503643",
            "extra": "mean: 19.956336148930724 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.0782913008489,
            "unit": "iter/sec",
            "range": "stddev: 0.00009464412105490373",
            "extra": "mean: 5.879645146664339 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.747167809623136,
            "unit": "iter/sec",
            "range": "stddev: 0.0007408481131756223",
            "extra": "mean: 22.858622627909373 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 169.81665911554163,
            "unit": "iter/sec",
            "range": "stddev: 0.00012065606125540871",
            "extra": "mean: 5.8887037656276675 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 42.96556258600504,
            "unit": "iter/sec",
            "range": "stddev: 0.0022752622938258887",
            "extra": "mean: 23.27445376743944 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.4368143248588,
            "unit": "iter/sec",
            "range": "stddev: 0.00005674572868382354",
            "extra": "mean: 5.833052859376409 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.89959245810783,
            "unit": "iter/sec",
            "range": "stddev: 0.00037135877039339027",
            "extra": "mean: 29.498879705877645 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.70793187541457,
            "unit": "iter/sec",
            "range": "stddev: 0.0002393191002217656",
            "extra": "mean: 7.709628744682378 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.94521622357336,
            "unit": "iter/sec",
            "range": "stddev: 0.00023686827254871203",
            "extra": "mean: 30.35342045454441 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.69553776792333,
            "unit": "iter/sec",
            "range": "stddev: 0.0002235620154094359",
            "extra": "mean: 7.7702771777783 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.51623701731833,
            "unit": "iter/sec",
            "range": "stddev: 0.0005932744624435266",
            "extra": "mean: 27.38507802777532 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 160.62794313303277,
            "unit": "iter/sec",
            "range": "stddev: 0.00012028737208275031",
            "extra": "mean: 6.22556686274564 msec\nrounds: 51"
          },
          {
            "name": "equator-float64-none",
            "value": 27.37917898637671,
            "unit": "iter/sec",
            "range": "stddev: 0.00026374201217586857",
            "extra": "mean: 36.52410470370855 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 119.06871538906073,
            "unit": "iter/sec",
            "range": "stddev: 0.00035634662951552446",
            "extra": "mean: 8.398511705887385 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.481572376118,
            "unit": "iter/sec",
            "range": "stddev: 0.0010079797796644216",
            "extra": "mean: 37.76210814814889 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 111.40642892332984,
            "unit": "iter/sec",
            "range": "stddev: 0.0003632341068092815",
            "extra": "mean: 8.976142666669645 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.751573361894653,
            "unit": "iter/sec",
            "range": "stddev: 0.0002500050904026185",
            "extra": "mean: 37.38097892307206 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 112.23637104905205,
            "unit": "iter/sec",
            "range": "stddev: 0.000435624172134284",
            "extra": "mean: 8.909767757574393 msec\nrounds: 33"
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
          "id": "cdbb4a4c326831b8f47caaafc13f54bff41024e1",
          "message": "update pystac dependency",
          "timestamp": "2025-03-31T21:22:43+02:00",
          "tree_id": "c5369623762d105965e5c530b79685f73b75ede8",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/cdbb4a4c326831b8f47caaafc13f54bff41024e1"
        },
        "date": 1743449343267,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.97073237717873,
            "unit": "iter/sec",
            "range": "stddev: 0.00015051938447687175",
            "extra": "mean: 26.33607353333597 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.63512667918818,
            "unit": "iter/sec",
            "range": "stddev: 0.00013080998558872705",
            "extra": "mean: 12.249628813951936 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.08343971503975,
            "unit": "iter/sec",
            "range": "stddev: 0.00014606710153238498",
            "extra": "mean: 21.238890065216975 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.66944955197008,
            "unit": "iter/sec",
            "range": "stddev: 0.00013464436357169874",
            "extra": "mean: 7.771852630768395 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.75654738456476,
            "unit": "iter/sec",
            "range": "stddev: 0.0002688785753662675",
            "extra": "mean: 26.48547256756876 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 119.43704067497558,
            "unit": "iter/sec",
            "range": "stddev: 0.00021969099273262032",
            "extra": "mean: 8.37261200000177 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.38286090638038,
            "unit": "iter/sec",
            "range": "stddev: 0.00020935638268578012",
            "extra": "mean: 26.750226594597617 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 110.93489510021237,
            "unit": "iter/sec",
            "range": "stddev: 0.0002589690690762249",
            "extra": "mean: 9.014296169808931 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.051704068240188,
            "unit": "iter/sec",
            "range": "stddev: 0.0005667354109620207",
            "extra": "mean: 32.20435174193239 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 78.80494045547894,
            "unit": "iter/sec",
            "range": "stddev: 0.0002528599161262152",
            "extra": "mean: 12.689559743591872 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.230933770531536,
            "unit": "iter/sec",
            "range": "stddev: 0.0006438291499952049",
            "extra": "mean: 33.07870036666808 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 80.76967738140726,
            "unit": "iter/sec",
            "range": "stddev: 0.00017129286890153308",
            "extra": "mean: 12.380883921051721 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.578088312861446,
            "unit": "iter/sec",
            "range": "stddev: 0.0010951067293693743",
            "extra": "mean: 30.69547821212123 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 91.99492805483358,
            "unit": "iter/sec",
            "range": "stddev: 0.00011483611743544919",
            "extra": "mean: 10.870164487806871 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.959786680920548,
            "unit": "iter/sec",
            "range": "stddev: 0.00013245991332826626",
            "extra": "mean: 38.5211177692366 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.15245101767853,
            "unit": "iter/sec",
            "range": "stddev: 0.000470094078920075",
            "extra": "mean: 13.485730900002105 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.011529272200363,
            "unit": "iter/sec",
            "range": "stddev: 0.00019900979830501573",
            "extra": "mean: 38.44449088461488 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 72.6243015031046,
            "unit": "iter/sec",
            "range": "stddev: 0.00018315594023631015",
            "extra": "mean: 13.769495599999004 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.085732115053975,
            "unit": "iter/sec",
            "range": "stddev: 0.0004690670628458571",
            "extra": "mean: 38.335132615384936 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 74.56239312832344,
            "unit": "iter/sec",
            "range": "stddev: 0.00026059319788503783",
            "extra": "mean: 13.411586700000083 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.08850728787984,
            "unit": "iter/sec",
            "range": "stddev: 0.0006783903196369622",
            "extra": "mean: 22.68164792857265 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.66816600252496,
            "unit": "iter/sec",
            "range": "stddev: 0.0000827937656799715",
            "extra": "mean: 9.933626882354426 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.744408513647855,
            "unit": "iter/sec",
            "range": "stddev: 0.00015568393137984325",
            "extra": "mean: 17.317694054544702 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.8464156549527,
            "unit": "iter/sec",
            "range": "stddev: 0.000050230350116703945",
            "extra": "mean: 6.375663707865059 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.33290707777039,
            "unit": "iter/sec",
            "range": "stddev: 0.0001527206542795388",
            "extra": "mean: 24.19379788889368 msec\nrounds: 36"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 110.67755258748603,
            "unit": "iter/sec",
            "range": "stddev: 0.00017164295144594287",
            "extra": "mean: 9.03525580952417 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.38786693993767,
            "unit": "iter/sec",
            "range": "stddev: 0.0002086624077762723",
            "extra": "mean: 24.759911225000764 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.04495903949044,
            "unit": "iter/sec",
            "range": "stddev: 0.00020047183015007398",
            "extra": "mean: 9.799602149999487 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.912632689750737,
            "unit": "iter/sec",
            "range": "stddev: 0.00017252327857039722",
            "extra": "mean: 31.335553218746703 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 100.75011903872628,
            "unit": "iter/sec",
            "range": "stddev: 0.0003121063303039167",
            "extra": "mean: 9.925546585365526 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.056907030430146,
            "unit": "iter/sec",
            "range": "stddev: 0.0003766446524771172",
            "extra": "mean: 32.1989565483833 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 102.10355818829738,
            "unit": "iter/sec",
            "range": "stddev: 0.0006119263481484637",
            "extra": "mean: 9.7939779743603 msec\nrounds: 39"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.45845656835351,
            "unit": "iter/sec",
            "range": "stddev: 0.0005841594313205532",
            "extra": "mean: 28.202017142858235 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 132.65877935936606,
            "unit": "iter/sec",
            "range": "stddev: 0.00018083024653842714",
            "extra": "mean: 7.538136599998779 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.22480095388644,
            "unit": "iter/sec",
            "range": "stddev: 0.0004305336524980969",
            "extra": "mean: 43.05741960869894 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 90.87088750290037,
            "unit": "iter/sec",
            "range": "stddev: 0.00033651287956230035",
            "extra": "mean: 11.004624555560575 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.51275282211142,
            "unit": "iter/sec",
            "range": "stddev: 0.0003563369203499987",
            "extra": "mean: 44.419267954553604 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 79.89857036287604,
            "unit": "iter/sec",
            "range": "stddev: 0.0007937281969511235",
            "extra": "mean: 12.51586850000308 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.76447379150055,
            "unit": "iter/sec",
            "range": "stddev: 0.0003651196151145847",
            "extra": "mean: 43.92809643477746 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 86.22073503690584,
            "unit": "iter/sec",
            "range": "stddev: 0.00031627573992040693",
            "extra": "mean: 11.59813819230329 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.32969564343409,
            "unit": "iter/sec",
            "range": "stddev: 0.000641457736759325",
            "extra": "mean: 22.55824195238109 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.85326847466666,
            "unit": "iter/sec",
            "range": "stddev: 0.00013793603202776254",
            "extra": "mean: 8.07407032786174 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 48.86488206806559,
            "unit": "iter/sec",
            "range": "stddev: 0.00016629537792770606",
            "extra": "mean: 20.464594565214856 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.75867305412282,
            "unit": "iter/sec",
            "range": "stddev: 0.00006630314187654875",
            "extra": "mean: 6.860655212116826 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.42666512287728,
            "unit": "iter/sec",
            "range": "stddev: 0.0002589541623301398",
            "extra": "mean: 24.139041774998304 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 137.74523990333915,
            "unit": "iter/sec",
            "range": "stddev: 0.00013477101055388733",
            "extra": "mean: 7.259778999998377 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.35480956175875,
            "unit": "iter/sec",
            "range": "stddev: 0.0002718906918346495",
            "extra": "mean: 24.180984282048566 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 139.23119543233597,
            "unit": "iter/sec",
            "range": "stddev: 0.0001846985884549883",
            "extra": "mean: 7.1822984561386125 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.571859700958285,
            "unit": "iter/sec",
            "range": "stddev: 0.0003072200816958829",
            "extra": "mean: 29.786851515153202 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 118.61541413233331,
            "unit": "iter/sec",
            "range": "stddev: 0.0001285351139081492",
            "extra": "mean: 8.430607500002907 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.321983454024405,
            "unit": "iter/sec",
            "range": "stddev: 0.00021777756339400552",
            "extra": "mean: 30.9386953750046 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 114.23322264339731,
            "unit": "iter/sec",
            "range": "stddev: 0.0001868016928581986",
            "extra": "mean: 8.754020738097422 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.20799792172004,
            "unit": "iter/sec",
            "range": "stddev: 0.00023430636001453125",
            "extra": "mean: 28.402637441167695 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 126.94971903058148,
            "unit": "iter/sec",
            "range": "stddev: 0.0006722037924989891",
            "extra": "mean: 7.877134409089204 msec\nrounds: 44"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.206937188568112,
            "unit": "iter/sec",
            "range": "stddev: 0.0004195728435705292",
            "extra": "mean: 36.75533166666708 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 106.44751960978631,
            "unit": "iter/sec",
            "range": "stddev: 0.0008006218509225323",
            "extra": "mean: 9.394300625000795 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.568848667902568,
            "unit": "iter/sec",
            "range": "stddev: 0.0003352536285135524",
            "extra": "mean: 37.63806300000064 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 101.3933888234024,
            "unit": "iter/sec",
            "range": "stddev: 0.00024048800525818892",
            "extra": "mean: 9.862575968751841 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.987562401964677,
            "unit": "iter/sec",
            "range": "stddev: 0.00016284144195202274",
            "extra": "mean: 37.054106076923816 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 103.33798483434332,
            "unit": "iter/sec",
            "range": "stddev: 0.00022997076974629456",
            "extra": "mean: 9.676983750003032 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.83201426424402,
            "unit": "iter/sec",
            "range": "stddev: 0.0006221336791279208",
            "extra": "mean: 22.305488977272084 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 135.90614704461444,
            "unit": "iter/sec",
            "range": "stddev: 0.00041893829517900634",
            "extra": "mean: 7.358018910445059 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.513199253533685,
            "unit": "iter/sec",
            "range": "stddev: 0.0003541874357033325",
            "extra": "mean: 19.796805880000647 msec\nrounds: 50"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.32700462747908,
            "unit": "iter/sec",
            "range": "stddev: 0.00018257080836395087",
            "extra": "mean: 5.905732533331047 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.61432676472688,
            "unit": "iter/sec",
            "range": "stddev: 0.00024045481398625554",
            "extra": "mean: 22.928245697667183 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 170.97322713401337,
            "unit": "iter/sec",
            "range": "stddev: 0.00006335886544870147",
            "extra": "mean: 5.84886895312664 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.56741557243808,
            "unit": "iter/sec",
            "range": "stddev: 0.00029297127909283906",
            "extra": "mean: 22.952933674418528 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 169.7293214378906,
            "unit": "iter/sec",
            "range": "stddev: 0.00022256832781845237",
            "extra": "mean: 5.891733918030964 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.924103299893986,
            "unit": "iter/sec",
            "range": "stddev: 0.0003694670807658661",
            "extra": "mean: 29.477566176469136 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 131.48007066980674,
            "unit": "iter/sec",
            "range": "stddev: 0.00020711041250220128",
            "extra": "mean: 7.60571541303287 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 32.806846182767174,
            "unit": "iter/sec",
            "range": "stddev: 0.0007575548306779256",
            "extra": "mean: 30.481442636362935 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 129.03971110227874,
            "unit": "iter/sec",
            "range": "stddev: 0.00020884455744098334",
            "extra": "mean: 7.749552377774509 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.72341847290865,
            "unit": "iter/sec",
            "range": "stddev: 0.00032262609566426856",
            "extra": "mean: 27.23058041935048 msec\nrounds: 31"
          },
          {
            "name": "dateline-float32-none",
            "value": 155.56496155653227,
            "unit": "iter/sec",
            "range": "stddev: 0.0001253229936595639",
            "extra": "mean: 6.428182734687337 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 27.602534325895324,
            "unit": "iter/sec",
            "range": "stddev: 0.0001991938181659551",
            "extra": "mean: 36.228557428578206 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 120.47131453802898,
            "unit": "iter/sec",
            "range": "stddev: 0.00021266663099594573",
            "extra": "mean: 8.300731205886624 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.869785606489504,
            "unit": "iter/sec",
            "range": "stddev: 0.0008674433040635964",
            "extra": "mean: 37.216523222220395 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 112.26574559354006,
            "unit": "iter/sec",
            "range": "stddev: 0.00016496704957685396",
            "extra": "mean: 8.907436500003447 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.062756475500482,
            "unit": "iter/sec",
            "range": "stddev: 0.00020468231922447807",
            "extra": "mean: 36.95115096295846 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 107.93520517576042,
            "unit": "iter/sec",
            "range": "stddev: 0.00019529184343971518",
            "extra": "mean: 9.264817705878373 msec\nrounds: 34"
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
          "id": "d46ba03e4c42fcbfe5ed978e919479ba3f950cf5",
          "message": "Bump version: 7.5.1 → 7.6.0",
          "timestamp": "2025-03-31T21:36:03+02:00",
          "tree_id": "537cb9e7eafacfdd72412629b37a58a835142344",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/d46ba03e4c42fcbfe5ed978e919479ba3f950cf5"
        },
        "date": 1743450136042,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.01861140291494,
            "unit": "iter/sec",
            "range": "stddev: 0.0002069800740562909",
            "extra": "mean: 26.302906999999703 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.54374581214627,
            "unit": "iter/sec",
            "range": "stddev: 0.0000836937877672876",
            "extra": "mean: 12.263356190476179 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.19321876043277,
            "unit": "iter/sec",
            "range": "stddev: 0.0002739254751966537",
            "extra": "mean: 21.189484978261518 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 125.77623590091781,
            "unit": "iter/sec",
            "range": "stddev: 0.00008901064800156089",
            "extra": "mean: 7.95062749999742 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.20619266427278,
            "unit": "iter/sec",
            "range": "stddev: 0.0003777654452768831",
            "extra": "mean: 26.87724618918746 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.53890671145767,
            "unit": "iter/sec",
            "range": "stddev: 0.00011248133860402818",
            "extra": "mean: 8.227817964284258 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.51083682638024,
            "unit": "iter/sec",
            "range": "stddev: 0.0008114979230562414",
            "extra": "mean: 27.389128459456952 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 112.16115728170473,
            "unit": "iter/sec",
            "range": "stddev: 0.00006275596267195642",
            "extra": "mean: 8.915742528301426 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 31.044295366576513,
            "unit": "iter/sec",
            "range": "stddev: 0.00034262147289154",
            "extra": "mean: 32.212037290324155 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.43135876215557,
            "unit": "iter/sec",
            "range": "stddev: 0.0000890993082430098",
            "extra": "mean: 12.589486263156333 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.205983056131643,
            "unit": "iter/sec",
            "range": "stddev: 0.00033186032908204336",
            "extra": "mean: 33.10602400000372 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 79.97695747132985,
            "unit": "iter/sec",
            "range": "stddev: 0.00010177062027692276",
            "extra": "mean: 12.503601432431084 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.37678935410521,
            "unit": "iter/sec",
            "range": "stddev: 0.0018535979175946056",
            "extra": "mean: 30.886323812500116 msec\nrounds: 32"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 90.60500924772819,
            "unit": "iter/sec",
            "range": "stddev: 0.00011835073398917009",
            "extra": "mean: 11.036917365858265 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.77693996353181,
            "unit": "iter/sec",
            "range": "stddev: 0.00021002140461535537",
            "extra": "mean: 38.794364319999204 msec\nrounds: 25"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 74.82914583669688,
            "unit": "iter/sec",
            "range": "stddev: 0.00031941205803449397",
            "extra": "mean: 13.363776758622189 msec\nrounds: 29"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.716269573125413,
            "unit": "iter/sec",
            "range": "stddev: 0.0003458712427803973",
            "extra": "mean: 38.88588883999887 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 74.19638515672267,
            "unit": "iter/sec",
            "range": "stddev: 0.00013676489559537785",
            "extra": "mean: 13.477745551723737 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.93429634198396,
            "unit": "iter/sec",
            "range": "stddev: 0.0005953668493050694",
            "extra": "mean: 38.558979461538016 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 71.87466065426743,
            "unit": "iter/sec",
            "range": "stddev: 0.00048718332411738796",
            "extra": "mean: 13.913109166667443 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.059369200778704,
            "unit": "iter/sec",
            "range": "stddev: 0.00034246523830121494",
            "extra": "mean: 22.696648139536368 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.46011218910475,
            "unit": "iter/sec",
            "range": "stddev: 0.0002640491456500333",
            "extra": "mean: 9.954199514705037 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.64926838125641,
            "unit": "iter/sec",
            "range": "stddev: 0.00020136038902442062",
            "extra": "mean: 17.346273909091472 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.61730855760638,
            "unit": "iter/sec",
            "range": "stddev: 0.00006069517066417998",
            "extra": "mean: 6.384990325843735 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.646766346559126,
            "unit": "iter/sec",
            "range": "stddev: 0.00022959668195343894",
            "extra": "mean: 24.602203074996964 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.89691309715286,
            "unit": "iter/sec",
            "range": "stddev: 0.00014801591603359583",
            "extra": "mean: 8.779869206349874 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.19307234926132,
            "unit": "iter/sec",
            "range": "stddev: 0.00043899829970209323",
            "extra": "mean: 24.87990943589507 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.90354318198526,
            "unit": "iter/sec",
            "range": "stddev: 0.000360085890818457",
            "extra": "mean: 9.717838366668255 msec\nrounds: 60"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.711069131362528,
            "unit": "iter/sec",
            "range": "stddev: 0.0003429201484108854",
            "extra": "mean: 31.534729903224584 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 102.1100435125351,
            "unit": "iter/sec",
            "range": "stddev: 0.000689675067531369",
            "extra": "mean: 9.793355928569744 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.043468679104738,
            "unit": "iter/sec",
            "range": "stddev: 0.0006322217995167593",
            "extra": "mean: 32.21289509677432 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 100.36190603677612,
            "unit": "iter/sec",
            "range": "stddev: 0.0001728440611014587",
            "extra": "mean: 9.96393990000115 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.26269327720379,
            "unit": "iter/sec",
            "range": "stddev: 0.0001965232464196805",
            "extra": "mean: 28.358582599998627 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 128.72281064231112,
            "unit": "iter/sec",
            "range": "stddev: 0.00019526823650027424",
            "extra": "mean: 7.768630866667081 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.029199618240654,
            "unit": "iter/sec",
            "range": "stddev: 0.0008105517665692794",
            "extra": "mean: 43.4231330909101 msec\nrounds: 22"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 88.99504534324059,
            "unit": "iter/sec",
            "range": "stddev: 0.00023276242173224704",
            "extra": "mean: 11.236580600000252 msec\nrounds: 25"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.480491804739795,
            "unit": "iter/sec",
            "range": "stddev: 0.0003821790282638282",
            "extra": "mean: 44.48301259090603 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 83.54655695715431,
            "unit": "iter/sec",
            "range": "stddev: 0.00019909784569559048",
            "extra": "mean: 11.969374160000825 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.781157571055328,
            "unit": "iter/sec",
            "range": "stddev: 0.0001883625658966799",
            "extra": "mean: 43.89592569565267 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 85.35925565234385,
            "unit": "iter/sec",
            "range": "stddev: 0.000955322621237125",
            "extra": "mean: 11.71519119230442 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.07272792157142,
            "unit": "iter/sec",
            "range": "stddev: 0.00022678678001107508",
            "extra": "mean: 22.68976864285611 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 123.49648895845036,
            "unit": "iter/sec",
            "range": "stddev: 0.0005127686453175903",
            "extra": "mean: 8.097396196716524 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.50247263583689,
            "unit": "iter/sec",
            "range": "stddev: 0.00011825181358190295",
            "extra": "mean: 20.201011116282274 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 145.31177771379993,
            "unit": "iter/sec",
            "range": "stddev: 0.00010646398414814267",
            "extra": "mean: 6.8817546363623645 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-mask",
            "value": 40.94312079826177,
            "unit": "iter/sec",
            "range": "stddev: 0.000658037833361323",
            "extra": "mean: 24.42412743589528 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 136.62481943593852,
            "unit": "iter/sec",
            "range": "stddev: 0.0005344405470673688",
            "extra": "mean: 7.319314339287279 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-mask",
            "value": 40.74267860645901,
            "unit": "iter/sec",
            "range": "stddev: 0.0008817311235991958",
            "extra": "mean: 24.544287076929404 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-mask",
            "value": 141.04051696170012,
            "unit": "iter/sec",
            "range": "stddev: 0.00010768678406021585",
            "extra": "mean: 7.090161192982243 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.07850822130305,
            "unit": "iter/sec",
            "range": "stddev: 0.000974284958012474",
            "extra": "mean: 30.23110937499851 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 114.22482281626527,
            "unit": "iter/sec",
            "range": "stddev: 0.00015549761442732154",
            "extra": "mean: 8.754664488370762 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.57426494180972,
            "unit": "iter/sec",
            "range": "stddev: 0.00020428823231597828",
            "extra": "mean: 30.699081062500966 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 114.72575388985533,
            "unit": "iter/sec",
            "range": "stddev: 0.00020707705780596776",
            "extra": "mean: 8.716438690479814 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.33618724871398,
            "unit": "iter/sec",
            "range": "stddev: 0.00036547474945759035",
            "extra": "mean: 28.299601000003015 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 127.11531213844162,
            "unit": "iter/sec",
            "range": "stddev: 0.00015677316085179296",
            "extra": "mean: 7.866872866668474 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 26.87458269185352,
            "unit": "iter/sec",
            "range": "stddev: 0.0012180414957433615",
            "extra": "mean: 37.2098801111107 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 103.04314413631371,
            "unit": "iter/sec",
            "range": "stddev: 0.0002563783786955146",
            "extra": "mean: 9.704672818184973 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.452470917015614,
            "unit": "iter/sec",
            "range": "stddev: 0.0002354867615010365",
            "extra": "mean: 37.80365180769361 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 96.92304174178382,
            "unit": "iter/sec",
            "range": "stddev: 0.0003882040590153817",
            "extra": "mean: 10.317464062509885 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.817246606555248,
            "unit": "iter/sec",
            "range": "stddev: 0.00010996636941493026",
            "extra": "mean: 37.2894359615412 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 95.452004031432,
            "unit": "iter/sec",
            "range": "stddev: 0.0002387544635883821",
            "extra": "mean: 10.476469406244249 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 45.24488565566878,
            "unit": "iter/sec",
            "range": "stddev: 0.0001615677150710819",
            "extra": "mean: 22.10194556817736 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.08905782973684,
            "unit": "iter/sec",
            "range": "stddev: 0.000049751363991824215",
            "extra": "mean: 7.241703402980671 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.79930034724809,
            "unit": "iter/sec",
            "range": "stddev: 0.000645049113198128",
            "extra": "mean: 19.685310489796386 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 165.0553863201112,
            "unit": "iter/sec",
            "range": "stddev: 0.0003249251564659765",
            "extra": "mean: 6.058572351347462 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.3596385841623,
            "unit": "iter/sec",
            "range": "stddev: 0.0008281230148817624",
            "extra": "mean: 23.607378000006985 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 165.47458464512053,
            "unit": "iter/sec",
            "range": "stddev: 0.0003549876473222429",
            "extra": "mean: 6.043224112902995 msec\nrounds: 62"
          },
          {
            "name": "equator-int16-none",
            "value": 42.62369906822773,
            "unit": "iter/sec",
            "range": "stddev: 0.000876416074081986",
            "extra": "mean: 23.46112660000017 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-none",
            "value": 167.04429947198213,
            "unit": "iter/sec",
            "range": "stddev: 0.00011244382635954555",
            "extra": "mean: 5.986435952384757 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.37362760627405,
            "unit": "iter/sec",
            "range": "stddev: 0.0008555493132481523",
            "extra": "mean: 29.963778939392427 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 127.43412722885802,
            "unit": "iter/sec",
            "range": "stddev: 0.0001958927307291027",
            "extra": "mean: 7.847191499998328 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 32.846310514920816,
            "unit": "iter/sec",
            "range": "stddev: 0.0002600800035290917",
            "extra": "mean: 30.444819656251454 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 126.07955478705169,
            "unit": "iter/sec",
            "range": "stddev: 0.00009593082714044611",
            "extra": "mean: 7.931500088884352 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.996618231625,
            "unit": "iter/sec",
            "range": "stddev: 0.0007028543323739179",
            "extra": "mean: 27.029497499995614 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 152.73066326868545,
            "unit": "iter/sec",
            "range": "stddev: 0.00009907146004686113",
            "extra": "mean: 6.547473693876318 msec\nrounds: 49"
          },
          {
            "name": "equator-float64-none",
            "value": 27.31197872433362,
            "unit": "iter/sec",
            "range": "stddev: 0.00020459952964898618",
            "extra": "mean: 36.61397111110992 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 108.99240175829505,
            "unit": "iter/sec",
            "range": "stddev: 0.0002476808913376049",
            "extra": "mean: 9.174951499992002 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.660106448455345,
            "unit": "iter/sec",
            "range": "stddev: 0.00015100470852780754",
            "extra": "mean: 37.5092275769191 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-none",
            "value": 102.07609002302047,
            "unit": "iter/sec",
            "range": "stddev: 0.000229662875730185",
            "extra": "mean: 9.796613484847208 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.843550312691555,
            "unit": "iter/sec",
            "range": "stddev: 0.0002565249262605376",
            "extra": "mean: 37.252896444446954 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 105.44402955340648,
            "unit": "iter/sec",
            "range": "stddev: 0.000149067541239437",
            "extra": "mean: 9.483704333335524 msec\nrounds: 33"
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
          "id": "80123542632e35059cc7926db8a4e10436a9cafa",
          "message": "fix xarray indexes check (#798)",
          "timestamp": "2025-04-22T22:25:47+02:00",
          "tree_id": "1c47b738b53d6c5a5a8db960cb6e016f316e6eb5",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/80123542632e35059cc7926db8a4e10436a9cafa"
        },
        "date": 1745353908229,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.55633945914306,
            "unit": "iter/sec",
            "range": "stddev: 0.00011577644418898258",
            "extra": "mean: 25.936072096773305 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.12252501625454,
            "unit": "iter/sec",
            "range": "stddev: 0.00006945308941253773",
            "extra": "mean: 12.176927095240552 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.79035387404772,
            "unit": "iter/sec",
            "range": "stddev: 0.0008446266207108888",
            "extra": "mean: 20.924724739128674 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.48597512206308,
            "unit": "iter/sec",
            "range": "stddev: 0.00003474456401919748",
            "extra": "mean: 7.7228441076906265 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.65143935981475,
            "unit": "iter/sec",
            "range": "stddev: 0.000266742188591861",
            "extra": "mean: 25.872257710528707 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.48836023853767,
            "unit": "iter/sec",
            "range": "stddev: 0.00003573280123201619",
            "extra": "mean: 8.097929214286584 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.60846884658391,
            "unit": "iter/sec",
            "range": "stddev: 0.001720565807476009",
            "extra": "mean: 26.58975572973461 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.84760268827196,
            "unit": "iter/sec",
            "range": "stddev: 0.00004951141971364114",
            "extra": "mean: 8.783671999999129 msec\nrounds: 49"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.460387131403365,
            "unit": "iter/sec",
            "range": "stddev: 0.0004884016446270203",
            "extra": "mean: 30.8067798437488 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.4555689593843,
            "unit": "iter/sec",
            "range": "stddev: 0.00006623698088903172",
            "extra": "mean: 12.127743615383661 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.904374330304734,
            "unit": "iter/sec",
            "range": "stddev: 0.000938975347907203",
            "extra": "mean: 32.35787883333406 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.85111675900546,
            "unit": "iter/sec",
            "range": "stddev: 0.00011460326418895804",
            "extra": "mean: 12.069843342109271 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 34.195221472704695,
            "unit": "iter/sec",
            "range": "stddev: 0.0003626695983963149",
            "extra": "mean: 29.24385212121582 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.37841773921424,
            "unit": "iter/sec",
            "range": "stddev: 0.0000865265081363023",
            "extra": "mean: 10.709112707315132 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.351910741876935,
            "unit": "iter/sec",
            "range": "stddev: 0.00035672539475611285",
            "extra": "mean: 37.94791238461725 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.44149160589545,
            "unit": "iter/sec",
            "range": "stddev: 0.0008244919806861203",
            "extra": "mean: 13.081900666664598 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.52576122451042,
            "unit": "iter/sec",
            "range": "stddev: 0.00024155318596930876",
            "extra": "mean: 37.69920084615618 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 73.776624575909,
            "unit": "iter/sec",
            "range": "stddev: 0.0002006122150325875",
            "extra": "mean: 13.554428733332696 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.499459777427564,
            "unit": "iter/sec",
            "range": "stddev: 0.0005995290763645827",
            "extra": "mean: 37.736618346152376 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.47805055858778,
            "unit": "iter/sec",
            "range": "stddev: 0.00010953297216594423",
            "extra": "mean: 13.075647099999326 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.72107635759618,
            "unit": "iter/sec",
            "range": "stddev: 0.00019065549044932546",
            "extra": "mean: 22.36082137209435 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 101.13481702668463,
            "unit": "iter/sec",
            "range": "stddev: 0.00027655229993502186",
            "extra": "mean: 9.887791656716479 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.82878268934981,
            "unit": "iter/sec",
            "range": "stddev: 0.00015714068852716145",
            "extra": "mean: 17.292426945451986 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 154.38492959043887,
            "unit": "iter/sec",
            "range": "stddev: 0.000484484968769974",
            "extra": "mean: 6.477316164556067 msec\nrounds: 79"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.78820256088238,
            "unit": "iter/sec",
            "range": "stddev: 0.00010271016243118405",
            "extra": "mean: 23.93019892499737 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 116.51752529630461,
            "unit": "iter/sec",
            "range": "stddev: 0.00035533146053475835",
            "extra": "mean: 8.582399921874373 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.687551608928764,
            "unit": "iter/sec",
            "range": "stddev: 0.00009199775606091499",
            "extra": "mean: 23.987976299999758 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 109.09363262724871,
            "unit": "iter/sec",
            "range": "stddev: 0.00027929122817211443",
            "extra": "mean: 9.166437819673687 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 33.10828261029399,
            "unit": "iter/sec",
            "range": "stddev: 0.0001873336345008103",
            "extra": "mean: 30.20392243749548 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 109.97158334287124,
            "unit": "iter/sec",
            "range": "stddev: 0.00010740715085938623",
            "extra": "mean: 9.0932581818176 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.77062321699484,
            "unit": "iter/sec",
            "range": "stddev: 0.00022588348329392646",
            "extra": "mean: 31.47561799999809 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 107.90848962358012,
            "unit": "iter/sec",
            "range": "stddev: 0.00012965873797069125",
            "extra": "mean: 9.267111452382707 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.49970243826147,
            "unit": "iter/sec",
            "range": "stddev: 0.0005503566709935762",
            "extra": "mean: 27.397483628571504 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 142.141687479592,
            "unit": "iter/sec",
            "range": "stddev: 0.00010560964630130385",
            "extra": "mean: 7.035233770835703 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.185990129583466,
            "unit": "iter/sec",
            "range": "stddev: 0.0006750418575924812",
            "extra": "mean: 43.12949304347715 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 94.13273553140696,
            "unit": "iter/sec",
            "range": "stddev: 0.0002792941590068401",
            "extra": "mean: 10.623296925928116 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.497418338100655,
            "unit": "iter/sec",
            "range": "stddev: 0.0004869407317341511",
            "extra": "mean: 44.44954460870042 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 89.4730041432374,
            "unit": "iter/sec",
            "range": "stddev: 0.0006560430159373554",
            "extra": "mean: 11.176555538462743 msec\nrounds: 26"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.82407626542591,
            "unit": "iter/sec",
            "range": "stddev: 0.00021342934984920015",
            "extra": "mean: 43.8133832173882 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 94.60555183992305,
            "unit": "iter/sec",
            "range": "stddev: 0.00016910934342057602",
            "extra": "mean: 10.570204185184037 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.34245502333644,
            "unit": "iter/sec",
            "range": "stddev: 0.00005830852306248729",
            "extra": "mean: 22.05438588372264 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.03063841412298,
            "unit": "iter/sec",
            "range": "stddev: 0.00006965009263003721",
            "extra": "mean: 7.9345785483852636 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.36342965408055,
            "unit": "iter/sec",
            "range": "stddev: 0.00033602664456788595",
            "extra": "mean: 20.257911717390908 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 147.50451798856304,
            "unit": "iter/sec",
            "range": "stddev: 0.00008143236130019544",
            "extra": "mean: 6.779453359371246 msec\nrounds: 64"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.69427371763235,
            "unit": "iter/sec",
            "range": "stddev: 0.00019215786966660109",
            "extra": "mean: 23.42234480000087 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.23373066402522,
            "unit": "iter/sec",
            "range": "stddev: 0.000081959832967635",
            "extra": "mean: 7.030681086205433 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.96641375160928,
            "unit": "iter/sec",
            "range": "stddev: 0.00008373999642073129",
            "extra": "mean: 23.27399269999688 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 142.76582890267463,
            "unit": "iter/sec",
            "range": "stddev: 0.000051410532749610605",
            "extra": "mean: 7.004477245613958 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.720926946047584,
            "unit": "iter/sec",
            "range": "stddev: 0.0001472850025765255",
            "extra": "mean: 28.801074393949435 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 119.73904822921473,
            "unit": "iter/sec",
            "range": "stddev: 0.0003436669575837548",
            "extra": "mean: 8.351494477271228 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.31457427828369,
            "unit": "iter/sec",
            "range": "stddev: 0.00037326690700726137",
            "extra": "mean: 30.016892656252736 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 118.83366942211472,
            "unit": "iter/sec",
            "range": "stddev: 0.00007308665056566476",
            "extra": "mean: 8.415123465117048 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.5331009121165,
            "unit": "iter/sec",
            "range": "stddev: 0.00022517592819565338",
            "extra": "mean: 27.372436914281803 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 135.40629578934434,
            "unit": "iter/sec",
            "range": "stddev: 0.00013920939800215196",
            "extra": "mean: 7.385180978259165 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.855918845965522,
            "unit": "iter/sec",
            "range": "stddev: 0.00023636566579677922",
            "extra": "mean: 35.899013259253294 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.38600470429532,
            "unit": "iter/sec",
            "range": "stddev: 0.00010995663935345221",
            "extra": "mean: 8.897905060609212 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 27.149343993797288,
            "unit": "iter/sec",
            "range": "stddev: 0.0004164878026589879",
            "extra": "mean: 36.83330249999655 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 104.94764343346851,
            "unit": "iter/sec",
            "range": "stddev: 0.0003545856483297347",
            "extra": "mean: 9.528560787874664 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.367441703658937,
            "unit": "iter/sec",
            "range": "stddev: 0.0005710841235711592",
            "extra": "mean: 36.539769074078386 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 107.02850483027757,
            "unit": "iter/sec",
            "range": "stddev: 0.0004307444290527712",
            "extra": "mean: 9.343305333338707 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.580630472134075,
            "unit": "iter/sec",
            "range": "stddev: 0.00013577616243481993",
            "extra": "mean: 21.93914365908902 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.91019363526985,
            "unit": "iter/sec",
            "range": "stddev: 0.000044550854714508424",
            "extra": "mean: 7.19889573133599 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.03169076848672,
            "unit": "iter/sec",
            "range": "stddev: 0.00008504226877467499",
            "extra": "mean: 19.595666632654932 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 165.75754848566564,
            "unit": "iter/sec",
            "range": "stddev: 0.00034356195183183556",
            "extra": "mean: 6.032907756755813 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.580805493656925,
            "unit": "iter/sec",
            "range": "stddev: 0.00007928744534083634",
            "extra": "mean: 22.43117837209744 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.6685416716267,
            "unit": "iter/sec",
            "range": "stddev: 0.00003585629605887841",
            "extra": "mean: 5.825179093749355 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.41096266393857,
            "unit": "iter/sec",
            "range": "stddev: 0.0003949946722017306",
            "extra": "mean: 22.516962930236005 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.58509942643693,
            "unit": "iter/sec",
            "range": "stddev: 0.00004184526021672535",
            "extra": "mean: 5.828011892307272 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.75629087663871,
            "unit": "iter/sec",
            "range": "stddev: 0.00026137711442175715",
            "extra": "mean: 28.771769794116487 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 131.73927782522748,
            "unit": "iter/sec",
            "range": "stddev: 0.00016157277777666983",
            "extra": "mean: 7.590750583335175 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.241157852266035,
            "unit": "iter/sec",
            "range": "stddev: 0.0005473518216394267",
            "extra": "mean: 30.083187969694336 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.0760374114203,
            "unit": "iter/sec",
            "range": "stddev: 0.0003340756498630074",
            "extra": "mean: 7.807861800000006 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.58208256945682,
            "unit": "iter/sec",
            "range": "stddev: 0.000533323899145549",
            "extra": "mean: 26.60842432432698 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 158.76533810499578,
            "unit": "iter/sec",
            "range": "stddev: 0.00011036332905008407",
            "extra": "mean: 6.298604039999418 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.807400898962324,
            "unit": "iter/sec",
            "range": "stddev: 0.0006083618265900236",
            "extra": "mean: 35.96164933333689 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 122.90837986905662,
            "unit": "iter/sec",
            "range": "stddev: 0.00011987786119262553",
            "extra": "mean: 8.136141742860607 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.312190960917643,
            "unit": "iter/sec",
            "range": "stddev: 0.0005172616705534137",
            "extra": "mean: 36.61368659258971 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 115.77072818107868,
            "unit": "iter/sec",
            "range": "stddev: 0.00010165389593875482",
            "extra": "mean: 8.63776202941287 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.352074286444683,
            "unit": "iter/sec",
            "range": "stddev: 0.0003362997288814328",
            "extra": "mean: 36.56029848147884 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.66997935342769,
            "unit": "iter/sec",
            "range": "stddev: 0.00022575877863263255",
            "extra": "mean: 8.498344314282999 msec\nrounds: 35"
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
          "id": "1c32a4ff5b283d082a610f08b25494ea8383be17",
          "message": "Bump version: 7.6.0 → 7.6.1",
          "timestamp": "2025-04-22T22:26:08+02:00",
          "tree_id": "09074bd4244604d3b7baa7b13a0af3341dc5af52",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/1c32a4ff5b283d082a610f08b25494ea8383be17"
        },
        "date": 1745353946304,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.01280605820972,
            "unit": "iter/sec",
            "range": "stddev: 0.0011490134825242408",
            "extra": "mean: 26.30692399999835 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.4031616696511,
            "unit": "iter/sec",
            "range": "stddev: 0.0004780654933445815",
            "extra": "mean: 12.284535139534048 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 48.07705472604809,
            "unit": "iter/sec",
            "range": "stddev: 0.00013746054769785512",
            "extra": "mean: 20.799943043478518 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.3929826801575,
            "unit": "iter/sec",
            "range": "stddev: 0.00007379860343401046",
            "extra": "mean: 7.728394378788446 msec\nrounds: 66"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.229982291137866,
            "unit": "iter/sec",
            "range": "stddev: 0.0003988781558435587",
            "extra": "mean: 26.860071868420885 msec\nrounds: 38"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 121.11585164533388,
            "unit": "iter/sec",
            "range": "stddev: 0.00045992911692081947",
            "extra": "mean: 8.256557555556984 msec\nrounds: 54"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.79085697321337,
            "unit": "iter/sec",
            "range": "stddev: 0.00039533721375454656",
            "extra": "mean: 26.461426918918836 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.46386183176313,
            "unit": "iter/sec",
            "range": "stddev: 0.00008637803691611992",
            "extra": "mean: 8.81337884905359 msec\nrounds: 53"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.10584771455874,
            "unit": "iter/sec",
            "range": "stddev: 0.00026113795434848684",
            "extra": "mean: 31.146973874997208 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.40271090867623,
            "unit": "iter/sec",
            "range": "stddev: 0.000056875415317718774",
            "extra": "mean: 12.13552307894654 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.453929492905132,
            "unit": "iter/sec",
            "range": "stddev: 0.0012163531014035783",
            "extra": "mean: 32.836485033334384 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.25957021222729,
            "unit": "iter/sec",
            "range": "stddev: 0.00028159455247848134",
            "extra": "mean: 12.306242789474267 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.87494108377741,
            "unit": "iter/sec",
            "range": "stddev: 0.00047616439254383",
            "extra": "mean: 29.52034654545559 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 91.19622921295378,
            "unit": "iter/sec",
            "range": "stddev: 0.0002394901969302565",
            "extra": "mean: 10.96536565853928 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.918219051190444,
            "unit": "iter/sec",
            "range": "stddev: 0.0007367541209484985",
            "extra": "mean: 38.58289792307582 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 77.4775649829213,
            "unit": "iter/sec",
            "range": "stddev: 0.0007604521688191935",
            "extra": "mean: 12.906962166666366 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.419625608340684,
            "unit": "iter/sec",
            "range": "stddev: 0.0005714588997680866",
            "extra": "mean: 37.8506499230746 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.82348110609597,
            "unit": "iter/sec",
            "range": "stddev: 0.0003569608087610093",
            "extra": "mean: 13.188526633336059 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.602911792651618,
            "unit": "iter/sec",
            "range": "stddev: 0.0002803021376320431",
            "extra": "mean: 37.58987015384626 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 76.01539540817,
            "unit": "iter/sec",
            "range": "stddev: 0.0002003995477750392",
            "extra": "mean: 13.155229866666218 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.88519624108658,
            "unit": "iter/sec",
            "range": "stddev: 0.0001142382844370916",
            "extra": "mean: 22.279060441861887 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.0447718272582,
            "unit": "iter/sec",
            "range": "stddev: 0.00021066094895785546",
            "extra": "mean: 9.995524820893639 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.45505104893137,
            "unit": "iter/sec",
            "range": "stddev: 0.0001564598411254853",
            "extra": "mean: 17.404910129630796 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 154.4806288876887,
            "unit": "iter/sec",
            "range": "stddev: 0.0002564547364886205",
            "extra": "mean: 6.473303528088464 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.48516978349646,
            "unit": "iter/sec",
            "range": "stddev: 0.00038718197466547453",
            "extra": "mean: 24.104999575000363 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 111.24613154159674,
            "unit": "iter/sec",
            "range": "stddev: 0.000133572891809431",
            "extra": "mean: 8.989076619047053 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.06989575490452,
            "unit": "iter/sec",
            "range": "stddev: 0.0002246040724746931",
            "extra": "mean: 24.34873480000448 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 102.60047548053831,
            "unit": "iter/sec",
            "range": "stddev: 0.00019403038430579168",
            "extra": "mean: 9.746543525421421 msec\nrounds: 59"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.48940775537765,
            "unit": "iter/sec",
            "range": "stddev: 0.0006513199912812611",
            "extra": "mean: 31.75671031250893 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 103.10075962048438,
            "unit": "iter/sec",
            "range": "stddev: 0.00016544463962201914",
            "extra": "mean: 9.699249585366942 msec\nrounds: 41"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.83479150399928,
            "unit": "iter/sec",
            "range": "stddev: 0.0001253696945516393",
            "extra": "mean: 32.4308987096702 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 100.6835215496566,
            "unit": "iter/sec",
            "range": "stddev: 0.00024177707426819672",
            "extra": "mean: 9.932111874998384 msec\nrounds: 40"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.03309257454129,
            "unit": "iter/sec",
            "range": "stddev: 0.000623880213596123",
            "extra": "mean: 28.54443974285914 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 132.82554030890657,
            "unit": "iter/sec",
            "range": "stddev: 0.00021742036546259843",
            "extra": "mean: 7.5286725555517675 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.083252427538817,
            "unit": "iter/sec",
            "range": "stddev: 0.0006253329395040996",
            "extra": "mean: 43.32145147825783 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 90.5690620210483,
            "unit": "iter/sec",
            "range": "stddev: 0.0006172269565546638",
            "extra": "mean: 11.04129796295781 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.320216109935348,
            "unit": "iter/sec",
            "range": "stddev: 0.0009636338118229994",
            "extra": "mean: 44.80243359090382 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 83.98448830687946,
            "unit": "iter/sec",
            "range": "stddev: 0.00022052247427492626",
            "extra": "mean: 11.906960680000793 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.305144559338856,
            "unit": "iter/sec",
            "range": "stddev: 0.0008403857388615757",
            "extra": "mean: 44.83270652381017 msec\nrounds: 21"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 87.20733265277075,
            "unit": "iter/sec",
            "range": "stddev: 0.0003163735873261396",
            "extra": "mean: 11.466925653851288 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 43.38049049490672,
            "unit": "iter/sec",
            "range": "stddev: 0.0007244970913068788",
            "extra": "mean: 23.051837095235463 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 122.23626659976364,
            "unit": "iter/sec",
            "range": "stddev: 0.0005505871854232812",
            "extra": "mean: 8.180878129027656 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.01071864416669,
            "unit": "iter/sec",
            "range": "stddev: 0.0002400835846201071",
            "extra": "mean: 20.40370000000033 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 147.03112094281948,
            "unit": "iter/sec",
            "range": "stddev: 0.00006332314214034171",
            "extra": "mean: 6.801281208955081 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.98256874719553,
            "unit": "iter/sec",
            "range": "stddev: 0.00023027660729984828",
            "extra": "mean: 23.81940957499893 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 140.51381959588122,
            "unit": "iter/sec",
            "range": "stddev: 0.00008102526330420429",
            "extra": "mean: 7.116737719293428 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.94048253384035,
            "unit": "iter/sec",
            "range": "stddev: 0.0002176053276097564",
            "extra": "mean: 23.843311750005114 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 138.9962106268379,
            "unit": "iter/sec",
            "range": "stddev: 0.00015152730931230454",
            "extra": "mean: 7.194440736839169 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.31867537107284,
            "unit": "iter/sec",
            "range": "stddev: 0.00018057336551456963",
            "extra": "mean: 30.01319796969469 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 107.0706800326148,
            "unit": "iter/sec",
            "range": "stddev: 0.0004892925506452329",
            "extra": "mean: 9.339625000003641 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-mask",
            "value": 31.984559554986777,
            "unit": "iter/sec",
            "range": "stddev: 0.0003247302282676936",
            "extra": "mean: 31.265085838710196 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 113.54006194176836,
            "unit": "iter/sec",
            "range": "stddev: 0.0001606590901412844",
            "extra": "mean: 8.807463928572393 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 34.917836492417635,
            "unit": "iter/sec",
            "range": "stddev: 0.000940298910889601",
            "extra": "mean: 28.63865864705417 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 127.27645968704664,
            "unit": "iter/sec",
            "range": "stddev: 0.0009246261705647997",
            "extra": "mean: 7.856912444444536 msec\nrounds: 45"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.187676585842826,
            "unit": "iter/sec",
            "range": "stddev: 0.00023146513405013575",
            "extra": "mean: 36.78137029630256 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 102.92582250159185,
            "unit": "iter/sec",
            "range": "stddev: 0.00030571254338619414",
            "extra": "mean: 9.71573484374666 msec\nrounds: 32"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.43350942235839,
            "unit": "iter/sec",
            "range": "stddev: 0.0002672562476291349",
            "extra": "mean: 37.830769423077996 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 98.5874573956044,
            "unit": "iter/sec",
            "range": "stddev: 0.00017657178057567144",
            "extra": "mean: 10.143278124997934 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 26.668882755093,
            "unit": "iter/sec",
            "range": "stddev: 0.0002770387120087605",
            "extra": "mean: 37.49688388460999 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 93.80727321738514,
            "unit": "iter/sec",
            "range": "stddev: 0.00015321514431515225",
            "extra": "mean: 10.660154225809771 msec\nrounds: 31"
          },
          {
            "name": "equator-int8-none",
            "value": 42.57033555981199,
            "unit": "iter/sec",
            "range": "stddev: 0.0006901740956099374",
            "extra": "mean: 23.490536000003672 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 130.84680938495734,
            "unit": "iter/sec",
            "range": "stddev: 0.00018740260835620288",
            "extra": "mean: 7.642524909093915 msec\nrounds: 66"
          },
          {
            "name": "equator-uint8-none",
            "value": 48.18146744776568,
            "unit": "iter/sec",
            "range": "stddev: 0.000277917025667279",
            "extra": "mean: 20.754868063828 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 170.46397398131734,
            "unit": "iter/sec",
            "range": "stddev: 0.00011588962135550813",
            "extra": "mean: 5.866342175676363 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 42.93819378037952,
            "unit": "iter/sec",
            "range": "stddev: 0.00031168599415589326",
            "extra": "mean: 23.289288904764014 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 169.90919426115508,
            "unit": "iter/sec",
            "range": "stddev: 0.00010053962629178706",
            "extra": "mean: 5.885496687501046 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 43.23855936854934,
            "unit": "iter/sec",
            "range": "stddev: 0.0002755215716357278",
            "extra": "mean: 23.12750504651122 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 168.62778640963145,
            "unit": "iter/sec",
            "range": "stddev: 0.00012377219105395105",
            "extra": "mean: 5.930220761902164 msec\nrounds: 63"
          },
          {
            "name": "equator-uint32-none",
            "value": 33.63691466659263,
            "unit": "iter/sec",
            "range": "stddev: 0.00023938108331302503",
            "extra": "mean: 29.729242705876818 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 131.3108431235853,
            "unit": "iter/sec",
            "range": "stddev: 0.00014880402040346423",
            "extra": "mean: 7.615517319151123 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 32.60612068789975,
            "unit": "iter/sec",
            "range": "stddev: 0.00022872282885104376",
            "extra": "mean: 30.669088468751937 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 125.80540128658615,
            "unit": "iter/sec",
            "range": "stddev: 0.000180871272020015",
            "extra": "mean: 7.948784311112275 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.38927613733506,
            "unit": "iter/sec",
            "range": "stddev: 0.0006592093504344054",
            "extra": "mean: 27.480623583331166 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 159.80557042187888,
            "unit": "iter/sec",
            "range": "stddev: 0.00014034799079899694",
            "extra": "mean: 6.257604145838276 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-none",
            "value": 27.40368374749406,
            "unit": "iter/sec",
            "range": "stddev: 0.00016888260546370402",
            "extra": "mean: 36.491444333335124 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 119.20109694709289,
            "unit": "iter/sec",
            "range": "stddev: 0.00021879814185647722",
            "extra": "mean: 8.38918454285574 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 26.67821565963684,
            "unit": "iter/sec",
            "range": "stddev: 0.00022293111718420616",
            "extra": "mean: 37.48376625926161 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 113.23198919329846,
            "unit": "iter/sec",
            "range": "stddev: 0.0002496155165384176",
            "extra": "mean: 8.831426588231166 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.139460678116976,
            "unit": "iter/sec",
            "range": "stddev: 0.00025827861773587723",
            "extra": "mean: 36.846716000009444 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 115.1599601954042,
            "unit": "iter/sec",
            "range": "stddev: 0.00017320849967540137",
            "extra": "mean: 8.683573685708065 msec\nrounds: 35"
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
          "id": "1dcad4898b3c43c4d71cc1108c3245770a598e39",
          "message": "allow optional height or width (#799)",
          "timestamp": "2025-05-05T11:02:33+02:00",
          "tree_id": "a6df28ec5aa606be784cc41846922f586a9ea375",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/1dcad4898b3c43c4d71cc1108c3245770a598e39"
        },
        "date": 1746436451291,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.2017405214704,
            "unit": "iter/sec",
            "range": "stddev: 0.00014957150645139697",
            "extra": "mean: 26.176817766666243 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 81.75210774743994,
            "unit": "iter/sec",
            "range": "stddev: 0.00006986175932273034",
            "extra": "mean: 12.232100523809615 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.520449867751616,
            "unit": "iter/sec",
            "range": "stddev: 0.00014449731352369984",
            "extra": "mean: 21.04357182608705 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 128.57395845481219,
            "unit": "iter/sec",
            "range": "stddev: 0.00016631887331314493",
            "extra": "mean: 7.777624738460969 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.552275088168805,
            "unit": "iter/sec",
            "range": "stddev: 0.0001394734162020696",
            "extra": "mean: 25.93880640540685 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 122.91139762240658,
            "unit": "iter/sec",
            "range": "stddev: 0.00005336141198972641",
            "extra": "mean: 8.135941982142926 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.89012019775327,
            "unit": "iter/sec",
            "range": "stddev: 0.000521726809989742",
            "extra": "mean: 26.39210418918903 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 113.44902877892808,
            "unit": "iter/sec",
            "range": "stddev: 0.00008768098067116739",
            "extra": "mean: 8.814531166667326 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.25217538972538,
            "unit": "iter/sec",
            "range": "stddev: 0.0010086067785795981",
            "extra": "mean: 31.00566048386836 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 81.61496917503518,
            "unit": "iter/sec",
            "range": "stddev: 0.0001719288603655649",
            "extra": "mean: 12.252654263157956 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.93472434222309,
            "unit": "iter/sec",
            "range": "stddev: 0.0004514067396902357",
            "extra": "mean: 32.32613256666686 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 81.03090389244517,
            "unit": "iter/sec",
            "range": "stddev: 0.0005190973544997834",
            "extra": "mean: 12.340970567566803 msec\nrounds: 37"
          },
          {
            "name": "equator-float32-nodata",
            "value": 34.117893842489515,
            "unit": "iter/sec",
            "range": "stddev: 0.00015653340709174786",
            "extra": "mean: 29.310132818181955 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.84740573884923,
            "unit": "iter/sec",
            "range": "stddev: 0.00010778782243116591",
            "extra": "mean: 10.655595560976048 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.2607653027779,
            "unit": "iter/sec",
            "range": "stddev: 0.0004734406766606512",
            "extra": "mean: 38.079621384614356 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.77058593345981,
            "unit": "iter/sec",
            "range": "stddev: 0.0005973512589528609",
            "extra": "mean: 13.025822166666028 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.19988166603446,
            "unit": "iter/sec",
            "range": "stddev: 0.0005137248980416477",
            "extra": "mean: 38.16811131999884 msec\nrounds: 25"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.61156981625986,
            "unit": "iter/sec",
            "range": "stddev: 0.00012890144703798186",
            "extra": "mean: 13.225489200000123 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.627933428906186,
            "unit": "iter/sec",
            "range": "stddev: 0.0007824770344462745",
            "extra": "mean: 37.55454784615171 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 75.28595506704758,
            "unit": "iter/sec",
            "range": "stddev: 0.000580922008592799",
            "extra": "mean: 13.282689966666794 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.700511892803924,
            "unit": "iter/sec",
            "range": "stddev: 0.0000789617023976999",
            "extra": "mean: 22.37110846511322 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 100.96254876076178,
            "unit": "iter/sec",
            "range": "stddev: 0.00008254591971697627",
            "extra": "mean: 9.904662791047143 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.528112563721905,
            "unit": "iter/sec",
            "range": "stddev: 0.00031816776027855523",
            "extra": "mean: 17.382805648148715 msec\nrounds: 54"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.16584755450737,
            "unit": "iter/sec",
            "range": "stddev: 0.00004622733309063513",
            "extra": "mean: 6.403448741575618 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.484853247431616,
            "unit": "iter/sec",
            "range": "stddev: 0.00047042024056962784",
            "extra": "mean: 24.10518350000217 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 110.32616237030314,
            "unit": "iter/sec",
            "range": "stddev: 0.00008656676935095483",
            "extra": "mean: 9.06403321311549 msec\nrounds: 61"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.34382445557245,
            "unit": "iter/sec",
            "range": "stddev: 0.00018227572793464",
            "extra": "mean: 24.187409200002463 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.25593815381261,
            "unit": "iter/sec",
            "range": "stddev: 0.00037225300796133094",
            "extra": "mean: 9.41123872580592 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.79119328971262,
            "unit": "iter/sec",
            "range": "stddev: 0.0003415921611335047",
            "extra": "mean: 30.495992968750052 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 111.29051259509083,
            "unit": "iter/sec",
            "range": "stddev: 0.00010865812937808063",
            "extra": "mean: 8.98549190476198 msec\nrounds: 42"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.858460072188997,
            "unit": "iter/sec",
            "range": "stddev: 0.00019176387765720205",
            "extra": "mean: 31.388836677418535 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 108.27950035303795,
            "unit": "iter/sec",
            "range": "stddev: 0.00014975000197767712",
            "extra": "mean: 9.235358463417064 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.36026613528646,
            "unit": "iter/sec",
            "range": "stddev: 0.00032782223573416745",
            "extra": "mean: 27.502548971431548 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 141.07823914534163,
            "unit": "iter/sec",
            "range": "stddev: 0.00017793699232052391",
            "extra": "mean: 7.088265391303756 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.056535940348265,
            "unit": "iter/sec",
            "range": "stddev: 0.00039711826526584636",
            "extra": "mean: 43.37164969565221 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 91.87090508186247,
            "unit": "iter/sec",
            "range": "stddev: 0.00024658919521521603",
            "extra": "mean: 10.884838884616844 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.674534895897125,
            "unit": "iter/sec",
            "range": "stddev: 0.0011180311070975966",
            "extra": "mean: 44.10233791304563 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 88.78557842829814,
            "unit": "iter/sec",
            "range": "stddev: 0.00020962346121790288",
            "extra": "mean: 11.26309044444177 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.894631282922933,
            "unit": "iter/sec",
            "range": "stddev: 0.00031569747842777275",
            "extra": "mean: 43.67836230434942 msec\nrounds: 23"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 92.27111477597178,
            "unit": "iter/sec",
            "range": "stddev: 0.00016311934027876486",
            "extra": "mean: 10.83762781481436 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.39201186662392,
            "unit": "iter/sec",
            "range": "stddev: 0.00010074978095064994",
            "extra": "mean: 22.030307952384135 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.70320106939661,
            "unit": "iter/sec",
            "range": "stddev: 0.00003711974529632995",
            "extra": "mean: 7.892460423729073 msec\nrounds: 59"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.79525853065988,
            "unit": "iter/sec",
            "range": "stddev: 0.0008346220762361459",
            "extra": "mean: 20.082233319147868 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.77668085493372,
            "unit": "iter/sec",
            "range": "stddev: 0.00008202276799441873",
            "extra": "mean: 6.721483462687682 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.852149051346736,
            "unit": "iter/sec",
            "range": "stddev: 0.0001018214448990255",
            "extra": "mean: 23.33605249999877 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 143.54640318650516,
            "unit": "iter/sec",
            "range": "stddev: 0.00007739345307097524",
            "extra": "mean: 6.9663884137921075 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.78236080311989,
            "unit": "iter/sec",
            "range": "stddev: 0.00010541449254379377",
            "extra": "mean: 23.37411917500063 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.62799501391706,
            "unit": "iter/sec",
            "range": "stddev: 0.00005605394628760404",
            "extra": "mean: 6.962430965516879 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.63420756849358,
            "unit": "iter/sec",
            "range": "stddev: 0.0001960819182357822",
            "extra": "mean: 28.8731883939418 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 122.66734248196553,
            "unit": "iter/sec",
            "range": "stddev: 0.00009396741029153957",
            "extra": "mean: 8.152128999998668 msec\nrounds: 45"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.11022289006209,
            "unit": "iter/sec",
            "range": "stddev: 0.00030932509733916076",
            "extra": "mean: 30.202152468751464 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 120.1614461245695,
            "unit": "iter/sec",
            "range": "stddev: 0.0001251577809886515",
            "extra": "mean: 8.322136860464509 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.51470911878304,
            "unit": "iter/sec",
            "range": "stddev: 0.00018758697708710394",
            "extra": "mean: 27.386223911766113 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.29133171053584,
            "unit": "iter/sec",
            "range": "stddev: 0.00008985847331419707",
            "extra": "mean: 7.2311112173910335 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.849544133340114,
            "unit": "iter/sec",
            "range": "stddev: 0.00042808064499944644",
            "extra": "mean: 35.90723048148026 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 103.51405985835648,
            "unit": "iter/sec",
            "range": "stddev: 0.0008470932661167719",
            "extra": "mean: 9.660523424241601 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.932070593231263,
            "unit": "iter/sec",
            "range": "stddev: 0.0006853624857175862",
            "extra": "mean: 37.1304536923101 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 106.47685995125194,
            "unit": "iter/sec",
            "range": "stddev: 0.00013449205809335933",
            "extra": "mean: 9.391711968758543 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.26739526705727,
            "unit": "iter/sec",
            "range": "stddev: 0.0008684852751002574",
            "extra": "mean: 36.673836653849236 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.77075344070437,
            "unit": "iter/sec",
            "range": "stddev: 0.0002163495610857265",
            "extra": "mean: 9.365860666660506 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.50196785928931,
            "unit": "iter/sec",
            "range": "stddev: 0.00019235474180340364",
            "extra": "mean: 21.97707147726905 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.62723903578834,
            "unit": "iter/sec",
            "range": "stddev: 0.00003820525040613154",
            "extra": "mean: 7.2135895294130306 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.00548783659202,
            "unit": "iter/sec",
            "range": "stddev: 0.00017121688033864578",
            "extra": "mean: 19.60573346938144 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 173.4886377710637,
            "unit": "iter/sec",
            "range": "stddev: 0.00004621942859466985",
            "extra": "mean: 5.764066240001284 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.401684494618344,
            "unit": "iter/sec",
            "range": "stddev: 0.00015726050351995928",
            "extra": "mean: 22.521668071426518 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.72033301364,
            "unit": "iter/sec",
            "range": "stddev: 0.00004367440609534516",
            "extra": "mean: 5.823422203127038 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.2363605820985,
            "unit": "iter/sec",
            "range": "stddev: 0.0005000394395078156",
            "extra": "mean: 22.605837976749797 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 172.0971270856785,
            "unit": "iter/sec",
            "range": "stddev: 0.00005891830147717063",
            "extra": "mean: 5.810672246156383 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.54967001350327,
            "unit": "iter/sec",
            "range": "stddev: 0.0009602187371152274",
            "extra": "mean: 28.94383650000604 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 133.75667693121824,
            "unit": "iter/sec",
            "range": "stddev: 0.00019228363978303394",
            "extra": "mean: 7.476262291670348 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.26472845976871,
            "unit": "iter/sec",
            "range": "stddev: 0.00028476473812028816",
            "extra": "mean: 30.061871727268958 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 128.9589491080929,
            "unit": "iter/sec",
            "range": "stddev: 0.0001655538434133673",
            "extra": "mean: 7.75440562222482 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 37.659152514932714,
            "unit": "iter/sec",
            "range": "stddev: 0.00025454363255465946",
            "extra": "mean: 26.553969837836295 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 163.0766329811391,
            "unit": "iter/sec",
            "range": "stddev: 0.00008431642112728366",
            "extra": "mean: 6.132086380000601 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.936038684637847,
            "unit": "iter/sec",
            "range": "stddev: 0.0005378677374384765",
            "extra": "mean: 35.796055814810444 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 123.90368076200276,
            "unit": "iter/sec",
            "range": "stddev: 0.0001204876913364019",
            "extra": "mean: 8.070785257145221 msec\nrounds: 35"
          },
          {
            "name": "equator-int64-none",
            "value": 27.282628882821257,
            "unit": "iter/sec",
            "range": "stddev: 0.00032917596351515044",
            "extra": "mean: 36.65335933333238 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 115.83867560579664,
            "unit": "iter/sec",
            "range": "stddev: 0.00014004815165445967",
            "extra": "mean: 8.632695382352589 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 26.973178410853112,
            "unit": "iter/sec",
            "range": "stddev: 0.00022516246492436417",
            "extra": "mean: 37.073865925924146 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 117.80984798230556,
            "unit": "iter/sec",
            "range": "stddev: 0.00014285277563571346",
            "extra": "mean: 8.488254735293394 msec\nrounds: 34"
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
          "id": "c93e772949e1734415b78faadae4a99fbd18820a",
          "message": "Bump version: 7.6.1 → 7.7.0",
          "timestamp": "2025-05-05T11:04:04+02:00",
          "tree_id": "467321b0b5df57f0f3abc2b6a18b9efaf3393be6",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/c93e772949e1734415b78faadae4a99fbd18820a"
        },
        "date": 1746436545411,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.4738664239344,
            "unit": "iter/sec",
            "range": "stddev: 0.0005602415309574522",
            "extra": "mean: 25.991668967741305 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.57478207252436,
            "unit": "iter/sec",
            "range": "stddev: 0.00022010289048001965",
            "extra": "mean: 12.566795333333133 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.637085702363855,
            "unit": "iter/sec",
            "range": "stddev: 0.00023339458657259304",
            "extra": "mean: 20.992048217390803 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 129.29538345328257,
            "unit": "iter/sec",
            "range": "stddev: 0.00006711235013348303",
            "extra": "mean: 7.734228193548172 msec\nrounds: 62"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.79439675942825,
            "unit": "iter/sec",
            "range": "stddev: 0.0015213224686395437",
            "extra": "mean: 26.458948567568772 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 123.37339096229903,
            "unit": "iter/sec",
            "range": "stddev: 0.00005604203227161296",
            "extra": "mean: 8.10547551785769 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 38.14080879248945,
            "unit": "iter/sec",
            "range": "stddev: 0.0002501586202820964",
            "extra": "mean: 26.21863645945852 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.19228421304666,
            "unit": "iter/sec",
            "range": "stddev: 0.000035856190728795845",
            "extra": "mean: 8.757159092590848 msec\nrounds: 54"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.30446352781622,
            "unit": "iter/sec",
            "range": "stddev: 0.00033418103364642047",
            "extra": "mean: 30.95547459374881 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 79.70545800372706,
            "unit": "iter/sec",
            "range": "stddev: 0.0013177101416469543",
            "extra": "mean: 12.546192256410338 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.977828269949534,
            "unit": "iter/sec",
            "range": "stddev: 0.0005981283061777735",
            "extra": "mean: 32.281152548387766 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 82.46511689204588,
            "unit": "iter/sec",
            "range": "stddev: 0.00013335100904435763",
            "extra": "mean: 12.126339447370071 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.83529261311725,
            "unit": "iter/sec",
            "range": "stddev: 0.0005300411520650591",
            "extra": "mean: 29.554938727272024 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.0335195800067,
            "unit": "iter/sec",
            "range": "stddev: 0.00012419249230568295",
            "extra": "mean: 10.74881402439067 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.625844144305137,
            "unit": "iter/sec",
            "range": "stddev: 0.000292144179818453",
            "extra": "mean: 37.557494687502135 msec\nrounds: 16"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 76.4583911906092,
            "unit": "iter/sec",
            "range": "stddev: 0.000908563215601838",
            "extra": "mean: 13.079009176468551 msec\nrounds: 17"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.808197120159345,
            "unit": "iter/sec",
            "range": "stddev: 0.0005617971403045752",
            "extra": "mean: 37.30202353846524 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 75.95928544827498,
            "unit": "iter/sec",
            "range": "stddev: 0.0004589019065726142",
            "extra": "mean: 13.164947433331994 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 27.016290943972614,
            "unit": "iter/sec",
            "range": "stddev: 0.0001733536892172859",
            "extra": "mean: 37.01470353846267 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.20673108765787,
            "unit": "iter/sec",
            "range": "stddev: 0.00016200339652642012",
            "extra": "mean: 12.952238566668939 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.85341018912925,
            "unit": "iter/sec",
            "range": "stddev: 0.000434964268544928",
            "extra": "mean: 22.294848837209745 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.81860710651794,
            "unit": "iter/sec",
            "range": "stddev: 0.00006107794508518982",
            "extra": "mean: 9.63218471014545 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 58.032442942269405,
            "unit": "iter/sec",
            "range": "stddev: 0.00042570618324384873",
            "extra": "mean: 17.231740545453146 msec\nrounds: 55"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 157.3225992984082,
            "unit": "iter/sec",
            "range": "stddev: 0.0000550733197727829",
            "extra": "mean: 6.356365865168604 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 41.92063110738076,
            "unit": "iter/sec",
            "range": "stddev: 0.0003520678701983562",
            "extra": "mean: 23.85460270000408 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 116.09074585774773,
            "unit": "iter/sec",
            "range": "stddev: 0.00004508628237819336",
            "extra": "mean: 8.613951031250622 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-alpha",
            "value": 41.67730623915491,
            "unit": "iter/sec",
            "range": "stddev: 0.00035104038555989304",
            "extra": "mean: 23.99387317073103 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 107.59360748409081,
            "unit": "iter/sec",
            "range": "stddev: 0.00004187078553439683",
            "extra": "mean: 9.294232467740835 msec\nrounds: 62"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 33.313622066959255,
            "unit": "iter/sec",
            "range": "stddev: 0.0007045159028776161",
            "extra": "mean: 30.01775063636232 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 111.92987873940129,
            "unit": "iter/sec",
            "range": "stddev: 0.00010465116890123848",
            "extra": "mean: 8.934164954544727 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-alpha",
            "value": 32.02807216305958,
            "unit": "iter/sec",
            "range": "stddev: 0.0004466375489690445",
            "extra": "mean: 31.22260980644899 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 109.77083104399031,
            "unit": "iter/sec",
            "range": "stddev: 0.00008372543157874699",
            "extra": "mean: 9.109888214285752 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-alpha",
            "value": 37.04116133407974,
            "unit": "iter/sec",
            "range": "stddev: 0.00013819048685839843",
            "extra": "mean: 26.996993722222996 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 143.74083240438932,
            "unit": "iter/sec",
            "range": "stddev: 0.00008376049520763878",
            "extra": "mean: 6.956965416665166 msec\nrounds: 48"
          },
          {
            "name": "equator-float64-alpha",
            "value": 23.737854263685865,
            "unit": "iter/sec",
            "range": "stddev: 0.0003679251028253744",
            "extra": "mean: 42.12680678260792 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 94.01825301008819,
            "unit": "iter/sec",
            "range": "stddev: 0.00013093914531628703",
            "extra": "mean: 10.636232518516374 msec\nrounds: 27"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.57830491998652,
            "unit": "iter/sec",
            "range": "stddev: 0.000527313143840273",
            "extra": "mean: 44.29030449999774 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 91.86157293834476,
            "unit": "iter/sec",
            "range": "stddev: 0.0002236621062809062",
            "extra": "mean: 10.885944666669005 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.870404198644223,
            "unit": "iter/sec",
            "range": "stddev: 0.0002297851347829707",
            "extra": "mean: 43.724631681817016 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 96.12007302431684,
            "unit": "iter/sec",
            "range": "stddev: 0.00014020620937871435",
            "extra": "mean: 10.403654185187895 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 45.197965918731626,
            "unit": "iter/sec",
            "range": "stddev: 0.00009790862057865751",
            "extra": "mean: 22.124889465115615 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-mask",
            "value": 126.64743235343431,
            "unit": "iter/sec",
            "range": "stddev: 0.00006349030661471366",
            "extra": "mean: 7.89593583870935 msec\nrounds: 62"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.73686905200835,
            "unit": "iter/sec",
            "range": "stddev: 0.00014823628898568165",
            "extra": "mean: 20.105809212765884 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.97441046317937,
            "unit": "iter/sec",
            "range": "stddev: 0.00005189690550026232",
            "extra": "mean: 6.712562223880461 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.88010310022792,
            "unit": "iter/sec",
            "range": "stddev: 0.0001513648943568133",
            "extra": "mean: 23.320839450003206 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 144.36625164473074,
            "unit": "iter/sec",
            "range": "stddev: 0.00003408862088861803",
            "extra": "mean: 6.926826655172072 msec\nrounds: 58"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.98349544798145,
            "unit": "iter/sec",
            "range": "stddev: 0.0005595622222855061",
            "extra": "mean: 23.264743585365185 msec\nrounds: 41"
          },
          {
            "name": "dateline-int16-mask",
            "value": 144.73706738679883,
            "unit": "iter/sec",
            "range": "stddev: 0.00008470530579226608",
            "extra": "mean: 6.909080155172523 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 33.80601501103119,
            "unit": "iter/sec",
            "range": "stddev: 0.0038457910340650614",
            "extra": "mean: 29.580534696967135 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 124.3883100071436,
            "unit": "iter/sec",
            "range": "stddev: 0.00004727765835944446",
            "extra": "mean: 8.039340673915177 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.41429790175888,
            "unit": "iter/sec",
            "range": "stddev: 0.0005545364925914311",
            "extra": "mean: 29.92730845161231 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-mask",
            "value": 119.86368700110155,
            "unit": "iter/sec",
            "range": "stddev: 0.00018005501369416322",
            "extra": "mean: 8.34281027906984 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 36.03740933497307,
            "unit": "iter/sec",
            "range": "stddev: 0.0007414073242458804",
            "extra": "mean: 27.748942514287073 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.96508602443907,
            "unit": "iter/sec",
            "range": "stddev: 0.00004589466941157523",
            "extra": "mean: 7.196052106384011 msec\nrounds: 47"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.784705888474278,
            "unit": "iter/sec",
            "range": "stddev: 0.0012420966183848497",
            "extra": "mean: 35.99102340740711 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-mask",
            "value": 113.924913510245,
            "unit": "iter/sec",
            "range": "stddev: 0.00013615537279607558",
            "extra": "mean: 8.77771129411542 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-mask",
            "value": 27.283403351127863,
            "unit": "iter/sec",
            "range": "stddev: 0.0005992296599010195",
            "extra": "mean: 36.652318888899224 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-mask",
            "value": 106.61610091158728,
            "unit": "iter/sec",
            "range": "stddev: 0.00022196865260406054",
            "extra": "mean: 9.379446363633784 msec\nrounds: 33"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.285646612978876,
            "unit": "iter/sec",
            "range": "stddev: 0.0010079716959712022",
            "extra": "mean: 36.649305555556566 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 110.34081180731849,
            "unit": "iter/sec",
            "range": "stddev: 0.00014325457917153643",
            "extra": "mean: 9.062829823531112 msec\nrounds: 34"
          },
          {
            "name": "equator-int8-none",
            "value": 45.4414944977237,
            "unit": "iter/sec",
            "range": "stddev: 0.0011280944455452815",
            "extra": "mean: 22.00631847726956 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 138.77925242921364,
            "unit": "iter/sec",
            "range": "stddev: 0.0004469618809660365",
            "extra": "mean: 7.2056880441121 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 50.218066882384754,
            "unit": "iter/sec",
            "range": "stddev: 0.0000887067370169563",
            "extra": "mean: 19.913152020409115 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 176.09782389825887,
            "unit": "iter/sec",
            "range": "stddev: 0.000029035633765360035",
            "extra": "mean: 5.678661881578694 msec\nrounds: 76"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.244384143912136,
            "unit": "iter/sec",
            "range": "stddev: 0.0003416048768036315",
            "extra": "mean: 22.60173848837709 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 171.74884284363617,
            "unit": "iter/sec",
            "range": "stddev: 0.0000470327351029531",
            "extra": "mean: 5.822455531245829 msec\nrounds: 64"
          },
          {
            "name": "equator-int16-none",
            "value": 44.79822041299094,
            "unit": "iter/sec",
            "range": "stddev: 0.00005447571368827616",
            "extra": "mean: 22.322315279068807 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 173.70049681161484,
            "unit": "iter/sec",
            "range": "stddev: 0.00005656418172588315",
            "extra": "mean: 5.75703592307246 msec\nrounds: 65"
          },
          {
            "name": "equator-uint32-none",
            "value": 35.107981023493075,
            "unit": "iter/sec",
            "range": "stddev: 0.00015394363300431934",
            "extra": "mean: 28.483551911767123 msec\nrounds: 34"
          },
          {
            "name": "dateline-uint32-none",
            "value": 135.98502315342185,
            "unit": "iter/sec",
            "range": "stddev: 0.00009607613888299536",
            "extra": "mean: 7.353751000003683 msec\nrounds: 48"
          },
          {
            "name": "equator-int32-none",
            "value": 33.44263687611243,
            "unit": "iter/sec",
            "range": "stddev: 0.0009135467808374878",
            "extra": "mean: 29.90194833333507 msec\nrounds: 33"
          },
          {
            "name": "dateline-int32-none",
            "value": 131.99456942200436,
            "unit": "iter/sec",
            "range": "stddev: 0.0006250563610822024",
            "extra": "mean: 7.576069260871375 msec\nrounds: 46"
          },
          {
            "name": "equator-float32-none",
            "value": 37.91769376945176,
            "unit": "iter/sec",
            "range": "stddev: 0.0006408996874507126",
            "extra": "mean: 26.372911972975693 msec\nrounds: 37"
          },
          {
            "name": "dateline-float32-none",
            "value": 165.5568025166323,
            "unit": "iter/sec",
            "range": "stddev: 0.00003488098485409638",
            "extra": "mean: 6.040222961539362 msec\nrounds: 52"
          },
          {
            "name": "equator-float64-none",
            "value": 28.283266702025927,
            "unit": "iter/sec",
            "range": "stddev: 0.0008144021537260373",
            "extra": "mean: 35.35659478572078 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 126.87284048328446,
            "unit": "iter/sec",
            "range": "stddev: 0.00009368076234208884",
            "extra": "mean: 7.881907555555599 msec\nrounds: 36"
          },
          {
            "name": "equator-int64-none",
            "value": 27.618896128183856,
            "unit": "iter/sec",
            "range": "stddev: 0.0006471071815148265",
            "extra": "mean: 36.207095148149115 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 116.77301730297623,
            "unit": "iter/sec",
            "range": "stddev: 0.0003117709311410315",
            "extra": "mean: 8.563622171425322 msec\nrounds: 35"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.90956481904772,
            "unit": "iter/sec",
            "range": "stddev: 0.00019319020037612749",
            "extra": "mean: 35.83001048147909 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 121.05365349012538,
            "unit": "iter/sec",
            "range": "stddev: 0.00011352359412862511",
            "extra": "mean: 8.26079982857826 msec\nrounds: 35"
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
          "id": "72986b23607ba0c95b4419f4fc3295a907dee1e1",
          "message": "add more reproject methods (#800)",
          "timestamp": "2025-05-13T16:41:44+02:00",
          "tree_id": "4601956b324008d6338315756225d0c6c82cfc32",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/72986b23607ba0c95b4419f4fc3295a907dee1e1"
        },
        "date": 1747147977482,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 38.41651635388789,
            "unit": "iter/sec",
            "range": "stddev: 0.00011460489615429352",
            "extra": "mean: 26.030470612903354 msec\nrounds: 31"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 82.53695758309146,
            "unit": "iter/sec",
            "range": "stddev: 0.00006201967462732502",
            "extra": "mean: 12.11578460465158 msec\nrounds: 43"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 47.474245877078275,
            "unit": "iter/sec",
            "range": "stddev: 0.00024098838288170288",
            "extra": "mean: 21.064052340909843 msec\nrounds: 44"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 130.03358739698825,
            "unit": "iter/sec",
            "range": "stddev: 0.00010712571977148424",
            "extra": "mean: 7.690320785713872 msec\nrounds: 56"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 38.45988256769802,
            "unit": "iter/sec",
            "range": "stddev: 0.00007940269624981344",
            "extra": "mean: 26.001119432431334 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 124.06973152269823,
            "unit": "iter/sec",
            "range": "stddev: 0.000029987415447092553",
            "extra": "mean: 8.059983589285455 msec\nrounds: 56"
          },
          {
            "name": "equator-int16-nodata",
            "value": 37.93053863905959,
            "unit": "iter/sec",
            "range": "stddev: 0.00008907965807703792",
            "extra": "mean: 26.363981000001772 msec\nrounds: 37"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 114.6255841263652,
            "unit": "iter/sec",
            "range": "stddev: 0.00004484334463445547",
            "extra": "mean: 8.724055869565584 msec\nrounds: 46"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 32.107104162349486,
            "unit": "iter/sec",
            "range": "stddev: 0.00015893304680780735",
            "extra": "mean: 31.14575499999946 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 82.67657920693176,
            "unit": "iter/sec",
            "range": "stddev: 0.00008265485483187507",
            "extra": "mean: 12.095323846153496 msec\nrounds: 39"
          },
          {
            "name": "equator-int32-nodata",
            "value": 31.00223357245213,
            "unit": "iter/sec",
            "range": "stddev: 0.0001994794998351162",
            "extra": "mean: 32.25574046666679 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 83.1019657971176,
            "unit": "iter/sec",
            "range": "stddev: 0.00010616195130735458",
            "extra": "mean: 12.033409684210925 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-nodata",
            "value": 33.45228994670708,
            "unit": "iter/sec",
            "range": "stddev: 0.0019447194768117857",
            "extra": "mean: 29.89331975757421 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 93.65035901595665,
            "unit": "iter/sec",
            "range": "stddev: 0.00006343439020164295",
            "extra": "mean: 10.678015658537035 msec\nrounds: 41"
          },
          {
            "name": "equator-float64-nodata",
            "value": 26.55809537499525,
            "unit": "iter/sec",
            "range": "stddev: 0.0002003986645376372",
            "extra": "mean: 37.65330253846108 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 78.08015535411612,
            "unit": "iter/sec",
            "range": "stddev: 0.00012163923728244043",
            "extra": "mean: 12.807351566665185 msec\nrounds: 30"
          },
          {
            "name": "equator-int64-nodata",
            "value": 26.70542837709482,
            "unit": "iter/sec",
            "range": "stddev: 0.00016401014911423146",
            "extra": "mean: 37.44557046153574 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 76.42508518912999,
            "unit": "iter/sec",
            "range": "stddev: 0.00010330116676838768",
            "extra": "mean: 13.084709000000316 msec\nrounds: 30"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 26.835186075521197,
            "unit": "iter/sec",
            "range": "stddev: 0.00021074817974021536",
            "extra": "mean: 37.264507769230285 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 77.30066191653766,
            "unit": "iter/sec",
            "range": "stddev: 0.000146946674735875",
            "extra": "mean: 12.93649983333533 msec\nrounds: 30"
          },
          {
            "name": "equator-int8-alpha",
            "value": 44.34581540912583,
            "unit": "iter/sec",
            "range": "stddev: 0.00016594575975798203",
            "extra": "mean: 22.550041999999223 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 103.73069301577358,
            "unit": "iter/sec",
            "range": "stddev: 0.0000556177525138562",
            "extra": "mean: 9.64034820289822 msec\nrounds: 69"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 57.53678217924477,
            "unit": "iter/sec",
            "range": "stddev: 0.00035826837537428956",
            "extra": "mean: 17.38018641509517 msec\nrounds: 53"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 156.94838421382707,
            "unit": "iter/sec",
            "range": "stddev: 0.00006525576975830142",
            "extra": "mean: 6.37152147191013 msec\nrounds: 89"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 40.85814417410335,
            "unit": "iter/sec",
            "range": "stddev: 0.000239965179152803",
            "extra": "mean: 24.474924649999608 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 113.15126981505828,
            "unit": "iter/sec",
            "range": "stddev: 0.0000755054240040471",
            "extra": "mean: 8.837726714286674 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-alpha",
            "value": 40.81016261362236,
            "unit": "iter/sec",
            "range": "stddev: 0.001122329073455673",
            "extra": "mean: 24.50370045000021 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 106.55599544374543,
            "unit": "iter/sec",
            "range": "stddev: 0.00006461816396792463",
            "extra": "mean: 9.384737065573512 msec\nrounds: 61"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 32.140263871946956,
            "unit": "iter/sec",
            "range": "stddev: 0.0004109503533246613",
            "extra": "mean: 31.113621343751063 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 109.48711755354111,
            "unit": "iter/sec",
            "range": "stddev: 0.0003503565292960336",
            "extra": "mean: 9.133494627904353 msec\nrounds: 43"
          },
          {
            "name": "equator-int32-alpha",
            "value": 31.153446644134807,
            "unit": "iter/sec",
            "range": "stddev: 0.0004231075731490653",
            "extra": "mean: 32.099177064514876 msec\nrounds: 31"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 109.84979080660317,
            "unit": "iter/sec",
            "range": "stddev: 0.00015300582974107885",
            "extra": "mean: 9.103340048781314 msec\nrounds: 41"
          },
          {
            "name": "equator-float32-alpha",
            "value": 36.06891763115352,
            "unit": "iter/sec",
            "range": "stddev: 0.000874392284268582",
            "extra": "mean: 27.72470219999832 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 140.06726821909285,
            "unit": "iter/sec",
            "range": "stddev: 0.000154383170252479",
            "extra": "mean: 7.1394267391279636 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.992253426984135,
            "unit": "iter/sec",
            "range": "stddev: 0.0016719687435590876",
            "extra": "mean: 43.49290960869374 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 95.85702650197715,
            "unit": "iter/sec",
            "range": "stddev: 0.00026107316678270696",
            "extra": "mean: 10.432203423077953 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.456943300169698,
            "unit": "iter/sec",
            "range": "stddev: 0.0003903669838220557",
            "extra": "mean: 44.529657782608524 msec\nrounds: 23"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 92.06309875219233,
            "unit": "iter/sec",
            "range": "stddev: 0.0001825961794645392",
            "extra": "mean: 10.862115370369137 msec\nrounds: 27"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.959807427326705,
            "unit": "iter/sec",
            "range": "stddev: 0.0002220245731189389",
            "extra": "mean: 43.55437227273094 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 94.44436712057508,
            "unit": "iter/sec",
            "range": "stddev: 0.0001359569729031449",
            "extra": "mean: 10.588243962959924 msec\nrounds: 27"
          },
          {
            "name": "equator-int8-mask",
            "value": 44.98025398977997,
            "unit": "iter/sec",
            "range": "stddev: 0.00005626842900544422",
            "extra": "mean: 22.23197761905061 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-mask",
            "value": 127.10266167621972,
            "unit": "iter/sec",
            "range": "stddev: 0.0000391879768900247",
            "extra": "mean: 7.8676558524587925 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 49.687764625485016,
            "unit": "iter/sec",
            "range": "stddev: 0.00006712525414333838",
            "extra": "mean: 20.125678978262922 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 148.604909200469,
            "unit": "iter/sec",
            "range": "stddev: 0.000053469832514933204",
            "extra": "mean: 6.729252791043353 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 42.414126622906394,
            "unit": "iter/sec",
            "range": "stddev: 0.00019736568406574263",
            "extra": "mean: 23.57705037500253 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 142.88610146517073,
            "unit": "iter/sec",
            "range": "stddev: 0.00009673510992640332",
            "extra": "mean: 6.998581315788473 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 42.36793400201749,
            "unit": "iter/sec",
            "range": "stddev: 0.0001012583679112822",
            "extra": "mean: 23.6027557999968 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 143.91455647877515,
            "unit": "iter/sec",
            "range": "stddev: 0.00006823644614232624",
            "extra": "mean: 6.948567431033164 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-mask",
            "value": 34.148928484204845,
            "unit": "iter/sec",
            "range": "stddev: 0.00019839025744544756",
            "extra": "mean: 29.283495687501215 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 124.37020131359857,
            "unit": "iter/sec",
            "range": "stddev: 0.00004775741728669398",
            "extra": "mean: 8.040511227271452 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 33.15295456546199,
            "unit": "iter/sec",
            "range": "stddev: 0.00011784108120380565",
            "extra": "mean: 30.163224156249946 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 120.61645239939013,
            "unit": "iter/sec",
            "range": "stddev: 0.0000829928933512218",
            "extra": "mean: 8.29074293023276 msec\nrounds: 43"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.34403412428774,
            "unit": "iter/sec",
            "range": "stddev: 0.000441186230470128",
            "extra": "mean: 28.29331808823768 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 138.60180613157002,
            "unit": "iter/sec",
            "range": "stddev: 0.00011772670248900035",
            "extra": "mean: 7.214913195652977 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.058482175024935,
            "unit": "iter/sec",
            "range": "stddev: 0.0001245838762567744",
            "extra": "mean: 36.95698796154217 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.00268529493783,
            "unit": "iter/sec",
            "range": "stddev: 0.00016111353098066474",
            "extra": "mean: 8.928357363635431 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.864289000682398,
            "unit": "iter/sec",
            "range": "stddev: 0.0005343889313249559",
            "extra": "mean: 37.224137961536904 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 98.76426533523887,
            "unit": "iter/sec",
            "range": "stddev: 0.00022274743798481362",
            "extra": "mean: 10.125119612905197 msec\nrounds: 31"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.19475685255558,
            "unit": "iter/sec",
            "range": "stddev: 0.00040312290000696404",
            "extra": "mean: 36.771794115380246 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 106.0836686602671,
            "unit": "iter/sec",
            "range": "stddev: 0.00014803884861444634",
            "extra": "mean: 9.42652165624569 msec\nrounds: 32"
          },
          {
            "name": "equator-int8-none",
            "value": 44.89576807416159,
            "unit": "iter/sec",
            "range": "stddev: 0.00015177141535514075",
            "extra": "mean: 22.27381427906832 msec\nrounds: 43"
          },
          {
            "name": "dateline-int8-none",
            "value": 137.5232491006428,
            "unit": "iter/sec",
            "range": "stddev: 0.00016196459078615913",
            "extra": "mean: 7.27149777611912 msec\nrounds: 67"
          },
          {
            "name": "equator-uint8-none",
            "value": 49.66894018632226,
            "unit": "iter/sec",
            "range": "stddev: 0.00011960648805822246",
            "extra": "mean: 20.133306574465184 msec\nrounds: 47"
          },
          {
            "name": "dateline-uint8-none",
            "value": 169.0705760901835,
            "unit": "iter/sec",
            "range": "stddev: 0.00008780376387000233",
            "extra": "mean: 5.914689729729155 msec\nrounds: 74"
          },
          {
            "name": "equator-uint16-none",
            "value": 43.07905741225003,
            "unit": "iter/sec",
            "range": "stddev: 0.00015542912149324315",
            "extra": "mean: 23.21313557143055 msec\nrounds: 42"
          },
          {
            "name": "dateline-uint16-none",
            "value": 165.7745766573557,
            "unit": "iter/sec",
            "range": "stddev: 0.0006489979871311716",
            "extra": "mean: 6.032288063488341 msec\nrounds: 63"
          },
          {
            "name": "equator-int16-none",
            "value": 43.40422606548904,
            "unit": "iter/sec",
            "range": "stddev: 0.0001389684931303148",
            "extra": "mean: 23.039231214287355 msec\nrounds: 42"
          },
          {
            "name": "dateline-int16-none",
            "value": 171.96524640404544,
            "unit": "iter/sec",
            "range": "stddev: 0.00006332755608570535",
            "extra": "mean: 5.815128468751318 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.09334046030262,
            "unit": "iter/sec",
            "range": "stddev: 0.00015710470741379712",
            "extra": "mean: 29.33124142424159 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 129.85684172440764,
            "unit": "iter/sec",
            "range": "stddev: 0.0003121090975321894",
            "extra": "mean: 7.700787934780351 msec\nrounds: 46"
          },
          {
            "name": "equator-int32-none",
            "value": 31.995433675699193,
            "unit": "iter/sec",
            "range": "stddev: 0.0002118410729153015",
            "extra": "mean: 31.254459937497536 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 127.33928455837382,
            "unit": "iter/sec",
            "range": "stddev: 0.0002483260231948799",
            "extra": "mean: 7.853036111111402 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 35.885672941902605,
            "unit": "iter/sec",
            "range": "stddev: 0.0003930416517936896",
            "extra": "mean: 27.86627414285801 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-none",
            "value": 159.1150464095069,
            "unit": "iter/sec",
            "range": "stddev: 0.00008527971121735281",
            "extra": "mean: 6.284760759999699 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.129217303024173,
            "unit": "iter/sec",
            "range": "stddev: 0.0003679029864337071",
            "extra": "mean: 36.860628481475835 msec\nrounds: 27"
          },
          {
            "name": "dateline-float64-none",
            "value": 116.82355984852637,
            "unit": "iter/sec",
            "range": "stddev: 0.00015433662577444933",
            "extra": "mean: 8.559917205883828 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.70534618894438,
            "unit": "iter/sec",
            "range": "stddev: 0.0003960482788556053",
            "extra": "mean: 37.445685703710716 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 111.85381974313862,
            "unit": "iter/sec",
            "range": "stddev: 0.0001469733167565223",
            "extra": "mean: 8.940240058823226 msec\nrounds: 34"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.562039652121328,
            "unit": "iter/sec",
            "range": "stddev: 0.00022373932174212",
            "extra": "mean: 36.28178511538548 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-none",
            "value": 114.86628129027251,
            "unit": "iter/sec",
            "range": "stddev: 0.0002388258609621236",
            "extra": "mean: 8.705775000001548 msec\nrounds: 34"
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
          "id": "5fb22065beed30928f2f9cf4c109b7f06d7e7c87",
          "message": "Bump version: 7.7.0 → 7.7.1",
          "timestamp": "2025-05-13T16:42:08+02:00",
          "tree_id": "e874b6a8c0234e6603bc0f6732357699187635f4",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/5fb22065beed30928f2f9cf4c109b7f06d7e7c87"
        },
        "date": 1747148017148,
        "tool": "pytest",
        "benches": [
          {
            "name": "equator-int8-nodata",
            "value": 37.746574164020736,
            "unit": "iter/sec",
            "range": "stddev: 0.0002373724433195706",
            "extra": "mean: 26.49247043333484 msec\nrounds: 30"
          },
          {
            "name": "dateline-int8-nodata",
            "value": 79.34931371203943,
            "unit": "iter/sec",
            "range": "stddev: 0.00024406316219392453",
            "extra": "mean: 12.602503452380494 msec\nrounds: 42"
          },
          {
            "name": "equator-uint8-nodata",
            "value": 46.319089148083364,
            "unit": "iter/sec",
            "range": "stddev: 0.000255533508165947",
            "extra": "mean: 21.589370999999016 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-nodata",
            "value": 125.99034810040273,
            "unit": "iter/sec",
            "range": "stddev: 0.00023121726615893181",
            "extra": "mean: 7.937115938461348 msec\nrounds: 65"
          },
          {
            "name": "equator-uint16-nodata",
            "value": 37.42224987746633,
            "unit": "iter/sec",
            "range": "stddev: 0.00018812511510683021",
            "extra": "mean: 26.72207051351411 msec\nrounds: 37"
          },
          {
            "name": "dateline-uint16-nodata",
            "value": 117.62038453305962,
            "unit": "iter/sec",
            "range": "stddev: 0.0001778713135951883",
            "extra": "mean: 8.50192765454639 msec\nrounds: 55"
          },
          {
            "name": "equator-int16-nodata",
            "value": 36.89281059101004,
            "unit": "iter/sec",
            "range": "stddev: 0.00021017534442654688",
            "extra": "mean: 27.105552111111802 msec\nrounds: 36"
          },
          {
            "name": "dateline-int16-nodata",
            "value": 105.94654441838445,
            "unit": "iter/sec",
            "range": "stddev: 0.00017632289291121938",
            "extra": "mean: 9.438722192306578 msec\nrounds: 52"
          },
          {
            "name": "equator-uint32-nodata",
            "value": 30.84070950668299,
            "unit": "iter/sec",
            "range": "stddev: 0.001746176615225077",
            "extra": "mean: 32.424675566666394 msec\nrounds: 30"
          },
          {
            "name": "dateline-uint32-nodata",
            "value": 76.40135542036714,
            "unit": "iter/sec",
            "range": "stddev: 0.00024758886917159974",
            "extra": "mean: 13.088773026314913 msec\nrounds: 38"
          },
          {
            "name": "equator-int32-nodata",
            "value": 30.05803039417522,
            "unit": "iter/sec",
            "range": "stddev: 0.00014597297388848496",
            "extra": "mean: 33.26897960000016 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-nodata",
            "value": 71.8209181316823,
            "unit": "iter/sec",
            "range": "stddev: 0.0020113872008647622",
            "extra": "mean: 13.923520138889323 msec\nrounds: 36"
          },
          {
            "name": "equator-float32-nodata",
            "value": 32.81817020597346,
            "unit": "iter/sec",
            "range": "stddev: 0.00030550368336751974",
            "extra": "mean: 30.470924909091462 msec\nrounds: 33"
          },
          {
            "name": "dateline-float32-nodata",
            "value": 87.94638387945237,
            "unit": "iter/sec",
            "range": "stddev: 0.00017911797541875118",
            "extra": "mean: 11.37056415384508 msec\nrounds: 39"
          },
          {
            "name": "equator-float64-nodata",
            "value": 25.71751160024295,
            "unit": "iter/sec",
            "range": "stddev: 0.0004878797849622649",
            "extra": "mean: 38.88401084615641 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-nodata",
            "value": 70.92370429621113,
            "unit": "iter/sec",
            "range": "stddev: 0.0003773876638228359",
            "extra": "mean: 14.099658357148469 msec\nrounds: 28"
          },
          {
            "name": "equator-int64-nodata",
            "value": 25.774105021562832,
            "unit": "iter/sec",
            "range": "stddev: 0.00037542903996102466",
            "extra": "mean: 38.79863138461614 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-nodata",
            "value": 69.00117156613342,
            "unit": "iter/sec",
            "range": "stddev: 0.0002574513928455508",
            "extra": "mean: 14.492507551724117 msec\nrounds: 29"
          },
          {
            "name": "equator-uint64-nodata",
            "value": 25.56921789674848,
            "unit": "iter/sec",
            "range": "stddev: 0.00026730502609494106",
            "extra": "mean: 39.109526307692235 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-nodata",
            "value": 70.46034134219407,
            "unit": "iter/sec",
            "range": "stddev: 0.00015913112120033207",
            "extra": "mean: 14.192380862071778 msec\nrounds: 29"
          },
          {
            "name": "equator-int8-alpha",
            "value": 42.43622787240174,
            "unit": "iter/sec",
            "range": "stddev: 0.00025273697947311426",
            "extra": "mean: 23.56477119047489 msec\nrounds: 42"
          },
          {
            "name": "dateline-int8-alpha",
            "value": 95.40709846364736,
            "unit": "iter/sec",
            "range": "stddev: 0.0002457333687187764",
            "extra": "mean: 10.48140040000301 msec\nrounds: 65"
          },
          {
            "name": "equator-uint8-alpha",
            "value": 54.838540262043914,
            "unit": "iter/sec",
            "range": "stddev: 0.00043807465575770014",
            "extra": "mean: 18.235350452830023 msec\nrounds: 53"
          },
          {
            "name": "dateline-uint8-alpha",
            "value": 143.4699291399331,
            "unit": "iter/sec",
            "range": "stddev: 0.00021428875555259673",
            "extra": "mean: 6.9701017209303275 msec\nrounds: 86"
          },
          {
            "name": "equator-uint16-alpha",
            "value": 39.626900055369795,
            "unit": "iter/sec",
            "range": "stddev: 0.00012994595796217952",
            "extra": "mean: 25.235383000000557 msec\nrounds: 39"
          },
          {
            "name": "dateline-uint16-alpha",
            "value": 101.58723686882333,
            "unit": "iter/sec",
            "range": "stddev: 0.0002687183281935837",
            "extra": "mean: 9.843756271186617 msec\nrounds: 59"
          },
          {
            "name": "equator-int16-alpha",
            "value": 39.46832854210808,
            "unit": "iter/sec",
            "range": "stddev: 0.0001503637709373565",
            "extra": "mean: 25.336770948714413 msec\nrounds: 39"
          },
          {
            "name": "dateline-int16-alpha",
            "value": 99.09553167534771,
            "unit": "iter/sec",
            "range": "stddev: 0.0001808559906608104",
            "extra": "mean: 10.091272362069306 msec\nrounds: 58"
          },
          {
            "name": "equator-uint32-alpha",
            "value": 31.679797416400607,
            "unit": "iter/sec",
            "range": "stddev: 0.00018795130259579627",
            "extra": "mean: 31.56585841935658 msec\nrounds: 31"
          },
          {
            "name": "dateline-uint32-alpha",
            "value": 96.6824623976081,
            "unit": "iter/sec",
            "range": "stddev: 0.00027400821926166477",
            "extra": "mean: 10.34313747500022 msec\nrounds: 40"
          },
          {
            "name": "equator-int32-alpha",
            "value": 30.71266871202367,
            "unit": "iter/sec",
            "range": "stddev: 0.00021228677306878223",
            "extra": "mean: 32.55985369999811 msec\nrounds: 30"
          },
          {
            "name": "dateline-int32-alpha",
            "value": 93.53117105709323,
            "unit": "iter/sec",
            "range": "stddev: 0.000565547769348322",
            "extra": "mean: 10.691622789471765 msec\nrounds: 38"
          },
          {
            "name": "equator-float32-alpha",
            "value": 35.29377151896181,
            "unit": "iter/sec",
            "range": "stddev: 0.0001538778127649341",
            "extra": "mean: 28.333611200002906 msec\nrounds: 35"
          },
          {
            "name": "dateline-float32-alpha",
            "value": 121.01132087641959,
            "unit": "iter/sec",
            "range": "stddev: 0.0004716195595103262",
            "extra": "mean: 8.263689651162721 msec\nrounds: 43"
          },
          {
            "name": "equator-float64-alpha",
            "value": 22.978476268088098,
            "unit": "iter/sec",
            "range": "stddev: 0.0011109949721411847",
            "extra": "mean: 43.51898656521337 msec\nrounds: 23"
          },
          {
            "name": "dateline-float64-alpha",
            "value": 86.50104599724284,
            "unit": "iter/sec",
            "range": "stddev: 0.00020249913211003472",
            "extra": "mean: 11.560553846156662 msec\nrounds: 26"
          },
          {
            "name": "equator-int64-alpha",
            "value": 22.23657399907739,
            "unit": "iter/sec",
            "range": "stddev: 0.00028780107301178425",
            "extra": "mean: 44.970956409089396 msec\nrounds: 22"
          },
          {
            "name": "dateline-int64-alpha",
            "value": 81.08915212547328,
            "unit": "iter/sec",
            "range": "stddev: 0.00020007281093787605",
            "extra": "mean: 12.332105759999195 msec\nrounds: 25"
          },
          {
            "name": "equator-uint64-alpha",
            "value": 22.284175651941,
            "unit": "iter/sec",
            "range": "stddev: 0.0007327186132637272",
            "extra": "mean: 44.87489309091395 msec\nrounds: 22"
          },
          {
            "name": "dateline-uint64-alpha",
            "value": 82.57775429236993,
            "unit": "iter/sec",
            "range": "stddev: 0.0002375318433080908",
            "extra": "mean: 12.109798923078712 msec\nrounds: 26"
          },
          {
            "name": "equator-int8-mask",
            "value": 42.78996062111433,
            "unit": "iter/sec",
            "range": "stddev: 0.00018651435017079734",
            "extra": "mean: 23.36996775609461 msec\nrounds: 41"
          },
          {
            "name": "dateline-int8-mask",
            "value": 120.97357070571445,
            "unit": "iter/sec",
            "range": "stddev: 0.00015896366116807597",
            "extra": "mean: 8.266268360654108 msec\nrounds: 61"
          },
          {
            "name": "equator-uint8-mask",
            "value": 47.9997871480742,
            "unit": "iter/sec",
            "range": "stddev: 0.00034696047548007756",
            "extra": "mean: 20.833425717391354 msec\nrounds: 46"
          },
          {
            "name": "dateline-uint8-mask",
            "value": 147.71305294085766,
            "unit": "iter/sec",
            "range": "stddev: 0.0001027146602606105",
            "extra": "mean: 6.769882417909179 msec\nrounds: 67"
          },
          {
            "name": "equator-uint16-mask",
            "value": 41.11669409230917,
            "unit": "iter/sec",
            "range": "stddev: 0.00027961693505297786",
            "extra": "mean: 24.321021474998616 msec\nrounds: 40"
          },
          {
            "name": "dateline-uint16-mask",
            "value": 138.3809394637679,
            "unit": "iter/sec",
            "range": "stddev: 0.00023830446807027042",
            "extra": "mean: 7.226428754386573 msec\nrounds: 57"
          },
          {
            "name": "equator-int16-mask",
            "value": 41.51572418588072,
            "unit": "iter/sec",
            "range": "stddev: 0.00023099842659751697",
            "extra": "mean: 24.08725897500048 msec\nrounds: 40"
          },
          {
            "name": "dateline-int16-mask",
            "value": 138.49711483783256,
            "unit": "iter/sec",
            "range": "stddev: 0.0001782285375552255",
            "extra": "mean: 7.220367017543351 msec\nrounds: 57"
          },
          {
            "name": "equator-uint32-mask",
            "value": 32.961213999744594,
            "unit": "iter/sec",
            "range": "stddev: 0.001155098223083944",
            "extra": "mean: 30.338688375001865 msec\nrounds: 32"
          },
          {
            "name": "dateline-uint32-mask",
            "value": 117.11861742962913,
            "unit": "iter/sec",
            "range": "stddev: 0.00027566046860163205",
            "extra": "mean: 8.538352159090772 msec\nrounds: 44"
          },
          {
            "name": "equator-int32-mask",
            "value": 32.07166011557257,
            "unit": "iter/sec",
            "range": "stddev: 0.000733729295112882",
            "extra": "mean: 31.18017578124821 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-mask",
            "value": 113.64841571869366,
            "unit": "iter/sec",
            "range": "stddev: 0.00022773776556276026",
            "extra": "mean: 8.799066785719507 msec\nrounds: 42"
          },
          {
            "name": "equator-float32-mask",
            "value": 35.65529167467145,
            "unit": "iter/sec",
            "range": "stddev: 0.00038457035704786424",
            "extra": "mean: 28.046327852938944 msec\nrounds: 34"
          },
          {
            "name": "dateline-float32-mask",
            "value": 132.7425880318888,
            "unit": "iter/sec",
            "range": "stddev: 0.00012781552610140014",
            "extra": "mean: 7.533377304349148 msec\nrounds: 46"
          },
          {
            "name": "equator-float64-mask",
            "value": 27.28227783472721,
            "unit": "iter/sec",
            "range": "stddev: 0.0002471604039543681",
            "extra": "mean: 36.653830961545104 msec\nrounds: 26"
          },
          {
            "name": "dateline-float64-mask",
            "value": 112.82325027900616,
            "unit": "iter/sec",
            "range": "stddev: 0.0001708131404337151",
            "extra": "mean: 8.863421303029748 msec\nrounds: 33"
          },
          {
            "name": "equator-int64-mask",
            "value": 26.97205190112194,
            "unit": "iter/sec",
            "range": "stddev: 0.00027013452792762067",
            "extra": "mean: 37.07541434615153 msec\nrounds: 26"
          },
          {
            "name": "dateline-int64-mask",
            "value": 101.64053799703301,
            "unit": "iter/sec",
            "range": "stddev: 0.00023302113899048747",
            "extra": "mean: 9.838594125005429 msec\nrounds: 32"
          },
          {
            "name": "equator-uint64-mask",
            "value": 27.174206285197847,
            "unit": "iter/sec",
            "range": "stddev: 0.0002952006195452708",
            "extra": "mean: 36.79960288461906 msec\nrounds: 26"
          },
          {
            "name": "dateline-uint64-mask",
            "value": 108.11443984223253,
            "unit": "iter/sec",
            "range": "stddev: 0.0002476342522775975",
            "extra": "mean: 9.249458272727155 msec\nrounds: 33"
          },
          {
            "name": "equator-int8-none",
            "value": 45.69594224737332,
            "unit": "iter/sec",
            "range": "stddev: 0.00019566536342693514",
            "extra": "mean: 21.883781159091466 msec\nrounds: 44"
          },
          {
            "name": "dateline-int8-none",
            "value": 141.04742615157102,
            "unit": "iter/sec",
            "range": "stddev: 0.000032724392188452775",
            "extra": "mean: 7.089813882356064 msec\nrounds: 68"
          },
          {
            "name": "equator-uint8-none",
            "value": 51.557635883947505,
            "unit": "iter/sec",
            "range": "stddev: 0.0002524583984969433",
            "extra": "mean: 19.395769081633752 msec\nrounds: 49"
          },
          {
            "name": "dateline-uint8-none",
            "value": 173.6650228447219,
            "unit": "iter/sec",
            "range": "stddev: 0.0000769989015111408",
            "extra": "mean: 5.758211893330554 msec\nrounds: 75"
          },
          {
            "name": "equator-uint16-none",
            "value": 44.309971626578616,
            "unit": "iter/sec",
            "range": "stddev: 0.00021820768830808093",
            "extra": "mean: 22.568283465118856 msec\nrounds: 43"
          },
          {
            "name": "dateline-uint16-none",
            "value": 174.87116575360363,
            "unit": "iter/sec",
            "range": "stddev: 0.00007422460771154218",
            "extra": "mean: 5.718495646154818 msec\nrounds: 65"
          },
          {
            "name": "equator-int16-none",
            "value": 42.06975554271882,
            "unit": "iter/sec",
            "range": "stddev: 0.003260479211889493",
            "extra": "mean: 23.770045418604145 msec\nrounds: 43"
          },
          {
            "name": "dateline-int16-none",
            "value": 173.6551179673113,
            "unit": "iter/sec",
            "range": "stddev: 0.00009588794487870521",
            "extra": "mean: 5.758540328124617 msec\nrounds: 64"
          },
          {
            "name": "equator-uint32-none",
            "value": 34.39345165688819,
            "unit": "iter/sec",
            "range": "stddev: 0.0003940730255414322",
            "extra": "mean: 29.075302181824593 msec\nrounds: 33"
          },
          {
            "name": "dateline-uint32-none",
            "value": 134.4019262552001,
            "unit": "iter/sec",
            "range": "stddev: 0.00013274901438452828",
            "extra": "mean: 7.440369553195368 msec\nrounds: 47"
          },
          {
            "name": "equator-int32-none",
            "value": 33.09666189663889,
            "unit": "iter/sec",
            "range": "stddev: 0.00020481572661700187",
            "extra": "mean: 30.214527468752195 msec\nrounds: 32"
          },
          {
            "name": "dateline-int32-none",
            "value": 119.29290071539099,
            "unit": "iter/sec",
            "range": "stddev: 0.0017852197549153128",
            "extra": "mean: 8.382728511110649 msec\nrounds: 45"
          },
          {
            "name": "equator-float32-none",
            "value": 36.96215099661093,
            "unit": "iter/sec",
            "range": "stddev: 0.00040534513070583986",
            "extra": "mean: 27.054702527774705 msec\nrounds: 36"
          },
          {
            "name": "dateline-float32-none",
            "value": 158.65751524626234,
            "unit": "iter/sec",
            "range": "stddev: 0.00028795850354705024",
            "extra": "mean: 6.302884539996967 msec\nrounds: 50"
          },
          {
            "name": "equator-float64-none",
            "value": 27.694866929317687,
            "unit": "iter/sec",
            "range": "stddev: 0.00021163348032147815",
            "extra": "mean: 36.10777414284679 msec\nrounds: 28"
          },
          {
            "name": "dateline-float64-none",
            "value": 119.41086849843907,
            "unit": "iter/sec",
            "range": "stddev: 0.00023826225982103764",
            "extra": "mean: 8.374447088231939 msec\nrounds: 34"
          },
          {
            "name": "equator-int64-none",
            "value": 26.812918465305287,
            "unit": "iter/sec",
            "range": "stddev: 0.00047344042515390735",
            "extra": "mean: 37.29545522222637 msec\nrounds: 27"
          },
          {
            "name": "dateline-int64-none",
            "value": 112.66108841711095,
            "unit": "iter/sec",
            "range": "stddev: 0.00013842544676117327",
            "extra": "mean: 8.87617911427989 msec\nrounds: 35"
          },
          {
            "name": "equator-uint64-none",
            "value": 27.279991466005377,
            "unit": "iter/sec",
            "range": "stddev: 0.00029691297388190766",
            "extra": "mean: 36.656902962969674 msec\nrounds: 27"
          },
          {
            "name": "dateline-uint64-none",
            "value": 115.52616080727982,
            "unit": "iter/sec",
            "range": "stddev: 0.00016808494796246825",
            "extra": "mean: 8.656048058830546 msec\nrounds: 34"
          }
        ]
      }
    ]
  }
}