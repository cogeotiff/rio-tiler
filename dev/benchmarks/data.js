window.BENCHMARK_DATA = {
  "lastUpdate": 1728041229959,
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
      }
    ]
  }
}