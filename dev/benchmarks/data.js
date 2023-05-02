window.BENCHMARK_DATA = {
  "lastUpdate": 1683060953673,
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
      }
    ]
  }
}