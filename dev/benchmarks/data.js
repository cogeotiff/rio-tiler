window.BENCHMARK_DATA = {
  "lastUpdate": 1683640299951,
  "repoUrl": "https://github.com/cogeotiff/rio-tiler",
  "entries": {
    "rio-tiler Benchmarks": [
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
          "id": "bc23cc25ede2816281ac2f79530bed5e658565bc",
          "message": "save benchmarks",
          "timestamp": "2023-05-02T22:51:09+02:00",
          "tree_id": "2efc0c182af631b247b4b7b6be4a119ed9811aac",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/bc23cc25ede2816281ac2f79530bed5e658565bc"
        },
        "date": 1683060952479,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 51.789559676374886,
            "unit": "iter/sec",
            "range": "stddev: 0.001499153160297739",
            "extra": "mean: 19.308911028571174 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 61.366300553686244,
            "unit": "iter/sec",
            "range": "stddev: 0.001108642020499364",
            "extra": "mean: 16.295588799998644 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 51.845353191918406,
            "unit": "iter/sec",
            "range": "stddev: 0.0022151322939278073",
            "extra": "mean: 19.2881316923091 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 58.14317215510305,
            "unit": "iter/sec",
            "range": "stddev: 0.00114757857747308",
            "extra": "mean: 17.19892401694896 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 48.53728928348101,
            "unit": "iter/sec",
            "range": "stddev: 0.0026151108810380888",
            "extra": "mean: 20.60271627777813 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 58.41646831766633,
            "unit": "iter/sec",
            "range": "stddev: 0.001997055388573157",
            "extra": "mean: 17.118460406781896 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 50.50505536592899,
            "unit": "iter/sec",
            "range": "stddev: 0.0016752700599623092",
            "extra": "mean: 19.79999809434138 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 59.86324988852811,
            "unit": "iter/sec",
            "range": "stddev: 0.0011469136147328318",
            "extra": "mean: 16.704739583335503 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 40.65242251507169,
            "unit": "iter/sec",
            "range": "stddev: 0.0007567952437924815",
            "extra": "mean: 24.598780051281192 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 53.855292141186474,
            "unit": "iter/sec",
            "range": "stddev: 0.0008180962102027799",
            "extra": "mean: 18.568277326922864 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 36.951896302425205,
            "unit": "iter/sec",
            "range": "stddev: 0.0017748245854509186",
            "extra": "mean: 27.062210605261104 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 52.91502720258321,
            "unit": "iter/sec",
            "range": "stddev: 0.0007922998706483218",
            "extra": "mean: 18.898223300000154 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 48.55231475293894,
            "unit": "iter/sec",
            "range": "stddev: 0.0018165938380973257",
            "extra": "mean: 20.596340361701678 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 56.429822199391054,
            "unit": "iter/sec",
            "range": "stddev: 0.0010171213444095126",
            "extra": "mean: 17.721126188676724 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 38.59751820612849,
            "unit": "iter/sec",
            "range": "stddev: 0.002748211731541547",
            "extra": "mean: 25.908401536584304 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 53.49434467202095,
            "unit": "iter/sec",
            "range": "stddev: 0.0011635318257627978",
            "extra": "mean: 18.693564826919513 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 65.83005756279577,
            "unit": "iter/sec",
            "range": "stddev: 0.0014357497901287032",
            "extra": "mean: 15.190629281253365 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 79.96509521462406,
            "unit": "iter/sec",
            "range": "stddev: 0.0004750761929978314",
            "extra": "mean: 12.505456253331886 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 63.052455860125434,
            "unit": "iter/sec",
            "range": "stddev: 0.0007862230616818301",
            "extra": "mean: 15.859810476191189 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 78.35932111281839,
            "unit": "iter/sec",
            "range": "stddev: 0.0006067194682760452",
            "extra": "mean: 12.761723631579745 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 71.90179484834759,
            "unit": "iter/sec",
            "range": "stddev: 0.001591611455192829",
            "extra": "mean: 13.907858657898045 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 87.53480320364532,
            "unit": "iter/sec",
            "range": "stddev: 0.0012524987651543777",
            "extra": "mean: 11.424027511360825 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 75.88178697160694,
            "unit": "iter/sec",
            "range": "stddev: 0.0006183680952174017",
            "extra": "mean: 13.178392864867229 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 88.32964176582269,
            "unit": "iter/sec",
            "range": "stddev: 0.0011992402088472124",
            "extra": "mean: 11.321227846153556 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 52.603952358351144,
            "unit": "iter/sec",
            "range": "stddev: 0.0014835970610425377",
            "extra": "mean: 19.009978436368286 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 83.48458609737455,
            "unit": "iter/sec",
            "range": "stddev: 0.0011826560112473234",
            "extra": "mean: 11.97825906250074 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 51.449361870701274,
            "unit": "iter/sec",
            "range": "stddev: 0.0023810783391406917",
            "extra": "mean: 19.436587037038983 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 79.7018047797069,
            "unit": "iter/sec",
            "range": "stddev: 0.0020142034573840013",
            "extra": "mean: 12.54676732558273 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 57.356748317845636,
            "unit": "iter/sec",
            "range": "stddev: 0.001240761166924354",
            "extra": "mean: 17.434740101695514 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 79.25185050358058,
            "unit": "iter/sec",
            "range": "stddev: 0.0014939458354783003",
            "extra": "mean: 12.618001897063843 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 55.635256748165986,
            "unit": "iter/sec",
            "range": "stddev: 0.0016413325022393982",
            "extra": "mean: 17.97421380702022 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 83.24091720217402,
            "unit": "iter/sec",
            "range": "stddev: 0.0009282820904361123",
            "extra": "mean: 12.013322697673047 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 71.68794345745923,
            "unit": "iter/sec",
            "range": "stddev: 0.0013562306560686993",
            "extra": "mean: 13.949347013886873 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 82.87730188410931,
            "unit": "iter/sec",
            "range": "stddev: 0.0009737067367959231",
            "extra": "mean: 12.066029869050762 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 57.386102425954626,
            "unit": "iter/sec",
            "range": "stddev: 0.001212253388057877",
            "extra": "mean: 17.425821892858146 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 75.98695550462982,
            "unit": "iter/sec",
            "range": "stddev: 0.0009658439112457377",
            "extra": "mean: 13.160153520548286 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 55.323836957791706,
            "unit": "iter/sec",
            "range": "stddev: 0.001258532396147483",
            "extra": "mean: 18.075391277776546 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 77.30248404125525,
            "unit": "iter/sec",
            "range": "stddev: 0.0008748520599002619",
            "extra": "mean: 12.936194902434364 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 50.744927142001664,
            "unit": "iter/sec",
            "range": "stddev: 0.001778520904334178",
            "extra": "mean: 19.706403306120787 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 78.14610128726692,
            "unit": "iter/sec",
            "range": "stddev: 0.0017864057204739095",
            "extra": "mean: 12.796543698629012 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 75.7067047847699,
            "unit": "iter/sec",
            "range": "stddev: 0.0013688512707968423",
            "extra": "mean: 13.208869714286816 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 82.2840089871588,
            "unit": "iter/sec",
            "range": "stddev: 0.0015149069948358314",
            "extra": "mean: 12.153029638554186 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 78.94937963153731,
            "unit": "iter/sec",
            "range": "stddev: 0.0010353465231742222",
            "extra": "mean: 12.666343987338154 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 86.41275837366408,
            "unit": "iter/sec",
            "range": "stddev: 0.000912450082908548",
            "extra": "mean: 11.572365225003267 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 75.54844300314211,
            "unit": "iter/sec",
            "range": "stddev: 0.0006857755741744133",
            "extra": "mean: 13.23654016216336 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 84.49893500016857,
            "unit": "iter/sec",
            "range": "stddev: 0.0007069236566229805",
            "extra": "mean: 11.834468682924879 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 74.94686301928019,
            "unit": "iter/sec",
            "range": "stddev: 0.000906946033925705",
            "extra": "mean: 13.34278660526123 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 84.40933228958833,
            "unit": "iter/sec",
            "range": "stddev: 0.000903372388114149",
            "extra": "mean: 11.847031280489674 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 59.69023782304391,
            "unit": "iter/sec",
            "range": "stddev: 0.0013091282475884438",
            "extra": "mean: 16.753158246153642 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 83.4585362860501,
            "unit": "iter/sec",
            "range": "stddev: 0.000723246247516284",
            "extra": "mean: 11.981997821918998 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 61.50936935973658,
            "unit": "iter/sec",
            "range": "stddev: 0.0012670173738461414",
            "extra": "mean: 16.257685786884203 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 80.13838419471092,
            "unit": "iter/sec",
            "range": "stddev: 0.0015947859297597519",
            "extra": "mean: 12.478414807694604 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 73.32507548286804,
            "unit": "iter/sec",
            "range": "stddev: 0.0006211589541041939",
            "extra": "mean: 13.637899360003303 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 79.72982106599594,
            "unit": "iter/sec",
            "range": "stddev: 0.000633414892255055",
            "extra": "mean: 12.542358513162286 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 62.37872706807367,
            "unit": "iter/sec",
            "range": "stddev: 0.0009399533370011657",
            "extra": "mean: 16.031106228068808 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 73.24568102951216,
            "unit": "iter/sec",
            "range": "stddev: 0.0009589575374222046",
            "extra": "mean: 13.65268212329243 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 57.64091438313059,
            "unit": "iter/sec",
            "range": "stddev: 0.0015038991962178332",
            "extra": "mean: 17.348787934784458 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 77.2098418880905,
            "unit": "iter/sec",
            "range": "stddev: 0.0007052917486546212",
            "extra": "mean: 12.95171671830931 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 54.42675907494046,
            "unit": "iter/sec",
            "range": "stddev: 0.0020191731105591556",
            "extra": "mean: 18.373315203705133 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 76.19538371001272,
            "unit": "iter/sec",
            "range": "stddev: 0.0010961186707602877",
            "extra": "mean: 13.124154657529356 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 80.36066148940868,
            "unit": "iter/sec",
            "range": "stddev: 0.0008967598227619721",
            "extra": "mean: 12.443899558141359 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 81.61765693786171,
            "unit": "iter/sec",
            "range": "stddev: 0.0007131639099338163",
            "extra": "mean: 12.252250769234088 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 81.92297907858942,
            "unit": "iter/sec",
            "range": "stddev: 0.0005611250521985297",
            "extra": "mean: 12.206587348840076 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 80.99076206908508,
            "unit": "iter/sec",
            "range": "stddev: 0.0011295832939852072",
            "extra": "mean: 12.347087179485984 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 84.04594925276402,
            "unit": "iter/sec",
            "range": "stddev: 0.000651981541761601",
            "extra": "mean: 11.898253382712706 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 83.03243490961276,
            "unit": "iter/sec",
            "range": "stddev: 0.0006384015471570553",
            "extra": "mean: 12.043486392860544 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 84.68038626421975,
            "unit": "iter/sec",
            "range": "stddev: 0.0009440499132536811",
            "extra": "mean: 11.809110044441695 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 82.01721412708834,
            "unit": "iter/sec",
            "range": "stddev: 0.0013466009212535054",
            "extra": "mean: 12.19256238636035 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 54.88383126481,
            "unit": "iter/sec",
            "range": "stddev: 0.0011263643606444545",
            "extra": "mean: 18.22030235416842 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 56.14669891073421,
            "unit": "iter/sec",
            "range": "stddev: 0.0011470646773354563",
            "extra": "mean: 17.81048609090745 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 54.7603298741417,
            "unit": "iter/sec",
            "range": "stddev: 0.000870881525499386",
            "extra": "mean: 18.261394741382095 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 51.795083513745496,
            "unit": "iter/sec",
            "range": "stddev: 0.0025739976087183064",
            "extra": "mean: 19.306851773578426 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 79.43805286870008,
            "unit": "iter/sec",
            "range": "stddev: 0.000732193173348225",
            "extra": "mean: 12.588425369046485 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 79.1791786807784,
            "unit": "iter/sec",
            "range": "stddev: 0.0007804627510873672",
            "extra": "mean: 12.62958288607205 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 57.87873876705684,
            "unit": "iter/sec",
            "range": "stddev: 0.0009794864464310793",
            "extra": "mean: 17.277501571426356 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 58.84669807384294,
            "unit": "iter/sec",
            "range": "stddev: 0.0007617407186060903",
            "extra": "mean: 16.993306892855134 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 52.42245834600424,
            "unit": "iter/sec",
            "range": "stddev: 0.0022832410533876577",
            "extra": "mean: 19.075793687501157 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 55.10887305783493,
            "unit": "iter/sec",
            "range": "stddev: 0.0010490450714831126",
            "extra": "mean: 18.145898192302596 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 50.21982293327087,
            "unit": "iter/sec",
            "range": "stddev: 0.0021681426842706315",
            "extra": "mean: 19.912455711537273 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 51.8756227992815,
            "unit": "iter/sec",
            "range": "stddev: 0.0009350327976172179",
            "extra": "mean: 19.276876999997203 msec\nrounds: 51"
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
          "id": "565a57122dc31559ed73bc867ec5c515b2ca58e3",
          "message": "add benchmarking in docs",
          "timestamp": "2023-05-02T23:08:00+02:00",
          "tree_id": "9ae1762afb054ccd7b6e3675eb76368c630065d3",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/565a57122dc31559ed73bc867ec5c515b2ca58e3"
        },
        "date": 1683062166910,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 55.4259156584913,
            "unit": "iter/sec",
            "range": "stddev: 0.0008058871221093398",
            "extra": "mean: 18.04210157142977 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 61.86644865245906,
            "unit": "iter/sec",
            "range": "stddev: 0.000802255265432087",
            "extra": "mean: 16.16385006383023 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 54.82772501218979,
            "unit": "iter/sec",
            "range": "stddev: 0.0008083019155132556",
            "extra": "mean: 18.238947535716118 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 60.64583216813199,
            "unit": "iter/sec",
            "range": "stddev: 0.001220868895340816",
            "extra": "mean: 16.48917929310693 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 50.12643710665063,
            "unit": "iter/sec",
            "range": "stddev: 0.001365103487645429",
            "extra": "mean: 19.9495527254883 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 56.699085236757234,
            "unit": "iter/sec",
            "range": "stddev: 0.0017790736787142425",
            "extra": "mean: 17.636968847457062 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 47.84696402146563,
            "unit": "iter/sec",
            "range": "stddev: 0.0017675938407560043",
            "extra": "mean: 20.899967645833684 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 59.00414060022055,
            "unit": "iter/sec",
            "range": "stddev: 0.0010182372815041392",
            "extra": "mean: 16.947963140001434 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 38.56154904892871,
            "unit": "iter/sec",
            "range": "stddev: 0.001573090382469437",
            "extra": "mean: 25.93256818420735 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 53.78887364523566,
            "unit": "iter/sec",
            "range": "stddev: 0.0007633394973546374",
            "extra": "mean: 18.59120543396199 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 36.79078204276946,
            "unit": "iter/sec",
            "range": "stddev: 0.0016184833359132848",
            "extra": "mean: 27.18072148717837 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 51.823060060602415,
            "unit": "iter/sec",
            "range": "stddev: 0.001568042206958979",
            "extra": "mean: 19.29642901886901 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 48.766390155138254,
            "unit": "iter/sec",
            "range": "stddev: 0.0006812927772107827",
            "extra": "mean: 20.50592625000018 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 54.93828369537987,
            "unit": "iter/sec",
            "range": "stddev: 0.00147186204631563",
            "extra": "mean: 18.20224318518521 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 39.146165945965215,
            "unit": "iter/sec",
            "range": "stddev: 0.001977773679160002",
            "extra": "mean: 25.545285875003287 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 50.95592048212863,
            "unit": "iter/sec",
            "range": "stddev: 0.0012283499663456323",
            "extra": "mean: 19.624804940001468 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 60.26973252186079,
            "unit": "iter/sec",
            "range": "stddev: 0.001710936065303929",
            "extra": "mean: 16.59207629032175 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 75.28075825481895,
            "unit": "iter/sec",
            "range": "stddev: 0.000762286531752678",
            "extra": "mean: 13.283606902777004 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 62.22227496573407,
            "unit": "iter/sec",
            "range": "stddev: 0.0007466736241526599",
            "extra": "mean: 16.07141494827539 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 78.38626260704783,
            "unit": "iter/sec",
            "range": "stddev: 0.0007150605147029336",
            "extra": "mean: 12.757337405063225 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 74.41180474197056,
            "unit": "iter/sec",
            "range": "stddev: 0.0007847246271963498",
            "extra": "mean: 13.43872794736786 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 87.73983303717205,
            "unit": "iter/sec",
            "range": "stddev: 0.0007313827730606164",
            "extra": "mean: 11.397331923076921 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 73.36627892587717,
            "unit": "iter/sec",
            "range": "stddev: 0.001218284121156245",
            "extra": "mean: 13.63024014084607 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 92.26240664549796,
            "unit": "iter/sec",
            "range": "stddev: 0.0010983978655155235",
            "extra": "mean: 10.838650717646287 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 56.213788555673005,
            "unit": "iter/sec",
            "range": "stddev: 0.0012131429967480044",
            "extra": "mean: 17.789229754717923 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 87.64541316233951,
            "unit": "iter/sec",
            "range": "stddev: 0.0012786129243470036",
            "extra": "mean: 11.409610199997227 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 56.88549849775115,
            "unit": "iter/sec",
            "range": "stddev: 0.0009529578759308429",
            "extra": "mean: 17.579172661017164 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 85.96906999319778,
            "unit": "iter/sec",
            "range": "stddev: 0.0014855837058710306",
            "extra": "mean: 11.632090472528365 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 61.487511259878985,
            "unit": "iter/sec",
            "range": "stddev: 0.0010440707072419178",
            "extra": "mean: 16.263465206348442 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 89.1894571262266,
            "unit": "iter/sec",
            "range": "stddev: 0.00054961242096124",
            "extra": "mean: 11.212087529412095 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 56.78091054694494,
            "unit": "iter/sec",
            "range": "stddev: 0.0018067181173441324",
            "extra": "mean: 17.611552727271373 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 87.55653177830258,
            "unit": "iter/sec",
            "range": "stddev: 0.0009243246862187805",
            "extra": "mean: 11.42119245348878 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 74.20417355175287,
            "unit": "iter/sec",
            "range": "stddev: 0.0005857656113092359",
            "extra": "mean: 13.476330941177602 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 84.87667582531846,
            "unit": "iter/sec",
            "range": "stddev: 0.0009056118768538991",
            "extra": "mean: 11.781799773333052 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 62.75627082597088,
            "unit": "iter/sec",
            "range": "stddev: 0.0010329241223180623",
            "extra": "mean: 15.93466257377044 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 76.75263622362323,
            "unit": "iter/sec",
            "range": "stddev: 0.0011332421633578357",
            "extra": "mean: 13.028868442856378 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 58.49072923480601,
            "unit": "iter/sec",
            "range": "stddev: 0.0015147206256687423",
            "extra": "mean: 17.09672649122882 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 79.14297101773616,
            "unit": "iter/sec",
            "range": "stddev: 0.0010330111923589351",
            "extra": "mean: 12.635360880954257 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 55.21243676304798,
            "unit": "iter/sec",
            "range": "stddev: 0.0012784549670826202",
            "extra": "mean: 18.11186135999833 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 82.75594733409979,
            "unit": "iter/sec",
            "range": "stddev: 0.00048773515972730234",
            "extra": "mean: 12.083723674418595 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 80.1544894958811,
            "unit": "iter/sec",
            "range": "stddev: 0.0013227471803281155",
            "extra": "mean: 12.475907541665363 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 88.52970884125303,
            "unit": "iter/sec",
            "range": "stddev: 0.0006943166598516864",
            "extra": "mean: 11.295643158537313 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 78.31962412025123,
            "unit": "iter/sec",
            "range": "stddev: 0.0013414910579132105",
            "extra": "mean: 12.76819202381014 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 90.4395690365187,
            "unit": "iter/sec",
            "range": "stddev: 0.0011800535731447783",
            "extra": "mean: 11.057107089886825 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 77.19998501719243,
            "unit": "iter/sec",
            "range": "stddev: 0.0008523920620250463",
            "extra": "mean: 12.953370389609532 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 85.78425434112008,
            "unit": "iter/sec",
            "range": "stddev: 0.0012335941379872665",
            "extra": "mean: 11.657150926829903 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 77.69637003265473,
            "unit": "iter/sec",
            "range": "stddev: 0.0008103755438309895",
            "extra": "mean: 12.870614155844265 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 86.67069010190654,
            "unit": "iter/sec",
            "range": "stddev: 0.0011320052832508804",
            "extra": "mean: 11.537925898873194 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 63.7733340141491,
            "unit": "iter/sec",
            "range": "stddev: 0.0009024948934191462",
            "extra": "mean: 15.68053506153739 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 75.51262846404798,
            "unit": "iter/sec",
            "range": "stddev: 0.0015833473472220297",
            "extra": "mean: 13.242818060241488 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 57.30126555867491,
            "unit": "iter/sec",
            "range": "stddev: 0.0014164221428463008",
            "extra": "mean: 17.45162153488613 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 75.5803678894013,
            "unit": "iter/sec",
            "range": "stddev: 0.0013991964747687188",
            "extra": "mean: 13.230949093332356 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 66.43274402392476,
            "unit": "iter/sec",
            "range": "stddev: 0.0019028974033336928",
            "extra": "mean: 15.052817924243275 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 76.75572672371085,
            "unit": "iter/sec",
            "range": "stddev: 0.0017287631119964084",
            "extra": "mean: 13.028343847223153 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 58.79393426400427,
            "unit": "iter/sec",
            "range": "stddev: 0.001997049685917352",
            "extra": "mean: 17.00855730303178 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 71.40424770659897,
            "unit": "iter/sec",
            "range": "stddev: 0.001590091570295034",
            "extra": "mean: 14.004769073529262 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 53.407676361037566,
            "unit": "iter/sec",
            "range": "stddev: 0.0013897712634989292",
            "extra": "mean: 18.723900160717882 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 72.7011555806766,
            "unit": "iter/sec",
            "range": "stddev: 0.0011786386443916248",
            "extra": "mean: 13.75493954687279 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 53.63796719850731,
            "unit": "iter/sec",
            "range": "stddev: 0.0013730717052064488",
            "extra": "mean: 18.643510413046172 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 68.80360238750627,
            "unit": "iter/sec",
            "range": "stddev: 0.0014167259984052309",
            "extra": "mean: 14.534122710144395 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 76.41616657957539,
            "unit": "iter/sec",
            "range": "stddev: 0.0015804871046839351",
            "extra": "mean: 13.086236129872567 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 73.40959864908179,
            "unit": "iter/sec",
            "range": "stddev: 0.0020579124920944458",
            "extra": "mean: 13.622196802631724 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 78.4688919354864,
            "unit": "iter/sec",
            "range": "stddev: 0.0018882738592627618",
            "extra": "mean: 12.743903671051646 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 77.22100035107475,
            "unit": "iter/sec",
            "range": "stddev: 0.0012277424993295978",
            "extra": "mean: 12.949845190474564 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 62.7214510682943,
            "unit": "iter/sec",
            "range": "stddev: 0.004613009217681355",
            "extra": "mean: 15.943508687500698 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 71.93642099434017,
            "unit": "iter/sec",
            "range": "stddev: 0.0026487003276177497",
            "extra": "mean: 13.901164197182931 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 57.30662026505911,
            "unit": "iter/sec",
            "range": "stddev: 0.004310229248871326",
            "extra": "mean: 17.449990862743626 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 76.11562896621666,
            "unit": "iter/sec",
            "range": "stddev: 0.0015165128272177641",
            "extra": "mean: 13.137906282609087 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 53.45918013630081,
            "unit": "iter/sec",
            "range": "stddev: 0.00080380319009729",
            "extra": "mean: 18.705861134614786 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 49.94444247451786,
            "unit": "iter/sec",
            "range": "stddev: 0.001701833746469828",
            "extra": "mean: 20.02224773077024 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 47.34894897073798,
            "unit": "iter/sec",
            "range": "stddev: 0.002024913504083873",
            "extra": "mean: 21.119792978256132 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 49.91170280374219,
            "unit": "iter/sec",
            "range": "stddev: 0.0011314736102148962",
            "extra": "mean: 20.035381360000883 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 75.41202622464311,
            "unit": "iter/sec",
            "range": "stddev: 0.001176502788894249",
            "extra": "mean: 13.260484435481462 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 77.81431857406334,
            "unit": "iter/sec",
            "range": "stddev: 0.0011054194747413422",
            "extra": "mean: 12.85110527631498 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 57.10236925645756,
            "unit": "iter/sec",
            "range": "stddev: 0.0011482743837176502",
            "extra": "mean: 17.51240820689612 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 53.98256718816035,
            "unit": "iter/sec",
            "range": "stddev: 0.0018225722644133544",
            "extra": "mean: 18.524498779660178 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 49.573894923122616,
            "unit": "iter/sec",
            "range": "stddev: 0.0017655669699440202",
            "extra": "mean: 20.17190704000086 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 48.21490903818677,
            "unit": "iter/sec",
            "range": "stddev: 0.004237513875102762",
            "extra": "mean: 20.740472603774663 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 41.12480177254948,
            "unit": "iter/sec",
            "range": "stddev: 0.0039626064078911345",
            "extra": "mean: 24.31622662963188 msec\nrounds: 27"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 45.83823716524097,
            "unit": "iter/sec",
            "range": "stddev: 0.0008476830380558006",
            "extra": "mean: 21.81584768181918 msec\nrounds: 44"
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
          "id": "30dc83cdc3154ac2820363d33f1ef6ced8cb8d25",
          "message": "fix nodata/mask/alpha forwarding for GCPS dataset (#604)",
          "timestamp": "2023-05-09T15:46:52+02:00",
          "tree_id": "b26b13ee3a93eeef539693fb858a28f76bb8b705",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/30dc83cdc3154ac2820363d33f1ef6ced8cb8d25"
        },
        "date": 1683640299175,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 48.91122639962229,
            "unit": "iter/sec",
            "range": "stddev: 0.0010854307450321383",
            "extra": "mean: 20.44520396666485 msec\nrounds: 30"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 55.40605672605749,
            "unit": "iter/sec",
            "range": "stddev: 0.0008728237901925868",
            "extra": "mean: 18.048568317075336 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 48.1628846177091,
            "unit": "iter/sec",
            "range": "stddev: 0.0013759340998717022",
            "extra": "mean: 20.762875976749697 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 52.187725675799925,
            "unit": "iter/sec",
            "range": "stddev: 0.002601869720240647",
            "extra": "mean: 19.161593785714867 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 46.102896732501634,
            "unit": "iter/sec",
            "range": "stddev: 0.0015470899549376268",
            "extra": "mean: 21.690611021736945 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 53.12503115562232,
            "unit": "iter/sec",
            "range": "stddev: 0.0013237448852133815",
            "extra": "mean: 18.823518372547216 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 46.3409579163616,
            "unit": "iter/sec",
            "range": "stddev: 0.0016923055057660992",
            "extra": "mean: 21.5791827567494 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 53.877325747217604,
            "unit": "iter/sec",
            "range": "stddev: 0.0012388959648540656",
            "extra": "mean: 18.56068366666553 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 35.68841867264321,
            "unit": "iter/sec",
            "range": "stddev: 0.002069914493874294",
            "extra": "mean: 28.020294459461308 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 47.91831823539989,
            "unit": "iter/sec",
            "range": "stddev: 0.0018097809647711614",
            "extra": "mean: 20.868845919998193 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 33.68548182821318,
            "unit": "iter/sec",
            "range": "stddev: 0.0018773333161012451",
            "extra": "mean: 29.686379583338862 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 47.555250828703755,
            "unit": "iter/sec",
            "range": "stddev: 0.0014668142787300487",
            "extra": "mean: 21.028172127659403 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 44.324345712158795,
            "unit": "iter/sec",
            "range": "stddev: 0.0017101048959896252",
            "extra": "mean: 22.5609647234045 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 50.425725914457914,
            "unit": "iter/sec",
            "range": "stddev: 0.0016824197417965672",
            "extra": "mean: 19.831147333335323 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 35.04025616001689,
            "unit": "iter/sec",
            "range": "stddev: 0.0027123955178601803",
            "extra": "mean: 28.538604153843547 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 46.6723423540953,
            "unit": "iter/sec",
            "range": "stddev: 0.001954565261073673",
            "extra": "mean: 21.4259655624988 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 55.6457486581195,
            "unit": "iter/sec",
            "range": "stddev: 0.0015413250264541358",
            "extra": "mean: 17.970824800001786 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 68.55116146812247,
            "unit": "iter/sec",
            "range": "stddev: 0.0014056663038178754",
            "extra": "mean: 14.587644885710915 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 56.36922866942659,
            "unit": "iter/sec",
            "range": "stddev: 0.001317640020869845",
            "extra": "mean: 17.740175333326455 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 69.15041659864272,
            "unit": "iter/sec",
            "range": "stddev: 0.0015124296386216185",
            "extra": "mean: 14.46122885714658 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 65.8997339617967,
            "unit": "iter/sec",
            "range": "stddev: 0.0016065327568936577",
            "extra": "mean: 15.174568088237178 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 77.5791257698644,
            "unit": "iter/sec",
            "range": "stddev: 0.0012194809457962716",
            "extra": "mean: 12.890065337504097 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 65.63770369038237,
            "unit": "iter/sec",
            "range": "stddev: 0.0014098413841783803",
            "extra": "mean: 15.235146017859945 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 78.56328234751392,
            "unit": "iter/sec",
            "range": "stddev: 0.0014710311800162294",
            "extra": "mean: 12.728592417723041 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 47.97406497768487,
            "unit": "iter/sec",
            "range": "stddev: 0.0013910572458610754",
            "extra": "mean: 20.84459593876712 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 78.45525806258999,
            "unit": "iter/sec",
            "range": "stddev: 0.0010710779605959517",
            "extra": "mean: 12.746118293336318 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 47.436916629573496,
            "unit": "iter/sec",
            "range": "stddev: 0.0016841873103328533",
            "extra": "mean: 21.080628148933524 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 76.87707074090672,
            "unit": "iter/sec",
            "range": "stddev: 0.0013611824581467708",
            "extra": "mean: 13.007779697671213 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 50.77426395172986,
            "unit": "iter/sec",
            "range": "stddev: 0.001426324036704653",
            "extra": "mean: 19.695017163630013 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 73.26329643225388,
            "unit": "iter/sec",
            "range": "stddev: 0.0014453532197522129",
            "extra": "mean: 13.64939947692217 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 49.956417678401124,
            "unit": "iter/sec",
            "range": "stddev: 0.0013110485260997113",
            "extra": "mean: 20.017448137246124 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 73.69691279232885,
            "unit": "iter/sec",
            "range": "stddev: 0.001390686088836034",
            "extra": "mean: 13.569089424653495 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 60.69616838565235,
            "unit": "iter/sec",
            "range": "stddev: 0.0016384258482780726",
            "extra": "mean: 16.475504576272147 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 70.18799684359006,
            "unit": "iter/sec",
            "range": "stddev: 0.0013943929023200023",
            "extra": "mean: 14.24745034722166 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 48.895437450303156,
            "unit": "iter/sec",
            "range": "stddev: 0.0018727508200829474",
            "extra": "mean: 20.451805979165034 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 67.40608300199264,
            "unit": "iter/sec",
            "range": "stddev: 0.001982985368064478",
            "extra": "mean: 14.835456318837549 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 46.69946460220801,
            "unit": "iter/sec",
            "range": "stddev: 0.005545361856826643",
            "extra": "mean: 21.413521729170288 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 66.89311566267739,
            "unit": "iter/sec",
            "range": "stddev: 0.0014571773705922353",
            "extra": "mean: 14.949221457148303 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 45.24488333435226,
            "unit": "iter/sec",
            "range": "stddev: 0.0013523626222317576",
            "extra": "mean: 22.101946702131247 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 63.6709275369484,
            "unit": "iter/sec",
            "range": "stddev: 0.00200918149512546",
            "extra": "mean: 15.705755180332462 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 66.55638898239877,
            "unit": "iter/sec",
            "range": "stddev: 0.0013837360856705915",
            "extra": "mean: 15.02485359090704 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 75.73958458630621,
            "unit": "iter/sec",
            "range": "stddev: 0.0013661214575286396",
            "extra": "mean: 13.203135526317647 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 69.07886812086512,
            "unit": "iter/sec",
            "range": "stddev: 0.00197776742087676",
            "extra": "mean: 14.476207083334536 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 75.3484529607661,
            "unit": "iter/sec",
            "range": "stddev: 0.0013742165554193775",
            "extra": "mean: 13.271672618423892 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 65.41376404490798,
            "unit": "iter/sec",
            "range": "stddev: 0.0013835003166947524",
            "extra": "mean: 15.287302521125037 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 72.17565692763783,
            "unit": "iter/sec",
            "range": "stddev: 0.0014249832681398362",
            "extra": "mean: 13.855086916667544 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 65.20834044743177,
            "unit": "iter/sec",
            "range": "stddev: 0.0012933966016099043",
            "extra": "mean: 15.33546158571783 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 74.63731659789907,
            "unit": "iter/sec",
            "range": "stddev: 0.0015104390866120681",
            "extra": "mean: 13.398123694443598 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 50.60869471675131,
            "unit": "iter/sec",
            "range": "stddev: 0.002152216514508855",
            "extra": "mean: 19.75945053704385 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 68.97287593372731,
            "unit": "iter/sec",
            "range": "stddev: 0.0012969943397326488",
            "extra": "mean: 14.498453000000339 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 49.99421994709116,
            "unit": "iter/sec",
            "range": "stddev: 0.0014177088269779511",
            "extra": "mean: 20.00231228846653 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 68.52991334572435,
            "unit": "iter/sec",
            "range": "stddev: 0.0013692527410281727",
            "extra": "mean: 14.592167874999815 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 66.03972714758417,
            "unit": "iter/sec",
            "range": "stddev: 0.0011826892227020753",
            "extra": "mean: 15.142400539681537 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 70.73359616286862,
            "unit": "iter/sec",
            "range": "stddev: 0.0012322598261775613",
            "extra": "mean: 14.13755350000071 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 50.419004790255975,
            "unit": "iter/sec",
            "range": "stddev: 0.0022294502213648566",
            "extra": "mean: 19.8337909318127 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 62.77048289623521,
            "unit": "iter/sec",
            "range": "stddev: 0.0020809025916391946",
            "extra": "mean: 15.931054754717795 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 48.21719812247407,
            "unit": "iter/sec",
            "range": "stddev: 0.0018697975245019372",
            "extra": "mean: 20.73948796153502 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 61.517042629182015,
            "unit": "iter/sec",
            "range": "stddev: 0.0015846206948488466",
            "extra": "mean: 16.255657900004888 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 46.247004105557075,
            "unit": "iter/sec",
            "range": "stddev: 0.0016930406950613607",
            "extra": "mean: 21.623022276589786 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 61.41917710835882,
            "unit": "iter/sec",
            "range": "stddev: 0.0015712706831240647",
            "extra": "mean: 16.281559719299878 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 66.12426948324652,
            "unit": "iter/sec",
            "range": "stddev: 0.002280722943720739",
            "extra": "mean: 15.123040417911364 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 69.99143026074897,
            "unit": "iter/sec",
            "range": "stddev: 0.000857062235179524",
            "extra": "mean: 14.287463426230305 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 67.80603531861286,
            "unit": "iter/sec",
            "range": "stddev: 0.0022825334577344348",
            "extra": "mean: 14.747949726025327 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 68.85376589234369,
            "unit": "iter/sec",
            "range": "stddev: 0.00159536776765316",
            "extra": "mean: 14.523533855265812 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 70.87280537736271,
            "unit": "iter/sec",
            "range": "stddev: 0.001048446865839221",
            "extra": "mean: 14.109784347825565 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 67.08848738400803,
            "unit": "iter/sec",
            "range": "stddev: 0.0020738761735872913",
            "extra": "mean: 14.905687085715565 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 71.0893843416877,
            "unit": "iter/sec",
            "range": "stddev: 0.001407383271981387",
            "extra": "mean: 14.066797866662455 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 70.01130073946271,
            "unit": "iter/sec",
            "range": "stddev: 0.0009768439548511383",
            "extra": "mean: 14.283408384617228 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 47.16342146815019,
            "unit": "iter/sec",
            "range": "stddev: 0.0013033911879133252",
            "extra": "mean: 21.202872244442815 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 46.950292512778056,
            "unit": "iter/sec",
            "range": "stddev: 0.0009834709513851284",
            "extra": "mean: 21.29912182608529 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 45.32934285940823,
            "unit": "iter/sec",
            "range": "stddev: 0.001473283682101435",
            "extra": "mean: 22.060765431821107 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 45.79362908719647,
            "unit": "iter/sec",
            "range": "stddev: 0.0019741722972648327",
            "extra": "mean: 21.837098739125523 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 66.67102347311526,
            "unit": "iter/sec",
            "range": "stddev: 0.0021513492380824555",
            "extra": "mean: 14.999019782608327 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 68.81005157288809,
            "unit": "iter/sec",
            "range": "stddev: 0.0010697873766138636",
            "extra": "mean: 14.532760507245586 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 48.9156842577562,
            "unit": "iter/sec",
            "range": "stddev: 0.0012649902582222653",
            "extra": "mean: 20.443340723408923 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 47.7323328002695,
            "unit": "iter/sec",
            "range": "stddev: 0.0017794438832188896",
            "extra": "mean: 20.950159804348676 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 45.099025073736215,
            "unit": "iter/sec",
            "range": "stddev: 0.001434101431954241",
            "extra": "mean: 22.17342832500293 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 43.72871890722221,
            "unit": "iter/sec",
            "range": "stddev: 0.0017715932161757124",
            "extra": "mean: 22.868266553192814 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 41.2334522748336,
            "unit": "iter/sec",
            "range": "stddev: 0.0014782259547208739",
            "extra": "mean: 24.252153162793487 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 39.983138794220146,
            "unit": "iter/sec",
            "range": "stddev: 0.0025489714947740418",
            "extra": "mean: 25.010542697677284 msec\nrounds: 43"
          }
        ]
      }
    ]
  }
}