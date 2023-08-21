window.BENCHMARK_DATA = {
  "lastUpdate": 1692618551868,
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
          "id": "b0aa6bf115f2a98d8ea2dcffc6a7ee28d189a992",
          "message": "remove boto3",
          "timestamp": "2023-05-15T18:03:49+02:00",
          "tree_id": "b0ba5f71ec646f7b942d8d34c03d71cfd83418d0",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/b0aa6bf115f2a98d8ea2dcffc6a7ee28d189a992"
        },
        "date": 1684166891954,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 66.80437846858646,
            "unit": "iter/sec",
            "range": "stddev: 0.00015040742074704433",
            "extra": "mean: 14.969078717950076 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 77.10180256781271,
            "unit": "iter/sec",
            "range": "stddev: 0.00007867078324729427",
            "extra": "mean: 12.969865381817478 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 67.51466625881153,
            "unit": "iter/sec",
            "range": "stddev: 0.0001133113880307498",
            "extra": "mean: 14.811596582090594 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 76.85194119504371,
            "unit": "iter/sec",
            "range": "stddev: 0.00008826895856752294",
            "extra": "mean: 13.012033065789254 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 62.31078576554918,
            "unit": "iter/sec",
            "range": "stddev: 0.0002859538167822985",
            "extra": "mean: 16.04858593442561 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 74.45110685042133,
            "unit": "iter/sec",
            "range": "stddev: 0.00007671313629895858",
            "extra": "mean: 13.431633756756444 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 61.93187376215828,
            "unit": "iter/sec",
            "range": "stddev: 0.00030029330799124967",
            "extra": "mean: 16.146774499999413 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 74.27854863558555,
            "unit": "iter/sec",
            "range": "stddev: 0.00011518759445769854",
            "extra": "mean: 13.462837095889586 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 45.79801437111004,
            "unit": "iter/sec",
            "range": "stddev: 0.00019124110792300818",
            "extra": "mean: 21.835007777778515 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 64.97441067302626,
            "unit": "iter/sec",
            "range": "stddev: 0.000196145355180193",
            "extra": "mean: 15.390674415384026 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 45.550462169988926,
            "unit": "iter/sec",
            "range": "stddev: 0.00023687004520748568",
            "extra": "mean: 21.953674065218447 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 65.70237574211254,
            "unit": "iter/sec",
            "range": "stddev: 0.00010937220570703539",
            "extra": "mean: 15.22014978461488 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 60.805859901787635,
            "unit": "iter/sec",
            "range": "stddev: 0.0001241797406229781",
            "extra": "mean: 16.445783377049175 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 68.93084998742181,
            "unit": "iter/sec",
            "range": "stddev: 0.000182818438994676",
            "extra": "mean: 14.507292455881155 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 48.01652708820418,
            "unit": "iter/sec",
            "range": "stddev: 0.00022574477728936614",
            "extra": "mean: 20.826162586957725 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 64.018707802873,
            "unit": "iter/sec",
            "range": "stddev: 0.00011426720498176097",
            "extra": "mean: 15.62043399999902 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 77.55341625477678,
            "unit": "iter/sec",
            "range": "stddev: 0.00008635432477607952",
            "extra": "mean: 12.894338486841406 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 96.12207757874495,
            "unit": "iter/sec",
            "range": "stddev: 0.00006442829019227926",
            "extra": "mean: 10.403437224718555 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 75.97899835938134,
            "unit": "iter/sec",
            "range": "stddev: 0.0001123971664491643",
            "extra": "mean: 13.161531760000193 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 95.68599722239851,
            "unit": "iter/sec",
            "range": "stddev: 0.00023737593286155",
            "extra": "mean: 10.450849957447238 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 91.73515942133919,
            "unit": "iter/sec",
            "range": "stddev: 0.0001371471477758474",
            "extra": "mean: 10.900945791209718 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 109.99057802377597,
            "unit": "iter/sec",
            "range": "stddev: 0.00007729551805305458",
            "extra": "mean: 9.091687833332744 msec\nrounds: 108"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 92.41900735372893,
            "unit": "iter/sec",
            "range": "stddev: 0.00003848275218797804",
            "extra": "mean: 10.820285010988616 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 110.37250918066245,
            "unit": "iter/sec",
            "range": "stddev: 0.000025423741975353273",
            "extra": "mean: 9.06022711111113 msec\nrounds: 108"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 64.88298373348209,
            "unit": "iter/sec",
            "range": "stddev: 0.00009192948672221403",
            "extra": "mean: 15.412361492308527 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 106.22581531570553,
            "unit": "iter/sec",
            "range": "stddev: 0.0002469618626745208",
            "extra": "mean: 9.413907504762165 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 64.74550123255237,
            "unit": "iter/sec",
            "range": "stddev: 0.00010454337138244119",
            "extra": "mean: 15.445088553847286 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 106.97999996060899,
            "unit": "iter/sec",
            "range": "stddev: 0.00006355342796500975",
            "extra": "mean: 9.347541600001954 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 69.81533641054094,
            "unit": "iter/sec",
            "range": "stddev: 0.00012620545000059012",
            "extra": "mean: 14.32350041428744 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 103.22426426595653,
            "unit": "iter/sec",
            "range": "stddev: 0.000039135807976900653",
            "extra": "mean: 9.687644732671648 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 68.2023752753689,
            "unit": "iter/sec",
            "range": "stddev: 0.00011153178447799866",
            "extra": "mean: 14.662245940298614 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 103.19172790915934,
            "unit": "iter/sec",
            "range": "stddev: 0.00004051256509474679",
            "extra": "mean: 9.69069924752408 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 89.03204131357005,
            "unit": "iter/sec",
            "range": "stddev: 0.00006589748247050483",
            "extra": "mean: 11.231911402300764 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 103.40608009867455,
            "unit": "iter/sec",
            "range": "stddev: 0.00005278611480991164",
            "extra": "mean: 9.670611235294452 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 71.15086474223709,
            "unit": "iter/sec",
            "range": "stddev: 0.00008615770741005071",
            "extra": "mean: 14.054642956522956 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 93.8463507806718,
            "unit": "iter/sec",
            "range": "stddev: 0.00013937581134950327",
            "extra": "mean: 10.655715344085129 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 66.22423673677766,
            "unit": "iter/sec",
            "range": "stddev: 0.0001116535782805618",
            "extra": "mean: 15.100211784617667 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 93.81998589804327,
            "unit": "iter/sec",
            "range": "stddev: 0.00009918069871501024",
            "extra": "mean: 10.658709766666638 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 62.73253019670212,
            "unit": "iter/sec",
            "range": "stddev: 0.00018411404459486828",
            "extra": "mean: 15.940692920633552 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 94.02167626795882,
            "unit": "iter/sec",
            "range": "stddev: 0.000130538548652711",
            "extra": "mean: 10.635845261363258 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 95.73008000989253,
            "unit": "iter/sec",
            "range": "stddev: 0.00004553455865879246",
            "extra": "mean: 10.446037440861453 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 107.43597834032549,
            "unit": "iter/sec",
            "range": "stddev: 0.0000430426901328348",
            "extra": "mean: 9.307868885712521 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 96.24555945498608,
            "unit": "iter/sec",
            "range": "stddev: 0.00005794230125541369",
            "extra": "mean: 10.39008974193452 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 108.34054025783762,
            "unit": "iter/sec",
            "range": "stddev: 0.00003367233352048432",
            "extra": "mean: 9.23015519047735 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 91.76482169315648,
            "unit": "iter/sec",
            "range": "stddev: 0.00005204879186561102",
            "extra": "mean: 10.897422144444452 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 106.57511013484289,
            "unit": "iter/sec",
            "range": "stddev: 0.000030302819952616176",
            "extra": "mean: 9.38305387378687 msec\nrounds: 103"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 91.79684194078952,
            "unit": "iter/sec",
            "range": "stddev: 0.00005082930894939001",
            "extra": "mean: 10.893620944443999 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 106.0553448231386,
            "unit": "iter/sec",
            "range": "stddev: 0.00007624618725626471",
            "extra": "mean: 9.42903916504758 msec\nrounds: 103"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 71.63150933168335,
            "unit": "iter/sec",
            "range": "stddev: 0.00012097232770530166",
            "extra": "mean: 13.96033685915494 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 96.99454142219487,
            "unit": "iter/sec",
            "range": "stddev: 0.00008776405776284358",
            "extra": "mean: 10.309858527473526 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 69.97485979746354,
            "unit": "iter/sec",
            "range": "stddev: 0.00007072236258709736",
            "extra": "mean: 14.290846782607606 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 94.6495554817265,
            "unit": "iter/sec",
            "range": "stddev: 0.00006597024440354727",
            "extra": "mean: 10.565289978494034 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 91.42901840685553,
            "unit": "iter/sec",
            "range": "stddev: 0.0001058028818140465",
            "extra": "mean: 10.937446528738166 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 101.93487866768267,
            "unit": "iter/sec",
            "range": "stddev: 0.00011130943611168378",
            "extra": "mean: 9.810184826531206 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 71.35738295306517,
            "unit": "iter/sec",
            "range": "stddev: 0.0002276144742052884",
            "extra": "mean: 14.013966861112928 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 87.98079423352378,
            "unit": "iter/sec",
            "range": "stddev: 0.00018561315510477196",
            "extra": "mean: 11.366116988507075 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 65.25005072237259,
            "unit": "iter/sec",
            "range": "stddev: 0.00023433943246624055",
            "extra": "mean: 15.325658584616628 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 85.95486202226161,
            "unit": "iter/sec",
            "range": "stddev: 0.00019648261517561834",
            "extra": "mean: 11.634013207315814 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 62.401313517854554,
            "unit": "iter/sec",
            "range": "stddev: 0.00022869275316878942",
            "extra": "mean: 16.02530369354926 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 85.2192229591494,
            "unit": "iter/sec",
            "range": "stddev: 0.00018108446143106567",
            "extra": "mean: 11.734441658537051 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 99.73690371637802,
            "unit": "iter/sec",
            "range": "stddev: 0.0001857578323415335",
            "extra": "mean: 10.026379030611391 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 98.67243341189636,
            "unit": "iter/sec",
            "range": "stddev: 0.0001568164555415675",
            "extra": "mean: 10.134542804124619 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 102.24369035214315,
            "unit": "iter/sec",
            "range": "stddev: 0.00011865108312604703",
            "extra": "mean: 9.780554639174747 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.5657818004202,
            "unit": "iter/sec",
            "range": "stddev: 0.00014428782004712035",
            "extra": "mean: 10.249495074467728 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 100.272727738578,
            "unit": "iter/sec",
            "range": "stddev: 0.0001957179171226544",
            "extra": "mean: 9.972801404257295 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 99.3959042236899,
            "unit": "iter/sec",
            "range": "stddev: 0.000239445216762066",
            "extra": "mean: 10.06077672727345 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 101.79177679572632,
            "unit": "iter/sec",
            "range": "stddev: 0.00011292395608341092",
            "extra": "mean: 9.823976272727608 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 100.11367591213752,
            "unit": "iter/sec",
            "range": "stddev: 0.00009296605696674118",
            "extra": "mean: 9.988645316326483 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 62.37655259447291,
            "unit": "iter/sec",
            "range": "stddev: 0.0002917188951005738",
            "extra": "mean: 16.03166507936523 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 61.68030078032085,
            "unit": "iter/sec",
            "range": "stddev: 0.00020412777508131688",
            "extra": "mean: 16.212631704919485 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 61.140311267174305,
            "unit": "iter/sec",
            "range": "stddev: 0.0001705871376208228",
            "extra": "mean: 16.35582121311331 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 61.24457039067626,
            "unit": "iter/sec",
            "range": "stddev: 0.00013813034769900764",
            "extra": "mean: 16.32797803333498 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 99.00301150422123,
            "unit": "iter/sec",
            "range": "stddev: 0.00007357420316732575",
            "extra": "mean: 10.100702845361049 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 97.07959481177845,
            "unit": "iter/sec",
            "range": "stddev: 0.0000733677147413588",
            "extra": "mean: 10.300825852629869 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 66.1693300417569,
            "unit": "iter/sec",
            "range": "stddev: 0.00008719706202291447",
            "extra": "mean: 15.112741799999167 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 64.60620297438736,
            "unit": "iter/sec",
            "range": "stddev: 0.00022999497268459793",
            "extra": "mean: 15.47838990625161 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 61.47856879113334,
            "unit": "iter/sec",
            "range": "stddev: 0.00010456757483673757",
            "extra": "mean: 16.26583083606565 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 60.187365328927406,
            "unit": "iter/sec",
            "range": "stddev: 0.00016799112324431597",
            "extra": "mean: 16.61478276271012 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 57.52080858142889,
            "unit": "iter/sec",
            "range": "stddev: 0.00030825319825886216",
            "extra": "mean: 17.38501291379376 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 57.08940417633547,
            "unit": "iter/sec",
            "range": "stddev: 0.0001493919088654968",
            "extra": "mean: 17.516385298246238 msec\nrounds: 57"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "aimee@developmentseed.org",
            "name": "Aimee Barciauskas",
            "username": "abarciauskas-bgse"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b6b077d2f8e3d30abb95b3f7874ac9253ef5df3b",
          "message": "Allow clip-box to auto expand (#608)\n\n* Allow clip-box to auto expand\r\n\r\n* Add test\r\n\r\n* Update tests/test_io_xarray.py\r\n\r\n* Fix import order\r\n\r\n* Changes from black linter\r\n\r\n* Change default to true\r\n\r\n* use auto_expand in part and update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2023-05-18T22:41:25+02:00",
          "tree_id": "8c0a394c967b1add0716be01358e4f7cff008a1a",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/b6b077d2f8e3d30abb95b3f7874ac9253ef5df3b"
        },
        "date": 1684442743526,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 57.6115336947248,
            "unit": "iter/sec",
            "range": "stddev: 0.00014252651888182246",
            "extra": "mean: 17.357635457143974 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 66.06032830520196,
            "unit": "iter/sec",
            "range": "stddev: 0.000051217907291553554",
            "extra": "mean: 15.137678326089311 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 57.867668158575974,
            "unit": "iter/sec",
            "range": "stddev: 0.00010318348142321739",
            "extra": "mean: 17.28080691379648 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 65.747249177066,
            "unit": "iter/sec",
            "range": "stddev: 0.0000668864524350148",
            "extra": "mean: 15.209761815385892 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 53.6702170868741,
            "unit": "iter/sec",
            "range": "stddev: 0.00011750693153726373",
            "extra": "mean: 18.632307716984542 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 63.251325449645215,
            "unit": "iter/sec",
            "range": "stddev: 0.00022908642368071915",
            "extra": "mean: 15.809945370964698 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 53.78048498591717,
            "unit": "iter/sec",
            "range": "stddev: 0.0000728437531829405",
            "extra": "mean: 18.594105283019623 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 63.805947599516266,
            "unit": "iter/sec",
            "range": "stddev: 0.00007847671347327387",
            "extra": "mean: 15.672520158725476 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 39.02688583237846,
            "unit": "iter/sec",
            "range": "stddev: 0.00012770245834160598",
            "extra": "mean: 25.623361400010936 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 55.37410507277231,
            "unit": "iter/sec",
            "range": "stddev: 0.000224627820335043",
            "extra": "mean: 18.05898260000421 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 39.300617022110266,
            "unit": "iter/sec",
            "range": "stddev: 0.0001448706621822203",
            "extra": "mean: 25.444893128202203 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 56.20020852204032,
            "unit": "iter/sec",
            "range": "stddev: 0.00014273054824033714",
            "extra": "mean: 17.7935282857149 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 51.99599979176562,
            "unit": "iter/sec",
            "range": "stddev: 0.00012727645506661469",
            "extra": "mean: 19.232248711531952 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 59.8663593114147,
            "unit": "iter/sec",
            "range": "stddev: 0.00007724115973985887",
            "extra": "mean: 16.70387194915543 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 40.777195321308646,
            "unit": "iter/sec",
            "range": "stddev: 0.0003836770728436204",
            "extra": "mean: 24.52351104877086 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 54.27192753913666,
            "unit": "iter/sec",
            "range": "stddev: 0.0000864443032710492",
            "extra": "mean: 18.42573214815115 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 65.25989134309313,
            "unit": "iter/sec",
            "range": "stddev: 0.00009795330989295391",
            "extra": "mean: 15.32334760937104 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 81.66016344421013,
            "unit": "iter/sec",
            "range": "stddev: 0.00009147705798737118",
            "extra": "mean: 12.24587311392287 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 64.15673027276773,
            "unit": "iter/sec",
            "range": "stddev: 0.00019246379432888357",
            "extra": "mean: 15.586829250000989 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 80.45936919345684,
            "unit": "iter/sec",
            "range": "stddev: 0.0002559939591936816",
            "extra": "mean: 12.428633358976453 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 78.65970193373086,
            "unit": "iter/sec",
            "range": "stddev: 0.00010529169673061392",
            "extra": "mean: 12.712989948048355 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 93.38500924516754,
            "unit": "iter/sec",
            "range": "stddev: 0.00009050803196544285",
            "extra": "mean: 10.708356813186779 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 78.91022115125732,
            "unit": "iter/sec",
            "range": "stddev: 0.0000798658491155001",
            "extra": "mean: 12.672629545457388 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 92.94880739055007,
            "unit": "iter/sec",
            "range": "stddev: 0.00022372848266308032",
            "extra": "mean: 10.758610336959183 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 54.99428691850105,
            "unit": "iter/sec",
            "range": "stddev: 0.00015244240144629255",
            "extra": "mean: 18.1837070000008 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 91.5463808253343,
            "unit": "iter/sec",
            "range": "stddev: 0.00009178749428514894",
            "extra": "mean: 10.923424727275105 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 55.14794257301164,
            "unit": "iter/sec",
            "range": "stddev: 0.00014512671775531626",
            "extra": "mean: 18.133042745449238 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 91.10332168508704,
            "unit": "iter/sec",
            "range": "stddev: 0.00007700327689346086",
            "extra": "mean: 10.976548181817753 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 59.71439151055355,
            "unit": "iter/sec",
            "range": "stddev: 0.00011352300064713231",
            "extra": "mean: 16.74638181355773 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 87.89422595446449,
            "unit": "iter/sec",
            "range": "stddev: 0.00015025051178453946",
            "extra": "mean: 11.377311639539002 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 56.71978463884438,
            "unit": "iter/sec",
            "range": "stddev: 0.00014312139815398592",
            "extra": "mean: 17.63053238596313 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 87.31333763055098,
            "unit": "iter/sec",
            "range": "stddev: 0.00011148530479253037",
            "extra": "mean: 11.453003941176789 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 75.42679467324197,
            "unit": "iter/sec",
            "range": "stddev: 0.00010724217042685275",
            "extra": "mean: 13.257888053338622 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 87.02083929023034,
            "unit": "iter/sec",
            "range": "stddev: 0.00011114059709768883",
            "extra": "mean: 11.491500290692647 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 59.98023751505195,
            "unit": "iter/sec",
            "range": "stddev: 0.00017719295465539",
            "extra": "mean: 16.672158054543406 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 78.71030913173223,
            "unit": "iter/sec",
            "range": "stddev: 0.00017229636018025412",
            "extra": "mean: 12.704816065788362 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 55.640194463943914,
            "unit": "iter/sec",
            "range": "stddev: 0.00021905679830379617",
            "extra": "mean: 17.972618709088486 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 79.81431384713662,
            "unit": "iter/sec",
            "range": "stddev: 0.0001908473071903304",
            "extra": "mean: 12.529080960530935 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 53.17608559433266,
            "unit": "iter/sec",
            "range": "stddev: 0.00017090056910742596",
            "extra": "mean: 18.805445884617292 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 79.1411623264763,
            "unit": "iter/sec",
            "range": "stddev: 0.0001292356887369502",
            "extra": "mean: 12.635649649353894 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 80.61822764222644,
            "unit": "iter/sec",
            "range": "stddev: 0.00013608310121461742",
            "extra": "mean: 12.404142701299193 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 90.91836829742167,
            "unit": "iter/sec",
            "range": "stddev: 0.0000792529290315608",
            "extra": "mean: 10.99887755055937 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 82.02887302513254,
            "unit": "iter/sec",
            "range": "stddev: 0.00009829115625795927",
            "extra": "mean: 12.190829437503226 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 91.89825357853442,
            "unit": "iter/sec",
            "range": "stddev: 0.00005986886270793501",
            "extra": "mean: 10.88159960673703 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 78.17372879991076,
            "unit": "iter/sec",
            "range": "stddev: 0.00010199437264561365",
            "extra": "mean: 12.7920212499975 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 90.41379266432527,
            "unit": "iter/sec",
            "range": "stddev: 0.000058430851521985716",
            "extra": "mean: 11.060259397729832 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 78.42962197269631,
            "unit": "iter/sec",
            "range": "stddev: 0.00005006837727977655",
            "extra": "mean: 12.750284584415438 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 90.39112910250631,
            "unit": "iter/sec",
            "range": "stddev: 0.000061016939218131355",
            "extra": "mean: 11.063032511364796 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 61.49069606203421,
            "unit": "iter/sec",
            "range": "stddev: 0.00008253222806513241",
            "extra": "mean: 16.26262286885094 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 83.18702353420709,
            "unit": "iter/sec",
            "range": "stddev: 0.00006486626420317549",
            "extra": "mean: 12.021105666664381 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 59.03780231808035,
            "unit": "iter/sec",
            "range": "stddev: 0.00016822788223329536",
            "extra": "mean: 16.938299881358382 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 80.62578045034826,
            "unit": "iter/sec",
            "range": "stddev: 0.00018262202441037692",
            "extra": "mean: 12.40298071428691 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 77.58628765108413,
            "unit": "iter/sec",
            "range": "stddev: 0.0001772952568030892",
            "extra": "mean: 12.888875473680779 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 87.16540884845263,
            "unit": "iter/sec",
            "range": "stddev: 0.00007155832630616873",
            "extra": "mean: 11.472440882352977 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 61.82343676534755,
            "unit": "iter/sec",
            "range": "stddev: 0.00023920914627761108",
            "extra": "mean: 16.175095599999167 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 78.87569128366968,
            "unit": "iter/sec",
            "range": "stddev: 0.00009773707909677942",
            "extra": "mean: 12.678177315791572 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 58.48553756698732,
            "unit": "iter/sec",
            "range": "stddev: 0.00020512065855976612",
            "extra": "mean: 17.09824414035067 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 77.9807165959132,
            "unit": "iter/sec",
            "range": "stddev: 0.00018350873196213137",
            "extra": "mean: 12.823683131585994 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 55.63385513312106,
            "unit": "iter/sec",
            "range": "stddev: 0.00019379047182816999",
            "extra": "mean: 17.9746666415116 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 76.97967401798428,
            "unit": "iter/sec",
            "range": "stddev: 0.00006840639390138306",
            "extra": "mean: 12.99044212328538 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 87.57014014381373,
            "unit": "iter/sec",
            "range": "stddev: 0.00004882557156774678",
            "extra": "mean: 11.419417604650752 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 86.05534958998757,
            "unit": "iter/sec",
            "range": "stddev: 0.0000561070979931679",
            "extra": "mean: 11.620428070590846 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 88.24525903007515,
            "unit": "iter/sec",
            "range": "stddev: 0.00004257072853429557",
            "extra": "mean: 11.332053540226866 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 86.52312682152905,
            "unit": "iter/sec",
            "range": "stddev: 0.000056079374181976897",
            "extra": "mean: 11.557603576471484 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 87.0456375490337,
            "unit": "iter/sec",
            "range": "stddev: 0.00008711394669107524",
            "extra": "mean: 11.488226499997657 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 85.01298602551799,
            "unit": "iter/sec",
            "range": "stddev: 0.00012258301953030313",
            "extra": "mean: 11.76290878313384 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 87.50419581345179,
            "unit": "iter/sec",
            "range": "stddev: 0.00008414930350623127",
            "extra": "mean: 11.428023430235017 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 85.72573788559964,
            "unit": "iter/sec",
            "range": "stddev: 0.00009101131087373315",
            "extra": "mean: 11.665108107141549 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 54.837470278526986,
            "unit": "iter/sec",
            "range": "stddev: 0.00011534512906188079",
            "extra": "mean: 18.235706259257835 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 53.646580298852875,
            "unit": "iter/sec",
            "range": "stddev: 0.00013161946556284747",
            "extra": "mean: 18.640517148143047 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 52.735179118198424,
            "unit": "iter/sec",
            "range": "stddev: 0.00008774898249829758",
            "extra": "mean: 18.962673811321316 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 51.84886006031048,
            "unit": "iter/sec",
            "range": "stddev: 0.00019425032478149454",
            "extra": "mean: 19.286827113205618 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 84.1353882946443,
            "unit": "iter/sec",
            "range": "stddev: 0.0000999631100149394",
            "extra": "mean: 11.88560509755983 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 82.45167898997157,
            "unit": "iter/sec",
            "range": "stddev: 0.00011211257921817727",
            "extra": "mean: 12.128315787500554 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 56.627740932812685,
            "unit": "iter/sec",
            "range": "stddev: 0.00014382678572333893",
            "extra": "mean: 17.659189357146943 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 55.70373866323826,
            "unit": "iter/sec",
            "range": "stddev: 0.00014062746511071927",
            "extra": "mean: 17.952116392861633 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 51.85112592870725,
            "unit": "iter/sec",
            "range": "stddev: 0.00022948474584283846",
            "extra": "mean: 19.28598428845983 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 51.35170882944441,
            "unit": "iter/sec",
            "range": "stddev: 0.0001063662650372903",
            "extra": "mean: 19.473548647062994 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 49.2717453034838,
            "unit": "iter/sec",
            "range": "stddev: 0.00018684227846773184",
            "extra": "mean: 20.295607428570108 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 48.60961429185533,
            "unit": "iter/sec",
            "range": "stddev: 0.000194809049627949",
            "extra": "mean: 20.57206202040473 msec\nrounds: 49"
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
          "id": "ed16b7e9d4b46775616e0bbb34a29dd9c6302254",
          "message": "allow morecantile 4.0 (#606)\n\n* allow morecantile 4.0\r\n\r\n* set morecantile min version to 4.0",
          "timestamp": "2023-05-22T18:10:21+02:00",
          "tree_id": "572a7216ae3d8da038e78a7a25d7e69f48b21ff9",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ed16b7e9d4b46775616e0bbb34a29dd9c6302254"
        },
        "date": 1684772060504,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 55.14192198121428,
            "unit": "iter/sec",
            "range": "stddev: 0.0005421686897164882",
            "extra": "mean: 18.13502257575787 msec\nrounds: 33"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 63.2394730822201,
            "unit": "iter/sec",
            "range": "stddev: 0.0002857261453580359",
            "extra": "mean: 15.812908477271167 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 56.376802314319775,
            "unit": "iter/sec",
            "range": "stddev: 0.0003196678796751241",
            "extra": "mean: 17.7377921228072 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 63.82729871411797,
            "unit": "iter/sec",
            "range": "stddev: 0.00031424649833572117",
            "extra": "mean: 15.66727748387086 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 51.92978163979534,
            "unit": "iter/sec",
            "range": "stddev: 0.0003007944119482896",
            "extra": "mean: 19.25677267307572 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 60.6860422351713,
            "unit": "iter/sec",
            "range": "stddev: 0.0003058657158523426",
            "extra": "mean: 16.478253699998884 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 52.300993104430574,
            "unit": "iter/sec",
            "range": "stddev: 0.0005933215830643731",
            "extra": "mean: 19.120095826923926 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 61.511485187694404,
            "unit": "iter/sec",
            "range": "stddev: 0.00035440366665767653",
            "extra": "mean: 16.25712656666683 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 37.863138762731865,
            "unit": "iter/sec",
            "range": "stddev: 0.0003160158861136775",
            "extra": "mean: 26.410911315791004 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 54.039043710727896,
            "unit": "iter/sec",
            "range": "stddev: 0.0003809407497318657",
            "extra": "mean: 18.505138716980642 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 37.956017970747375,
            "unit": "iter/sec",
            "range": "stddev: 0.0005206067716586083",
            "extra": "mean: 26.346283236842652 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 54.70247313214104,
            "unit": "iter/sec",
            "range": "stddev: 0.0003906424777340186",
            "extra": "mean: 18.280709129628715 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 50.76509898064197,
            "unit": "iter/sec",
            "range": "stddev: 0.0003427003023024935",
            "extra": "mean: 19.69857284000028 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 58.152047475231576,
            "unit": "iter/sec",
            "range": "stddev: 0.00035219906376126654",
            "extra": "mean: 17.19629907142866 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 39.989275171057905,
            "unit": "iter/sec",
            "range": "stddev: 0.00045838624299163037",
            "extra": "mean: 25.00670481578887 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 52.442228547660605,
            "unit": "iter/sec",
            "range": "stddev: 0.0004754612858174071",
            "extra": "mean: 19.0686023018869 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 63.028103328549946,
            "unit": "iter/sec",
            "range": "stddev: 0.0004745231262190382",
            "extra": "mean: 15.865938322580433 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 77.91140701387322,
            "unit": "iter/sec",
            "range": "stddev: 0.00023512262010211683",
            "extra": "mean: 12.835091013334363 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 62.80177067485809,
            "unit": "iter/sec",
            "range": "stddev: 0.0003890552652815869",
            "extra": "mean: 15.923117919354103 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 79.28575808213374,
            "unit": "iter/sec",
            "range": "stddev: 0.00037298905652287124",
            "extra": "mean: 12.612605645569783 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 76.6032529849899,
            "unit": "iter/sec",
            "range": "stddev: 0.0003055264651583092",
            "extra": "mean: 13.054275909091565 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 90.91759279655427,
            "unit": "iter/sec",
            "range": "stddev: 0.0003367354190155066",
            "extra": "mean: 10.998971367815399 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 77.64354452754614,
            "unit": "iter/sec",
            "range": "stddev: 0.0002996063424399672",
            "extra": "mean: 12.879370797468203 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 92.76553140257208,
            "unit": "iter/sec",
            "range": "stddev: 0.00028368503922898567",
            "extra": "mean: 10.779866022222489 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 53.786384370555865,
            "unit": "iter/sec",
            "range": "stddev: 0.0003896626030767091",
            "extra": "mean: 18.592065849055793 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 91.82248435322761,
            "unit": "iter/sec",
            "range": "stddev: 0.0003534013624607848",
            "extra": "mean: 10.890578784093304 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 52.98147190244671,
            "unit": "iter/sec",
            "range": "stddev: 0.0006102852187801685",
            "extra": "mean: 18.874522811319245 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 88.74400083159932,
            "unit": "iter/sec",
            "range": "stddev: 0.00030583039519404285",
            "extra": "mean: 11.268367333332208 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 57.55169469211892,
            "unit": "iter/sec",
            "range": "stddev: 0.00034500979206016097",
            "extra": "mean: 17.375682946430057 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 88.05284658468585,
            "unit": "iter/sec",
            "range": "stddev: 0.0003097733975023928",
            "extra": "mean: 11.356816261905152 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 57.01676106590285,
            "unit": "iter/sec",
            "range": "stddev: 0.000511284840330625",
            "extra": "mean: 17.538702327270915 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 86.22627974574442,
            "unit": "iter/sec",
            "range": "stddev: 0.000301790885873958",
            "extra": "mean: 11.597392383722244 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 72.55206781388186,
            "unit": "iter/sec",
            "range": "stddev: 0.00025127685150598696",
            "extra": "mean: 13.783204671234241 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 86.03834096067065,
            "unit": "iter/sec",
            "range": "stddev: 0.000294924147207034",
            "extra": "mean: 11.622725273806875 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 57.74169319511341,
            "unit": "iter/sec",
            "range": "stddev: 0.00037610518555821214",
            "extra": "mean: 17.318508423729917 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 77.6061975171004,
            "unit": "iter/sec",
            "range": "stddev: 0.0003154290596334845",
            "extra": "mean: 12.885568833335142 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 54.465457936474905,
            "unit": "iter/sec",
            "range": "stddev: 0.00039412899352442955",
            "extra": "mean: 18.36026057407499 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 78.89904758997241,
            "unit": "iter/sec",
            "range": "stddev: 0.00043851806923384163",
            "extra": "mean: 12.674424223684722 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 50.875471265467255,
            "unit": "iter/sec",
            "range": "stddev: 0.0005288529451673214",
            "extra": "mean: 19.655837580000366 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 77.66991413999331,
            "unit": "iter/sec",
            "range": "stddev: 0.0003171112935151161",
            "extra": "mean: 12.874998138887939 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 79.49320493793599,
            "unit": "iter/sec",
            "range": "stddev: 0.00020560289131274913",
            "extra": "mean: 12.57969156962216 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 89.85479590359674,
            "unit": "iter/sec",
            "range": "stddev: 0.00023992291592447821",
            "extra": "mean: 11.129066511629254 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 80.05537385050906,
            "unit": "iter/sec",
            "range": "stddev: 0.0001722667791518689",
            "extra": "mean: 12.49135382051109 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 89.35361871844543,
            "unit": "iter/sec",
            "range": "stddev: 0.00019152728954833354",
            "extra": "mean: 11.191488541174976 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 77.16102719332893,
            "unit": "iter/sec",
            "range": "stddev: 0.00023837145137011872",
            "extra": "mean: 12.95991041558421 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 88.57193657120942,
            "unit": "iter/sec",
            "range": "stddev: 0.00021148482993797377",
            "extra": "mean: 11.29025782558144 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 77.07099616364263,
            "unit": "iter/sec",
            "range": "stddev: 0.00031642684298282533",
            "extra": "mean: 12.975049626667971 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 89.66818868600829,
            "unit": "iter/sec",
            "range": "stddev: 0.0002732811428136332",
            "extra": "mean: 11.152227056818408 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 60.67003841234762,
            "unit": "iter/sec",
            "range": "stddev: 0.0004148217334674348",
            "extra": "mean: 16.48260040983391 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 80.40027154589018,
            "unit": "iter/sec",
            "range": "stddev: 0.00019210806103380258",
            "extra": "mean: 12.437768937499527 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 57.5087695792021,
            "unit": "iter/sec",
            "range": "stddev: 0.00040967178375741353",
            "extra": "mean: 17.38865232758601 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 78.37105973862339,
            "unit": "iter/sec",
            "range": "stddev: 0.00022701301618286793",
            "extra": "mean: 12.75981214666634 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 76.1241293384998,
            "unit": "iter/sec",
            "range": "stddev: 0.00023591282845228845",
            "extra": "mean: 13.136439243243332 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 84.35665322195653,
            "unit": "iter/sec",
            "range": "stddev: 0.0003189152470322078",
            "extra": "mean: 11.854429518070518 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 59.499058184279846,
            "unit": "iter/sec",
            "range": "stddev: 0.00034181855105023596",
            "extra": "mean: 16.806988724137625 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 75.71150952099863,
            "unit": "iter/sec",
            "range": "stddev: 0.00042033501363638296",
            "extra": "mean: 13.20803146478871 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 56.0500831747553,
            "unit": "iter/sec",
            "range": "stddev: 0.0004063474330628595",
            "extra": "mean: 17.841186727273143 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 75.4592610190512,
            "unit": "iter/sec",
            "range": "stddev: 0.00035852581467325095",
            "extra": "mean: 13.252183847222277 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 53.90889907884685,
            "unit": "iter/sec",
            "range": "stddev: 0.00042987961269364607",
            "extra": "mean: 18.5498130566051 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 72.46553767141273,
            "unit": "iter/sec",
            "range": "stddev: 0.00044043104717951423",
            "extra": "mean: 13.79966301408531 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 85.94556348874227,
            "unit": "iter/sec",
            "range": "stddev: 0.00024825774079319127",
            "extra": "mean: 11.635271902440744 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 83.89969824634083,
            "unit": "iter/sec",
            "range": "stddev: 0.0002639502638677367",
            "extra": "mean: 11.918994000000632 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 86.18874955883499,
            "unit": "iter/sec",
            "range": "stddev: 0.00021929594962321743",
            "extra": "mean: 11.602442373495284 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 85.03364704883391,
            "unit": "iter/sec",
            "range": "stddev: 0.0002364721936785883",
            "extra": "mean: 11.760050694117714 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 86.1128119170159,
            "unit": "iter/sec",
            "range": "stddev: 0.00020636962504118605",
            "extra": "mean: 11.612673860466515 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 84.78653817647519,
            "unit": "iter/sec",
            "range": "stddev: 0.00023468214025008477",
            "extra": "mean: 11.794325154762118 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 84.94016371293453,
            "unit": "iter/sec",
            "range": "stddev: 0.000293050283327855",
            "extra": "mean: 11.772993555553057 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 83.97177147993172,
            "unit": "iter/sec",
            "range": "stddev: 0.00020520785336999183",
            "extra": "mean: 11.908763890243621 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 52.51060752897829,
            "unit": "iter/sec",
            "range": "stddev: 0.00035332470476234453",
            "extra": "mean: 19.043771288460984 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 52.18716604921487,
            "unit": "iter/sec",
            "range": "stddev: 0.0003609182952652022",
            "extra": "mean: 19.16179926415154 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 50.58003186523046,
            "unit": "iter/sec",
            "range": "stddev: 0.00032219289032377153",
            "extra": "mean: 19.77064788461346 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 50.65019468563437,
            "unit": "iter/sec",
            "range": "stddev: 0.0004638762348072504",
            "extra": "mean: 19.743260735849145 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 81.21298824951333,
            "unit": "iter/sec",
            "range": "stddev: 0.0002988275973568623",
            "extra": "mean: 12.313301376470315 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 79.84473106560274,
            "unit": "iter/sec",
            "range": "stddev: 0.00025578888258131956",
            "extra": "mean: 12.524307949367016 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 54.360218914765554,
            "unit": "iter/sec",
            "range": "stddev: 0.00032674540810734537",
            "extra": "mean: 18.395805240739673 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 53.339815819931104,
            "unit": "iter/sec",
            "range": "stddev: 0.0004369135716022066",
            "extra": "mean: 18.747721277776463 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 49.828957267841346,
            "unit": "iter/sec",
            "range": "stddev: 0.0003267002929774988",
            "extra": "mean: 20.068651941175194 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 48.7704498649318,
            "unit": "iter/sec",
            "range": "stddev: 0.00043735001007332757",
            "extra": "mean: 20.504219312503125 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 47.580363144766196,
            "unit": "iter/sec",
            "range": "stddev: 0.00039448433148456756",
            "extra": "mean: 21.0170737234064 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 47.04420352849027,
            "unit": "iter/sec",
            "range": "stddev: 0.0004995175476633107",
            "extra": "mean: 21.256603895831578 msec\nrounds: 48"
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
          "id": "d0f9d11894f3b8a5d2e02fc637393873ddce0a57",
          "message": "update changelog",
          "timestamp": "2023-05-25T14:37:58+02:00",
          "tree_id": "ce4e3e17a3ac938e29ade853feb8b79800581cfb",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/d0f9d11894f3b8a5d2e02fc637393873ddce0a57"
        },
        "date": 1685018541611,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 48.19697780946427,
            "unit": "iter/sec",
            "range": "stddev: 0.0009446311564500916",
            "extra": "mean: 20.748188900002635 msec\nrounds: 30"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 54.488475330637954,
            "unit": "iter/sec",
            "range": "stddev: 0.0009511880176281447",
            "extra": "mean: 18.352504707315912 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 48.91235781011713,
            "unit": "iter/sec",
            "range": "stddev: 0.001271445480065383",
            "extra": "mean: 20.444731040815988 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 53.85216742449439,
            "unit": "iter/sec",
            "range": "stddev: 0.0013271240248878826",
            "extra": "mean: 18.569354732139434 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 43.478355747798254,
            "unit": "iter/sec",
            "range": "stddev: 0.0020626973174860215",
            "extra": "mean: 22.999949809524253 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 52.81466778812342,
            "unit": "iter/sec",
            "range": "stddev: 0.001460109199845849",
            "extra": "mean: 18.9341340555563 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 45.36560977423548,
            "unit": "iter/sec",
            "range": "stddev: 0.0009057830363155526",
            "extra": "mean: 22.043129255322622 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 51.924234935366115,
            "unit": "iter/sec",
            "range": "stddev: 0.001208332820723331",
            "extra": "mean: 19.258829740000465 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 33.88446106960419,
            "unit": "iter/sec",
            "range": "stddev: 0.001768426425910406",
            "extra": "mean: 29.5120526764713 msec\nrounds: 34"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 47.05116442427046,
            "unit": "iter/sec",
            "range": "stddev: 0.0014421650478917776",
            "extra": "mean: 21.2534591276591 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 34.06823141781558,
            "unit": "iter/sec",
            "range": "stddev: 0.001245352223057219",
            "extra": "mean: 29.352859199995386 msec\nrounds: 30"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 47.851599995429176,
            "unit": "iter/sec",
            "range": "stddev: 0.0008263919607597919",
            "extra": "mean: 20.89794280850632 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 43.58471248561927,
            "unit": "iter/sec",
            "range": "stddev: 0.0014449803352580295",
            "extra": "mean: 22.943824634152374 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 50.12713873880555,
            "unit": "iter/sec",
            "range": "stddev: 0.0013969794068308284",
            "extra": "mean: 19.949273490566448 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 35.52708267628302,
            "unit": "iter/sec",
            "range": "stddev: 0.001182179575230051",
            "extra": "mean: 28.14754054285394 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 46.42289309860311,
            "unit": "iter/sec",
            "range": "stddev: 0.0013107136313026489",
            "extra": "mean: 21.541096068183016 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 55.296102091653246,
            "unit": "iter/sec",
            "range": "stddev: 0.0007902025633786468",
            "extra": "mean: 18.084457351849156 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 70.05718001495612,
            "unit": "iter/sec",
            "range": "stddev: 0.0010616630627280467",
            "extra": "mean: 14.274054419354526 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 55.984739324086014,
            "unit": "iter/sec",
            "range": "stddev: 0.0009736406277139561",
            "extra": "mean: 17.862010470588643 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 69.45877486468139,
            "unit": "iter/sec",
            "range": "stddev: 0.0012941327163370853",
            "extra": "mean: 14.397029057137647 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 65.25453400724818,
            "unit": "iter/sec",
            "range": "stddev: 0.001055558559515458",
            "extra": "mean: 15.324605641792257 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 79.09103405285182,
            "unit": "iter/sec",
            "range": "stddev: 0.0006857749847596928",
            "extra": "mean: 12.643658184210357 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 62.386120845201425,
            "unit": "iter/sec",
            "range": "stddev: 0.0010310931367317523",
            "extra": "mean: 16.02920627941106 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 77.18099683075573,
            "unit": "iter/sec",
            "range": "stddev: 0.0005736247124339153",
            "extra": "mean: 12.956557197529115 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 45.26080008496241,
            "unit": "iter/sec",
            "range": "stddev: 0.0013325646920805112",
            "extra": "mean: 22.094174166670182 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 72.33179941371957,
            "unit": "iter/sec",
            "range": "stddev: 0.001041493113773478",
            "extra": "mean: 13.82517797297221 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 44.62169443117398,
            "unit": "iter/sec",
            "range": "stddev: 0.001807578783046196",
            "extra": "mean: 22.410623638294016 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 73.8167802943853,
            "unit": "iter/sec",
            "range": "stddev: 0.0009569018836453747",
            "extra": "mean: 13.547055236112252 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 48.26512001077768,
            "unit": "iter/sec",
            "range": "stddev: 0.0012706008726144416",
            "extra": "mean: 20.718895959995507 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 68.20190040852741,
            "unit": "iter/sec",
            "range": "stddev: 0.0020497589097482486",
            "extra": "mean: 14.662348028574407 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 47.159836477738786,
            "unit": "iter/sec",
            "range": "stddev: 0.001181251806544957",
            "extra": "mean: 21.20448404167045 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 68.45467642513174,
            "unit": "iter/sec",
            "range": "stddev: 0.0010076314093887518",
            "extra": "mean: 14.608205782605532 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 58.98302856469964,
            "unit": "iter/sec",
            "range": "stddev: 0.001062150189948556",
            "extra": "mean: 16.954029393439512 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 68.4069765682007,
            "unit": "iter/sec",
            "range": "stddev: 0.0021318252044227885",
            "extra": "mean: 14.618392014490151 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 49.10811738831833,
            "unit": "iter/sec",
            "range": "stddev: 0.0013647873890186833",
            "extra": "mean: 20.36323225532316 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 62.913481130050585,
            "unit": "iter/sec",
            "range": "stddev: 0.0014115729506211105",
            "extra": "mean: 15.894844507695675 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 42.87617611673058,
            "unit": "iter/sec",
            "range": "stddev: 0.0012954045755181717",
            "extra": "mean: 23.32297538095504 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 62.68947684477845,
            "unit": "iter/sec",
            "range": "stddev: 0.0011347820898013486",
            "extra": "mean: 15.95164053571604 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 45.78014682111202,
            "unit": "iter/sec",
            "range": "stddev: 0.001237155743912811",
            "extra": "mean: 21.843529770831555 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 63.26724442819985,
            "unit": "iter/sec",
            "range": "stddev: 0.0013465319727421871",
            "extra": "mean: 15.80596735384723 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 69.05180162579978,
            "unit": "iter/sec",
            "range": "stddev: 0.0007651184012244599",
            "extra": "mean: 14.481881376812197 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 76.7805575941371,
            "unit": "iter/sec",
            "range": "stddev: 0.0010352251894629474",
            "extra": "mean: 13.024130474357994 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 68.11571289908967,
            "unit": "iter/sec",
            "range": "stddev: 0.001093079139424759",
            "extra": "mean: 14.680900447763857 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 76.73580079354102,
            "unit": "iter/sec",
            "range": "stddev: 0.0010866120539878477",
            "extra": "mean: 13.03172690789423 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 62.938320254420795,
            "unit": "iter/sec",
            "range": "stddev: 0.0008460781505723425",
            "extra": "mean: 15.888571476925614 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 72.62782549428348,
            "unit": "iter/sec",
            "range": "stddev: 0.0006989761991842042",
            "extra": "mean: 13.768827487182715 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 63.80528831117924,
            "unit": "iter/sec",
            "range": "stddev: 0.0008996368692779004",
            "extra": "mean: 15.672682100000657 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 72.89847452603553,
            "unit": "iter/sec",
            "range": "stddev: 0.0014694639063745117",
            "extra": "mean: 13.717708175674543 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 51.06302798905039,
            "unit": "iter/sec",
            "range": "stddev: 0.0014305090668026408",
            "extra": "mean: 19.583640833333135 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 68.44126249975768,
            "unit": "iter/sec",
            "range": "stddev: 0.000987576596642555",
            "extra": "mean: 14.611068870968598 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 50.3701834303568,
            "unit": "iter/sec",
            "range": "stddev: 0.001972658141332711",
            "extra": "mean: 19.853014857145148 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 68.59094500437597,
            "unit": "iter/sec",
            "range": "stddev: 0.000736925024856129",
            "extra": "mean: 14.579183884056444 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 63.31135581449027,
            "unit": "iter/sec",
            "range": "stddev: 0.0010143789191966572",
            "extra": "mean: 15.794954746035101 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 67.88644973965778,
            "unit": "iter/sec",
            "range": "stddev: 0.0013518491247131303",
            "extra": "mean: 14.730480144932692 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 51.94007928473958,
            "unit": "iter/sec",
            "range": "stddev: 0.0009827888282880363",
            "extra": "mean: 19.25295482353659 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 62.80407269795206,
            "unit": "iter/sec",
            "range": "stddev: 0.0015514306370042216",
            "extra": "mean: 15.922534272727326 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 44.390231483773626,
            "unit": "iter/sec",
            "range": "stddev: 0.002387522114351991",
            "extra": "mean: 22.527478829785768 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 63.38822630206401,
            "unit": "iter/sec",
            "range": "stddev: 0.001245961286554191",
            "extra": "mean: 15.77580030768961 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 48.852594752797565,
            "unit": "iter/sec",
            "range": "stddev: 0.0012518110063961037",
            "extra": "mean: 20.469741782604792 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 62.273614140251624,
            "unit": "iter/sec",
            "range": "stddev: 0.0014143931372659958",
            "extra": "mean: 16.05816546551829 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 67.36931380740798,
            "unit": "iter/sec",
            "range": "stddev: 0.0014125988418403933",
            "extra": "mean: 14.843553295774244 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 68.10000157962475,
            "unit": "iter/sec",
            "range": "stddev: 0.0009290035973871225",
            "extra": "mean: 14.684287471429311 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 68.85160856146291,
            "unit": "iter/sec",
            "range": "stddev: 0.0014412775535835559",
            "extra": "mean: 14.523988921875564 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 65.96771697106516,
            "unit": "iter/sec",
            "range": "stddev: 0.0013715785478970032",
            "extra": "mean: 15.15892994202939 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 69.29387956628925,
            "unit": "iter/sec",
            "range": "stddev: 0.0012747815173571038",
            "extra": "mean: 14.43128897182558 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 68.35469657492632,
            "unit": "iter/sec",
            "range": "stddev: 0.001494976406245592",
            "extra": "mean: 14.629572657145218 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 70.25245905862512,
            "unit": "iter/sec",
            "range": "stddev: 0.0009149770592741334",
            "extra": "mean: 14.234377179103552 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 70.9944426970153,
            "unit": "iter/sec",
            "range": "stddev: 0.0010890305823747944",
            "extra": "mean: 14.085609549295627 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 45.067857882621595,
            "unit": "iter/sec",
            "range": "stddev: 0.0013744210478653755",
            "extra": "mean: 22.188762612247547 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 43.615964141945035,
            "unit": "iter/sec",
            "range": "stddev: 0.0017224485756769622",
            "extra": "mean: 22.92738495349023 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 43.16937562240947,
            "unit": "iter/sec",
            "range": "stddev: 0.0009988452195184268",
            "extra": "mean: 23.164569456522187 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 43.30987290242774,
            "unit": "iter/sec",
            "range": "stddev: 0.0013506150571834898",
            "extra": "mean: 23.089423565220038 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 66.36790924678633,
            "unit": "iter/sec",
            "range": "stddev: 0.0011522582108542288",
            "extra": "mean: 15.067523014496983 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 67.85369000286205,
            "unit": "iter/sec",
            "range": "stddev: 0.0007549489900257676",
            "extra": "mean: 14.737592015376322 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 47.651540346097725,
            "unit": "iter/sec",
            "range": "stddev: 0.0011162989346695784",
            "extra": "mean: 20.985680478257443 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 47.204045339283205,
            "unit": "iter/sec",
            "range": "stddev: 0.0012470469050749188",
            "extra": "mean: 21.184625021275455 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 41.13414540767382,
            "unit": "iter/sec",
            "range": "stddev: 0.0012168583274651892",
            "extra": "mean: 24.3107031904799 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 39.751662726001534,
            "unit": "iter/sec",
            "range": "stddev: 0.0012766656541735898",
            "extra": "mean: 25.156180431816274 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 42.47447527780784,
            "unit": "iter/sec",
            "range": "stddev: 0.001791550233973427",
            "extra": "mean: 23.54355159091235 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 42.196356409840426,
            "unit": "iter/sec",
            "range": "stddev: 0.0015216059775998534",
            "extra": "mean: 23.698728636361466 msec\nrounds: 44"
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
          "id": "0a74d6f422a4de036a43cb875a46c638ace6f068",
          "message": "forward statistics from STAC raster:bands (#611)\n\n* forward statistics from STAC raster:bands\r\n\r\n* forward tags as metadata and forward metadata when creating ImageData from list\r\n\r\n* update changelog",
          "timestamp": "2023-05-26T20:43:39+02:00",
          "tree_id": "f19440645bc75f5409b8e3d44b81dc09e7368d4e",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/0a74d6f422a4de036a43cb875a46c638ace6f068"
        },
        "date": 1685126856635,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 57.11043268304582,
            "unit": "iter/sec",
            "range": "stddev: 0.0006467777886158778",
            "extra": "mean: 17.50993562857153 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 69.37357423374618,
            "unit": "iter/sec",
            "range": "stddev: 0.00042392550432014615",
            "extra": "mean: 14.41471065957502 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 56.83484112733396,
            "unit": "iter/sec",
            "range": "stddev: 0.0007562431530080401",
            "extra": "mean: 17.594841124999 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 66.53947601466953,
            "unit": "iter/sec",
            "range": "stddev: 0.0006206725612338214",
            "extra": "mean: 15.028672599999682 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 54.76844836571591,
            "unit": "iter/sec",
            "range": "stddev: 0.0007251853492082735",
            "extra": "mean: 18.258687799999507 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 62.984969329903016,
            "unit": "iter/sec",
            "range": "stddev: 0.0005648808626380704",
            "extra": "mean: 15.87680379365106 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 53.42030186409253,
            "unit": "iter/sec",
            "range": "stddev: 0.0005234315247939539",
            "extra": "mean: 18.719474901959863 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 67.94206117613815,
            "unit": "iter/sec",
            "range": "stddev: 0.000646532860341781",
            "extra": "mean: 14.718423060606362 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 40.859559597805735,
            "unit": "iter/sec",
            "range": "stddev: 0.0014342503117389812",
            "extra": "mean: 24.474076809523485 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 57.039191343174515,
            "unit": "iter/sec",
            "range": "stddev: 0.0009523616047695735",
            "extra": "mean: 17.53180535087763 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 37.701625303276316,
            "unit": "iter/sec",
            "range": "stddev: 0.0004671628829872181",
            "extra": "mean: 26.524055447368173 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 55.170596692759844,
            "unit": "iter/sec",
            "range": "stddev: 0.0003295460989461134",
            "extra": "mean: 18.125596965516092 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 49.465719751460206,
            "unit": "iter/sec",
            "range": "stddev: 0.00048249955808429574",
            "extra": "mean: 20.216020408163182 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 57.5199549796534,
            "unit": "iter/sec",
            "range": "stddev: 0.0006246443450557599",
            "extra": "mean: 17.385270909091137 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 42.17029770766368,
            "unit": "iter/sec",
            "range": "stddev: 0.0008304075573442626",
            "extra": "mean: 23.713373022222424 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 58.21966707078909,
            "unit": "iter/sec",
            "range": "stddev: 0.0006604074557723645",
            "extra": "mean: 17.17632632258277 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 68.57842286144822,
            "unit": "iter/sec",
            "range": "stddev: 0.0007893627299522196",
            "extra": "mean: 14.581845984127408 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 83.13942010751852,
            "unit": "iter/sec",
            "range": "stddev: 0.00036023221739463234",
            "extra": "mean: 12.027988632910459 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 68.96842921875056,
            "unit": "iter/sec",
            "range": "stddev: 0.0006849216531159656",
            "extra": "mean: 14.499387782607762 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 86.88634219313708,
            "unit": "iter/sec",
            "range": "stddev: 0.00046593052128902543",
            "extra": "mean: 11.509288741573787 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 76.90602547686414,
            "unit": "iter/sec",
            "range": "stddev: 0.0006834803882684681",
            "extra": "mean: 13.002882333333332 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 97.3866279125264,
            "unit": "iter/sec",
            "range": "stddev: 0.000428090582854353",
            "extra": "mean: 10.268350197916387 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 73.692184649646,
            "unit": "iter/sec",
            "range": "stddev: 0.0006198807971149373",
            "extra": "mean: 13.56996002702715 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 88.837470169611,
            "unit": "iter/sec",
            "range": "stddev: 0.0004149274840841871",
            "extra": "mean: 11.25651144827483 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 53.01625918235509,
            "unit": "iter/sec",
            "range": "stddev: 0.000432957685845354",
            "extra": "mean: 18.862138057692697 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 92.64001981839733,
            "unit": "iter/sec",
            "range": "stddev: 0.0003177500634996455",
            "extra": "mean: 10.794470920454298 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 53.0598079012098,
            "unit": "iter/sec",
            "range": "stddev: 0.00044558882748849576",
            "extra": "mean: 18.84665700000017 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 92.45231597355374,
            "unit": "iter/sec",
            "range": "stddev: 0.0004415015266000703",
            "extra": "mean: 10.816386690475692 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 56.92625164251124,
            "unit": "iter/sec",
            "range": "stddev: 0.0006218157147922918",
            "extra": "mean: 17.566587842105918 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 83.06812028930355,
            "unit": "iter/sec",
            "range": "stddev: 0.0005815568303303287",
            "extra": "mean: 12.038312610388598 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 53.594363875363314,
            "unit": "iter/sec",
            "range": "stddev: 0.0004673187065399153",
            "extra": "mean: 18.658678407407837 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 83.97472615776641,
            "unit": "iter/sec",
            "range": "stddev: 0.00043193308472080005",
            "extra": "mean: 11.908344876543726 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 72.90177939295977,
            "unit": "iter/sec",
            "range": "stddev: 0.0006950007144266313",
            "extra": "mean: 13.717086308822957 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 87.05549105244414,
            "unit": "iter/sec",
            "range": "stddev: 0.0004238679992674568",
            "extra": "mean: 11.486926188235248 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 58.53855301022959,
            "unit": "iter/sec",
            "range": "stddev: 0.0008677683842209505",
            "extra": "mean: 17.082759114753834 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 82.21002666163237,
            "unit": "iter/sec",
            "range": "stddev: 0.0006740080696307677",
            "extra": "mean: 12.163966375000612 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 54.19770515947608,
            "unit": "iter/sec",
            "range": "stddev: 0.0007171194614654458",
            "extra": "mean: 18.450965719997043 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 82.21405665241629,
            "unit": "iter/sec",
            "range": "stddev: 0.0005394691627393539",
            "extra": "mean: 12.163370118418912 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 57.093437006546424,
            "unit": "iter/sec",
            "range": "stddev: 0.0007695758907079618",
            "extra": "mean: 17.515148017544266 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 79.90736633001136,
            "unit": "iter/sec",
            "range": "stddev: 0.00035287744904738264",
            "extra": "mean: 12.514490790124105 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 76.9214587291935,
            "unit": "iter/sec",
            "range": "stddev: 0.000389905812984183",
            "extra": "mean: 13.000273480519377 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 93.53702415873647,
            "unit": "iter/sec",
            "range": "stddev: 0.0004555582563460204",
            "extra": "mean: 10.690953758620283 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 81.64673760578995,
            "unit": "iter/sec",
            "range": "stddev: 0.0005338027105151772",
            "extra": "mean: 12.24788680263307 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 96.05352573643346,
            "unit": "iter/sec",
            "range": "stddev: 0.0005266387697264556",
            "extra": "mean: 10.410861989011782 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 81.9911493661155,
            "unit": "iter/sec",
            "range": "stddev: 0.0006102195109694315",
            "extra": "mean: 12.196438368423097 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 92.45880551206275,
            "unit": "iter/sec",
            "range": "stddev: 0.0003819380470151023",
            "extra": "mean: 10.815627505262695 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 76.58329191994949,
            "unit": "iter/sec",
            "range": "stddev: 0.0006153042657197944",
            "extra": "mean: 13.05767844303786 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 94.68005205977025,
            "unit": "iter/sec",
            "range": "stddev: 0.0005459713310114363",
            "extra": "mean: 10.56188688371985 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 63.44892385189088,
            "unit": "iter/sec",
            "range": "stddev: 0.0007587089849773825",
            "extra": "mean: 15.760708602943444 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 87.21850008360055,
            "unit": "iter/sec",
            "range": "stddev: 0.000455150095459751",
            "extra": "mean: 11.465457432098484 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 62.692531553690245,
            "unit": "iter/sec",
            "range": "stddev: 0.000711311910976144",
            "extra": "mean: 15.950863288134956 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 87.77838141909,
            "unit": "iter/sec",
            "range": "stddev: 0.0004700771392565437",
            "extra": "mean: 11.392326719099433 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 73.41466543437079,
            "unit": "iter/sec",
            "range": "stddev: 0.000517478550485244",
            "extra": "mean: 13.621256653331102 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 87.40235196670524,
            "unit": "iter/sec",
            "range": "stddev: 0.0004304273227576141",
            "extra": "mean: 11.441339706521132 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 62.56254331301752,
            "unit": "iter/sec",
            "range": "stddev: 0.0004159117924091931",
            "extra": "mean: 15.984004918034204 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 79.58135064030313,
            "unit": "iter/sec",
            "range": "stddev: 0.0002959434082118932",
            "extra": "mean: 12.565758082190182 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 56.2548033291714,
            "unit": "iter/sec",
            "range": "stddev: 0.0005067840326636585",
            "extra": "mean: 17.776259818180566 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 80.02156267263537,
            "unit": "iter/sec",
            "range": "stddev: 0.0005674141374015675",
            "extra": "mean: 12.496631740259248 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 58.126558344628016,
            "unit": "iter/sec",
            "range": "stddev: 0.00039040290136658123",
            "extra": "mean: 17.20383983636318 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 84.36911840448155,
            "unit": "iter/sec",
            "range": "stddev: 0.0005265894874330841",
            "extra": "mean: 11.852678075949667 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 91.4436141643616,
            "unit": "iter/sec",
            "range": "stddev: 0.00045023044637386157",
            "extra": "mean: 10.935700750000876 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 88.76564342578472,
            "unit": "iter/sec",
            "range": "stddev: 0.0005331630352947738",
            "extra": "mean: 11.265619911109878 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 89.03469678490865,
            "unit": "iter/sec",
            "range": "stddev: 0.00044858367189278686",
            "extra": "mean: 11.23157640909156 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 86.25066669541873,
            "unit": "iter/sec",
            "range": "stddev: 0.0008459659745815013",
            "extra": "mean: 11.594113278351225 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 87.98653815765894,
            "unit": "iter/sec",
            "range": "stddev: 0.0007316374257674784",
            "extra": "mean: 11.365374987343486 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 91.32576775623541,
            "unit": "iter/sec",
            "range": "stddev: 0.0005848951125276688",
            "extra": "mean: 10.949812134831173 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 94.2036648519511,
            "unit": "iter/sec",
            "range": "stddev: 0.00039724014550976075",
            "extra": "mean: 10.615298264367775 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 88.92609426378965,
            "unit": "iter/sec",
            "range": "stddev: 0.000503802575455676",
            "extra": "mean: 11.24529316483425 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 56.268975642924616,
            "unit": "iter/sec",
            "range": "stddev: 0.0013000430242284394",
            "extra": "mean: 17.771782560000133 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 53.50346022211739,
            "unit": "iter/sec",
            "range": "stddev: 0.0011021357781462835",
            "extra": "mean: 18.690379946428543 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 53.20518607463686,
            "unit": "iter/sec",
            "range": "stddev: 0.0011552677027585694",
            "extra": "mean: 18.79516027999955 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 51.472108977857616,
            "unit": "iter/sec",
            "range": "stddev: 0.0006127156806189517",
            "extra": "mean: 19.42799741176687 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 90.06551407384059,
            "unit": "iter/sec",
            "range": "stddev: 0.0004736784647516358",
            "extra": "mean: 11.103028837210054 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 85.54790655879017,
            "unit": "iter/sec",
            "range": "stddev: 0.00030636360018363677",
            "extra": "mean: 11.68935676190721 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 59.29094880865246,
            "unit": "iter/sec",
            "range": "stddev: 0.0006014581611792879",
            "extra": "mean: 16.865980728816872 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 56.05867107240998,
            "unit": "iter/sec",
            "range": "stddev: 0.0006891839628063256",
            "extra": "mean: 17.83845355000153 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 51.7279791236788,
            "unit": "iter/sec",
            "range": "stddev: 0.0008058744799718261",
            "extra": "mean: 19.331897687498174 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 51.56738531360126,
            "unit": "iter/sec",
            "range": "stddev: 0.0007698581231790553",
            "extra": "mean: 19.392102079999063 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 56.09513896177148,
            "unit": "iter/sec",
            "range": "stddev: 0.0007558952517967231",
            "extra": "mean: 17.826856631578973 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 52.87179708766141,
            "unit": "iter/sec",
            "range": "stddev: 0.000801367266308803",
            "extra": "mean: 18.91367525000144 msec\nrounds: 60"
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
          "id": "0a74d6f422a4de036a43cb875a46c638ace6f068",
          "message": "forward statistics from STAC raster:bands (#611)\n\n* forward statistics from STAC raster:bands\r\n\r\n* forward tags as metadata and forward metadata when creating ImageData from list\r\n\r\n* update changelog",
          "timestamp": "2023-05-26T20:43:39+02:00",
          "tree_id": "f19440645bc75f5409b8e3d44b81dc09e7368d4e",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/0a74d6f422a4de036a43cb875a46c638ace6f068"
        },
        "date": 1685523779735,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 61.6477009650958,
            "unit": "iter/sec",
            "range": "stddev: 0.00025321093504281945",
            "extra": "mean: 16.221205078940223 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 69.89549509267651,
            "unit": "iter/sec",
            "range": "stddev: 0.00016255259727546644",
            "extra": "mean: 14.307073705881477 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 62.35935324231371,
            "unit": "iter/sec",
            "range": "stddev: 0.00023210348670973824",
            "extra": "mean: 16.03608677778033 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 70.02825384287932,
            "unit": "iter/sec",
            "range": "stddev: 0.0001971737870189021",
            "extra": "mean: 14.279950521737634 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 58.7271217859005,
            "unit": "iter/sec",
            "range": "stddev: 0.0002104286701687537",
            "extra": "mean: 17.02790754237312 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 66.61131286450262,
            "unit": "iter/sec",
            "range": "stddev: 0.00018981390454503061",
            "extra": "mean: 15.012464955226896 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 58.33460399063264,
            "unit": "iter/sec",
            "range": "stddev: 0.00023165578118500423",
            "extra": "mean: 17.142483733335705 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 66.5089025863691,
            "unit": "iter/sec",
            "range": "stddev: 0.00018578474834003307",
            "extra": "mean: 15.035581119405636 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 44.78563940294785,
            "unit": "iter/sec",
            "range": "stddev: 0.00019973913491305034",
            "extra": "mean: 22.328585978258438 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 59.86104807986249,
            "unit": "iter/sec",
            "range": "stddev: 0.00028192552866929186",
            "extra": "mean: 16.705354016953873 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 44.25606915662355,
            "unit": "iter/sec",
            "range": "stddev: 0.00047878910105634317",
            "extra": "mean: 22.59577090909204 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 61.275710096480346,
            "unit": "iter/sec",
            "range": "stddev: 0.00022744040133904704",
            "extra": "mean: 16.319680317461383 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 56.37266296481632,
            "unit": "iter/sec",
            "range": "stddev: 0.0003027952189250693",
            "extra": "mean: 17.739094578947363 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 63.79422573432016,
            "unit": "iter/sec",
            "range": "stddev: 0.0002875506358164624",
            "extra": "mean: 15.675399904759999 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 47.40775772719809,
            "unit": "iter/sec",
            "range": "stddev: 0.00024788567421528396",
            "extra": "mean: 21.093594127660978 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 60.53966684666567,
            "unit": "iter/sec",
            "range": "stddev: 0.0003195226913271647",
            "extra": "mean: 16.518095524588716 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 72.44916337613954,
            "unit": "iter/sec",
            "range": "stddev: 0.00036060501643307214",
            "extra": "mean: 13.802781887324604 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 91.75783329644501,
            "unit": "iter/sec",
            "range": "stddev: 0.00024845536421339763",
            "extra": "mean: 10.898252106381669 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 74.65807660254919,
            "unit": "iter/sec",
            "range": "stddev: 0.0008371932286452889",
            "extra": "mean: 13.394398108105761 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 89.89349681262374,
            "unit": "iter/sec",
            "range": "stddev: 0.00031008038553868226",
            "extra": "mean: 11.124275230770309 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 88.25298606669202,
            "unit": "iter/sec",
            "range": "stddev: 0.0001906948221092484",
            "extra": "mean: 11.3310613563184 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 104.05458716700939,
            "unit": "iter/sec",
            "range": "stddev: 0.00014323482948511694",
            "extra": "mean: 9.610340372548718 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 89.02594402960848,
            "unit": "iter/sec",
            "range": "stddev: 0.00020614255024388106",
            "extra": "mean: 11.232680662924702 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 104.58692503917895,
            "unit": "iter/sec",
            "range": "stddev: 0.00015545302892252245",
            "extra": "mean: 9.561424620002867 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 62.636372389845484,
            "unit": "iter/sec",
            "range": "stddev: 0.00023249348379051995",
            "extra": "mean: 15.965164677418619 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 102.13540137204429,
            "unit": "iter/sec",
            "range": "stddev: 0.00017191077233310773",
            "extra": "mean: 9.790924464646126 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 62.12049873437289,
            "unit": "iter/sec",
            "range": "stddev: 0.0002303008908457076",
            "extra": "mean: 16.097745838712562 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 101.7050964234316,
            "unit": "iter/sec",
            "range": "stddev: 0.0001538943471612702",
            "extra": "mean: 9.832348969383725 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 67.18628665920164,
            "unit": "iter/sec",
            "range": "stddev: 0.0002591469974926766",
            "extra": "mean: 14.883989720587465 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 94.03447682147606,
            "unit": "iter/sec",
            "range": "stddev: 0.00019302238140183521",
            "extra": "mean: 10.634397444444705 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 64.57744453469061,
            "unit": "iter/sec",
            "range": "stddev: 0.0003812782081237777",
            "extra": "mean: 15.48528293749385 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 93.83877176812271,
            "unit": "iter/sec",
            "range": "stddev: 0.00021376497180964255",
            "extra": "mean: 10.656575967032241 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 80.18140522730987,
            "unit": "iter/sec",
            "range": "stddev: 0.00024001823231799903",
            "extra": "mean: 12.471719560976204 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 95.66512653287083,
            "unit": "iter/sec",
            "range": "stddev: 0.00023253412852775577",
            "extra": "mean: 10.453129956990093 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 67.80415579605096,
            "unit": "iter/sec",
            "range": "stddev: 0.0002690637666485582",
            "extra": "mean: 14.748358537313162 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 87.23511276095329,
            "unit": "iter/sec",
            "range": "stddev: 0.0002595335818544537",
            "extra": "mean: 11.463274000003393 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 58.645574946056314,
            "unit": "iter/sec",
            "range": "stddev: 0.00028126994127055554",
            "extra": "mean: 17.051584896555713 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 85.95220765434077,
            "unit": "iter/sec",
            "range": "stddev: 0.00029239728113169996",
            "extra": "mean: 11.63437248780774 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 64.27473470479595,
            "unit": "iter/sec",
            "range": "stddev: 0.00032154558392080874",
            "extra": "mean: 15.558212796876525 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 86.87798395481867,
            "unit": "iter/sec",
            "range": "stddev: 0.00031096752639056606",
            "extra": "mean: 11.510396011491876 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 92.35776679436152,
            "unit": "iter/sec",
            "range": "stddev: 0.00019727849809514085",
            "extra": "mean: 10.827459722218515 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 102.74993251114347,
            "unit": "iter/sec",
            "range": "stddev: 0.0001771118472463901",
            "extra": "mean: 9.732366489793534 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 92.36380109369244,
            "unit": "iter/sec",
            "range": "stddev: 0.000216611895607808",
            "extra": "mean: 10.826752344087865 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 102.03225831675334,
            "unit": "iter/sec",
            "range": "stddev: 0.00020906066695146797",
            "extra": "mean: 9.800821980197252 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 87.73856672309974,
            "unit": "iter/sec",
            "range": "stddev: 0.00026795451377230437",
            "extra": "mean: 11.397496418604257 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 100.23423140396262,
            "unit": "iter/sec",
            "range": "stddev: 0.0001969203006763683",
            "extra": "mean: 9.976631595745108 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 88.99020634134695,
            "unit": "iter/sec",
            "range": "stddev: 0.00021843996937023937",
            "extra": "mean: 11.237191609200442 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 100.54914628961599,
            "unit": "iter/sec",
            "range": "stddev: 0.000236484162237129",
            "extra": "mean: 9.945385285715478 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 71.41836169238523,
            "unit": "iter/sec",
            "range": "stddev: 0.00031683926725124465",
            "extra": "mean: 14.002001394364413 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 94.67624659929446,
            "unit": "iter/sec",
            "range": "stddev: 0.00023550185246673885",
            "extra": "mean: 10.5623114130451 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 69.62091924663457,
            "unit": "iter/sec",
            "range": "stddev: 0.0002591834955995577",
            "extra": "mean: 14.363498942860328 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 92.73934186740615,
            "unit": "iter/sec",
            "range": "stddev: 0.0002528227118652722",
            "extra": "mean: 10.782910249996679 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 86.59240888675937,
            "unit": "iter/sec",
            "range": "stddev: 0.00026457409598940035",
            "extra": "mean: 11.548356407404523 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 95.60919649479852,
            "unit": "iter/sec",
            "range": "stddev: 0.00019566321711414987",
            "extra": "mean: 10.459244891305028 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 70.72496347053192,
            "unit": "iter/sec",
            "range": "stddev: 0.0003319325760606083",
            "extra": "mean: 14.139279130439672 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 87.03901571220874,
            "unit": "iter/sec",
            "range": "stddev: 0.0003402135418721891",
            "extra": "mean: 11.489100512194012 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 63.417752752987795,
            "unit": "iter/sec",
            "range": "stddev: 0.00030520783764985144",
            "extra": "mean: 15.768455307695953 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 85.63810611317483,
            "unit": "iter/sec",
            "range": "stddev: 0.00034671967197788886",
            "extra": "mean: 11.677044780491205 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 68.03337782096769,
            "unit": "iter/sec",
            "range": "stddev: 0.00029386849987798056",
            "extra": "mean: 14.69866750746283 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 87.01382266287189,
            "unit": "iter/sec",
            "range": "stddev: 0.0003182579844417004",
            "extra": "mean: 11.492426943181432 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 96.37145945371124,
            "unit": "iter/sec",
            "range": "stddev: 0.00019517678760901908",
            "extra": "mean: 10.376516093754043 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 94.66668654267644,
            "unit": "iter/sec",
            "range": "stddev: 0.00021421228164850058",
            "extra": "mean: 10.563378063825995 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 97.65699902929046,
            "unit": "iter/sec",
            "range": "stddev: 0.0002419783300260846",
            "extra": "mean: 10.239921459188684 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 95.3300074773149,
            "unit": "iter/sec",
            "range": "stddev: 0.0002515662878604485",
            "extra": "mean: 10.489876445650799 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 98.12998806312791,
            "unit": "iter/sec",
            "range": "stddev: 0.00022415532965921076",
            "extra": "mean: 10.190564777779153 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 96.33609766963451,
            "unit": "iter/sec",
            "range": "stddev: 0.00025858705757539867",
            "extra": "mean: 10.380324968417355 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 98.41667364788572,
            "unit": "iter/sec",
            "range": "stddev: 0.00024247483016030935",
            "extra": "mean: 10.160879888887436 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 95.80729290291312,
            "unit": "iter/sec",
            "range": "stddev: 0.00021840808699297146",
            "extra": "mean: 10.437618783502796 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 62.935148973127866,
            "unit": "iter/sec",
            "range": "stddev: 0.00026367728229062396",
            "extra": "mean: 15.88937209677507 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 62.45609373204629,
            "unit": "iter/sec",
            "range": "stddev: 0.00032033335203971136",
            "extra": "mean: 16.011247906253523 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 61.38629616571513,
            "unit": "iter/sec",
            "range": "stddev: 0.00030380909225700454",
            "extra": "mean: 16.290280770490764 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 60.4585918762995,
            "unit": "iter/sec",
            "range": "stddev: 0.00029943322570654904",
            "extra": "mean: 16.5402462903211 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 95.07128259849684,
            "unit": "iter/sec",
            "range": "stddev: 0.00017758232352290605",
            "extra": "mean: 10.51842336263812 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 93.26842007436024,
            "unit": "iter/sec",
            "range": "stddev: 0.00027354476318777597",
            "extra": "mean: 10.721742677775914 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 64.64056616612338,
            "unit": "iter/sec",
            "range": "stddev: 0.000322013087976137",
            "extra": "mean: 15.470161530300409 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 63.430675000337814,
            "unit": "iter/sec",
            "range": "stddev: 0.00031739563864366025",
            "extra": "mean: 15.76524292063224 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 55.73587166144103,
            "unit": "iter/sec",
            "range": "stddev: 0.0002861713402407923",
            "extra": "mean: 17.94176658928645 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 55.42555167991855,
            "unit": "iter/sec",
            "range": "stddev: 0.00028715708985225125",
            "extra": "mean: 18.042220053577093 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 61.241341593709905,
            "unit": "iter/sec",
            "range": "stddev: 0.00031774775434423097",
            "extra": "mean: 16.32883888524594 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 60.249844648042114,
            "unit": "iter/sec",
            "range": "stddev: 0.00033535263276037304",
            "extra": "mean: 16.5975531695001 msec\nrounds: 59"
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
          "id": "495e26493b93e427636a33930970cb5a5c09306b",
          "message": "handle nodata in XarrayReader (#612)\n\n* handle nodata in XarrayReader\r\n\r\n* update changelog",
          "timestamp": "2023-06-01T08:44:13+02:00",
          "tree_id": "f3c88884429c4b0734699a986c5d2704b4e56d3c",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/495e26493b93e427636a33930970cb5a5c09306b"
        },
        "date": 1685602107062,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 52.22811827988347,
            "unit": "iter/sec",
            "range": "stddev: 0.00027627633623781845",
            "extra": "mean: 19.146774437500014 msec\nrounds: 32"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 64.7895345070645,
            "unit": "iter/sec",
            "range": "stddev: 0.00025805800198881637",
            "extra": "mean: 15.434591521736621 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 52.87806207841188,
            "unit": "iter/sec",
            "range": "stddev: 0.00025335743491585247",
            "extra": "mean: 18.91143435848914 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 64.97531048658324,
            "unit": "iter/sec",
            "range": "stddev: 0.00018251721702191537",
            "extra": "mean: 15.390461276925949 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 53.98952179103479,
            "unit": "iter/sec",
            "range": "stddev: 0.00015395088809493998",
            "extra": "mean: 18.522112566036 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 63.47301489251223,
            "unit": "iter/sec",
            "range": "stddev: 0.00017568265624579046",
            "extra": "mean: 15.754726661297566 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 53.45559034317313,
            "unit": "iter/sec",
            "range": "stddev: 0.0002481338346338976",
            "extra": "mean: 18.70711732075579 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 63.99852323408356,
            "unit": "iter/sec",
            "range": "stddev: 0.00016561610775418225",
            "extra": "mean: 15.625360546873246 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 37.95912678900396,
            "unit": "iter/sec",
            "range": "stddev: 0.0013357259162401778",
            "extra": "mean: 26.34412550000178 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 55.980061583431365,
            "unit": "iter/sec",
            "range": "stddev: 0.00022619205009251678",
            "extra": "mean: 17.863503035087298 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 37.190904108220685,
            "unit": "iter/sec",
            "range": "stddev: 0.0003589691744131011",
            "extra": "mean: 26.88829497368847 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 55.23717512703775,
            "unit": "iter/sec",
            "range": "stddev: 0.00035965667381596887",
            "extra": "mean: 18.10374983333489 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 47.717320778469656,
            "unit": "iter/sec",
            "range": "stddev: 0.00028348058175042064",
            "extra": "mean: 20.956750791658152 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 55.964584582789726,
            "unit": "iter/sec",
            "range": "stddev: 0.000263131093597664",
            "extra": "mean: 17.868443185183953 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 40.69994081373856,
            "unit": "iter/sec",
            "range": "stddev: 0.0015716234204770643",
            "extra": "mean: 24.570060300000307 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 55.71589242352301,
            "unit": "iter/sec",
            "range": "stddev: 0.0002911766214764702",
            "extra": "mean: 17.948200351858752 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 63.9447054981571,
            "unit": "iter/sec",
            "range": "stddev: 0.000592192903794502",
            "extra": "mean: 15.638511307692557 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 82.78819825901805,
            "unit": "iter/sec",
            "range": "stddev: 0.0002714109159432458",
            "extra": "mean: 12.079016345679088 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 65.1425431846229,
            "unit": "iter/sec",
            "range": "stddev: 0.0003345702239866704",
            "extra": "mean: 15.350951177418159 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 80.90015766233667,
            "unit": "iter/sec",
            "range": "stddev: 0.0003046048261590303",
            "extra": "mean: 12.360915341770134 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 73.15698053217736,
            "unit": "iter/sec",
            "range": "stddev: 0.00020335026058124393",
            "extra": "mean: 13.66923556338086 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 89.49247519675467,
            "unit": "iter/sec",
            "range": "stddev: 0.0003651793492437898",
            "extra": "mean: 11.174123833332791 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 72.4326785610613,
            "unit": "iter/sec",
            "range": "stddev: 0.00016557535580161771",
            "extra": "mean: 13.805923236112172 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 91.39995779007305,
            "unit": "iter/sec",
            "range": "stddev: 0.00010916356500770336",
            "extra": "mean: 10.940924089886288 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 52.270796875425255,
            "unit": "iter/sec",
            "range": "stddev: 0.00020644011671074866",
            "extra": "mean: 19.13114128302381 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 89.79580442427678,
            "unit": "iter/sec",
            "range": "stddev: 0.00015138300852216515",
            "extra": "mean: 11.136377767441042 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 53.02269127690375,
            "unit": "iter/sec",
            "range": "stddev: 0.0004532476871063865",
            "extra": "mean: 18.859849923076084 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 89.35027342473359,
            "unit": "iter/sec",
            "range": "stddev: 0.0001721581428188048",
            "extra": "mean: 11.191907552945262 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 58.03685499538971,
            "unit": "iter/sec",
            "range": "stddev: 0.00023621607687764634",
            "extra": "mean: 17.230430561398226 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 85.65391539515052,
            "unit": "iter/sec",
            "range": "stddev: 0.0001932184876328252",
            "extra": "mean: 11.674889529412185 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 54.223235052451315,
            "unit": "iter/sec",
            "range": "stddev: 0.000491572256115779",
            "extra": "mean: 18.44227846296294 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 82.0853047235872,
            "unit": "iter/sec",
            "range": "stddev: 0.00015244027857170764",
            "extra": "mean: 12.182448531651124 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 68.67832844106997,
            "unit": "iter/sec",
            "range": "stddev: 0.00018746923325323655",
            "extra": "mean: 14.56063393939558 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 85.24176096200824,
            "unit": "iter/sec",
            "range": "stddev: 0.00013526987147756877",
            "extra": "mean: 11.731339060976158 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 57.50506925155736,
            "unit": "iter/sec",
            "range": "stddev: 0.00020884590331328383",
            "extra": "mean: 17.389771250000155 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 78.7707466472331,
            "unit": "iter/sec",
            "range": "stddev: 0.0001926327826587745",
            "extra": "mean: 12.69506818918957 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 51.184945094104364,
            "unit": "iter/sec",
            "range": "stddev: 0.00022299230317850417",
            "extra": "mean: 19.536994680007638 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 76.87848405978373,
            "unit": "iter/sec",
            "range": "stddev: 0.0002458904405830173",
            "extra": "mean: 13.00754056521667 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 55.85610404908354,
            "unit": "iter/sec",
            "range": "stddev: 0.0003900049981987089",
            "extra": "mean: 17.90314625454812 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 77.97750816122092,
            "unit": "iter/sec",
            "range": "stddev: 0.0003904629582506516",
            "extra": "mean: 12.82421077027069 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 76.20530140716086,
            "unit": "iter/sec",
            "range": "stddev: 0.00021378497501783013",
            "extra": "mean: 13.122446621620893 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 91.98276350823888,
            "unit": "iter/sec",
            "range": "stddev: 0.00018526841358563236",
            "extra": "mean: 10.871602046512011 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 76.4532202272257,
            "unit": "iter/sec",
            "range": "stddev: 0.00021283634436470314",
            "extra": "mean: 13.07989378377931 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 90.84425288822094,
            "unit": "iter/sec",
            "range": "stddev: 0.00011445624645379347",
            "extra": "mean: 11.007851000001589 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 79.036295787822,
            "unit": "iter/sec",
            "range": "stddev: 0.0001815191651858104",
            "extra": "mean: 12.65241481818131 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 91.89469464380107,
            "unit": "iter/sec",
            "range": "stddev: 0.00013263374061763683",
            "extra": "mean: 10.882021033707813 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 79.80472397923408,
            "unit": "iter/sec",
            "range": "stddev: 0.0001803707448085805",
            "extra": "mean: 12.530586538463677 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 91.91502428431255,
            "unit": "iter/sec",
            "range": "stddev: 0.00015978115649868183",
            "extra": "mean: 10.879614163042476 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 62.515888515559766,
            "unit": "iter/sec",
            "range": "stddev: 0.00034493344949502314",
            "extra": "mean: 15.995933573768324 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 86.80077523088782,
            "unit": "iter/sec",
            "range": "stddev: 0.00022536534075583777",
            "extra": "mean: 11.520634433736632 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 58.985709396822614,
            "unit": "iter/sec",
            "range": "stddev: 0.0003802400462566994",
            "extra": "mean: 16.953258852454645 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 82.79447901020521,
            "unit": "iter/sec",
            "range": "stddev: 0.00017620569555127613",
            "extra": "mean: 12.078100037041606 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 74.41069077819049,
            "unit": "iter/sec",
            "range": "stddev: 0.0003593574061510374",
            "extra": "mean: 13.438929131579794 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 83.3141064865648,
            "unit": "iter/sec",
            "range": "stddev: 0.00021873614131879624",
            "extra": "mean: 12.002769304874674 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 61.72785523970596,
            "unit": "iter/sec",
            "range": "stddev: 0.00027023875462000056",
            "extra": "mean: 16.20014167213051 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 79.0537756031373,
            "unit": "iter/sec",
            "range": "stddev: 0.00022299471115720565",
            "extra": "mean: 12.649617205130863 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 54.71675131391042,
            "unit": "iter/sec",
            "range": "stddev: 0.0002884318210215785",
            "extra": "mean: 18.275938830194658 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 78.08279448546067,
            "unit": "iter/sec",
            "range": "stddev: 0.00026218751717773677",
            "extra": "mean: 12.80691868918964 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 60.01677967131133,
            "unit": "iter/sec",
            "range": "stddev: 0.00029519945975063833",
            "extra": "mean: 16.662006949999864 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 79.01461792186034,
            "unit": "iter/sec",
            "range": "stddev: 0.000270018527078131",
            "extra": "mean: 12.655886041098457 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 84.99462348073172,
            "unit": "iter/sec",
            "range": "stddev: 0.0002162901467074332",
            "extra": "mean: 11.765450084342099 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 82.2819522268327,
            "unit": "iter/sec",
            "range": "stddev: 0.0005094858750223968",
            "extra": "mean: 12.153333421686769 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 85.20128114976072,
            "unit": "iter/sec",
            "range": "stddev: 0.00027915290536451693",
            "extra": "mean: 11.73691271428503 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 84.6403446921983,
            "unit": "iter/sec",
            "range": "stddev: 0.00016163271157867032",
            "extra": "mean: 11.814696686746537 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 86.32073372646705,
            "unit": "iter/sec",
            "range": "stddev: 0.0002870953481073469",
            "extra": "mean: 11.584702270590029 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 85.95732453097358,
            "unit": "iter/sec",
            "range": "stddev: 0.00022934130494370764",
            "extra": "mean: 11.633679915661673 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 87.82074253722675,
            "unit": "iter/sec",
            "range": "stddev: 0.00018630682340365634",
            "extra": "mean: 11.386831528737133 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 86.30318642687966,
            "unit": "iter/sec",
            "range": "stddev: 0.00022548915003709",
            "extra": "mean: 11.587057690474149 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 52.292159265593824,
            "unit": "iter/sec",
            "range": "stddev: 0.0007717180672011413",
            "extra": "mean: 19.123325830187326 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 51.84900294472762,
            "unit": "iter/sec",
            "range": "stddev: 0.0009071877883924909",
            "extra": "mean: 19.286773962963682 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 50.50564413894048,
            "unit": "iter/sec",
            "range": "stddev: 0.00030897043967338103",
            "extra": "mean: 19.799767274505218 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 50.91557235798672,
            "unit": "iter/sec",
            "range": "stddev: 0.0003585053359958977",
            "extra": "mean: 19.640356647059043 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 84.97668582681432,
            "unit": "iter/sec",
            "range": "stddev: 0.00015672270800593218",
            "extra": "mean: 11.767933642858674 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 83.25721046067456,
            "unit": "iter/sec",
            "range": "stddev: 0.00014900431971038588",
            "extra": "mean: 12.010971716045383 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 57.009432552665416,
            "unit": "iter/sec",
            "range": "stddev: 0.0002961869268420485",
            "extra": "mean: 17.54095691228286 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 57.49939658489672,
            "unit": "iter/sec",
            "range": "stddev: 0.00023210746365950568",
            "extra": "mean: 17.391486857145008 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 49.23696965703575,
            "unit": "iter/sec",
            "range": "stddev: 0.00032602481301907595",
            "extra": "mean: 20.309942040819813 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 48.03853806030856,
            "unit": "iter/sec",
            "range": "stddev: 0.000574649847019429",
            "extra": "mean: 20.81662016326516 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 51.22036569650598,
            "unit": "iter/sec",
            "range": "stddev: 0.0007476743918836504",
            "extra": "mean: 19.523484192308597 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 52.122171803443734,
            "unit": "iter/sec",
            "range": "stddev: 0.0006078096953204162",
            "extra": "mean: 19.18569325489867 msec\nrounds: 51"
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
          "id": "ef87347870f0e01c3f6d60a81556d5e31c8f7103",
          "message": "add AWS credential overrides for S3 stac (#613)\n\n* add AWS credential overrides for S3 stac\r\n\r\n* catch warnings",
          "timestamp": "2023-06-01T11:55:16+02:00",
          "tree_id": "b02ec7fb9c5a59d0988aabfb90c3d7b921deab15",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/ef87347870f0e01c3f6d60a81556d5e31c8f7103"
        },
        "date": 1685613583650,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 58.695217094750134,
            "unit": "iter/sec",
            "range": "stddev: 0.0005221888721450761",
            "extra": "mean: 17.037163324325498 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 73.04330449543357,
            "unit": "iter/sec",
            "range": "stddev: 0.000534218133519661",
            "extra": "mean: 13.690508759259606 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 62.29902144089417,
            "unit": "iter/sec",
            "range": "stddev: 0.00037383552681963174",
            "extra": "mean: 16.051616492062305 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 71.41921772904315,
            "unit": "iter/sec",
            "range": "stddev: 0.00047937949660444614",
            "extra": "mean: 14.001833565216195 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 59.22532892332864,
            "unit": "iter/sec",
            "range": "stddev: 0.0003526475908105411",
            "extra": "mean: 16.88466772881195 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 70.08754962899114,
            "unit": "iter/sec",
            "range": "stddev: 0.0003567650353672839",
            "extra": "mean: 14.267869333333895 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 59.60394080446198,
            "unit": "iter/sec",
            "range": "stddev: 0.00041159106209390955",
            "extra": "mean: 16.77741415254106 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 68.65885713958811,
            "unit": "iter/sec",
            "range": "stddev: 0.0004705866598760901",
            "extra": "mean: 14.564763260870077 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 42.47461209137725,
            "unit": "iter/sec",
            "range": "stddev: 0.00099516909058736",
            "extra": "mean: 23.543475755556326 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 62.391609856152506,
            "unit": "iter/sec",
            "range": "stddev: 0.0005219954255715424",
            "extra": "mean: 16.027796081966123 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 42.17468209269402,
            "unit": "iter/sec",
            "range": "stddev: 0.0004425934089259438",
            "extra": "mean: 23.710907833333295 msec\nrounds: 42"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 64.99571386796615,
            "unit": "iter/sec",
            "range": "stddev: 0.000807208577860734",
            "extra": "mean: 15.385629920634829 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 54.94253178370464,
            "unit": "iter/sec",
            "range": "stddev: 0.0008032230384840334",
            "extra": "mean: 18.20083581034737 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 62.086043460991235,
            "unit": "iter/sec",
            "range": "stddev: 0.0005563024427932182",
            "extra": "mean: 16.10667944444393 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 43.84685961929063,
            "unit": "iter/sec",
            "range": "stddev: 0.0038122344782306294",
            "extra": "mean: 22.80665043477926 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 59.133437379733905,
            "unit": "iter/sec",
            "range": "stddev: 0.0005584823736701211",
            "extra": "mean: 16.91090598333318 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 69.60819288430447,
            "unit": "iter/sec",
            "range": "stddev: 0.0005753161233395695",
            "extra": "mean: 14.36612499999959 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 89.54015392767258,
            "unit": "iter/sec",
            "range": "stddev: 0.000523696123852327",
            "extra": "mean: 11.16817378723478 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 70.32097541864965,
            "unit": "iter/sec",
            "range": "stddev: 0.0007888187283738364",
            "extra": "mean: 14.22050809230943 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 88.50481125588303,
            "unit": "iter/sec",
            "range": "stddev: 0.0005914454738949088",
            "extra": "mean: 11.298820773808822 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 80.48064067190818,
            "unit": "iter/sec",
            "range": "stddev: 0.00036741417388530507",
            "extra": "mean: 12.425348402439479 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 105.39518183153191,
            "unit": "iter/sec",
            "range": "stddev: 0.0003743557375325999",
            "extra": "mean: 9.488099765304662 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 81.68601786006519,
            "unit": "iter/sec",
            "range": "stddev: 0.0005302264832887065",
            "extra": "mean: 12.241997176470049 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 103.15613789514009,
            "unit": "iter/sec",
            "range": "stddev: 0.0004114706180338039",
            "extra": "mean: 9.69404264646391 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 58.16507462913517,
            "unit": "iter/sec",
            "range": "stddev: 0.0004635007106361469",
            "extra": "mean: 17.19244763934499 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 97.54690383399367,
            "unit": "iter/sec",
            "range": "stddev: 0.0004222709064085775",
            "extra": "mean: 10.251478629212162 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 58.559489586117095,
            "unit": "iter/sec",
            "range": "stddev: 0.00047807345371321855",
            "extra": "mean: 17.07665157377112 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 97.04970988146034,
            "unit": "iter/sec",
            "range": "stddev: 0.0004758225029895532",
            "extra": "mean: 10.30399782978674 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 63.512634578280185,
            "unit": "iter/sec",
            "range": "stddev: 0.0005980267214773725",
            "extra": "mean: 15.744898737706848 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 91.11112289173623,
            "unit": "iter/sec",
            "range": "stddev: 0.00046701695050367555",
            "extra": "mean: 10.975608336956409 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 59.45692499858802,
            "unit": "iter/sec",
            "range": "stddev: 0.0005611538097943462",
            "extra": "mean: 16.81889872413933 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 91.19597967571673,
            "unit": "iter/sec",
            "range": "stddev: 0.000707929269015249",
            "extra": "mean: 10.965395662790117 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 77.7827003160345,
            "unit": "iter/sec",
            "range": "stddev: 0.0009292522885012964",
            "extra": "mean: 12.856329182928292 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 92.62049600848891,
            "unit": "iter/sec",
            "range": "stddev: 0.0006034380587409827",
            "extra": "mean: 10.796746326086911 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 63.278467105642335,
            "unit": "iter/sec",
            "range": "stddev: 0.0006079066457021866",
            "extra": "mean: 15.80316410526375 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 83.96487946791221,
            "unit": "iter/sec",
            "range": "stddev: 0.000571064598330413",
            "extra": "mean: 11.909741386363299 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 54.390362052707495,
            "unit": "iter/sec",
            "range": "stddev: 0.0004697581683063073",
            "extra": "mean: 18.3856102857146 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 82.13848898685126,
            "unit": "iter/sec",
            "range": "stddev: 0.0007344424102886583",
            "extra": "mean: 12.174560456792433 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 59.1178115118434,
            "unit": "iter/sec",
            "range": "stddev: 0.0006132725019948503",
            "extra": "mean: 16.91537583050862 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 83.78774545824767,
            "unit": "iter/sec",
            "range": "stddev: 0.000633281170236616",
            "extra": "mean: 11.934919534245145 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 83.77217386612762,
            "unit": "iter/sec",
            "range": "stddev: 0.00063551055629416",
            "extra": "mean: 11.937138000000491 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 101.1969511629612,
            "unit": "iter/sec",
            "range": "stddev: 0.0005160248247333183",
            "extra": "mean: 9.881720629998654 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 87.9887652701814,
            "unit": "iter/sec",
            "range": "stddev: 0.000638687113291322",
            "extra": "mean: 11.365087314606185 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 99.37568984980027,
            "unit": "iter/sec",
            "range": "stddev: 0.0005413162719583387",
            "extra": "mean: 10.06282322680158 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 85.252576291589,
            "unit": "iter/sec",
            "range": "stddev: 0.0006070770795763189",
            "extra": "mean: 11.729850797466865 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 97.95670544960431,
            "unit": "iter/sec",
            "range": "stddev: 0.0004252400772771775",
            "extra": "mean: 10.208591595748072 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 84.70142366998924,
            "unit": "iter/sec",
            "range": "stddev: 0.0005092379916798084",
            "extra": "mean: 11.806177000001387 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 100.47136570313974,
            "unit": "iter/sec",
            "range": "stddev: 0.0005598769904153769",
            "extra": "mean: 9.953084572918769 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 68.66282230708026,
            "unit": "iter/sec",
            "range": "stddev: 0.0005580625352062359",
            "extra": "mean: 14.5639221692302 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 90.53015491827557,
            "unit": "iter/sec",
            "range": "stddev: 0.0004060251735145355",
            "extra": "mean: 11.046043176472322 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 63.77860937810989,
            "unit": "iter/sec",
            "range": "stddev: 0.0005164662000342376",
            "extra": "mean: 15.679238066661584 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 88.73207808634427,
            "unit": "iter/sec",
            "range": "stddev: 0.00046565321746010234",
            "extra": "mean: 11.269881440474213 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 83.50055190854864,
            "unit": "iter/sec",
            "range": "stddev: 0.0006170520348897137",
            "extra": "mean: 11.975968746831981 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 92.94627794474087,
            "unit": "iter/sec",
            "range": "stddev: 0.0005296774735149352",
            "extra": "mean: 10.758903122452386 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 67.17882346134223,
            "unit": "iter/sec",
            "range": "stddev: 0.0006657747094930314",
            "extra": "mean: 14.885643249995972 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 86.16633921900991,
            "unit": "iter/sec",
            "range": "stddev: 0.00042371054172083013",
            "extra": "mean: 11.605459963412036 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 59.043311280032555,
            "unit": "iter/sec",
            "range": "stddev: 0.0006222182747852158",
            "extra": "mean: 16.936719474576336 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 80.34766259883517,
            "unit": "iter/sec",
            "range": "stddev: 0.00068039564026325",
            "extra": "mean: 12.445912770267661 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 61.89577568403354,
            "unit": "iter/sec",
            "range": "stddev: 0.0007100653789598195",
            "extra": "mean: 16.15619141934362 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 85.2058996711137,
            "unit": "iter/sec",
            "range": "stddev: 0.0007980984189952834",
            "extra": "mean: 11.73627652380763 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 93.8334181836861,
            "unit": "iter/sec",
            "range": "stddev: 0.0006245386315777322",
            "extra": "mean: 10.65718396874793 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 92.33417232777622,
            "unit": "iter/sec",
            "range": "stddev: 0.0004994327509858412",
            "extra": "mean: 10.83022650000164 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 93.38209141006301,
            "unit": "iter/sec",
            "range": "stddev: 0.0005171146625736261",
            "extra": "mean: 10.708691408599552 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.28716530055172,
            "unit": "iter/sec",
            "range": "stddev: 0.0004202015432396974",
            "extra": "mean: 10.278848159576595 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 90.9590075586465,
            "unit": "iter/sec",
            "range": "stddev: 0.0006267331926884673",
            "extra": "mean: 10.993963399999087 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 90.02450152341252,
            "unit": "iter/sec",
            "range": "stddev: 0.0005165499626361223",
            "extra": "mean: 11.108087054943942 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 90.87280059410973,
            "unit": "iter/sec",
            "range": "stddev: 0.0005112314275773303",
            "extra": "mean: 11.004392881722396 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 89.19688910796965,
            "unit": "iter/sec",
            "range": "stddev: 0.0004791163414231326",
            "extra": "mean: 11.211153326093422 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 58.07272749439108,
            "unit": "iter/sec",
            "range": "stddev: 0.0009052575102440891",
            "extra": "mean: 17.219787035086036 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 56.23063508422886,
            "unit": "iter/sec",
            "range": "stddev: 0.000795895196464648",
            "extra": "mean: 17.783900155174884 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 55.36588320999575,
            "unit": "iter/sec",
            "range": "stddev: 0.0005291536022351816",
            "extra": "mean: 18.06166436841849 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 55.261899733156845,
            "unit": "iter/sec",
            "range": "stddev: 0.0005288093141204666",
            "extra": "mean: 18.09565007407817 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 91.5955440921493,
            "unit": "iter/sec",
            "range": "stddev: 0.0004949732461443052",
            "extra": "mean: 10.917561655553401 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 97.87055855442632,
            "unit": "iter/sec",
            "range": "stddev: 0.00007486689646232726",
            "extra": "mean: 10.2175773263202 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 66.75029278195635,
            "unit": "iter/sec",
            "range": "stddev: 0.00015752769789547882",
            "extra": "mean: 14.981207696969319 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 66.62013855625982,
            "unit": "iter/sec",
            "range": "stddev: 0.00012656788472766267",
            "extra": "mean: 15.01047613636398 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 57.56511564655358,
            "unit": "iter/sec",
            "range": "stddev: 0.00018309349908467634",
            "extra": "mean: 17.371631912284187 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 55.9665954518552,
            "unit": "iter/sec",
            "range": "stddev: 0.00035734410703355205",
            "extra": "mean: 17.867801175439403 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 61.25369520698296,
            "unit": "iter/sec",
            "range": "stddev: 0.0007334332915901093",
            "extra": "mean: 16.325545693543717 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 57.97980047905081,
            "unit": "iter/sec",
            "range": "stddev: 0.0010160065180347248",
            "extra": "mean: 17.2473860161233 msec\nrounds: 62"
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
          "id": "5b4775de282e12632f0497d686200ed8558f1dd0",
          "message": "deprecated model methods (#615)",
          "timestamp": "2023-06-01T15:22:04+02:00",
          "tree_id": "e2c0b18132a2c308b992ba79713d9a6d96ae5d52",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/5b4775de282e12632f0497d686200ed8558f1dd0"
        },
        "date": 1685625985597,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 61.97050738565655,
            "unit": "iter/sec",
            "range": "stddev: 0.0002798696287523651",
            "extra": "mean: 16.136708285713603 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 70.75752629369214,
            "unit": "iter/sec",
            "range": "stddev: 0.0000818181435733309",
            "extra": "mean: 14.132772192308078 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 63.06851454384398,
            "unit": "iter/sec",
            "range": "stddev: 0.00014562658755211844",
            "extra": "mean: 15.855772206349014 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 70.7116401075339,
            "unit": "iter/sec",
            "range": "stddev: 0.00010665431614019098",
            "extra": "mean: 14.141943228572577 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 60.04336984365373,
            "unit": "iter/sec",
            "range": "stddev: 0.00007259300097574452",
            "extra": "mean: 16.65462818965506 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 68.45620054051516,
            "unit": "iter/sec",
            "range": "stddev: 0.00012650248279500874",
            "extra": "mean: 14.60788054411754 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 59.06638203962164,
            "unit": "iter/sec",
            "range": "stddev: 0.00014939102711777644",
            "extra": "mean: 16.930104155172423 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 68.19978068655709,
            "unit": "iter/sec",
            "range": "stddev: 0.00015832108288397597",
            "extra": "mean: 14.662803749999606 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 45.18514790576464,
            "unit": "iter/sec",
            "range": "stddev: 0.00021762897592091728",
            "extra": "mean: 22.1311658 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 60.05314415002056,
            "unit": "iter/sec",
            "range": "stddev: 0.00018492563794494428",
            "extra": "mean: 16.651917466667022 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 44.44232575757088,
            "unit": "iter/sec",
            "range": "stddev: 0.0002109130484494661",
            "extra": "mean: 22.501072636362807 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 61.89637488315284,
            "unit": "iter/sec",
            "range": "stddev: 0.00020218272147734767",
            "extra": "mean: 16.15603501639291 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 57.09607512413415,
            "unit": "iter/sec",
            "range": "stddev: 0.00015526746639021253",
            "extra": "mean: 17.51433873214354 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 64.76390194571202,
            "unit": "iter/sec",
            "range": "stddev: 0.0001987399082682193",
            "extra": "mean: 15.440700296875942 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 47.22627786045881,
            "unit": "iter/sec",
            "range": "stddev: 0.00034019265569330647",
            "extra": "mean: 21.17465202222238 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 59.86677057302909,
            "unit": "iter/sec",
            "range": "stddev: 0.00014299919017177388",
            "extra": "mean: 16.703757200000286 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 72.44252355848812,
            "unit": "iter/sec",
            "range": "stddev: 0.00018283190569292956",
            "extra": "mean: 13.804047000000311 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 90.62668488537918,
            "unit": "iter/sec",
            "range": "stddev: 0.00022833581362649737",
            "extra": "mean: 11.034277611111538 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 74.55964299427683,
            "unit": "iter/sec",
            "range": "stddev: 0.00019501513214354596",
            "extra": "mean: 13.41208138666597 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 90.32455497865847,
            "unit": "iter/sec",
            "range": "stddev: 0.0002455884310069295",
            "extra": "mean: 11.071186569768054 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 86.949550313634,
            "unit": "iter/sec",
            "range": "stddev: 0.00043617735618515325",
            "extra": "mean: 11.500922044943533 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 103.91985203011679,
            "unit": "iter/sec",
            "range": "stddev: 0.00009185407546375119",
            "extra": "mean: 9.622800460783875 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 88.23923076111019,
            "unit": "iter/sec",
            "range": "stddev: 0.0002899439599412682",
            "extra": "mean: 11.332827715909005 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 104.68695959760613,
            "unit": "iter/sec",
            "range": "stddev: 0.00011067202721967789",
            "extra": "mean: 9.552288115384973 msec\nrounds: 104"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 55.99444423124123,
            "unit": "iter/sec",
            "range": "stddev: 0.00047301268698871464",
            "extra": "mean: 17.858914642857826 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 101.02686092074727,
            "unit": "iter/sec",
            "range": "stddev: 0.00018421392242801341",
            "extra": "mean: 9.8983576336641 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 54.54698142015274,
            "unit": "iter/sec",
            "range": "stddev: 0.00019163284853991345",
            "extra": "mean: 18.332820148147434 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 100.8876362249663,
            "unit": "iter/sec",
            "range": "stddev: 0.00021255956965469535",
            "extra": "mean: 9.91201734343473 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 68.39671830422263,
            "unit": "iter/sec",
            "range": "stddev: 0.0001373077606294246",
            "extra": "mean: 14.620584507462585 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 96.24356453070824,
            "unit": "iter/sec",
            "range": "stddev: 0.00013925923117869894",
            "extra": "mean: 10.390305106383835 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 65.53543275198572,
            "unit": "iter/sec",
            "range": "stddev: 0.00021331781656658662",
            "extra": "mean: 15.25892113636344 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 94.37093846457212,
            "unit": "iter/sec",
            "range": "stddev: 0.00012322282227140283",
            "extra": "mean: 10.596482521739581 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 81.80128464736373,
            "unit": "iter/sec",
            "range": "stddev: 0.00023893643829324643",
            "extra": "mean: 12.224746888889204 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 97.6249950113963,
            "unit": "iter/sec",
            "range": "stddev: 0.00011239708510184509",
            "extra": "mean: 10.243278372339631 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 69.19063479178766,
            "unit": "iter/sec",
            "range": "stddev: 0.0002978089009651264",
            "extra": "mean: 14.452823030302525 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 88.55240375824123,
            "unit": "iter/sec",
            "range": "stddev: 0.00020304419631502255",
            "extra": "mean: 11.292748220930521 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 60.16417588281767,
            "unit": "iter/sec",
            "range": "stddev: 0.00019985892585276376",
            "extra": "mean: 16.621186700000834 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 86.49178178719632,
            "unit": "iter/sec",
            "range": "stddev: 0.0001923046896493962",
            "extra": "mean: 11.561792107143683 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 65.08531990348628,
            "unit": "iter/sec",
            "range": "stddev: 0.0002842940822194021",
            "extra": "mean: 15.364447796874625 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 87.83350391770034,
            "unit": "iter/sec",
            "range": "stddev: 0.0001221210811899313",
            "extra": "mean: 11.385177129412897 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 93.34280068673038,
            "unit": "iter/sec",
            "range": "stddev: 0.00014411988121762058",
            "extra": "mean: 10.713199010988749 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 102.66748461440268,
            "unit": "iter/sec",
            "range": "stddev: 0.00011424445911225532",
            "extra": "mean: 9.740182140000684 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 94.77573249662343,
            "unit": "iter/sec",
            "range": "stddev: 0.0000552965316448836",
            "extra": "mean: 10.551224175826095 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 103.54149373695994,
            "unit": "iter/sec",
            "range": "stddev: 0.00013221071230653186",
            "extra": "mean: 9.657963816326925 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 89.50042137904158,
            "unit": "iter/sec",
            "range": "stddev: 0.00016840048547297505",
            "extra": "mean: 11.173131752809503 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 101.26835588023117,
            "unit": "iter/sec",
            "range": "stddev: 0.00013368383771757389",
            "extra": "mean: 9.874752989795624 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 90.03662540543141,
            "unit": "iter/sec",
            "range": "stddev: 0.00014874685277330523",
            "extra": "mean: 11.10659129545381 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 101.53095363924244,
            "unit": "iter/sec",
            "range": "stddev: 0.00013439045945180626",
            "extra": "mean: 9.849213113403604 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 73.291964697902,
            "unit": "iter/sec",
            "range": "stddev: 0.00009884577549859646",
            "extra": "mean: 13.644060493150146 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 96.06846510468284,
            "unit": "iter/sec",
            "range": "stddev: 0.00017897351739837894",
            "extra": "mean: 10.409243021737995 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 70.7028244668309,
            "unit": "iter/sec",
            "range": "stddev: 0.00023089370270633946",
            "extra": "mean: 14.143706528572052 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 93.96189466872634,
            "unit": "iter/sec",
            "range": "stddev: 0.00011459723703076207",
            "extra": "mean: 10.642612130434546 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 88.6396365214199,
            "unit": "iter/sec",
            "range": "stddev: 0.00012692044787932297",
            "extra": "mean: 11.281634709302407 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 97.49853285274278,
            "unit": "iter/sec",
            "range": "stddev: 0.00012991187353841217",
            "extra": "mean: 10.25656459374987 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 72.76993715339219,
            "unit": "iter/sec",
            "range": "stddev: 0.00015120436449758207",
            "extra": "mean: 13.741938486109914 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 90.15963391192736,
            "unit": "iter/sec",
            "range": "stddev: 0.00015995296153905507",
            "extra": "mean: 11.09143811494235 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 64.26368580899448,
            "unit": "iter/sec",
            "range": "stddev: 0.00019371763493529712",
            "extra": "mean: 15.560887730159386 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 87.84303063879308,
            "unit": "iter/sec",
            "range": "stddev: 0.0001430765736436436",
            "extra": "mean: 11.383942388235202 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 69.67068027507187,
            "unit": "iter/sec",
            "range": "stddev: 0.00024512363157163806",
            "extra": "mean: 14.35324007246416 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 88.34824318900249,
            "unit": "iter/sec",
            "range": "stddev: 0.00031569976770046723",
            "extra": "mean: 11.318844199999658 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 98.9318583255536,
            "unit": "iter/sec",
            "range": "stddev: 0.00007036361165623283",
            "extra": "mean: 10.107967412370996 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 95.79307382782223,
            "unit": "iter/sec",
            "range": "stddev: 0.000313499094813766",
            "extra": "mean: 10.43916809473504 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 99.14577898805703,
            "unit": "iter/sec",
            "range": "stddev: 0.00011726141255147372",
            "extra": "mean: 10.086158081631076 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.70744462983085,
            "unit": "iter/sec",
            "range": "stddev: 0.00008917972954353867",
            "extra": "mean: 10.234634666667889 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 100.36663881953169,
            "unit": "iter/sec",
            "range": "stddev: 0.00009629457230643843",
            "extra": "mean: 9.963470051020545 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 97.76166222034806,
            "unit": "iter/sec",
            "range": "stddev: 0.0001132283190587826",
            "extra": "mean: 10.228958645834693 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 99.82250016758783,
            "unit": "iter/sec",
            "range": "stddev: 0.00012478410296508613",
            "extra": "mean: 10.0177815454546 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 98.47513398904479,
            "unit": "iter/sec",
            "range": "stddev: 0.00007639924868747559",
            "extra": "mean: 10.154847822915869 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 65.00725233907995,
            "unit": "iter/sec",
            "range": "stddev: 0.00016688332240424728",
            "extra": "mean: 15.382899046155146 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 63.894533957097764,
            "unit": "iter/sec",
            "range": "stddev: 0.0002083441734116533",
            "extra": "mean: 15.650791046875057 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 63.27722619694494,
            "unit": "iter/sec",
            "range": "stddev: 0.00015576765611826252",
            "extra": "mean: 15.803474015873984 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 62.37196933519936,
            "unit": "iter/sec",
            "range": "stddev: 0.00017649602725379893",
            "extra": "mean: 16.03284312903127 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 95.94631730505385,
            "unit": "iter/sec",
            "range": "stddev: 0.00019983720994959261",
            "extra": "mean: 10.422494870965998 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 94.14896805308341,
            "unit": "iter/sec",
            "range": "stddev: 0.00012803184724319218",
            "extra": "mean: 10.62146532966964 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 65.21316985302084,
            "unit": "iter/sec",
            "range": "stddev: 0.0009613616023999239",
            "extra": "mean: 15.334325907693588 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 65.09764459144803,
            "unit": "iter/sec",
            "range": "stddev: 0.00016049752304985316",
            "extra": "mean: 15.361538904763558 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 57.28107208075655,
            "unit": "iter/sec",
            "range": "stddev: 0.00020781596937033346",
            "extra": "mean: 17.45777381034647 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 56.22727175697995,
            "unit": "iter/sec",
            "range": "stddev: 0.000286620242426526",
            "extra": "mean: 17.784963928573713 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 62.53682983569694,
            "unit": "iter/sec",
            "range": "stddev: 0.000154910661133826",
            "extra": "mean: 15.990577114754629 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 61.057885073126926,
            "unit": "iter/sec",
            "range": "stddev: 0.0004819577304278267",
            "extra": "mean: 16.37790104918201 msec\nrounds: 61"
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
          "id": "2a2a6a53905b2cc81b0565c324b54c5f84ef9c08",
          "message": "rio-tiler V5.0 (#616)\n\n* update readme\r\n\r\n* PER_BAND mask and MaskedArray (#580)\r\n\r\n* sketch use of MaskedArray with PER_BAND mask\r\n\r\n* update PointData and fix tests\r\n\r\n* update mosaics\r\n\r\n* update nodata mask\r\n\r\n* remove unused\r\n\r\n* update changelog\r\n\r\n* migration guide\r\n\r\n* split resampling option to RasterIO and Warp options (#590)\r\n\r\n* refactor Mask tests and Benchmark\r\n\r\n* refactor Mask tests and Benchmark (#591)\r\n\r\n* change arguments in dynamic_tiler.md (#592)\r\n\r\n* change arguments\r\n\r\nThe argument  (\"tile\", {\"z\": \"{z}\", \"x\": \"{x}\", \"y\": \"{y}\"}) causes errors below.\r\n\r\nFile \"/home/ubuntu/app/app.py\", line 48, in tilejson\r\n    tile_url = request.url_for(\"tile\", {\"z\": \"{z}\", \"x\": \"{x}\", \"y\": \"{y}\"})\r\nTypeError: HTTPConnection.url_for() takes 2 positional arguments but 3 were given\r\n\r\n(\"tile\", z='{z}', x='{x}', y='{y}') is correct.\r\n\r\n* Update docs/src/advanced/dynamic_tiler.md\r\n\r\n---------\r\n\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>\r\n\r\n* refactor MosaicMethods (#594)\r\n\r\n* refactor MosaicMethods\r\n\r\n* fix tests\r\n\r\n* Optional boto3 (#597)\r\n\r\n* make boto3 an optional dependency\r\n\r\n* update migration\r\n\r\n* update test dependencies\r\n\r\n* add flake8 rules in ruff (#600)\r\n\r\n* update dev version\r\n\r\n* update mosaic example notebook custom pixel_selection class (#602)\r\n\r\n* improve cutline handling (#598)\r\n\r\n* Improve cutline handling\r\n\r\nCloses #588\r\n\r\n* handle projection\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>\r\n\r\n* remove useless cache\r\n\r\n* save benchmarks\r\n\r\n* add benchmarking in docs\r\n\r\n* fix nodata/mask/alpha forwarding for GCPS dataset (#604)\r\n\r\n* remove boto3\r\n\r\n* Allow clip-box to auto expand (#608)\r\n\r\n* Allow clip-box to auto expand\r\n\r\n* Add test\r\n\r\n* Update tests/test_io_xarray.py\r\n\r\n* Fix import order\r\n\r\n* Changes from black linter\r\n\r\n* Change default to true\r\n\r\n* use auto_expand in part and update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>\r\n\r\n* allow morecantile 4.0 (#606)\r\n\r\n* allow morecantile 4.0\r\n\r\n* set morecantile min version to 4.0\r\n\r\n* update changelog\r\n\r\n* forward statistics from STAC raster:bands (#611)\r\n\r\n* forward statistics from STAC raster:bands\r\n\r\n* forward tags as metadata and forward metadata when creating ImageData from list\r\n\r\n* update changelog\r\n\r\n* handle nodata in XarrayReader (#612)\r\n\r\n* handle nodata in XarrayReader\r\n\r\n* update changelog\r\n\r\n* add AWS credential overrides for S3 stac (#613)\r\n\r\n* add AWS credential overrides for S3 stac\r\n\r\n* catch warnings\r\n\r\n* deprecated model methods (#615)\r\n\r\n* update readme\r\n\r\n---------\r\n\r\nCo-authored-by: TTY6335 <36815385+TTY6335@users.noreply.github.com>\r\nCo-authored-by: Daniel Wiesmann <yellowcap@users.noreply.github.com>\r\nCo-authored-by: Aimee Barciauskas <aimee@developmentseed.org>",
          "timestamp": "2023-06-01T21:56:30+02:00",
          "tree_id": "d235f01ac6674c5d55445a256f2c2723053e4e2f",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/2a2a6a53905b2cc81b0565c324b54c5f84ef9c08"
        },
        "date": 1685649667357,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 57.94733064422441,
            "unit": "iter/sec",
            "range": "stddev: 0.00035751399569733557",
            "extra": "mean: 17.257050305554838 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 69.03239091148265,
            "unit": "iter/sec",
            "range": "stddev: 0.00299793049223928",
            "extra": "mean: 14.48595343137192 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 57.98951056836275,
            "unit": "iter/sec",
            "range": "stddev: 0.00026982530264172766",
            "extra": "mean: 17.24449801694944 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 71.7558546409054,
            "unit": "iter/sec",
            "range": "stddev: 0.00018733000886022905",
            "extra": "mean: 13.936145071428589 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 59.537207547138635,
            "unit": "iter/sec",
            "range": "stddev: 0.00031218624416769664",
            "extra": "mean: 16.796219392860326 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 69.50510114609438,
            "unit": "iter/sec",
            "range": "stddev: 0.0001654878881435799",
            "extra": "mean: 14.387433202896533 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 59.09211106905603,
            "unit": "iter/sec",
            "range": "stddev: 0.00017839168686730332",
            "extra": "mean: 16.92273269491732 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 68.98427907626055,
            "unit": "iter/sec",
            "range": "stddev: 0.0001956058507796511",
            "extra": "mean: 14.496056397060014 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 43.63124494851996,
            "unit": "iter/sec",
            "range": "stddev: 0.0006896665254889306",
            "extra": "mean: 22.91935518181728 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 61.57400021891243,
            "unit": "iter/sec",
            "range": "stddev: 0.00024686951699078713",
            "extra": "mean: 16.240620983608768 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 42.21627130317439,
            "unit": "iter/sec",
            "range": "stddev: 0.00019692801053022691",
            "extra": "mean: 23.68754911627656 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 61.62274224033411,
            "unit": "iter/sec",
            "range": "stddev: 0.00025482738494827975",
            "extra": "mean: 16.227775065574203 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 53.872565523698405,
            "unit": "iter/sec",
            "range": "stddev: 0.0002008107800567055",
            "extra": "mean: 18.56232370370597 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 62.36643316730182,
            "unit": "iter/sec",
            "range": "stddev: 0.00038493090642085056",
            "extra": "mean: 16.034266338712012 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 45.17069880600669,
            "unit": "iter/sec",
            "range": "stddev: 0.0002587599312590589",
            "extra": "mean: 22.138245066667473 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 58.20057347721252,
            "unit": "iter/sec",
            "range": "stddev: 0.00023423192348812365",
            "extra": "mean: 17.181961280699984 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 67.56219743356974,
            "unit": "iter/sec",
            "range": "stddev: 0.00018693486889203293",
            "extra": "mean: 14.801176367646212 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 86.62355622142734,
            "unit": "iter/sec",
            "range": "stddev: 0.0002787843942637791",
            "extra": "mean: 11.544203951218508 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 70.45182226058711,
            "unit": "iter/sec",
            "range": "stddev: 0.0003478101865748463",
            "extra": "mean: 14.194097014285894 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 87.45912400524394,
            "unit": "iter/sec",
            "range": "stddev: 0.00021942987707715186",
            "extra": "mean: 11.433912829266863 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 78.23557483035631,
            "unit": "iter/sec",
            "range": "stddev: 0.00026139246769526",
            "extra": "mean: 12.781909024997518 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 100.88272134113639,
            "unit": "iter/sec",
            "range": "stddev: 0.00016305357881357338",
            "extra": "mean: 9.912500244898087 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 78.79472689289693,
            "unit": "iter/sec",
            "range": "stddev: 0.00016717203717715775",
            "extra": "mean: 12.691204594937767 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 100.209770061031,
            "unit": "iter/sec",
            "range": "stddev: 0.00016327086325464894",
            "extra": "mean: 9.979066905262508 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 57.988167139049565,
            "unit": "iter/sec",
            "range": "stddev: 0.000184309610857328",
            "extra": "mean: 17.244897525422807 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 96.88017685341396,
            "unit": "iter/sec",
            "range": "stddev: 0.00027465500302207093",
            "extra": "mean: 10.322029051547517 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 58.28132136608516,
            "unit": "iter/sec",
            "range": "stddev: 0.0002657957779984431",
            "extra": "mean: 17.15815593333332 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 97.62228580672551,
            "unit": "iter/sec",
            "range": "stddev: 0.0002672978818547101",
            "extra": "mean: 10.243562642856153 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 62.07579485589392,
            "unit": "iter/sec",
            "range": "stddev: 0.00020286202498932983",
            "extra": "mean: 16.109338629033324 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 90.09573933646264,
            "unit": "iter/sec",
            "range": "stddev: 0.0001544268914014709",
            "extra": "mean: 11.099303999998256 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 58.24196262668373,
            "unit": "iter/sec",
            "range": "stddev: 0.00018798803078390168",
            "extra": "mean: 17.169751067795353 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 88.84859769517875,
            "unit": "iter/sec",
            "range": "stddev: 0.0002737851674629158",
            "extra": "mean: 11.255101666666638 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 73.85948577441187,
            "unit": "iter/sec",
            "range": "stddev: 0.00020747581307346984",
            "extra": "mean: 13.539222342466449 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 89.72640234447748,
            "unit": "iter/sec",
            "range": "stddev: 0.00032049283661459246",
            "extra": "mean: 11.144991595236387 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 61.60202862276341,
            "unit": "iter/sec",
            "range": "stddev: 0.0005502905172263666",
            "extra": "mean: 16.23323163793467 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 82.60021722980032,
            "unit": "iter/sec",
            "range": "stddev: 0.00027123140475569736",
            "extra": "mean: 12.106505691358183 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 54.55015747232931,
            "unit": "iter/sec",
            "range": "stddev: 0.0002471237108689518",
            "extra": "mean: 18.33175276363322 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 80.4755697888177,
            "unit": "iter/sec",
            "range": "stddev: 0.00021419955943434646",
            "extra": "mean: 12.426131341774642 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 58.77864216110713,
            "unit": "iter/sec",
            "range": "stddev: 0.0004069041845203047",
            "extra": "mean: 17.012982322032673 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 84.53793943286615,
            "unit": "iter/sec",
            "range": "stddev: 0.0002849202454927894",
            "extra": "mean: 11.829008451218838 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 81.94732931923632,
            "unit": "iter/sec",
            "range": "stddev: 0.0002892406907923747",
            "extra": "mean: 12.2029602222224 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 99.93454276927407,
            "unit": "iter/sec",
            "range": "stddev: 0.0001999968700248637",
            "extra": "mean: 10.006550010528096 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 84.13565772326355,
            "unit": "iter/sec",
            "range": "stddev: 0.00018132461856293326",
            "extra": "mean: 11.885567036145003 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 100.61813674986097,
            "unit": "iter/sec",
            "range": "stddev: 0.00022366276005614903",
            "extra": "mean: 9.938566070707743 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 85.73669081127412,
            "unit": "iter/sec",
            "range": "stddev: 0.00019637266330455917",
            "extra": "mean: 11.663617880951652 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 98.2067713353219,
            "unit": "iter/sec",
            "range": "stddev: 0.00020066945078651632",
            "extra": "mean: 10.182597252744946 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 84.0543617662061,
            "unit": "iter/sec",
            "range": "stddev: 0.00021966119990321384",
            "extra": "mean: 11.897062555557326 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 97.67867430641397,
            "unit": "iter/sec",
            "range": "stddev: 0.00018685828170023048",
            "extra": "mean: 10.237649180854373 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 66.52998733022423,
            "unit": "iter/sec",
            "range": "stddev: 0.00032070762118299647",
            "extra": "mean: 15.030816029416334 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 89.69211465124856,
            "unit": "iter/sec",
            "range": "stddev: 0.0002024974970323377",
            "extra": "mean: 11.149252126436286 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 64.64975066619961,
            "unit": "iter/sec",
            "range": "stddev: 0.00017223169731300339",
            "extra": "mean: 15.467963753846666 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 89.33286009216062,
            "unit": "iter/sec",
            "range": "stddev: 0.00025671274404988093",
            "extra": "mean: 11.194089151162807 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 80.52392904624898,
            "unit": "iter/sec",
            "range": "stddev: 0.00021849717462559678",
            "extra": "mean: 12.418668734180239 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 90.45212971382969,
            "unit": "iter/sec",
            "range": "stddev: 0.0002783345777830465",
            "extra": "mean: 11.05557163953769 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 66.40299508399863,
            "unit": "iter/sec",
            "range": "stddev: 0.0002847895797368668",
            "extra": "mean: 15.059561676924625 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 82.5210814622109,
            "unit": "iter/sec",
            "range": "stddev: 0.0002765929499002946",
            "extra": "mean: 12.118115544304066 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 59.233333546800196,
            "unit": "iter/sec",
            "range": "stddev: 0.00022626758331438783",
            "extra": "mean: 16.882385983052956 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 80.98378613339925,
            "unit": "iter/sec",
            "range": "stddev: 0.00021113864488050103",
            "extra": "mean: 12.348150756409018 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 62.862327620249985,
            "unit": "iter/sec",
            "range": "stddev: 0.00023585520684271736",
            "extra": "mean: 15.907778758066028 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 82.15489398311571,
            "unit": "iter/sec",
            "range": "stddev: 0.00040094690876328235",
            "extra": "mean: 12.172129395060965 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 93.55485104988645,
            "unit": "iter/sec",
            "range": "stddev: 0.00023124274249436592",
            "extra": "mean: 10.68891659574946 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 91.29747538785284,
            "unit": "iter/sec",
            "range": "stddev: 0.0002142325044235062",
            "extra": "mean: 10.953205395349302 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 96.31076930793766,
            "unit": "iter/sec",
            "range": "stddev: 0.00018961283531541818",
            "extra": "mean: 10.383054846158132 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 94.93265758419095,
            "unit": "iter/sec",
            "range": "stddev: 0.00017878722669229774",
            "extra": "mean: 10.533782846152292 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 95.78030553704028,
            "unit": "iter/sec",
            "range": "stddev: 0.0001868517964123444",
            "extra": "mean: 10.440559720424767 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 95.34220482498976,
            "unit": "iter/sec",
            "range": "stddev: 0.0001090452381566729",
            "extra": "mean: 10.488534451616687 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 95.49840371928087,
            "unit": "iter/sec",
            "range": "stddev: 0.00021003844660342916",
            "extra": "mean: 10.471379217390023 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 93.98206915083519,
            "unit": "iter/sec",
            "range": "stddev: 0.00016635286776307012",
            "extra": "mean: 10.640327554345118 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 59.62298110822504,
            "unit": "iter/sec",
            "range": "stddev: 0.0005135513522791901",
            "extra": "mean: 16.772056368413438 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 58.29439841556862,
            "unit": "iter/sec",
            "range": "stddev: 0.0006701057718017298",
            "extra": "mean: 17.154306883333938 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 56.75382596658495,
            "unit": "iter/sec",
            "range": "stddev: 0.0003338579463442203",
            "extra": "mean: 17.619957473682422 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 56.4781883252484,
            "unit": "iter/sec",
            "range": "stddev: 0.00030342869939628075",
            "extra": "mean: 17.705950379306927 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 91.40174725000989,
            "unit": "iter/sec",
            "range": "stddev: 0.00021179177952351157",
            "extra": "mean: 10.940709888889918 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 90.75749529951737,
            "unit": "iter/sec",
            "range": "stddev: 0.00019140475825855344",
            "extra": "mean: 11.018373707866283 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 61.9488711419424,
            "unit": "iter/sec",
            "range": "stddev: 0.00043299631981493815",
            "extra": "mean: 16.142344187494828 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 60.27034322723175,
            "unit": "iter/sec",
            "range": "stddev: 0.00019504930209295876",
            "extra": "mean: 16.591908166671487 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 52.72678141856662,
            "unit": "iter/sec",
            "range": "stddev: 0.00023272843566466168",
            "extra": "mean: 18.965693962269263 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 51.99472624980112,
            "unit": "iter/sec",
            "range": "stddev: 0.0002455428996944879",
            "extra": "mean: 19.232719779995477 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 57.13138544704641,
            "unit": "iter/sec",
            "range": "stddev: 0.0006006725861370699",
            "extra": "mean: 17.50351391227636 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 57.00083778652595,
            "unit": "iter/sec",
            "range": "stddev: 0.0005007599333047212",
            "extra": "mean: 17.543601793101775 msec\nrounds: 58"
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
          "id": "90bb3c8e36ee400b6916da02937e26560b66f45f",
          "message": "Bump version: 4.1.11 → 5.0.0",
          "timestamp": "2023-06-01T22:07:30+02:00",
          "tree_id": "2dcabd21da2fea9be157faa88ea13e9ff962db45",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/90bb3c8e36ee400b6916da02937e26560b66f45f"
        },
        "date": 1685650332809,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 63.871731363728095,
            "unit": "iter/sec",
            "range": "stddev: 0.0001339139932903419",
            "extra": "mean: 15.656378473684004 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 71.64235287290118,
            "unit": "iter/sec",
            "range": "stddev: 0.00013901914361275482",
            "extra": "mean: 13.95822387037 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 64.33309760814993,
            "unit": "iter/sec",
            "range": "stddev: 0.00011871623284145131",
            "extra": "mean: 15.544098406250484 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 70.64866238929311,
            "unit": "iter/sec",
            "range": "stddev: 0.0001537730494669711",
            "extra": "mean: 14.15454965714328 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 59.84460188135861,
            "unit": "iter/sec",
            "range": "stddev: 0.00017104560896692228",
            "extra": "mean: 16.709944900001027 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 68.3688439920027,
            "unit": "iter/sec",
            "range": "stddev: 0.00021443778056852368",
            "extra": "mean: 14.626545391303868 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 59.220629475365236,
            "unit": "iter/sec",
            "range": "stddev: 0.0002281212088140943",
            "extra": "mean: 16.88600761016873 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 68.68547847910817,
            "unit": "iter/sec",
            "range": "stddev: 0.00019528213974574527",
            "extra": "mean: 14.559118202898835 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 45.90860588195051,
            "unit": "iter/sec",
            "range": "stddev: 0.00038560385719191547",
            "extra": "mean: 21.782408347824855 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 60.79700584991971,
            "unit": "iter/sec",
            "range": "stddev: 0.0002328033350520415",
            "extra": "mean: 16.448178426229532 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 44.79844311353404,
            "unit": "iter/sec",
            "range": "stddev: 0.00027792242989445104",
            "extra": "mean: 22.32220431111121 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 62.186419775183516,
            "unit": "iter/sec",
            "range": "stddev: 0.00029290196003238105",
            "extra": "mean: 16.08068133871032 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 58.1594831593232,
            "unit": "iter/sec",
            "range": "stddev: 0.0002633810216558268",
            "extra": "mean: 17.194100526316248 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 66.13654582589609,
            "unit": "iter/sec",
            "range": "stddev: 0.0001794439596720418",
            "extra": "mean: 15.12023326153881 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 49.33146407623413,
            "unit": "iter/sec",
            "range": "stddev: 0.00015250064597010542",
            "extra": "mean: 20.27103834693929 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 61.97447661747584,
            "unit": "iter/sec",
            "range": "stddev: 0.0002440917767217193",
            "extra": "mean: 16.135674790321918 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 75.82915885616303,
            "unit": "iter/sec",
            "range": "stddev: 0.00014686954229537196",
            "extra": "mean: 13.187539135134752 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 94.21475408537408,
            "unit": "iter/sec",
            "range": "stddev: 0.00009712100994165821",
            "extra": "mean: 10.614048826087634 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 78.35082498591925,
            "unit": "iter/sec",
            "range": "stddev: 0.00014173903011369403",
            "extra": "mean: 12.763107474359257 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 93.56361571271977,
            "unit": "iter/sec",
            "range": "stddev: 0.0001310005927541783",
            "extra": "mean: 10.687915301076295 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 91.21651729235685,
            "unit": "iter/sec",
            "range": "stddev: 0.00008128540250592626",
            "extra": "mean: 10.962926777777682 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 107.33947888730532,
            "unit": "iter/sec",
            "range": "stddev: 0.00006471458939860897",
            "extra": "mean: 9.316236769230922 msec\nrounds: 104"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 91.1095773499905,
            "unit": "iter/sec",
            "range": "stddev: 0.00011950908481940702",
            "extra": "mean: 10.97579452222214 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 106.71253286511785,
            "unit": "iter/sec",
            "range": "stddev: 0.00007310185805790354",
            "extra": "mean: 9.370970523808827 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 64.62884453858307,
            "unit": "iter/sec",
            "range": "stddev: 0.00013206816768728888",
            "extra": "mean: 15.47296732812553 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 103.96652970304217,
            "unit": "iter/sec",
            "range": "stddev: 0.0001020720483073013",
            "extra": "mean: 9.618480128713376 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 64.50401430704974,
            "unit": "iter/sec",
            "range": "stddev: 0.00019203587338303168",
            "extra": "mean: 15.502911109374296 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 103.77084830574765,
            "unit": "iter/sec",
            "range": "stddev: 0.00013019922941418717",
            "extra": "mean: 9.636617762376066 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 68.36145941271755,
            "unit": "iter/sec",
            "range": "stddev: 0.00017239013009559407",
            "extra": "mean: 14.628125388059901 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 95.93910196798014,
            "unit": "iter/sec",
            "range": "stddev: 0.0001430514582149174",
            "extra": "mean: 10.423278720429881 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 65.92229104732561,
            "unit": "iter/sec",
            "range": "stddev: 0.00022062141165838276",
            "extra": "mean: 15.16937570149223 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 95.37753129949837,
            "unit": "iter/sec",
            "range": "stddev: 0.00017570534648979653",
            "extra": "mean: 10.484649648352342 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 80.69922698325371,
            "unit": "iter/sec",
            "range": "stddev: 0.0002478231286953043",
            "extra": "mean: 12.391692428572021 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 97.2660296205062,
            "unit": "iter/sec",
            "range": "stddev: 0.0001855799576250378",
            "extra": "mean: 10.281081729166974 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 69.16472938927228,
            "unit": "iter/sec",
            "range": "stddev: 0.00023129102778206225",
            "extra": "mean: 14.458236283580455 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 89.50958824835783,
            "unit": "iter/sec",
            "range": "stddev: 0.00021947518753672758",
            "extra": "mean: 11.171987488372189 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 59.74502361091185,
            "unit": "iter/sec",
            "range": "stddev: 0.00022727065874972852",
            "extra": "mean: 16.737795711865108 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 87.15087515221094,
            "unit": "iter/sec",
            "range": "stddev: 0.0003555292557317042",
            "extra": "mean: 11.474354081395944 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 66.03484131535326,
            "unit": "iter/sec",
            "range": "stddev: 0.0002234792080100179",
            "extra": "mean: 15.143520906250707 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 89.41451398078827,
            "unit": "iter/sec",
            "range": "stddev: 0.00014514722363412292",
            "extra": "mean: 11.183866639535294 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 94.92493747630408,
            "unit": "iter/sec",
            "range": "stddev: 0.00011164151287883471",
            "extra": "mean: 10.534639543477475 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 103.9897769974811,
            "unit": "iter/sec",
            "range": "stddev: 0.00010230099025866487",
            "extra": "mean: 9.616329882352018 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 95.31263303574262,
            "unit": "iter/sec",
            "range": "stddev: 0.00011872663825287637",
            "extra": "mean: 10.491788634408998 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 103.22685971573702,
            "unit": "iter/sec",
            "range": "stddev: 0.00014427337419210492",
            "extra": "mean: 9.687401154639106 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 90.14140276115843,
            "unit": "iter/sec",
            "range": "stddev: 0.00017135335845505653",
            "extra": "mean: 11.093681364706873 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 102.64065382991345,
            "unit": "iter/sec",
            "range": "stddev: 0.00010306482690114166",
            "extra": "mean: 9.742728272728144 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 91.08839522652856,
            "unit": "iter/sec",
            "range": "stddev: 0.00014164094421502605",
            "extra": "mean: 10.978346885056991 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 100.88814792642506,
            "unit": "iter/sec",
            "range": "stddev: 0.0002302789494521548",
            "extra": "mean: 9.91196706999986 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 72.27266788988202,
            "unit": "iter/sec",
            "range": "stddev: 0.00026289670177829155",
            "extra": "mean: 13.836489356164993 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 94.17425748783684,
            "unit": "iter/sec",
            "range": "stddev: 0.0002382656809092641",
            "extra": "mean: 10.618613054943978 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 71.16387065835507,
            "unit": "iter/sec",
            "range": "stddev: 0.00018392517491376176",
            "extra": "mean: 14.052074328570743 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 93.78477070373819,
            "unit": "iter/sec",
            "range": "stddev: 0.00022508319853847217",
            "extra": "mean: 10.662712000000026 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 87.64607211579671,
            "unit": "iter/sec",
            "range": "stddev: 0.00019811527524760117",
            "extra": "mean: 11.409524418605029 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 95.88104062301637,
            "unit": "iter/sec",
            "range": "stddev: 0.0002250025839593526",
            "extra": "mean: 10.42959059999969 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 72.76992391371887,
            "unit": "iter/sec",
            "range": "stddev: 0.0002295156989649778",
            "extra": "mean: 13.741940986301843 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 90.93077181444575,
            "unit": "iter/sec",
            "range": "stddev: 0.00013375002115634295",
            "extra": "mean: 10.997377235954954 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 65.34299298314633,
            "unit": "iter/sec",
            "range": "stddev: 0.0002720670951326844",
            "extra": "mean: 15.303859746031623 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 86.77609119918995,
            "unit": "iter/sec",
            "range": "stddev: 0.0001391585271823661",
            "extra": "mean: 11.523911554215466 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 68.06295020737392,
            "unit": "iter/sec",
            "range": "stddev: 0.0003626992442208924",
            "extra": "mean: 14.692281144928396 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 89.29169162403865,
            "unit": "iter/sec",
            "range": "stddev: 0.00027238690262626567",
            "extra": "mean: 11.199250252873306 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 99.55296835647725,
            "unit": "iter/sec",
            "range": "stddev: 0.0003512336462409616",
            "extra": "mean: 10.044903898989935 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 98.35436996759181,
            "unit": "iter/sec",
            "range": "stddev: 0.00006537648782537965",
            "extra": "mean: 10.16731641237196 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 98.97115109711021,
            "unit": "iter/sec",
            "range": "stddev: 0.0001978995538910534",
            "extra": "mean: 10.103954424242302 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 96.56583913913983,
            "unit": "iter/sec",
            "range": "stddev: 0.00017132096997067074",
            "extra": "mean: 10.355628956520738 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 99.06321159907554,
            "unit": "iter/sec",
            "range": "stddev: 0.00016348047919805214",
            "extra": "mean: 10.094564711339643 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 97.73927219466748,
            "unit": "iter/sec",
            "range": "stddev: 0.00014903625012208406",
            "extra": "mean: 10.231301886597828 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 101.11379798502962,
            "unit": "iter/sec",
            "range": "stddev: 0.0001161908413655921",
            "extra": "mean: 9.889847082472906 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 99.06761383041285,
            "unit": "iter/sec",
            "range": "stddev: 0.00010610642754996528",
            "extra": "mean: 10.094116142858073 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 64.03508571995411,
            "unit": "iter/sec",
            "range": "stddev: 0.0002379456384512912",
            "extra": "mean: 15.616438843750746 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 63.509583432326515,
            "unit": "iter/sec",
            "range": "stddev: 0.000254469736584355",
            "extra": "mean: 15.745655158729916 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 63.09178206213858,
            "unit": "iter/sec",
            "range": "stddev: 0.0002559189846495098",
            "extra": "mean: 15.849924781251357 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 61.211284398208875,
            "unit": "iter/sec",
            "range": "stddev: 0.0002194357462431104",
            "extra": "mean: 16.336857000002134 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 96.01848877506036,
            "unit": "iter/sec",
            "range": "stddev: 0.0001872888171545951",
            "extra": "mean: 10.414660892473222 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 92.91894521753402,
            "unit": "iter/sec",
            "range": "stddev: 0.0002714097903485869",
            "extra": "mean: 10.762067925533207 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 66.87487225949555,
            "unit": "iter/sec",
            "range": "stddev: 0.0002964437265784154",
            "extra": "mean: 14.953299590908903 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 66.27739888338594,
            "unit": "iter/sec",
            "range": "stddev: 0.00017218589213570523",
            "extra": "mean: 15.088099666667436 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 57.93136830244962,
            "unit": "iter/sec",
            "range": "stddev: 0.00031782673247612555",
            "extra": "mean: 17.26180529310431 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 56.78417055872569,
            "unit": "iter/sec",
            "range": "stddev: 0.0004186271112579207",
            "extra": "mean: 17.61054163793427 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 63.856310402614035,
            "unit": "iter/sec",
            "range": "stddev: 0.00016147119745115102",
            "extra": "mean: 15.660159406251317 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 61.64853051960639,
            "unit": "iter/sec",
            "range": "stddev: 0.00027296751997036347",
            "extra": "mean: 16.220986803277736 msec\nrounds: 61"
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
          "id": "bff8f0e2e16c4ad76f234f2d8c2d07d1ec3988df",
          "message": "Bump version: 5.0.0 → 5.0.1",
          "timestamp": "2023-06-22T23:35:41+02:00",
          "tree_id": "d6b890f04760ae8a42cd3b5df3b83e1df94a2fb1",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/bff8f0e2e16c4ad76f234f2d8c2d07d1ec3988df"
        },
        "date": 1687469993161,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 57.71225130230785,
            "unit": "iter/sec",
            "range": "stddev: 0.0017598071236137034",
            "extra": "mean: 17.32734345714237 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 68.71078040682633,
            "unit": "iter/sec",
            "range": "stddev: 0.0012682573031013434",
            "extra": "mean: 14.55375698076995 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 58.02591350258437,
            "unit": "iter/sec",
            "range": "stddev: 0.002004923259838376",
            "extra": "mean: 17.23367956896468 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 61.34359569684904,
            "unit": "iter/sec",
            "range": "stddev: 0.0012847439168602267",
            "extra": "mean: 16.301620220338105 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 52.46656125697487,
            "unit": "iter/sec",
            "range": "stddev: 0.0013568572545615387",
            "extra": "mean: 19.059758749999283 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 60.68375408355307,
            "unit": "iter/sec",
            "range": "stddev: 0.0008295310439690565",
            "extra": "mean: 16.47887503174473 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 49.985477258644586,
            "unit": "iter/sec",
            "range": "stddev: 0.0013913800983498582",
            "extra": "mean: 20.00581078431252 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 58.58056473032089,
            "unit": "iter/sec",
            "range": "stddev: 0.001334967680813779",
            "extra": "mean: 17.0705080192306 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 35.75662563841981,
            "unit": "iter/sec",
            "range": "stddev: 0.0018187817698909253",
            "extra": "mean: 27.966844805554558 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 54.20717389042174,
            "unit": "iter/sec",
            "range": "stddev: 0.0019375095299644565",
            "extra": "mean: 18.447742765956985 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 40.66313685233884,
            "unit": "iter/sec",
            "range": "stddev: 0.002164008778078505",
            "extra": "mean: 24.592298514286476 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 57.67680721674516,
            "unit": "iter/sec",
            "range": "stddev: 0.0012067308801223362",
            "extra": "mean: 17.337991616666198 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 52.749221826701415,
            "unit": "iter/sec",
            "range": "stddev: 0.0012552250947705762",
            "extra": "mean: 18.957625636361605 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 60.20286322159647,
            "unit": "iter/sec",
            "range": "stddev: 0.0011396740324187298",
            "extra": "mean: 16.610505655174084 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 43.32256613752807,
            "unit": "iter/sec",
            "range": "stddev: 0.0020132976305085276",
            "extra": "mean: 23.082658511628477 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 54.154376461567054,
            "unit": "iter/sec",
            "range": "stddev: 0.0012762069357627188",
            "extra": "mean: 18.465728263156944 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 62.88683697943456,
            "unit": "iter/sec",
            "range": "stddev: 0.002177544633799446",
            "extra": "mean: 15.90157890000133 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 78.69247632852668,
            "unit": "iter/sec",
            "range": "stddev: 0.0014686507613288506",
            "extra": "mean: 12.707695152776525 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 67.7942032837591,
            "unit": "iter/sec",
            "range": "stddev: 0.000962366662739443",
            "extra": "mean: 14.750523666668148 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 83.20864298322608,
            "unit": "iter/sec",
            "range": "stddev: 0.0013579061120836734",
            "extra": "mean: 12.017982317072383 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 78.19748562184925,
            "unit": "iter/sec",
            "range": "stddev: 0.000938513002196439",
            "extra": "mean: 12.788134964285717 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 94.13382600944533,
            "unit": "iter/sec",
            "range": "stddev: 0.0013226165038097107",
            "extra": "mean: 10.623173862068038 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 74.92941949919705,
            "unit": "iter/sec",
            "range": "stddev: 0.001614105760814282",
            "extra": "mean: 13.345892797297275 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 95.58568634480511,
            "unit": "iter/sec",
            "range": "stddev: 0.0007775777776621897",
            "extra": "mean: 10.461817435643155 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 57.005940589068175,
            "unit": "iter/sec",
            "range": "stddev: 0.0012580857637343778",
            "extra": "mean: 17.542031403508958 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 92.16185710557849,
            "unit": "iter/sec",
            "range": "stddev: 0.0007482824874664903",
            "extra": "mean: 10.850475797752459 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 54.73921235842491,
            "unit": "iter/sec",
            "range": "stddev: 0.0022331826074547894",
            "extra": "mean: 18.268439696430708 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 86.62068103750354,
            "unit": "iter/sec",
            "range": "stddev: 0.0015422827507492061",
            "extra": "mean: 11.544587135802326 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 60.415906039167844,
            "unit": "iter/sec",
            "range": "stddev: 0.0014907810892920278",
            "extra": "mean: 16.551932521738504 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 86.70706936021077,
            "unit": "iter/sec",
            "range": "stddev: 0.0009324772704114531",
            "extra": "mean: 11.533084988095476 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 57.64457072059446,
            "unit": "iter/sec",
            "range": "stddev: 0.0014682087541406754",
            "extra": "mean: 17.347687518518267 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 76.39967458164689,
            "unit": "iter/sec",
            "range": "stddev: 0.0022067299461463715",
            "extra": "mean: 13.089060987181547 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 73.71814427580335,
            "unit": "iter/sec",
            "range": "stddev: 0.0010082295368540794",
            "extra": "mean: 13.56518140579716 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 80.82206657015385,
            "unit": "iter/sec",
            "range": "stddev: 0.001148970056084894",
            "extra": "mean: 12.372858582278347 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 60.651697930949446,
            "unit": "iter/sec",
            "range": "stddev: 0.0021141362510960294",
            "extra": "mean: 16.48758458730169 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 80.38649938107514,
            "unit": "iter/sec",
            "range": "stddev: 0.0008714396819824244",
            "extra": "mean: 12.43989983018745 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 51.4386435902901,
            "unit": "iter/sec",
            "range": "stddev: 0.0015627350303478915",
            "extra": "mean: 19.44063704255154 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 77.06668140661975,
            "unit": "iter/sec",
            "range": "stddev: 0.001394463253510484",
            "extra": "mean: 12.97577606493516 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 57.47798767488486,
            "unit": "iter/sec",
            "range": "stddev: 0.0014179436332656028",
            "extra": "mean: 17.397964689653747 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 80.52256384297337,
            "unit": "iter/sec",
            "range": "stddev: 0.0009301604069559369",
            "extra": "mean: 12.418879283949463 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 82.67324374577068,
            "unit": "iter/sec",
            "range": "stddev: 0.000975888921081495",
            "extra": "mean: 12.095811833331593 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 91.03348219523889,
            "unit": "iter/sec",
            "range": "stddev: 0.0009562275054345517",
            "extra": "mean: 10.98496922105327 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 84.0039352301315,
            "unit": "iter/sec",
            "range": "stddev: 0.0007895938799701145",
            "extra": "mean: 11.90420421686755 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 92.5049545958697,
            "unit": "iter/sec",
            "range": "stddev: 0.0009861843668735545",
            "extra": "mean: 10.810231780219148 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 79.64861917808773,
            "unit": "iter/sec",
            "range": "stddev: 0.000893637425492606",
            "extra": "mean: 12.555145466666318 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 91.51501769890174,
            "unit": "iter/sec",
            "range": "stddev: 0.0009569493581258732",
            "extra": "mean: 10.927168295920035 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 77.99738376606177,
            "unit": "iter/sec",
            "range": "stddev: 0.0013417269402594707",
            "extra": "mean: 12.82094285366428 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 87.29177302953478,
            "unit": "iter/sec",
            "range": "stddev: 0.0009604593945076123",
            "extra": "mean: 11.455833296703165 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 64.44480653883626,
            "unit": "iter/sec",
            "range": "stddev: 0.0009921816775018718",
            "extra": "mean: 15.517154192981739 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 82.96225787875538,
            "unit": "iter/sec",
            "range": "stddev: 0.0012309112141007524",
            "extra": "mean: 12.053673870128307 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 60.058709161369386,
            "unit": "iter/sec",
            "range": "stddev: 0.0011403545755957378",
            "extra": "mean: 16.65037450793588 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 78.84642050813312,
            "unit": "iter/sec",
            "range": "stddev: 0.0015073421865924017",
            "extra": "mean: 12.68288393506524 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 73.93651406209405,
            "unit": "iter/sec",
            "range": "stddev: 0.001626422623500658",
            "extra": "mean: 13.525116955881511 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 81.9868329571384,
            "unit": "iter/sec",
            "range": "stddev: 0.0007688680619839268",
            "extra": "mean: 12.197080481481535 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 56.898841766448356,
            "unit": "iter/sec",
            "range": "stddev: 0.001492156412069985",
            "extra": "mean: 17.575050193546677 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 73.69457967007327,
            "unit": "iter/sec",
            "range": "stddev: 0.0013890911301567867",
            "extra": "mean: 13.569519013161443 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 54.6788633187884,
            "unit": "iter/sec",
            "range": "stddev: 0.0012985641473372317",
            "extra": "mean: 18.28860256603737 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 77.75121709807681,
            "unit": "iter/sec",
            "range": "stddev: 0.0010471552208450806",
            "extra": "mean: 12.86153500000626 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 56.43127312056366,
            "unit": "iter/sec",
            "range": "stddev: 0.0018235216888610952",
            "extra": "mean: 17.720670555554026 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 77.6358826863574,
            "unit": "iter/sec",
            "range": "stddev: 0.0009889350369504102",
            "extra": "mean: 12.88064185526064 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 84.42793886090408,
            "unit": "iter/sec",
            "range": "stddev: 0.000910668374592818",
            "extra": "mean: 11.844420383725234 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 81.19978042889538,
            "unit": "iter/sec",
            "range": "stddev: 0.0016241239668602714",
            "extra": "mean: 12.315304237499447 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 84.32875848996972,
            "unit": "iter/sec",
            "range": "stddev: 0.0011842399298547409",
            "extra": "mean: 11.858350791669045 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 88.4055741628886,
            "unit": "iter/sec",
            "range": "stddev: 0.0007528218209877863",
            "extra": "mean: 11.311503934780006 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 89.6498982596866,
            "unit": "iter/sec",
            "range": "stddev: 0.0007478280516732897",
            "extra": "mean: 11.154502340909806 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 89.4540280842523,
            "unit": "iter/sec",
            "range": "stddev: 0.001287246880355535",
            "extra": "mean: 11.178926443179838 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 83.93802901484759,
            "unit": "iter/sec",
            "range": "stddev: 0.0012035367816451929",
            "extra": "mean: 11.913551124998568 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 87.29041969459178,
            "unit": "iter/sec",
            "range": "stddev: 0.0009856464428118661",
            "extra": "mean: 11.456010905879019 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 58.51141886030691,
            "unit": "iter/sec",
            "range": "stddev: 0.0011225938934438663",
            "extra": "mean: 17.090681092308667 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 56.97171375957516,
            "unit": "iter/sec",
            "range": "stddev: 0.0011593954873746375",
            "extra": "mean: 17.55257010909087 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 56.75543505391079,
            "unit": "iter/sec",
            "range": "stddev: 0.001393014576729859",
            "extra": "mean: 17.61945792592588 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 58.47332442762716,
            "unit": "iter/sec",
            "range": "stddev: 0.0009260661619930418",
            "extra": "mean: 17.10181539682607 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 87.43929122242866,
            "unit": "iter/sec",
            "range": "stddev: 0.001124368072202596",
            "extra": "mean: 11.436506243585542 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 88.09283076699037,
            "unit": "iter/sec",
            "range": "stddev: 0.0008877944445102821",
            "extra": "mean: 11.351661551722028 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 62.12312415369857,
            "unit": "iter/sec",
            "range": "stddev: 0.0010058011928889973",
            "extra": "mean: 16.097065523071635 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 56.103127252657664,
            "unit": "iter/sec",
            "range": "stddev: 0.0015145496821684485",
            "extra": "mean: 17.824318339627474 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 48.729750397897696,
            "unit": "iter/sec",
            "range": "stddev: 0.0018123696983872487",
            "extra": "mean: 20.52134459615747 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 46.43507751091668,
            "unit": "iter/sec",
            "range": "stddev: 0.0023611230824014252",
            "extra": "mean: 21.535443755098818 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 49.39689635019785,
            "unit": "iter/sec",
            "range": "stddev: 0.0019248887741244857",
            "extra": "mean: 20.244186859646593 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 50.29199307658821,
            "unit": "iter/sec",
            "range": "stddev: 0.001913535761687762",
            "extra": "mean: 19.883880888894762 msec\nrounds: 54"
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
          "id": "6d71e7d380cd815b8f65a1917653769d882c2aa6",
          "message": "update changelog",
          "timestamp": "2023-06-22T23:56:33+02:00",
          "tree_id": "ead1265affae147808efd7b4f89123794e829143",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/6d71e7d380cd815b8f65a1917653769d882c2aa6"
        },
        "date": 1687471250603,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 46.26816931922933,
            "unit": "iter/sec",
            "range": "stddev: 0.0029722556621949985",
            "extra": "mean: 21.61313090000287 msec\nrounds: 30"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 57.99421295981338,
            "unit": "iter/sec",
            "range": "stddev: 0.0013890245963694581",
            "extra": "mean: 17.243099767436135 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 51.728250440450104,
            "unit": "iter/sec",
            "range": "stddev: 0.0012987755937764103",
            "extra": "mean: 19.33179629091083 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 59.27783907096113,
            "unit": "iter/sec",
            "range": "stddev: 0.0015526552767169883",
            "extra": "mean: 16.869710766664525 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 48.50472498623066,
            "unit": "iter/sec",
            "range": "stddev: 0.0014496458462683207",
            "extra": "mean: 20.61654818749877 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 56.47915501284611,
            "unit": "iter/sec",
            "range": "stddev: 0.0013389046107358557",
            "extra": "mean: 17.705647327275898 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 47.821239377262124,
            "unit": "iter/sec",
            "range": "stddev: 0.0012465877039378474",
            "extra": "mean: 20.911210437500216 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 54.811843006290616,
            "unit": "iter/sec",
            "range": "stddev: 0.0015395974525522968",
            "extra": "mean: 18.24423236206877 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 33.827354025269294,
            "unit": "iter/sec",
            "range": "stddev: 0.0024415657764573252",
            "extra": "mean: 29.561874666667464 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 48.60811900459025,
            "unit": "iter/sec",
            "range": "stddev: 0.0016079224825305736",
            "extra": "mean: 20.572694859999956 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 35.049105978311815,
            "unit": "iter/sec",
            "range": "stddev: 0.0013059948858434541",
            "extra": "mean: 28.531398222219824 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 51.518386174368565,
            "unit": "iter/sec",
            "range": "stddev: 0.0012789137757016618",
            "extra": "mean: 19.410545909093713 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 46.29638305542079,
            "unit": "iter/sec",
            "range": "stddev: 0.0021043086987739784",
            "extra": "mean: 21.59995952173873 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 55.52013662150639,
            "unit": "iter/sec",
            "range": "stddev: 0.0007255274927413865",
            "extra": "mean: 18.0114830555485 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 38.50083148053053,
            "unit": "iter/sec",
            "range": "stddev: 0.0018551291557660696",
            "extra": "mean: 25.973465027779714 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 51.78676180557459,
            "unit": "iter/sec",
            "range": "stddev: 0.0010971302198118941",
            "extra": "mean: 19.30995422641689 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 59.41477309527904,
            "unit": "iter/sec",
            "range": "stddev: 0.0013661017890304003",
            "extra": "mean: 16.83083091803405 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 77.78433929107533,
            "unit": "iter/sec",
            "range": "stddev: 0.0003108185873212901",
            "extra": "mean: 12.85605829031881 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 60.36886010863326,
            "unit": "iter/sec",
            "range": "stddev: 0.0009076746620460068",
            "extra": "mean: 16.564831573770125 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 73.79878744830683,
            "unit": "iter/sec",
            "range": "stddev: 0.0003861143976718837",
            "extra": "mean: 13.550358136987834 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 67.90103752852909,
            "unit": "iter/sec",
            "range": "stddev: 0.001112684452025267",
            "extra": "mean: 14.72731546377098 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 83.40085030521475,
            "unit": "iter/sec",
            "range": "stddev: 0.0006206888203374506",
            "extra": "mean: 11.99028542683184 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 69.73420910297627,
            "unit": "iter/sec",
            "range": "stddev: 0.0007211416154551178",
            "extra": "mean: 14.340164072461244 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 82.55287111900498,
            "unit": "iter/sec",
            "range": "stddev: 0.0008095754652295277",
            "extra": "mean: 12.113449071425261 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 48.779041963978194,
            "unit": "iter/sec",
            "range": "stddev: 0.0016706934544117023",
            "extra": "mean: 20.500607632648236 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 82.42142133759674,
            "unit": "iter/sec",
            "range": "stddev: 0.0005518294553247343",
            "extra": "mean: 12.132768202382934 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 49.68230239371079,
            "unit": "iter/sec",
            "range": "stddev: 0.0013731845370421097",
            "extra": "mean: 20.127891660000614 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 80.45181814391411,
            "unit": "iter/sec",
            "range": "stddev: 0.00046417580574407714",
            "extra": "mean: 12.429799886078104 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 53.20327292348164,
            "unit": "iter/sec",
            "range": "stddev: 0.001066919417900356",
            "extra": "mean: 18.79583614034848 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 76.71463582051253,
            "unit": "iter/sec",
            "range": "stddev: 0.0005011985999064756",
            "extra": "mean: 13.03532226027478 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 51.81465293037419,
            "unit": "iter/sec",
            "range": "stddev: 0.0010714689412778776",
            "extra": "mean: 19.29955993999897 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 76.0988977035895,
            "unit": "iter/sec",
            "range": "stddev: 0.00048130300007537854",
            "extra": "mean: 13.140794810130755 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 66.75424108352219,
            "unit": "iter/sec",
            "range": "stddev: 0.0005006619885660129",
            "extra": "mean: 14.98032160606561 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 77.84174795990391,
            "unit": "iter/sec",
            "range": "stddev: 0.00041668347917146097",
            "extra": "mean: 12.84657688461849 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 55.49760613244393,
            "unit": "iter/sec",
            "range": "stddev: 0.000623410695370473",
            "extra": "mean: 18.01879521818509 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 67.85299589569219,
            "unit": "iter/sec",
            "range": "stddev: 0.0017607658390202431",
            "extra": "mean: 14.737742774648622 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 46.57665719195571,
            "unit": "iter/sec",
            "range": "stddev: 0.0008837164110090919",
            "extra": "mean: 21.46998218181941 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 72.22293167879926,
            "unit": "iter/sec",
            "range": "stddev: 0.0005572872923077981",
            "extra": "mean: 13.846017833329604 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 50.57596189248169,
            "unit": "iter/sec",
            "range": "stddev: 0.001783670278869755",
            "extra": "mean: 19.77223887754973 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 69.39709231988246,
            "unit": "iter/sec",
            "range": "stddev: 0.0009084419465655552",
            "extra": "mean: 14.40982563636167 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 71.74681459888188,
            "unit": "iter/sec",
            "range": "stddev: 0.0006549932192101165",
            "extra": "mean: 13.937901014710471 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 80.88145100580982,
            "unit": "iter/sec",
            "range": "stddev: 0.0008798370871802729",
            "extra": "mean: 12.363774234566694 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 72.83461710484718,
            "unit": "iter/sec",
            "range": "stddev: 0.0005800764412790999",
            "extra": "mean: 13.729735114286054 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 83.31988031367958,
            "unit": "iter/sec",
            "range": "stddev: 0.0006818591884967637",
            "extra": "mean: 12.001937547620537 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 67.25197454974311,
            "unit": "iter/sec",
            "range": "stddev: 0.0010236572284817494",
            "extra": "mean: 14.869451888886134 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 78.03746781726542,
            "unit": "iter/sec",
            "range": "stddev: 0.0013119674407900564",
            "extra": "mean: 12.814357358975643 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 68.05926964805633,
            "unit": "iter/sec",
            "range": "stddev: 0.0009442567881619685",
            "extra": "mean: 14.693075684930722 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 79.76753115230312,
            "unit": "iter/sec",
            "range": "stddev: 0.0006399080248781433",
            "extra": "mean: 12.536429115383587 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 54.92640539611009,
            "unit": "iter/sec",
            "range": "stddev: 0.0020186049299153576",
            "extra": "mean: 18.206179574074593 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 76.8609012477984,
            "unit": "iter/sec",
            "range": "stddev: 0.0008278752287974723",
            "extra": "mean: 13.010516189187204 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 56.411609808377584,
            "unit": "iter/sec",
            "range": "stddev: 0.0010850168991669025",
            "extra": "mean: 17.726847423728223 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 75.03285149269622,
            "unit": "iter/sec",
            "range": "stddev: 0.0012475216414199175",
            "extra": "mean: 13.327495624997551 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 69.58289217201812,
            "unit": "iter/sec",
            "range": "stddev: 0.0007482989855563507",
            "extra": "mean: 14.371348599995924 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 77.06379116100238,
            "unit": "iter/sec",
            "range": "stddev: 0.0015341704588874632",
            "extra": "mean: 12.976262716050275 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 56.91238944614893,
            "unit": "iter/sec",
            "range": "stddev: 0.0018231158763892693",
            "extra": "mean: 17.570866550001558 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 73.43898760314302,
            "unit": "iter/sec",
            "range": "stddev: 0.0009001327115327535",
            "extra": "mean: 13.616745445946238 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 50.88941797056561,
            "unit": "iter/sec",
            "range": "stddev: 0.0007305242497977713",
            "extra": "mean: 19.65045071999839 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 70.35517807019583,
            "unit": "iter/sec",
            "range": "stddev: 0.001564915097890233",
            "extra": "mean: 14.213594897055975 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 53.75739564926863,
            "unit": "iter/sec",
            "range": "stddev: 0.0009109693581406506",
            "extra": "mean: 18.60209163636455 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 67.72777376703347,
            "unit": "iter/sec",
            "range": "stddev: 0.002012357044605019",
            "extra": "mean: 14.764991441173732 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 73.18253394384443,
            "unit": "iter/sec",
            "range": "stddev: 0.001314250797533784",
            "extra": "mean: 13.664462626660832 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 74.0322051937649,
            "unit": "iter/sec",
            "range": "stddev: 0.001837300558468994",
            "extra": "mean: 13.507634918920683 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 76.32100086345672,
            "unit": "iter/sec",
            "range": "stddev: 0.00132868359334591",
            "extra": "mean: 13.102553539478155 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 77.46557129831695,
            "unit": "iter/sec",
            "range": "stddev: 0.0007319554004735868",
            "extra": "mean: 12.908960500001196 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 77.92490151570838,
            "unit": "iter/sec",
            "range": "stddev: 0.001367733109694749",
            "extra": "mean: 12.832868319999307 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 76.29809652068371,
            "unit": "iter/sec",
            "range": "stddev: 0.0009049947632726969",
            "extra": "mean: 13.106486866666575 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 75.91223831674178,
            "unit": "iter/sec",
            "range": "stddev: 0.0010986634517818666",
            "extra": "mean: 13.173106500002367 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 75.5437076032684,
            "unit": "iter/sec",
            "range": "stddev: 0.0009042929716563316",
            "extra": "mean: 13.237369884619419 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 48.18578313871159,
            "unit": "iter/sec",
            "range": "stddev: 0.0016667460968969275",
            "extra": "mean: 20.75300918366974 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 47.23745848949379,
            "unit": "iter/sec",
            "range": "stddev: 0.001980276774161889",
            "extra": "mean: 21.169640196083215 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 47.789627842353006,
            "unit": "iter/sec",
            "range": "stddev: 0.0015263546446566084",
            "extra": "mean: 20.92504263265598 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 49.038975834723665,
            "unit": "iter/sec",
            "range": "stddev: 0.000843438074492831",
            "extra": "mean: 20.39194299999873 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 75.03992401394649,
            "unit": "iter/sec",
            "range": "stddev: 0.0009298447045677169",
            "extra": "mean: 13.326239507040887 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 74.70805138422855,
            "unit": "iter/sec",
            "range": "stddev: 0.0009780230966658845",
            "extra": "mean: 13.385438135133956 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 51.02841252090916,
            "unit": "iter/sec",
            "range": "stddev: 0.0012699564399354089",
            "extra": "mean: 19.596925528307292 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 51.215955751657766,
            "unit": "iter/sec",
            "range": "stddev: 0.0015936304108515604",
            "extra": "mean: 19.525165260000676 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 45.92155596107772,
            "unit": "iter/sec",
            "range": "stddev: 0.0010684239065844455",
            "extra": "mean: 21.776265613638657 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 44.595852664036215,
            "unit": "iter/sec",
            "range": "stddev: 0.0006944059335421432",
            "extra": "mean: 22.42360982608676 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 46.42137889276884,
            "unit": "iter/sec",
            "range": "stddev: 0.0017693259780230718",
            "extra": "mean: 21.541798711105763 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 47.00053613512582,
            "unit": "iter/sec",
            "range": "stddev: 0.0010393617969046709",
            "extra": "mean: 21.276353042548603 msec\nrounds: 47"
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
          "id": "efc8f47b20b05914ecee54dfb43c7661efb2f168",
          "message": "do not try to assign attribute (#624)",
          "timestamp": "2023-07-12T00:05:39+02:00",
          "tree_id": "f843b65ba731cfb8304191a9ba396f3fce265381",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/efc8f47b20b05914ecee54dfb43c7661efb2f168"
        },
        "date": 1689113382103,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 50.63164287748001,
            "unit": "iter/sec",
            "range": "stddev: 0.0009083123441143951",
            "extra": "mean: 19.750494812499575 msec\nrounds: 32"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 59.02239669766943,
            "unit": "iter/sec",
            "range": "stddev: 0.0008541173774031266",
            "extra": "mean: 16.942721000001107 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 51.61499046942046,
            "unit": "iter/sec",
            "range": "stddev: 0.000752124862500096",
            "extra": "mean: 19.374216500000223 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 59.05960835264776,
            "unit": "iter/sec",
            "range": "stddev: 0.000540151754495207",
            "extra": "mean: 16.932045909091578 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 48.07094675268668,
            "unit": "iter/sec",
            "range": "stddev: 0.0015654642292514832",
            "extra": "mean: 20.802585918366795 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 56.73162533671371,
            "unit": "iter/sec",
            "range": "stddev: 0.0005727550153139746",
            "extra": "mean: 17.626852642856555 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 47.92774107018639,
            "unit": "iter/sec",
            "range": "stddev: 0.0009759613266314706",
            "extra": "mean: 20.864743000000335 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 56.6662706854202,
            "unit": "iter/sec",
            "range": "stddev: 0.000918944371748139",
            "extra": "mean: 17.647182140350242 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 37.05802731206629,
            "unit": "iter/sec",
            "range": "stddev: 0.000666680323156154",
            "extra": "mean: 26.984706756756985 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 50.584667558659426,
            "unit": "iter/sec",
            "range": "stddev: 0.001326722925689958",
            "extra": "mean: 19.768836057692212 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 35.84454413027357,
            "unit": "iter/sec",
            "range": "stddev: 0.0014310263839983446",
            "extra": "mean: 27.89824851351424 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 50.98010017083575,
            "unit": "iter/sec",
            "range": "stddev: 0.001199105141396775",
            "extra": "mean: 19.615496961539343 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 47.44580899085591,
            "unit": "iter/sec",
            "range": "stddev: 0.00043886230857183685",
            "extra": "mean: 21.076677187498838 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 52.66716631377889,
            "unit": "iter/sec",
            "range": "stddev: 0.0015395786553485443",
            "extra": "mean: 18.987161641509807 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 37.815590721408846,
            "unit": "iter/sec",
            "range": "stddev: 0.0018392310233658",
            "extra": "mean: 26.444119499999292 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 50.365009195460004,
            "unit": "iter/sec",
            "range": "stddev: 0.00045998616759876186",
            "extra": "mean: 19.85505445098066 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 59.55690125492412,
            "unit": "iter/sec",
            "range": "stddev: 0.00036944487703146055",
            "extra": "mean: 16.790665379309353 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 75.45491580099574,
            "unit": "iter/sec",
            "range": "stddev: 0.0008246505510667037",
            "extra": "mean: 13.252946999999217 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 60.639579864342245,
            "unit": "iter/sec",
            "range": "stddev: 0.0006227150565812016",
            "extra": "mean: 16.490879426228148 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 74.32014034371966,
            "unit": "iter/sec",
            "range": "stddev: 0.0005840793874919949",
            "extra": "mean: 13.455302901409333 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 69.74144316549794,
            "unit": "iter/sec",
            "range": "stddev: 0.0005709630768925009",
            "extra": "mean: 14.338676611939022 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 84.0334924142614,
            "unit": "iter/sec",
            "range": "stddev: 0.0004873284425294529",
            "extra": "mean: 11.900017139241127 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 69.73048677721845,
            "unit": "iter/sec",
            "range": "stddev: 0.00043813769294029614",
            "extra": "mean: 14.340929573529216 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 82.94836943237077,
            "unit": "iter/sec",
            "range": "stddev: 0.0008606557856761143",
            "extra": "mean: 12.055692074999946 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 45.6711133843463,
            "unit": "iter/sec",
            "range": "stddev: 0.0005753009396616181",
            "extra": "mean: 21.895678162791373 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 80.91130772690485,
            "unit": "iter/sec",
            "range": "stddev: 0.0006164871401797455",
            "extra": "mean: 12.35921193333373 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 45.8472812702341,
            "unit": "iter/sec",
            "range": "stddev: 0.0007807298515164948",
            "extra": "mean: 21.81154415909151 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 79.83744808156067,
            "unit": "iter/sec",
            "range": "stddev: 0.0008920296357149428",
            "extra": "mean: 12.525450449999553 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 54.07661899839363,
            "unit": "iter/sec",
            "range": "stddev: 0.0009475261717988092",
            "extra": "mean: 18.49228037037052 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 77.00265464625492,
            "unit": "iter/sec",
            "range": "stddev: 0.0004865696851434054",
            "extra": "mean: 12.98656526315792 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 51.79568931371758,
            "unit": "iter/sec",
            "range": "stddev: 0.0005181090984707715",
            "extra": "mean: 19.30662596153846 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 75.4354437820028,
            "unit": "iter/sec",
            "range": "stddev: 0.0005066663000343543",
            "extra": "mean: 13.256367959998368 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 64.41923260111112,
            "unit": "iter/sec",
            "range": "stddev: 0.0010116499350233627",
            "extra": "mean: 15.52331438333141 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 77.72819056826687,
            "unit": "iter/sec",
            "range": "stddev: 0.00029331940747605697",
            "extra": "mean: 12.865345155844366 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 54.846180121060236,
            "unit": "iter/sec",
            "range": "stddev: 0.00044822724062025093",
            "extra": "mean: 18.232810339621313 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 72.01417610917686,
            "unit": "iter/sec",
            "range": "stddev: 0.0004944722338840021",
            "extra": "mean: 13.886154838235646 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 46.90245028035241,
            "unit": "iter/sec",
            "range": "stddev: 0.0006574055580275594",
            "extra": "mean: 21.320847717393203 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 68.52135806026534,
            "unit": "iter/sec",
            "range": "stddev: 0.0003728863243599792",
            "extra": "mean: 14.59398979104425 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 49.63399734530397,
            "unit": "iter/sec",
            "range": "stddev: 0.0016189827820344126",
            "extra": "mean: 20.147480627905 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 70.15365932957417,
            "unit": "iter/sec",
            "range": "stddev: 0.0004024273673260089",
            "extra": "mean: 14.254423925373729 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 70.54214220512311,
            "unit": "iter/sec",
            "range": "stddev: 0.00157259140368217",
            "extra": "mean: 14.175923338026658 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 80.76489814661876,
            "unit": "iter/sec",
            "range": "stddev: 0.0006952290113080334",
            "extra": "mean: 12.381616555556386 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 72.66627130091834,
            "unit": "iter/sec",
            "range": "stddev: 0.0003181954295932186",
            "extra": "mean: 13.76154276388972 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 80.78999656666998,
            "unit": "iter/sec",
            "range": "stddev: 0.00037531501528055827",
            "extra": "mean: 12.37777005194912 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 67.98051871114203,
            "unit": "iter/sec",
            "range": "stddev: 0.0010135161762644678",
            "extra": "mean: 14.710096641791287 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 78.76687121735519,
            "unit": "iter/sec",
            "range": "stddev: 0.00046011449938416224",
            "extra": "mean: 12.695692802631772 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 68.14539276121198,
            "unit": "iter/sec",
            "range": "stddev: 0.0005211541514443752",
            "extra": "mean: 14.674506367643906 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 79.17879694084178,
            "unit": "iter/sec",
            "range": "stddev: 0.0011834758829969703",
            "extra": "mean: 12.629643776314856 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 55.0834750374619,
            "unit": "iter/sec",
            "range": "stddev: 0.0017048449206081432",
            "extra": "mean: 18.15426494642734 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 73.88187706585445,
            "unit": "iter/sec",
            "range": "stddev: 0.0007263182585266864",
            "extra": "mean: 13.535119026668099 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 54.2625528635013,
            "unit": "iter/sec",
            "range": "stddev: 0.0006912843691562806",
            "extra": "mean: 18.42891547169782 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 72.85325482149997,
            "unit": "iter/sec",
            "range": "stddev: 0.0005787059451057077",
            "extra": "mean: 13.726222698630707 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 66.05931108822807,
            "unit": "iter/sec",
            "range": "stddev: 0.0010039267595790516",
            "extra": "mean: 15.137911424241334 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 75.80981439325454,
            "unit": "iter/sec",
            "range": "stddev: 0.0004114109298332085",
            "extra": "mean: 13.19090421211978 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 56.73180677894898,
            "unit": "iter/sec",
            "range": "stddev: 0.000445887483807909",
            "extra": "mean: 17.626796267857664 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 70.36986874490476,
            "unit": "iter/sec",
            "range": "stddev: 0.0007087058520705099",
            "extra": "mean: 14.210627614285645 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 50.72587794866219,
            "unit": "iter/sec",
            "range": "stddev: 0.0012609527527099893",
            "extra": "mean: 19.71380369230994 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 69.21461055583237,
            "unit": "iter/sec",
            "range": "stddev: 0.0005795592059662228",
            "extra": "mean: 14.44781660937533 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 53.06390713678244,
            "unit": "iter/sec",
            "range": "stddev: 0.0012484798222871022",
            "extra": "mean: 18.845201078433735 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 70.05575269969853,
            "unit": "iter/sec",
            "range": "stddev: 0.00043105114373874606",
            "extra": "mean: 14.274345238807252 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 74.86414418726922,
            "unit": "iter/sec",
            "range": "stddev: 0.00056653328570252",
            "extra": "mean: 13.3575293066671 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 72.30576960108327,
            "unit": "iter/sec",
            "range": "stddev: 0.001173627034436965",
            "extra": "mean: 13.830154986484208 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 74.99608559904682,
            "unit": "iter/sec",
            "range": "stddev: 0.0010468852723113926",
            "extra": "mean: 13.334029263158099 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 73.83727202977474,
            "unit": "iter/sec",
            "range": "stddev: 0.0012000187171158922",
            "extra": "mean: 13.54329558108203 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 75.90924037022417,
            "unit": "iter/sec",
            "range": "stddev: 0.0005010663248876514",
            "extra": "mean: 13.173626756410748 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 74.4161712921586,
            "unit": "iter/sec",
            "range": "stddev: 0.0003624581608985239",
            "extra": "mean: 13.437939397258031 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 77.04629661675581,
            "unit": "iter/sec",
            "range": "stddev: 0.000574386629987659",
            "extra": "mean: 12.97920917567533 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 73.91217794991252,
            "unit": "iter/sec",
            "range": "stddev: 0.0007154872036066059",
            "extra": "mean: 13.52957019718269 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 48.68348603021226,
            "unit": "iter/sec",
            "range": "stddev: 0.0012293160115931985",
            "extra": "mean: 20.540846219997775 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 48.40994617119004,
            "unit": "iter/sec",
            "range": "stddev: 0.0012394756159946575",
            "extra": "mean: 20.656912041664793 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 48.418101197921246,
            "unit": "iter/sec",
            "range": "stddev: 0.0012633865599640693",
            "extra": "mean: 20.653432812498096 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 47.15558475516452,
            "unit": "iter/sec",
            "range": "stddev: 0.0012797110854593508",
            "extra": "mean: 21.20639591666773 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 74.91624356375988,
            "unit": "iter/sec",
            "range": "stddev: 0.00034122158271384696",
            "extra": "mean: 13.348240013514797 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 70.77911626326012,
            "unit": "iter/sec",
            "range": "stddev: 0.0010894474843693971",
            "extra": "mean: 14.128461229729679 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 52.032082149339935,
            "unit": "iter/sec",
            "range": "stddev: 0.0008539692095015524",
            "extra": "mean: 19.21891184615386 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 51.876115116369725,
            "unit": "iter/sec",
            "range": "stddev: 0.0012405326035996862",
            "extra": "mean: 19.2766940576945 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 45.05618258158624,
            "unit": "iter/sec",
            "range": "stddev: 0.0007528862373165433",
            "extra": "mean: 22.19451233333479 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 44.807271651333195,
            "unit": "iter/sec",
            "range": "stddev: 0.0004932140619453487",
            "extra": "mean: 22.317806086955663 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 48.10715076309823,
            "unit": "iter/sec",
            "range": "stddev: 0.0008105762324625988",
            "extra": "mean: 20.78693051110968 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 47.541915509352854,
            "unit": "iter/sec",
            "range": "stddev: 0.0011396590586808825",
            "extra": "mean: 21.034070446809647 msec\nrounds: 47"
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
          "id": "584ecdbc204f4c2870250e777e69db89a7f3157f",
          "message": "Bump version: 5.0.1 → 5.0.2",
          "timestamp": "2023-07-12T00:07:13+02:00",
          "tree_id": "1b44f0e388a7d754594ae47d1f3b5125a30a8459",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/584ecdbc204f4c2870250e777e69db89a7f3157f"
        },
        "date": 1689113478608,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 62.50313076578838,
            "unit": "iter/sec",
            "range": "stddev: 0.00024720080415400623",
            "extra": "mean: 15.999198564103905 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 69.74978304740458,
            "unit": "iter/sec",
            "range": "stddev: 0.0002265394847876923",
            "extra": "mean: 14.33696215686237 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 62.696315786260065,
            "unit": "iter/sec",
            "range": "stddev: 0.0001945706066321838",
            "extra": "mean: 15.949900523806386 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 68.42314268458217,
            "unit": "iter/sec",
            "range": "stddev: 0.00025034665459792754",
            "extra": "mean: 14.614938173913057 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 59.42247424187214,
            "unit": "iter/sec",
            "range": "stddev: 0.00015143102057215658",
            "extra": "mean: 16.828649644065955 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 68.51514900674375,
            "unit": "iter/sec",
            "range": "stddev: 0.00009336336899212815",
            "extra": "mean: 14.595312343282984 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 59.496125292033454,
            "unit": "iter/sec",
            "range": "stddev: 0.00016329240213341014",
            "extra": "mean: 16.80781723333335 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 68.04043044431967,
            "unit": "iter/sec",
            "range": "stddev: 0.00010034163079165108",
            "extra": "mean: 14.697143940297995 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 45.940282861659384,
            "unit": "iter/sec",
            "range": "stddev: 0.000152128997540677",
            "extra": "mean: 21.76738882978396 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 61.443373176821325,
            "unit": "iter/sec",
            "range": "stddev: 0.00015283035944738645",
            "extra": "mean: 16.275148129029418 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 44.15522324038408,
            "unit": "iter/sec",
            "range": "stddev: 0.0002061752808557472",
            "extra": "mean: 22.647377288886776 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 62.28109083566695,
            "unit": "iter/sec",
            "range": "stddev: 0.00014188043758034345",
            "extra": "mean: 16.056237721310477 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 57.955114459314835,
            "unit": "iter/sec",
            "range": "stddev: 0.00014667404495400524",
            "extra": "mean: 17.254732551723485 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 64.12140966310135,
            "unit": "iter/sec",
            "range": "stddev: 0.00016774910787522627",
            "extra": "mean: 15.595415092308082 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 46.77644023653907,
            "unit": "iter/sec",
            "range": "stddev: 0.00019365565829137723",
            "extra": "mean: 21.378283489363465 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 59.64676428675362,
            "unit": "iter/sec",
            "range": "stddev: 0.00021124093990105888",
            "extra": "mean: 16.765368783333656 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 73.31847706141812,
            "unit": "iter/sec",
            "range": "stddev: 0.00018287572411880917",
            "extra": "mean: 13.6391267260272 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 91.77789493657461,
            "unit": "iter/sec",
            "range": "stddev: 0.00012236823564786727",
            "extra": "mean: 10.895869868131914 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 77.58511161053276,
            "unit": "iter/sec",
            "range": "stddev: 0.00015290806741635228",
            "extra": "mean: 12.8890708441572 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 91.86699808153365,
            "unit": "iter/sec",
            "range": "stddev: 0.00022207437541533456",
            "extra": "mean: 10.885301804598878 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 90.04973078338512,
            "unit": "iter/sec",
            "range": "stddev: 0.00013169330665072627",
            "extra": "mean: 11.104974898875632 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 104.75229360692842,
            "unit": "iter/sec",
            "range": "stddev: 0.00009979203149980194",
            "extra": "mean: 9.546330352940922 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 90.03761982181064,
            "unit": "iter/sec",
            "range": "stddev: 0.0001721476223071877",
            "extra": "mean: 11.106468629213596 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 104.82096439688559,
            "unit": "iter/sec",
            "range": "stddev: 0.00013793813049459643",
            "extra": "mean: 9.54007631730692 msec\nrounds: 104"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 62.772110786256505,
            "unit": "iter/sec",
            "range": "stddev: 0.0004160540226936859",
            "extra": "mean: 15.930641609377627 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 102.66408313834597,
            "unit": "iter/sec",
            "range": "stddev: 0.00013284704226039777",
            "extra": "mean: 9.740504852631279 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 63.61747132578537,
            "unit": "iter/sec",
            "range": "stddev: 0.00009162314707818961",
            "extra": "mean: 15.718952343751535 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 103.08466691603154,
            "unit": "iter/sec",
            "range": "stddev: 0.00009417194587551202",
            "extra": "mean: 9.700763750001329 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 66.03289561549792,
            "unit": "iter/sec",
            "range": "stddev: 0.000812803569048919",
            "extra": "mean: 15.143967119401925 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 93.61704137215982,
            "unit": "iter/sec",
            "range": "stddev: 0.00017552050096271882",
            "extra": "mean: 10.6818158888899 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 64.32131945104949,
            "unit": "iter/sec",
            "range": "stddev: 0.00021608984447439906",
            "extra": "mean: 15.54694475384683 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 91.6078470130058,
            "unit": "iter/sec",
            "range": "stddev: 0.00025745181681724916",
            "extra": "mean: 10.916095428572046 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 81.90244405780344,
            "unit": "iter/sec",
            "range": "stddev: 0.00012698072990222046",
            "extra": "mean: 12.209647849998717 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 97.6110759824753,
            "unit": "iter/sec",
            "range": "stddev: 0.00013338572877989564",
            "extra": "mean: 10.244739031250264 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 69.09455826642372,
            "unit": "iter/sec",
            "range": "stddev: 0.00013156382979655752",
            "extra": "mean: 14.472919794118532 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 87.57664069233893,
            "unit": "iter/sec",
            "range": "stddev: 0.00031685509833564144",
            "extra": "mean: 11.418569975903159 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 59.952894665172515,
            "unit": "iter/sec",
            "range": "stddev: 0.0001729469561307394",
            "extra": "mean: 16.67976176271125 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 85.6564075304845,
            "unit": "iter/sec",
            "range": "stddev: 0.00021770778785223726",
            "extra": "mean: 11.67454985365931 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 63.903301460327285,
            "unit": "iter/sec",
            "range": "stddev: 0.00019536545360319735",
            "extra": "mean: 15.648643765624914 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 87.38692932392752,
            "unit": "iter/sec",
            "range": "stddev: 0.00018206026315926166",
            "extra": "mean: 11.443358952380407 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 93.47098157141514,
            "unit": "iter/sec",
            "range": "stddev: 0.00011663079071786781",
            "extra": "mean: 10.698507528092714 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 101.69252834099068,
            "unit": "iter/sec",
            "range": "stddev: 0.00011097072343140052",
            "extra": "mean: 9.833564140000988 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 94.17145002613597,
            "unit": "iter/sec",
            "range": "stddev: 0.00008544788280105442",
            "extra": "mean: 10.618929619565844 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 102.42091025302769,
            "unit": "iter/sec",
            "range": "stddev: 0.00016415521425701383",
            "extra": "mean: 9.763631250000913 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 88.41864048120053,
            "unit": "iter/sec",
            "range": "stddev: 0.0001453515316069823",
            "extra": "mean: 11.309832344828001 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 101.27939292823108,
            "unit": "iter/sec",
            "range": "stddev: 0.00017636165163961883",
            "extra": "mean: 9.87367687628838 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 89.25707538579317,
            "unit": "iter/sec",
            "range": "stddev: 0.00009981428771727938",
            "extra": "mean: 11.203593616278935 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 100.24980025932305,
            "unit": "iter/sec",
            "range": "stddev: 0.0001034854659043511",
            "extra": "mean: 9.975082218749876 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 71.95420637767639,
            "unit": "iter/sec",
            "range": "stddev: 0.00012988552516368472",
            "extra": "mean: 13.897728157144229 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 95.64511992779127,
            "unit": "iter/sec",
            "range": "stddev: 0.00014542969244306307",
            "extra": "mean: 10.455316494505576 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 69.86780110737057,
            "unit": "iter/sec",
            "range": "stddev: 0.00019733598349947712",
            "extra": "mean: 14.312744699997536 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 92.80975335336329,
            "unit": "iter/sec",
            "range": "stddev: 0.0001412865513580331",
            "extra": "mean: 10.774729636362745 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 89.9530091817617,
            "unit": "iter/sec",
            "range": "stddev: 0.00009558728700781788",
            "extra": "mean: 11.116915477272922 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 99.0057374598556,
            "unit": "iter/sec",
            "range": "stddev: 0.00008978750247122465",
            "extra": "mean: 10.100424739581134 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 73.06578507184703,
            "unit": "iter/sec",
            "range": "stddev: 0.00012254014847376757",
            "extra": "mean: 13.686296520548984 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 88.84766085094095,
            "unit": "iter/sec",
            "range": "stddev: 0.0001365300641397294",
            "extra": "mean: 11.25522034482925 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 64.96807222464705,
            "unit": "iter/sec",
            "range": "stddev: 0.00015861028785291544",
            "extra": "mean: 15.392175968253962 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 87.4734424042007,
            "unit": "iter/sec",
            "range": "stddev: 0.00014506986643685434",
            "extra": "mean: 11.43204122891564 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 69.11194435864272,
            "unit": "iter/sec",
            "range": "stddev: 0.0001948785468635575",
            "extra": "mean: 14.469278925372125 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 89.17612563250697,
            "unit": "iter/sec",
            "range": "stddev: 0.00008296258555562272",
            "extra": "mean: 11.213763694118986 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 99.86232572172841,
            "unit": "iter/sec",
            "range": "stddev: 0.000056143004347329796",
            "extra": "mean: 10.0137864081651 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 97.65387908414344,
            "unit": "iter/sec",
            "range": "stddev: 0.00009438984544785049",
            "extra": "mean: 10.240248614582429 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 99.80022927620801,
            "unit": "iter/sec",
            "range": "stddev: 0.00010687008568661877",
            "extra": "mean: 10.020017060606055 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.04782360459963,
            "unit": "iter/sec",
            "range": "stddev: 0.00008735259781904623",
            "extra": "mean: 10.304198104166495 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 100.72156820670043,
            "unit": "iter/sec",
            "range": "stddev: 0.0000787605180058245",
            "extra": "mean: 9.928360109999517 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 94.96395521408424,
            "unit": "iter/sec",
            "range": "stddev: 0.00039107683876659765",
            "extra": "mean: 10.530311187498734 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 100.86258575171756,
            "unit": "iter/sec",
            "range": "stddev: 0.00013399424181607345",
            "extra": "mean: 9.91447911579018 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 97.93003013632824,
            "unit": "iter/sec",
            "range": "stddev: 0.00014985412396916587",
            "extra": "mean: 10.211372329896168 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 64.2888321810365,
            "unit": "iter/sec",
            "range": "stddev: 0.00042919538115944895",
            "extra": "mean: 15.554801138462329 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 63.398288241073374,
            "unit": "iter/sec",
            "range": "stddev: 0.00014198617787308717",
            "extra": "mean: 15.77329653124826 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 62.85063819839967,
            "unit": "iter/sec",
            "range": "stddev: 0.00015652664242477005",
            "extra": "mean: 15.910737403227554 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 61.095758804131584,
            "unit": "iter/sec",
            "range": "stddev: 0.00019593484432227812",
            "extra": "mean: 16.36774826229632 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 97.52510820352973,
            "unit": "iter/sec",
            "range": "stddev: 0.00012258792384207257",
            "extra": "mean: 10.253769705264547 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 92.8880966070966,
            "unit": "iter/sec",
            "range": "stddev: 0.00019668527539197964",
            "extra": "mean: 10.765642063157538 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 64.84400361332237,
            "unit": "iter/sec",
            "range": "stddev: 0.00023159063378059582",
            "extra": "mean: 15.421626430767569 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 63.573800541840555,
            "unit": "iter/sec",
            "range": "stddev: 0.00022093381533615244",
            "extra": "mean: 15.72975017187872 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 57.24044222781053,
            "unit": "iter/sec",
            "range": "stddev: 0.00015858109725182915",
            "extra": "mean: 17.47016551724238 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 55.261943640775144,
            "unit": "iter/sec",
            "range": "stddev: 0.00017140141611667796",
            "extra": "mean: 18.095635696427944 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 61.043307357542474,
            "unit": "iter/sec",
            "range": "stddev: 0.00014807315646860405",
            "extra": "mean: 16.38181224589956 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 60.07702818222594,
            "unit": "iter/sec",
            "range": "stddev: 0.00018968377678892776",
            "extra": "mean: 16.64529738333253 msec\nrounds: 60"
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
          "id": "46a9b421dea9808843ee4c7bd049d0220befb2d5",
          "message": "remove useless warnings (#629)\n\n* remove useless warnings\r\n\r\n* add note in changelog",
          "timestamp": "2023-07-18T22:29:22+02:00",
          "tree_id": "6415d89e3d6c8033c6ad83f190f93c7175bbaeaa",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/46a9b421dea9808843ee4c7bd049d0220befb2d5"
        },
        "date": 1689712420020,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 63.96038232516557,
            "unit": "iter/sec",
            "range": "stddev: 0.00015905822335401834",
            "extra": "mean: 15.634678275000626 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 72.01230844158246,
            "unit": "iter/sec",
            "range": "stddev: 0.00014822850835837276",
            "extra": "mean: 13.886514981132926 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 63.01687994093116,
            "unit": "iter/sec",
            "range": "stddev: 0.0007092078469049627",
            "extra": "mean: 15.868764066665147 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 72.16080776230395,
            "unit": "iter/sec",
            "range": "stddev: 0.00007811763229897658",
            "extra": "mean: 13.857938000001013 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 60.833249812667226,
            "unit": "iter/sec",
            "range": "stddev: 0.00013166020505362235",
            "extra": "mean: 16.438378733331643 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 69.60541108043701,
            "unit": "iter/sec",
            "range": "stddev: 0.00023767640888288903",
            "extra": "mean: 14.366699147058922 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 60.700541103825174,
            "unit": "iter/sec",
            "range": "stddev: 0.00016878712680257378",
            "extra": "mean: 16.474317721312417 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 69.59645357775076,
            "unit": "iter/sec",
            "range": "stddev: 0.0001304496046995083",
            "extra": "mean: 14.368548231884176 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 46.845607885128935,
            "unit": "iter/sec",
            "range": "stddev: 0.00028051447725447454",
            "extra": "mean: 21.34671840425511 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 63.85830226700632,
            "unit": "iter/sec",
            "range": "stddev: 0.00010498686979869343",
            "extra": "mean: 15.659670935484142 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 45.6710719162448,
            "unit": "iter/sec",
            "range": "stddev: 0.00017192971752296308",
            "extra": "mean: 21.895698043476596 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 63.80105529821753,
            "unit": "iter/sec",
            "range": "stddev: 0.0001315312936230992",
            "extra": "mean: 15.673721936507498 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 59.01584973617561,
            "unit": "iter/sec",
            "range": "stddev: 0.0002994719996535555",
            "extra": "mean: 16.94460055172295 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 67.14883935301864,
            "unit": "iter/sec",
            "range": "stddev: 0.00011550151736581945",
            "extra": "mean: 14.892290166666081 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 48.65148675613521,
            "unit": "iter/sec",
            "range": "stddev: 0.00021131262609350778",
            "extra": "mean: 20.55435643750177 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 62.92028170193037,
            "unit": "iter/sec",
            "range": "stddev: 0.0001639167828840883",
            "extra": "mean: 15.89312655555578 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 75.64724806160791,
            "unit": "iter/sec",
            "range": "stddev: 0.00025344923213083505",
            "extra": "mean: 13.219251534247345 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 95.37189578800455,
            "unit": "iter/sec",
            "range": "stddev: 0.00011522702766143549",
            "extra": "mean: 10.485269184779858 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 78.20484703915925,
            "unit": "iter/sec",
            "range": "stddev: 0.0002684783821261801",
            "extra": "mean: 12.786931217949617 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 95.32838434299507,
            "unit": "iter/sec",
            "range": "stddev: 0.00007040532721296526",
            "extra": "mean: 10.490055054347327 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 91.57504759520654,
            "unit": "iter/sec",
            "range": "stddev: 0.00006585579970617567",
            "extra": "mean: 10.92000524444548 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 107.73592865634605,
            "unit": "iter/sec",
            "range": "stddev: 0.00006114099656855748",
            "extra": "mean: 9.281954613207821 msec\nrounds: 106"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 91.74675343274787,
            "unit": "iter/sec",
            "range": "stddev: 0.00004947827070300648",
            "extra": "mean: 10.899568241758214 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 107.16622844357062,
            "unit": "iter/sec",
            "range": "stddev: 0.0001173504216176531",
            "extra": "mean: 9.331297877358438 msec\nrounds: 106"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 64.59247466765561,
            "unit": "iter/sec",
            "range": "stddev: 0.00015044823962413607",
            "extra": "mean: 15.481679640627632 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 105.3757004350963,
            "unit": "iter/sec",
            "range": "stddev: 0.00006361874003331513",
            "extra": "mean: 9.489853883494959 msec\nrounds: 103"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 64.46646515927766,
            "unit": "iter/sec",
            "range": "stddev: 0.00011626730113636877",
            "extra": "mean: 15.511940937498192 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 103.8634347595733,
            "unit": "iter/sec",
            "range": "stddev: 0.00013857004152867757",
            "extra": "mean: 9.628027441176338 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 68.23207338435935,
            "unit": "iter/sec",
            "range": "stddev: 0.0001899810414942643",
            "extra": "mean: 14.65586417646847 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 96.19236373705245,
            "unit": "iter/sec",
            "range": "stddev: 0.00023521892605160325",
            "extra": "mean: 10.395835606385134 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 67.2413996506055,
            "unit": "iter/sec",
            "range": "stddev: 0.00015097663190720374",
            "extra": "mean: 14.87179037313503 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 96.8856882191451,
            "unit": "iter/sec",
            "range": "stddev: 0.00005562530150042869",
            "extra": "mean: 10.321441880436526 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 83.67122706677588,
            "unit": "iter/sec",
            "range": "stddev: 0.00010629882158310572",
            "extra": "mean: 11.951539795178638 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 100.59497129478343,
            "unit": "iter/sec",
            "range": "stddev: 0.00004118821064531188",
            "extra": "mean: 9.940854767676218 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 71.59094748240385,
            "unit": "iter/sec",
            "range": "stddev: 0.00005350978016959123",
            "extra": "mean: 13.968246477612096 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 91.62689004234662,
            "unit": "iter/sec",
            "range": "stddev: 0.0001679822914748143",
            "extra": "mean: 10.913826711108893 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 59.40872886333621,
            "unit": "iter/sec",
            "range": "stddev: 0.000269415638723162",
            "extra": "mean: 16.83254328333466 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 85.52204942822388,
            "unit": "iter/sec",
            "range": "stddev: 0.00017154148938788172",
            "extra": "mean: 11.692890975902891 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 63.67472796748317,
            "unit": "iter/sec",
            "range": "stddev: 0.0001903883252069402",
            "extra": "mean: 15.704817781250213 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 86.00377830583989,
            "unit": "iter/sec",
            "range": "stddev: 0.00020272444850170633",
            "extra": "mean: 11.627396141177408 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 91.3266995472606,
            "unit": "iter/sec",
            "range": "stddev: 0.00010579699852998866",
            "extra": "mean: 10.949700415731225 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 102.61797750728344,
            "unit": "iter/sec",
            "range": "stddev: 0.00012229903443315867",
            "extra": "mean: 9.744881202019634 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 94.0084966415692,
            "unit": "iter/sec",
            "range": "stddev: 0.00010726092396060166",
            "extra": "mean: 10.637336365592027 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 102.21455853027759,
            "unit": "iter/sec",
            "range": "stddev: 0.00013915920363474562",
            "extra": "mean: 9.783342161613739 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 88.4598375002621,
            "unit": "iter/sec",
            "range": "stddev: 0.00017242520726843324",
            "extra": "mean: 11.304565193182015 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 101.30480272595777,
            "unit": "iter/sec",
            "range": "stddev: 0.00012848719165647887",
            "extra": "mean: 9.871200309279764 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 88.86345083519602,
            "unit": "iter/sec",
            "range": "stddev: 0.00011802433632530363",
            "extra": "mean: 11.253220425285706 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 99.8781159260645,
            "unit": "iter/sec",
            "range": "stddev: 0.00014057223848667176",
            "extra": "mean: 10.01220328124989 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 71.92612364508955,
            "unit": "iter/sec",
            "range": "stddev: 0.0001674921917248289",
            "extra": "mean: 13.903154366199058 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 94.7692076722021,
            "unit": "iter/sec",
            "range": "stddev: 0.00016829839028121698",
            "extra": "mean: 10.551950623655179 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 69.13899967221805,
            "unit": "iter/sec",
            "range": "stddev: 0.00014005194641622624",
            "extra": "mean: 14.463616840580752 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 90.90850441148218,
            "unit": "iter/sec",
            "range": "stddev: 0.00022221939431525247",
            "extra": "mean: 11.000070966668494 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 86.70019082884555,
            "unit": "iter/sec",
            "range": "stddev: 0.00014405086254796204",
            "extra": "mean: 11.533999988236419 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 94.39425231199158,
            "unit": "iter/sec",
            "range": "stddev: 0.00013961756912249848",
            "extra": "mean: 10.593865362636734 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 70.35751043206312,
            "unit": "iter/sec",
            "range": "stddev: 0.00017065738746792374",
            "extra": "mean: 14.213123714284848 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 87.38186982187021,
            "unit": "iter/sec",
            "range": "stddev: 0.0001857981301447509",
            "extra": "mean: 11.444021534884996 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 63.72360066638017,
            "unit": "iter/sec",
            "range": "stddev: 0.00017633503664095306",
            "extra": "mean: 15.692772999997603 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 87.21645255347507,
            "unit": "iter/sec",
            "range": "stddev: 0.00012485531447958736",
            "extra": "mean: 11.465726599999806 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 68.66067242100316,
            "unit": "iter/sec",
            "range": "stddev: 0.00020143790955536029",
            "extra": "mean: 14.564378191176907 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 87.8341556211815,
            "unit": "iter/sec",
            "range": "stddev: 0.00017242323192698207",
            "extra": "mean: 11.38509265476273 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 97.84012409541035,
            "unit": "iter/sec",
            "range": "stddev: 0.00012449287043603816",
            "extra": "mean: 10.2207556382986 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 96.08430304411658,
            "unit": "iter/sec",
            "range": "stddev: 0.0001614873727240431",
            "extra": "mean: 10.40752722680265 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 98.48381893570424,
            "unit": "iter/sec",
            "range": "stddev: 0.0001108000408578693",
            "extra": "mean: 10.15395230208179 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.55327319380082,
            "unit": "iter/sec",
            "range": "stddev: 0.00010033267721210516",
            "extra": "mean: 10.250809298970264 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 99.07567917099526,
            "unit": "iter/sec",
            "range": "stddev: 0.00010276637945936566",
            "extra": "mean: 10.09329442268162 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 98.44131265897555,
            "unit": "iter/sec",
            "range": "stddev: 0.00019311488735154867",
            "extra": "mean: 10.158336708331403 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 98.58134812645612,
            "unit": "iter/sec",
            "range": "stddev: 0.00019440006340562944",
            "extra": "mean: 10.143906722773165 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 95.89281039786468,
            "unit": "iter/sec",
            "range": "stddev: 0.0001334494053641713",
            "extra": "mean: 10.428310483871979 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 62.96056225933462,
            "unit": "iter/sec",
            "range": "stddev: 0.000194316750572012",
            "extra": "mean: 15.882958539680743 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 62.10321952545302,
            "unit": "iter/sec",
            "range": "stddev: 0.00015277552805968098",
            "extra": "mean: 16.10222477419467 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 61.203547585844156,
            "unit": "iter/sec",
            "range": "stddev: 0.00016905496964814278",
            "extra": "mean: 16.33892216129137 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 59.97697784687941,
            "unit": "iter/sec",
            "range": "stddev: 0.00042840206229662314",
            "extra": "mean: 16.673064163936193 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 96.91701009139972,
            "unit": "iter/sec",
            "range": "stddev: 0.00020341469268533505",
            "extra": "mean: 10.318106172042741 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 97.51375397980375,
            "unit": "iter/sec",
            "range": "stddev: 0.0000881237849061183",
            "extra": "mean: 10.254963624999114 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 65.96639935482307,
            "unit": "iter/sec",
            "range": "stddev: 0.00023074241563864452",
            "extra": "mean: 15.159232727273086 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 66.40275446961304,
            "unit": "iter/sec",
            "range": "stddev: 0.0002484713346783686",
            "extra": "mean: 15.059616246154606 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 58.58391215769012,
            "unit": "iter/sec",
            "range": "stddev: 0.0002653446777650455",
            "extra": "mean: 17.069532627119596 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 57.966651651071814,
            "unit": "iter/sec",
            "range": "stddev: 0.0001367700358645035",
            "extra": "mean: 17.251298315787913 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 64.93882806719441,
            "unit": "iter/sec",
            "range": "stddev: 0.00009738360939750174",
            "extra": "mean: 15.399107587301485 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 63.66800715041884,
            "unit": "iter/sec",
            "range": "stddev: 0.0001501813270254427",
            "extra": "mean: 15.706475587298502 msec\nrounds: 63"
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
          "id": "8b6892fcb6cef3cbf4f3572a05993ebce8bb20e1",
          "message": "Bump version: 5.0.2 → 5.0.3",
          "timestamp": "2023-07-18T22:36:02+02:00",
          "tree_id": "896a15aa4fb23cc632c4ba4a7e33eef4ce92e1fb",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/8b6892fcb6cef3cbf4f3572a05993ebce8bb20e1"
        },
        "date": 1689714173228,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 61.07415413171957,
            "unit": "iter/sec",
            "range": "stddev: 0.00016690750667356486",
            "extra": "mean: 16.373538270268707 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 76.48561201744825,
            "unit": "iter/sec",
            "range": "stddev: 0.0001301369173121925",
            "extra": "mean: 13.074354425926218 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 61.62091314875933,
            "unit": "iter/sec",
            "range": "stddev: 0.0000951679091874792",
            "extra": "mean: 16.228256754097355 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 75.7981682758364,
            "unit": "iter/sec",
            "range": "stddev: 0.0002600505446012048",
            "extra": "mean: 13.19293094736682 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 62.922986075042225,
            "unit": "iter/sec",
            "range": "stddev: 0.000256151680316617",
            "extra": "mean: 15.892443483330489 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 74.4423928277586,
            "unit": "iter/sec",
            "range": "stddev: 0.00007556778690013147",
            "extra": "mean: 13.433206027024875 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 63.44109035820158,
            "unit": "iter/sec",
            "range": "stddev: 0.00006459584380423592",
            "extra": "mean: 15.762654682537645 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 74.08786757357683,
            "unit": "iter/sec",
            "range": "stddev: 0.00011381853655637392",
            "extra": "mean: 13.497486602740965 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 44.756338916407934,
            "unit": "iter/sec",
            "range": "stddev: 0.0006763898117519465",
            "extra": "mean: 22.343203760873173 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 63.76305006588111,
            "unit": "iter/sec",
            "range": "stddev: 0.00023105341990123246",
            "extra": "mean: 15.683064078126474 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 43.42199030375191,
            "unit": "iter/sec",
            "range": "stddev: 0.00024874359366797594",
            "extra": "mean: 23.029805704543996 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 64.83621192847095,
            "unit": "iter/sec",
            "range": "stddev: 0.00028735032657475017",
            "extra": "mean: 15.423479723078623 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 55.95583081730931,
            "unit": "iter/sec",
            "range": "stddev: 0.0002644047820067887",
            "extra": "mean: 17.87123853571058 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 64.79251932230464,
            "unit": "iter/sec",
            "range": "stddev: 0.00029820810201491903",
            "extra": "mean: 15.433880492060954 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 46.40788123994683,
            "unit": "iter/sec",
            "range": "stddev: 0.0003357173737795296",
            "extra": "mean: 21.548064106387667 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 60.807529217466374,
            "unit": "iter/sec",
            "range": "stddev: 0.0003690106351307412",
            "extra": "mean: 16.44533189999701 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 73.38350216785973,
            "unit": "iter/sec",
            "range": "stddev: 0.0004000690078147737",
            "extra": "mean: 13.627041098591459 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 92.57009114430238,
            "unit": "iter/sec",
            "range": "stddev: 0.00035288233749628076",
            "extra": "mean: 10.802625206894907 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 70.73039323262476,
            "unit": "iter/sec",
            "range": "stddev: 0.0004358891494469317",
            "extra": "mean: 14.138193699999745 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 89.62444974111412,
            "unit": "iter/sec",
            "range": "stddev: 0.0003282729407689716",
            "extra": "mean: 11.157669619044393 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 83.33715844034555,
            "unit": "iter/sec",
            "range": "stddev: 0.00015428526410080193",
            "extra": "mean: 11.999449209872216 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 106.43095679524404,
            "unit": "iter/sec",
            "range": "stddev: 0.0000783054542667597",
            "extra": "mean: 9.395762568627832 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 82.99721485015431,
            "unit": "iter/sec",
            "range": "stddev: 0.00016178634983702933",
            "extra": "mean: 12.048597074075683 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 106.88652820326055,
            "unit": "iter/sec",
            "range": "stddev: 0.00007224755284254891",
            "extra": "mean: 9.355715980393263 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 61.572776618507696,
            "unit": "iter/sec",
            "range": "stddev: 0.00034615221631200955",
            "extra": "mean: 16.24094372413632 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 103.56307700334045,
            "unit": "iter/sec",
            "range": "stddev: 0.00014025322354430434",
            "extra": "mean: 9.655951029417025 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 61.83651039945849,
            "unit": "iter/sec",
            "range": "stddev: 0.00018230902153800228",
            "extra": "mean: 16.171675819674924 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 100.65053731566786,
            "unit": "iter/sec",
            "range": "stddev: 0.0001210009040032749",
            "extra": "mean: 9.935366731960148 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 63.53416943822702,
            "unit": "iter/sec",
            "range": "stddev: 0.00023571888579846368",
            "extra": "mean: 15.739562015873673 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 95.85581772236549,
            "unit": "iter/sec",
            "range": "stddev: 0.00016064980467617363",
            "extra": "mean: 10.432334977271555 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 61.85393212485363,
            "unit": "iter/sec",
            "range": "stddev: 0.0002625553064197124",
            "extra": "mean: 16.167120919353618 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 94.12536627398667,
            "unit": "iter/sec",
            "range": "stddev: 0.0001567583096394284",
            "extra": "mean: 10.624128644441399 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 79.30628162905055,
            "unit": "iter/sec",
            "range": "stddev: 0.0001561785120625239",
            "extra": "mean: 12.609341649346623 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 97.13904242477334,
            "unit": "iter/sec",
            "range": "stddev: 0.00016790895203553708",
            "extra": "mean: 10.294521904253097 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 66.88705008293448,
            "unit": "iter/sec",
            "range": "stddev: 0.0002628582972049324",
            "extra": "mean: 14.950577111116152 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 88.36731494880208,
            "unit": "iter/sec",
            "range": "stddev: 0.0003005315709964686",
            "extra": "mean: 11.316401325301964 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 58.13588478744386,
            "unit": "iter/sec",
            "range": "stddev: 0.00031391095924349375",
            "extra": "mean: 17.20107991228129 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 87.41545195697478,
            "unit": "iter/sec",
            "range": "stddev: 0.0002621346974415093",
            "extra": "mean: 11.43962511904866 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 61.78719458234956,
            "unit": "iter/sec",
            "range": "stddev: 0.0002918982743342916",
            "extra": "mean: 16.184583338983078 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 88.19731438644054,
            "unit": "iter/sec",
            "range": "stddev: 0.0002537712715129895",
            "extra": "mean: 11.338213719506863 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 87.67822049850629,
            "unit": "iter/sec",
            "range": "stddev: 0.000168993068984473",
            "extra": "mean: 11.405340965115007 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 104.81772044266656,
            "unit": "iter/sec",
            "range": "stddev: 0.00011681604190387344",
            "extra": "mean: 9.540371568631684 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 88.17201647740505,
            "unit": "iter/sec",
            "range": "stddev: 0.00018772418962445967",
            "extra": "mean: 11.341466827587638 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 106.63006903971055,
            "unit": "iter/sec",
            "range": "stddev: 0.00007336467791614299",
            "extra": "mean: 9.378217692305778 msec\nrounds: 104"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 88.72789740686669,
            "unit": "iter/sec",
            "range": "stddev: 0.00016117144137413702",
            "extra": "mean: 11.27041245454566 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 103.11079334658336,
            "unit": "iter/sec",
            "range": "stddev: 0.00022994989060342195",
            "extra": "mean: 9.698305749997758 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 88.70339079947506,
            "unit": "iter/sec",
            "range": "stddev: 0.00017216418019358544",
            "extra": "mean: 11.273526197669526 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 103.13343212501272,
            "unit": "iter/sec",
            "range": "stddev: 0.0001260708225153452",
            "extra": "mean: 9.696176878782182 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 70.82639842383738,
            "unit": "iter/sec",
            "range": "stddev: 0.00017344518640069305",
            "extra": "mean: 14.119029376812692 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 96.29285961139549,
            "unit": "iter/sec",
            "range": "stddev: 0.0001390751190792718",
            "extra": "mean: 10.384986010755652 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 68.19123645819072,
            "unit": "iter/sec",
            "range": "stddev: 0.00023658121254843215",
            "extra": "mean: 14.664640970590378 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 94.36846625443964,
            "unit": "iter/sec",
            "range": "stddev: 0.00018148138989805248",
            "extra": "mean: 10.596760122218837 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 85.19783823996002,
            "unit": "iter/sec",
            "range": "stddev: 0.0001665826947887765",
            "extra": "mean: 11.737387011903945 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 95.64198455790927,
            "unit": "iter/sec",
            "range": "stddev: 0.00020682872432060517",
            "extra": "mean: 10.455659244445314 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 71.27183769501566,
            "unit": "iter/sec",
            "range": "stddev: 0.00019467260569277773",
            "extra": "mean: 14.030787367644011 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 90.09767633024225,
            "unit": "iter/sec",
            "range": "stddev: 0.0001625247552687938",
            "extra": "mean: 11.099065378052812 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 62.35112974980377,
            "unit": "iter/sec",
            "range": "stddev: 0.00032008832937481285",
            "extra": "mean: 16.038201777781694 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 88.04675295465316,
            "unit": "iter/sec",
            "range": "stddev: 0.00016905217779300966",
            "extra": "mean: 11.357602256099455 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 67.86257517182854,
            "unit": "iter/sec",
            "range": "stddev: 0.00021103304938592207",
            "extra": "mean: 14.735662439393032 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 90.54935245673158,
            "unit": "iter/sec",
            "range": "stddev: 0.00015989717526993752",
            "extra": "mean: 11.043701284090833 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 99.05597863292753,
            "unit": "iter/sec",
            "range": "stddev: 0.00011554597732020203",
            "extra": "mean: 10.09530180612023 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 95.73146968545416,
            "unit": "iter/sec",
            "range": "stddev: 0.00015568761407930856",
            "extra": "mean: 10.445885802084831 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 96.84324952652297,
            "unit": "iter/sec",
            "range": "stddev: 0.00014814524731678535",
            "extra": "mean: 10.325964947367083 msec\nrounds: 95"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 97.57112413259914,
            "unit": "iter/sec",
            "range": "stddev: 0.00012288569595587216",
            "extra": "mean: 10.248933881718942 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 97.10120797445711,
            "unit": "iter/sec",
            "range": "stddev: 0.00012632889943452609",
            "extra": "mean: 10.298533054944633 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 95.93532734229979,
            "unit": "iter/sec",
            "range": "stddev: 0.00007728199999180211",
            "extra": "mean: 10.42368882978815 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 97.75262246502074,
            "unit": "iter/sec",
            "range": "stddev: 0.00006905803197055384",
            "extra": "mean: 10.229904577320518 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 95.36499572398905,
            "unit": "iter/sec",
            "range": "stddev: 0.00010280617981183285",
            "extra": "mean: 10.486027838707805 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 60.74495034257995,
            "unit": "iter/sec",
            "range": "stddev: 0.0008117057719359066",
            "extra": "mean: 16.46227372580527 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 58.888622862476424,
            "unit": "iter/sec",
            "range": "stddev: 0.0008443833163115946",
            "extra": "mean: 16.98120878688769 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 58.92003447845882,
            "unit": "iter/sec",
            "range": "stddev: 0.00026123249860123893",
            "extra": "mean: 16.97215571667054 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 57.83425748603125,
            "unit": "iter/sec",
            "range": "stddev: 0.0003601184522452292",
            "extra": "mean: 17.29078998276291 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 94.16342126417385,
            "unit": "iter/sec",
            "range": "stddev: 0.00018573890192137408",
            "extra": "mean: 10.619835033335475 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 93.1212079673086,
            "unit": "iter/sec",
            "range": "stddev: 0.00018886532432961533",
            "extra": "mean: 10.738692311112018 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 64.23886000799716,
            "unit": "iter/sec",
            "range": "stddev: 0.0002843671510168444",
            "extra": "mean: 15.566901403223982 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 63.93539594129748,
            "unit": "iter/sec",
            "range": "stddev: 0.0002614551617990512",
            "extra": "mean: 15.640788412699495 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 55.34106254612492,
            "unit": "iter/sec",
            "range": "stddev: 0.0002918564832306622",
            "extra": "mean: 18.069765089286705 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 53.32577587271842,
            "unit": "iter/sec",
            "range": "stddev: 0.0004906489938230659",
            "extra": "mean: 18.752657296292657 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 58.06374865417836,
            "unit": "iter/sec",
            "range": "stddev: 0.0006682472484089359",
            "extra": "mean: 17.222449862062746 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 57.103163354629906,
            "unit": "iter/sec",
            "range": "stddev: 0.0007222772121831157",
            "extra": "mean: 17.512164672728595 msec\nrounds: 55"
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
          "id": "6499e412661af333ef993e814be4806d3fb79b3e",
          "message": "update docs",
          "timestamp": "2023-07-19T10:05:47+02:00",
          "tree_id": "291b42559b565be7fd0b2d963d313201cfccc1ad",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/6499e412661af333ef993e814be4806d3fb79b3e"
        },
        "date": 1689754215083,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 50.35127244806408,
            "unit": "iter/sec",
            "range": "stddev: 0.00025872659065035374",
            "extra": "mean: 19.86047127272646 msec\nrounds: 33"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 65.41839614630477,
            "unit": "iter/sec",
            "range": "stddev: 0.00036827605478037615",
            "extra": "mean: 15.286220068183164 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 51.704691271672175,
            "unit": "iter/sec",
            "range": "stddev: 0.00034307647534114285",
            "extra": "mean: 19.340604796297804 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 64.38181603601477,
            "unit": "iter/sec",
            "range": "stddev: 0.00040790977081036164",
            "extra": "mean: 15.532336016129252 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 52.78412444966996,
            "unit": "iter/sec",
            "range": "stddev: 0.00038980523506169836",
            "extra": "mean: 18.94509022222216 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 62.81687739505206,
            "unit": "iter/sec",
            "range": "stddev: 0.0003639440648808809",
            "extra": "mean: 15.919288596773956 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 53.10800600358072,
            "unit": "iter/sec",
            "range": "stddev: 0.0004204691858420136",
            "extra": "mean: 18.82955274074076 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 62.21465928584831,
            "unit": "iter/sec",
            "range": "stddev: 0.00034260105090758446",
            "extra": "mean: 16.07338224590206 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 37.95776109782634,
            "unit": "iter/sec",
            "range": "stddev: 0.0008997489792761236",
            "extra": "mean: 26.34507334146389 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 55.94127402529189,
            "unit": "iter/sec",
            "range": "stddev: 0.0004528517670410856",
            "extra": "mean: 17.87588891071528 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 36.85133194149982,
            "unit": "iter/sec",
            "range": "stddev: 0.0006923618553415868",
            "extra": "mean: 27.136061230770828 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 55.50895611730154,
            "unit": "iter/sec",
            "range": "stddev: 0.00048727694649476936",
            "extra": "mean: 18.015110892858438 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 47.40530902603288,
            "unit": "iter/sec",
            "range": "stddev: 0.0004245330624340203",
            "extra": "mean: 21.094683708334117 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 56.01076761812656,
            "unit": "iter/sec",
            "range": "stddev: 0.00042150580729247156",
            "extra": "mean: 17.853709965516945 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 39.1816658328158,
            "unit": "iter/sec",
            "range": "stddev: 0.0004924688046532211",
            "extra": "mean: 25.52214099999981 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 52.88927410302256,
            "unit": "iter/sec",
            "range": "stddev: 0.0004369261519056788",
            "extra": "mean: 18.907425313724456 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 62.9299269033897,
            "unit": "iter/sec",
            "range": "stddev: 0.0003835799827229944",
            "extra": "mean: 15.8906906333326 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 80.55003438033647,
            "unit": "iter/sec",
            "range": "stddev: 0.00024113099882603367",
            "extra": "mean: 12.41464398734156 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 61.45445619230254,
            "unit": "iter/sec",
            "range": "stddev: 0.0005591490514380946",
            "extra": "mean: 16.272212984373535 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 75.81790929877555,
            "unit": "iter/sec",
            "range": "stddev: 0.0003129852528100799",
            "extra": "mean: 13.189495849315776 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 69.20949735405985,
            "unit": "iter/sec",
            "range": "stddev: 0.00017322857187303738",
            "extra": "mean: 14.448884014923996 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 88.66582144493967,
            "unit": "iter/sec",
            "range": "stddev: 0.00021347529905840046",
            "extra": "mean: 11.278303000000818 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 69.64986583753223,
            "unit": "iter/sec",
            "range": "stddev: 0.0002433882737613152",
            "extra": "mean: 14.357529450704696 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 87.8441398749923,
            "unit": "iter/sec",
            "range": "stddev: 0.0001468163249215005",
            "extra": "mean: 11.383798639534321 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 49.56668012309957,
            "unit": "iter/sec",
            "range": "stddev: 0.0002883531739616941",
            "extra": "mean: 20.17484321153818 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 85.3038845732535,
            "unit": "iter/sec",
            "range": "stddev: 0.0001671717443377093",
            "extra": "mean: 11.722795567900125 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 50.323134964558015,
            "unit": "iter/sec",
            "range": "stddev: 0.0002412199007343999",
            "extra": "mean: 19.871575979999818 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 86.20649778322937,
            "unit": "iter/sec",
            "range": "stddev: 0.0002566193000597774",
            "extra": "mean: 11.600053658536867 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 54.65195706769896,
            "unit": "iter/sec",
            "range": "stddev: 0.0003934851804861118",
            "extra": "mean: 18.297606410714096 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 81.52492002934746,
            "unit": "iter/sec",
            "range": "stddev: 0.00021508399232126382",
            "extra": "mean: 12.266188051948024 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 52.22301244289126,
            "unit": "iter/sec",
            "range": "stddev: 0.00034748634778083504",
            "extra": "mean: 19.1486464150944 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 79.10151104823315,
            "unit": "iter/sec",
            "range": "stddev: 0.00021789542740445359",
            "extra": "mean: 12.64198353164502 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 65.71121834060797,
            "unit": "iter/sec",
            "range": "stddev: 0.00025134528125092645",
            "extra": "mean: 15.218101646154135 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 80.80550054417901,
            "unit": "iter/sec",
            "range": "stddev: 0.0002582722682070973",
            "extra": "mean: 12.375395155844215 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 55.56958319442238,
            "unit": "iter/sec",
            "range": "stddev: 0.00035442779015281713",
            "extra": "mean: 17.99545619230723 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 75.11323084821282,
            "unit": "iter/sec",
            "range": "stddev: 0.00025713589936109154",
            "extra": "mean: 13.313233750000423 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 48.03723575154246,
            "unit": "iter/sec",
            "range": "stddev: 0.001179358437914984",
            "extra": "mean: 20.817184510203425 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 74.47724258217946,
            "unit": "iter/sec",
            "range": "stddev: 0.00031004786151773176",
            "extra": "mean: 13.426920295774686 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 52.416392634594,
            "unit": "iter/sec",
            "range": "stddev: 0.0005116038742427994",
            "extra": "mean: 19.078001169809912 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 75.71544778832042,
            "unit": "iter/sec",
            "range": "stddev: 0.00037230747455811736",
            "extra": "mean: 13.20734446153875 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 73.60974298231244,
            "unit": "iter/sec",
            "range": "stddev: 0.0008773165637713271",
            "extra": "mean: 13.585158152777252 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 90.25034945894681,
            "unit": "iter/sec",
            "range": "stddev: 0.00024430191252409816",
            "extra": "mean: 11.080289505747356 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 75.89326317632397,
            "unit": "iter/sec",
            "range": "stddev: 0.0003395102713983039",
            "extra": "mean: 13.176400093334829 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 89.97774112643208,
            "unit": "iter/sec",
            "range": "stddev: 0.0002816355208076569",
            "extra": "mean: 11.113859800001553 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 76.22143424236789,
            "unit": "iter/sec",
            "range": "stddev: 0.00026161388318665397",
            "extra": "mean: 13.11966915789348 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 88.01029914123467,
            "unit": "iter/sec",
            "range": "stddev: 0.00029536805445727274",
            "extra": "mean: 11.362306568180713 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 75.44322358617507,
            "unit": "iter/sec",
            "range": "stddev: 0.00019588361051184818",
            "extra": "mean: 13.255000945946449 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 87.71153778607449,
            "unit": "iter/sec",
            "range": "stddev: 0.00019423118127008312",
            "extra": "mean: 11.401008638555243 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 59.35173474995267,
            "unit": "iter/sec",
            "range": "stddev: 0.00026490731450986427",
            "extra": "mean: 16.848707189654593 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 79.65124971127105,
            "unit": "iter/sec",
            "range": "stddev: 0.00033156183891556345",
            "extra": "mean: 12.55473082500167 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 57.199701272105486,
            "unit": "iter/sec",
            "range": "stddev: 0.0002999012003205098",
            "extra": "mean: 17.482608785715264 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 79.48614138457965,
            "unit": "iter/sec",
            "range": "stddev: 0.0002700895917140697",
            "extra": "mean: 12.580809466667613 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 71.85750586955818,
            "unit": "iter/sec",
            "range": "stddev: 0.00017903500467144473",
            "extra": "mean: 13.916430690139517 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 80.66665025167967,
            "unit": "iter/sec",
            "range": "stddev: 0.00022520010441744355",
            "extra": "mean: 12.396696737499369 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 60.24721341193011,
            "unit": "iter/sec",
            "range": "stddev: 0.0002751329136682136",
            "extra": "mean: 16.598278050848087 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 76.04332915232905,
            "unit": "iter/sec",
            "range": "stddev: 0.0003187706949536691",
            "extra": "mean: 13.150397426667269 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 52.94774738986012,
            "unit": "iter/sec",
            "range": "stddev: 0.0003046466942856744",
            "extra": "mean: 18.88654474074014 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 75.60501714339777,
            "unit": "iter/sec",
            "range": "stddev: 0.00029839273815440725",
            "extra": "mean: 13.226635450704679 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 56.90124973342472,
            "unit": "iter/sec",
            "range": "stddev: 0.00037323912722729585",
            "extra": "mean: 17.57430644642913 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 75.92980433855325,
            "unit": "iter/sec",
            "range": "stddev: 0.00021702565407609545",
            "extra": "mean: 13.170058960526669 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 83.07102954841248,
            "unit": "iter/sec",
            "range": "stddev: 0.00015258767587047917",
            "extra": "mean: 12.037891012500523 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 80.68993224563951,
            "unit": "iter/sec",
            "range": "stddev: 0.0002223387896046873",
            "extra": "mean: 12.393119837500421 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 84.78623848825052,
            "unit": "iter/sec",
            "range": "stddev: 0.00029128098857238947",
            "extra": "mean: 11.794366843371376 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 83.68362288748291,
            "unit": "iter/sec",
            "range": "stddev: 0.00023638915101292934",
            "extra": "mean: 11.949769447058395 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 82.77027273917521,
            "unit": "iter/sec",
            "range": "stddev: 0.00022496955327160807",
            "extra": "mean: 12.081632292685432 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 80.70143159101711,
            "unit": "iter/sec",
            "range": "stddev: 0.00015670602455310377",
            "extra": "mean: 12.391353911388485 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 81.74018259873097,
            "unit": "iter/sec",
            "range": "stddev: 0.00033089915981558243",
            "extra": "mean: 12.233885075949479 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 81.35491898993902,
            "unit": "iter/sec",
            "range": "stddev: 0.0002224784550762338",
            "extra": "mean: 12.291819749997757 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 50.659257679867316,
            "unit": "iter/sec",
            "range": "stddev: 0.0009540011690814934",
            "extra": "mean: 19.73972864583473 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 51.594082148462114,
            "unit": "iter/sec",
            "range": "stddev: 0.0009234661384086514",
            "extra": "mean: 19.382067833332073 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 49.37632741096473,
            "unit": "iter/sec",
            "range": "stddev: 0.0003749847195183764",
            "extra": "mean: 20.25262008000084 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 49.42030850542573,
            "unit": "iter/sec",
            "range": "stddev: 0.0004111087224984299",
            "extra": "mean: 20.234596469388944 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 82.46677955037092,
            "unit": "iter/sec",
            "range": "stddev: 0.0002523159157178939",
            "extra": "mean: 12.126094961537786 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 81.24971348548033,
            "unit": "iter/sec",
            "range": "stddev: 0.0003274677305119366",
            "extra": "mean: 12.307735708861351 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 55.338228581202856,
            "unit": "iter/sec",
            "range": "stddev: 0.0004963868544457466",
            "extra": "mean: 18.070690472728238 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 55.08572899710772,
            "unit": "iter/sec",
            "range": "stddev: 0.0005171902474721062",
            "extra": "mean: 18.153522122807978 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 47.068858748535554,
            "unit": "iter/sec",
            "range": "stddev: 0.0003640856156538319",
            "extra": "mean: 21.245469437499647 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 46.47489511060037,
            "unit": "iter/sec",
            "range": "stddev: 0.000517938360535963",
            "extra": "mean: 21.516993155556623 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 49.64934314917138,
            "unit": "iter/sec",
            "range": "stddev: 0.0009219829439043128",
            "extra": "mean: 20.141253369566268 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 49.455441776374435,
            "unit": "iter/sec",
            "range": "stddev: 0.0009258626980304772",
            "extra": "mean: 20.220221760868267 msec\nrounds: 46"
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
          "id": "4f987f54e91a5b63faa3c5a1f0b72734a8b5933f",
          "message": "update morecantile and pydantic requirements (#630)\n\n* update morecantile and pydantic requirements\r\n\r\n* update version change\r\n\r\n* remove warning tests\r\n\r\n* update models",
          "timestamp": "2023-07-25T15:51:11+02:00",
          "tree_id": "0b425297b30b476d87cba04089352691f1fa6fd4",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/4f987f54e91a5b63faa3c5a1f0b72734a8b5933f"
        },
        "date": 1690293323791,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 54.67653472292331,
            "unit": "iter/sec",
            "range": "stddev: 0.0010614235595579123",
            "extra": "mean: 18.28938145161469 msec\nrounds: 31"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 62.33207349824152,
            "unit": "iter/sec",
            "range": "stddev: 0.0013214011115815427",
            "extra": "mean: 16.0431049999999 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 56.99435778388475,
            "unit": "iter/sec",
            "range": "stddev: 0.002049801532464523",
            "extra": "mean: 17.545596421875143 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 65.37685314414534,
            "unit": "iter/sec",
            "range": "stddev: 0.0015241637138964893",
            "extra": "mean: 15.295933528571075 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 53.281428923866855,
            "unit": "iter/sec",
            "range": "stddev: 0.0018653913477863528",
            "extra": "mean: 18.768265420000034 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 61.158465834355475,
            "unit": "iter/sec",
            "range": "stddev: 0.0012075684067212804",
            "extra": "mean: 16.350966074074652 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 47.42810110390602,
            "unit": "iter/sec",
            "range": "stddev: 0.0017010145294374791",
            "extra": "mean: 21.084546433963034 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 56.16197162633166,
            "unit": "iter/sec",
            "range": "stddev: 0.001306189496446791",
            "extra": "mean: 17.805642698112614 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 36.56174827641749,
            "unit": "iter/sec",
            "range": "stddev: 0.001676950532225678",
            "extra": "mean: 27.35098968571492 msec\nrounds: 35"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 49.2311261912697,
            "unit": "iter/sec",
            "range": "stddev: 0.0016564170135193108",
            "extra": "mean: 20.312352720002025 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 38.400304212329424,
            "unit": "iter/sec",
            "range": "stddev: 0.001713778504721266",
            "extra": "mean: 26.041460361111508 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 50.91318955785133,
            "unit": "iter/sec",
            "range": "stddev: 0.001363785823636574",
            "extra": "mean: 19.641275840000674 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 45.99329514726187,
            "unit": "iter/sec",
            "range": "stddev: 0.0017355467970111723",
            "extra": "mean: 21.74229954166555 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 53.785475436963765,
            "unit": "iter/sec",
            "range": "stddev: 0.00102196911591994",
            "extra": "mean: 18.592380040815918 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 37.795936394466565,
            "unit": "iter/sec",
            "range": "stddev: 0.0016880388830613129",
            "extra": "mean: 26.45787074999954 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 49.623662825274046,
            "unit": "iter/sec",
            "range": "stddev: 0.0018556377976425048",
            "extra": "mean: 20.15167650000003 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 62.44394901941757,
            "unit": "iter/sec",
            "range": "stddev: 0.00092917602047096",
            "extra": "mean: 16.01436193103418 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 76.98690173371926,
            "unit": "iter/sec",
            "range": "stddev: 0.001295005895064423",
            "extra": "mean: 12.989222549295201 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 62.98944471702594,
            "unit": "iter/sec",
            "range": "stddev: 0.0012203606830275646",
            "extra": "mean: 15.875675749999138 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 80.42715505466647,
            "unit": "iter/sec",
            "range": "stddev: 0.0010561641547255402",
            "extra": "mean: 12.433611500000197 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 75.14128854055012,
            "unit": "iter/sec",
            "range": "stddev: 0.0011840316344629521",
            "extra": "mean: 13.308262599999843 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 85.75194643787493,
            "unit": "iter/sec",
            "range": "stddev: 0.0011489259341876845",
            "extra": "mean: 11.661542875000208 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 77.6339755367932,
            "unit": "iter/sec",
            "range": "stddev: 0.0009041976962951166",
            "extra": "mean: 12.880958280000339 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 90.26489859259691,
            "unit": "iter/sec",
            "range": "stddev: 0.0010474425565177188",
            "extra": "mean: 11.078503555556148 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 49.81563448567692,
            "unit": "iter/sec",
            "range": "stddev: 0.0014204524484046977",
            "extra": "mean: 20.07401913725543 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 81.28562100585964,
            "unit": "iter/sec",
            "range": "stddev: 0.001051202077176474",
            "extra": "mean: 12.302298827586158 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 51.74862620920194,
            "unit": "iter/sec",
            "range": "stddev: 0.0011212622511147304",
            "extra": "mean: 19.324184490566825 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 85.29106249444621,
            "unit": "iter/sec",
            "range": "stddev: 0.0009400327179875524",
            "extra": "mean: 11.724557893332795 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 57.39609609834288,
            "unit": "iter/sec",
            "range": "stddev: 0.0012369663148554802",
            "extra": "mean: 17.422787749999458 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 79.83722884735879,
            "unit": "iter/sec",
            "range": "stddev: 0.001560677788901578",
            "extra": "mean: 12.525484845070277 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 54.658616708901434,
            "unit": "iter/sec",
            "range": "stddev: 0.0015580135489236709",
            "extra": "mean: 18.295377018517648 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 80.80793384323358,
            "unit": "iter/sec",
            "range": "stddev: 0.0011489512430042168",
            "extra": "mean: 12.375022506329488 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 68.60753969301958,
            "unit": "iter/sec",
            "range": "stddev: 0.0015615371557926353",
            "extra": "mean: 14.575657492958376 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 82.61468350949812,
            "unit": "iter/sec",
            "range": "stddev: 0.0013062596767665277",
            "extra": "mean: 12.104385776470728 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 63.089205484212414,
            "unit": "iter/sec",
            "range": "stddev: 0.0013185132350078314",
            "extra": "mean: 15.850572095891145 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 76.09604224050562,
            "unit": "iter/sec",
            "range": "stddev: 0.0011659088495458339",
            "extra": "mean: 13.1412879113929 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 51.24398572050328,
            "unit": "iter/sec",
            "range": "stddev: 0.0017604608928466542",
            "extra": "mean: 19.514485181816934 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 73.0421696971994,
            "unit": "iter/sec",
            "range": "stddev: 0.0011370768182352177",
            "extra": "mean: 13.69072145783126 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 50.79550734494543,
            "unit": "iter/sec",
            "range": "stddev: 0.0014343625118603534",
            "extra": "mean: 19.68678043137034 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 70.73262104452176,
            "unit": "iter/sec",
            "range": "stddev: 0.0011930661889878607",
            "extra": "mean: 14.137748400000087 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 77.21242438351912,
            "unit": "iter/sec",
            "range": "stddev: 0.0009278125060925645",
            "extra": "mean: 12.951283527025845 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 84.80516314652169,
            "unit": "iter/sec",
            "range": "stddev: 0.0012082101515748364",
            "extra": "mean: 11.791734876710928 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 76.88861269196171,
            "unit": "iter/sec",
            "range": "stddev: 0.0007910262269038291",
            "extra": "mean: 13.005827065787917 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 89.9729792346882,
            "unit": "iter/sec",
            "range": "stddev: 0.0006951642234240421",
            "extra": "mean: 11.114448009902732 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 69.5834323348438,
            "unit": "iter/sec",
            "range": "stddev: 0.0007236424824368811",
            "extra": "mean: 14.37123703797594 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 79.72872257495591,
            "unit": "iter/sec",
            "range": "stddev: 0.001231950443567005",
            "extra": "mean: 12.542531320000307 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 68.9162233131401,
            "unit": "iter/sec",
            "range": "stddev: 0.0012813411006559734",
            "extra": "mean: 14.510371461538469 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 82.49031171026287,
            "unit": "iter/sec",
            "range": "stddev: 0.0009750492634143295",
            "extra": "mean: 12.122635728573528 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 57.45258043436113,
            "unit": "iter/sec",
            "range": "stddev: 0.0008408697326743568",
            "extra": "mean: 17.40565858730206 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 76.97487361160857,
            "unit": "iter/sec",
            "range": "stddev: 0.0009652303191594801",
            "extra": "mean: 12.991252249996421 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 55.28218164934034,
            "unit": "iter/sec",
            "range": "stddev: 0.0010250863099777183",
            "extra": "mean: 18.089011145455267 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 74.84826882846387,
            "unit": "iter/sec",
            "range": "stddev: 0.0007657018559221706",
            "extra": "mean: 13.360362445947612 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 68.11999967494486,
            "unit": "iter/sec",
            "range": "stddev: 0.0008380496592930414",
            "extra": "mean: 14.679976582087518 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 76.65724997959092,
            "unit": "iter/sec",
            "range": "stddev: 0.0006405705153004011",
            "extra": "mean: 13.045080540539063 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 57.121009231132824,
            "unit": "iter/sec",
            "range": "stddev: 0.001118905517345588",
            "extra": "mean: 17.506693482141195 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 71.26482051092935,
            "unit": "iter/sec",
            "range": "stddev: 0.0012494127734845066",
            "extra": "mean: 14.032168927537501 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 50.50148615436374,
            "unit": "iter/sec",
            "range": "stddev: 0.0011512621376914484",
            "extra": "mean: 19.801397466668252 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 73.60202340795234,
            "unit": "iter/sec",
            "range": "stddev: 0.0010878609768419354",
            "extra": "mean: 13.586582999998813 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 56.98918099824135,
            "unit": "iter/sec",
            "range": "stddev: 0.0010939374938362097",
            "extra": "mean: 17.547190229507933 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 75.71356200543347,
            "unit": "iter/sec",
            "range": "stddev: 0.0008518557963997143",
            "extra": "mean: 13.20767341428523 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 78.92224737739757,
            "unit": "iter/sec",
            "range": "stddev: 0.0011986298706761784",
            "extra": "mean: 12.670698481482786 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 76.24032934895466,
            "unit": "iter/sec",
            "range": "stddev: 0.00085729241004756",
            "extra": "mean: 13.116417630135947 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 79.14329839711012,
            "unit": "iter/sec",
            "range": "stddev: 0.0008275241689315788",
            "extra": "mean: 12.635308614285837 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 79.59153382276703,
            "unit": "iter/sec",
            "range": "stddev: 0.0008492195744678169",
            "extra": "mean: 12.564150380953603 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 84.17157338239633,
            "unit": "iter/sec",
            "range": "stddev: 0.0006618568908020849",
            "extra": "mean: 11.88049551428654 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 81.40033718160456,
            "unit": "iter/sec",
            "range": "stddev: 0.0008798598802511982",
            "extra": "mean: 12.284961397260494 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 82.98274077324653,
            "unit": "iter/sec",
            "range": "stddev: 0.0012282274664150187",
            "extra": "mean: 12.050698623374439 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 79.98953773205444,
            "unit": "iter/sec",
            "range": "stddev: 0.0011353876393076286",
            "extra": "mean: 12.501634943181662 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 48.122522592966526,
            "unit": "iter/sec",
            "range": "stddev: 0.0020271755662711563",
            "extra": "mean: 20.78029051922888 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 48.469084904927485,
            "unit": "iter/sec",
            "range": "stddev: 0.0015726989394244972",
            "extra": "mean: 20.631707860000006 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 49.721083184588714,
            "unit": "iter/sec",
            "range": "stddev: 0.0011544253224669533",
            "extra": "mean: 20.112192574073987 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 48.658136672967295,
            "unit": "iter/sec",
            "range": "stddev: 0.0013684815998000277",
            "extra": "mean: 20.551547354166644 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 70.84933334504983,
            "unit": "iter/sec",
            "range": "stddev: 0.0008621022494948732",
            "extra": "mean: 14.114458849313491 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 69.59449518050126,
            "unit": "iter/sec",
            "range": "stddev: 0.001700419252258475",
            "extra": "mean: 14.368952564515139 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 48.2213739118166,
            "unit": "iter/sec",
            "range": "stddev: 0.0014935279568244674",
            "extra": "mean: 20.73769199999818 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 47.47024170297854,
            "unit": "iter/sec",
            "range": "stddev: 0.0016997865607958948",
            "extra": "mean: 21.06582911999908 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 42.930752707688804,
            "unit": "iter/sec",
            "range": "stddev: 0.0008238143186019611",
            "extra": "mean: 23.293325574999812 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 40.49482647282098,
            "unit": "iter/sec",
            "range": "stddev: 0.0015085265226386663",
            "extra": "mean: 24.694512536587176 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 44.80257964371504,
            "unit": "iter/sec",
            "range": "stddev: 0.001993718894736896",
            "extra": "mean: 22.320143347823528 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 47.25935155653632,
            "unit": "iter/sec",
            "range": "stddev: 0.002309079400159374",
            "extra": "mean: 21.15983328302126 msec\nrounds: 53"
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
          "id": "69c4081272f6b7bced6305b71a1bba5d5c838aac",
          "message": "Bump version: 5.0.3 → 6.0.0",
          "timestamp": "2023-07-25T16:36:01+02:00",
          "tree_id": "e772839b8ec882fe25c6b60743c8eb5e950efcd4",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/69c4081272f6b7bced6305b71a1bba5d5c838aac"
        },
        "date": 1690296125052,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 54.410122807474075,
            "unit": "iter/sec",
            "range": "stddev: 0.0017019660203448517",
            "extra": "mean: 18.378932970587496 msec\nrounds: 34"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 59.15915094742044,
            "unit": "iter/sec",
            "range": "stddev: 0.0015663873373261172",
            "extra": "mean: 16.90355564583375 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 55.14478346098826,
            "unit": "iter/sec",
            "range": "stddev: 0.0013059243563759658",
            "extra": "mean: 18.13408154385885 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 58.397362469937896,
            "unit": "iter/sec",
            "range": "stddev: 0.0022963918384570196",
            "extra": "mean: 17.124061048386995 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 49.30456180032072,
            "unit": "iter/sec",
            "range": "stddev: 0.002005003875604166",
            "extra": "mean: 20.28209892727401 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 59.68091651697295,
            "unit": "iter/sec",
            "range": "stddev: 0.0012302198030203898",
            "extra": "mean: 16.755774849999245 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 46.28618501699266,
            "unit": "iter/sec",
            "range": "stddev: 0.002225729314790241",
            "extra": "mean: 21.604718549020156 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 57.17976557295342,
            "unit": "iter/sec",
            "range": "stddev: 0.0012430168199054226",
            "extra": "mean: 17.488704089283807 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 34.11389216278059,
            "unit": "iter/sec",
            "range": "stddev: 0.002193678870064429",
            "extra": "mean: 29.313570999999637 msec\nrounds: 34"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 49.65045986880976,
            "unit": "iter/sec",
            "range": "stddev: 0.0015664425665666694",
            "extra": "mean: 20.14080036000223 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 33.54392756571526,
            "unit": "iter/sec",
            "range": "stddev: 0.0030932856106578965",
            "extra": "mean: 29.811655121211412 msec\nrounds: 33"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 47.70677123496216,
            "unit": "iter/sec",
            "range": "stddev: 0.0016566146666675214",
            "extra": "mean: 20.961385021737637 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 45.79901810788159,
            "unit": "iter/sec",
            "range": "stddev: 0.0016544144079134124",
            "extra": "mean: 21.834529239130333 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 55.12054043604648,
            "unit": "iter/sec",
            "range": "stddev: 0.0011891683137095453",
            "extra": "mean: 18.14205724561515 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 41.09730452200208,
            "unit": "iter/sec",
            "range": "stddev: 0.0016718269343006327",
            "extra": "mean: 24.332496051283233 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 50.82392811736495,
            "unit": "iter/sec",
            "range": "stddev: 0.002755260109349895",
            "extra": "mean: 19.675771571428992 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 64.43411744422117,
            "unit": "iter/sec",
            "range": "stddev: 0.0011481830119067162",
            "extra": "mean: 15.519728362317872 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 78.91352377000193,
            "unit": "iter/sec",
            "range": "stddev: 0.0014203149330716878",
            "extra": "mean: 12.672099181815254 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 63.54515276218103,
            "unit": "iter/sec",
            "range": "stddev: 0.001601870796120446",
            "extra": "mean: 15.736841545452243 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 71.71305969756853,
            "unit": "iter/sec",
            "range": "stddev: 0.0017022745206303942",
            "extra": "mean: 13.944461500000754 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 66.73331839698248,
            "unit": "iter/sec",
            "range": "stddev: 0.0016004732085507674",
            "extra": "mean: 14.985018338983386 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 85.0374679550948,
            "unit": "iter/sec",
            "range": "stddev: 0.0009302410027498413",
            "extra": "mean: 11.75952229113952 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 67.49847492321639,
            "unit": "iter/sec",
            "range": "stddev: 0.0017847849237813977",
            "extra": "mean: 14.815149544305417 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 82.13087633500095,
            "unit": "iter/sec",
            "range": "stddev: 0.0013544851293461235",
            "extra": "mean: 12.175688908043947 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 49.61092645808601,
            "unit": "iter/sec",
            "range": "stddev: 0.0016765496435843345",
            "extra": "mean: 20.156849939999688 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 79.21177669724452,
            "unit": "iter/sec",
            "range": "stddev: 0.0018143943395599082",
            "extra": "mean: 12.624385434783289 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 50.82106498471967,
            "unit": "iter/sec",
            "range": "stddev: 0.0016279474970645781",
            "extra": "mean: 19.676880055557064 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 83.0224348994144,
            "unit": "iter/sec",
            "range": "stddev: 0.001368711821343297",
            "extra": "mean: 12.044937024691544 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 49.94563976847362,
            "unit": "iter/sec",
            "range": "stddev: 0.0023150994732048964",
            "extra": "mean: 20.02176775861852 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 76.16321991285757,
            "unit": "iter/sec",
            "range": "stddev: 0.0010441381072823154",
            "extra": "mean: 13.129696999997554 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 51.699238205212765,
            "unit": "iter/sec",
            "range": "stddev: 0.0016494338978941495",
            "extra": "mean: 19.34264477999932 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 78.42713680850856,
            "unit": "iter/sec",
            "range": "stddev: 0.001250534306238588",
            "extra": "mean: 12.750688609755672 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 66.94862395793058,
            "unit": "iter/sec",
            "range": "stddev: 0.0012532233972844073",
            "extra": "mean: 14.936826791666155 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 76.38216999418236,
            "unit": "iter/sec",
            "range": "stddev: 0.0014743047690726288",
            "extra": "mean: 13.092060621950973 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 51.32754157092547,
            "unit": "iter/sec",
            "range": "stddev: 0.0016065084839196099",
            "extra": "mean: 19.482717648149567 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 70.69669371368985,
            "unit": "iter/sec",
            "range": "stddev: 0.0013011325286700608",
            "extra": "mean: 14.144933057970686 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 46.869183040058765,
            "unit": "iter/sec",
            "range": "stddev: 0.001625306241692635",
            "extra": "mean: 21.33598102500116 msec\nrounds: 40"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 70.3619012322044,
            "unit": "iter/sec",
            "range": "stddev: 0.001641752290646328",
            "extra": "mean: 14.21223677142913 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 48.334161241473055,
            "unit": "iter/sec",
            "range": "stddev: 0.0017463049116711246",
            "extra": "mean: 20.689300782609866 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 68.70865550231441,
            "unit": "iter/sec",
            "range": "stddev: 0.0015373882488299373",
            "extra": "mean: 14.554207074628545 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 71.08561626360846,
            "unit": "iter/sec",
            "range": "stddev: 0.0017454530828305878",
            "extra": "mean: 14.067543513890021 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 80.9995807756297,
            "unit": "iter/sec",
            "range": "stddev: 0.0012480498135025203",
            "extra": "mean: 12.345742909090088 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 73.41289891205376,
            "unit": "iter/sec",
            "range": "stddev: 0.0011467778912137175",
            "extra": "mean: 13.62158441935343 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 82.61085708602684,
            "unit": "iter/sec",
            "range": "stddev: 0.0009746426017772041",
            "extra": "mean: 12.104946435293 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 67.29232213554053,
            "unit": "iter/sec",
            "range": "stddev: 0.0014840913804599473",
            "extra": "mean: 14.860536362317754 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 79.37584816717643,
            "unit": "iter/sec",
            "range": "stddev: 0.0012436175693878147",
            "extra": "mean: 12.5982905769254 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 72.18963348718083,
            "unit": "iter/sec",
            "range": "stddev: 0.0014234287336456913",
            "extra": "mean: 13.852404447760167 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 86.84312472031503,
            "unit": "iter/sec",
            "range": "stddev: 0.000869653189628463",
            "extra": "mean: 11.515016338029946 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 56.594311794448714,
            "unit": "iter/sec",
            "range": "stddev: 0.0013737751219133091",
            "extra": "mean: 17.66962029032199 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 78.5592020439559,
            "unit": "iter/sec",
            "range": "stddev: 0.001020077874483068",
            "extra": "mean: 12.729253530865474 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 55.943829039013465,
            "unit": "iter/sec",
            "range": "stddev: 0.0019767364625225313",
            "extra": "mean: 17.87507250000052 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 75.40716135509903,
            "unit": "iter/sec",
            "range": "stddev: 0.0016016109648511322",
            "extra": "mean: 13.261339931507447 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 70.03202796048755,
            "unit": "iter/sec",
            "range": "stddev: 0.0018632359331329565",
            "extra": "mean: 14.279180956521856 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 79.00924362179614,
            "unit": "iter/sec",
            "range": "stddev: 0.0009044947817333905",
            "extra": "mean: 12.656746909093707 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 57.30270506503185,
            "unit": "iter/sec",
            "range": "stddev: 0.0018515671561081008",
            "extra": "mean: 17.451183131147427 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 71.06420640956264,
            "unit": "iter/sec",
            "range": "stddev: 0.001661962764189246",
            "extra": "mean: 14.071781710144258 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 49.21368191902789,
            "unit": "iter/sec",
            "range": "stddev: 0.0023585552320279147",
            "extra": "mean: 20.319552632646285 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 67.45998771046933,
            "unit": "iter/sec",
            "range": "stddev: 0.0016415087929994962",
            "extra": "mean: 14.823601870369252 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 49.67393597294645,
            "unit": "iter/sec",
            "range": "stddev: 0.0024810127045482265",
            "extra": "mean: 20.13128173585082 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 74.21963734723997,
            "unit": "iter/sec",
            "range": "stddev: 0.0012295864965915387",
            "extra": "mean: 13.473523123286824 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 77.30536791823023,
            "unit": "iter/sec",
            "range": "stddev: 0.0017646518981061954",
            "extra": "mean: 12.935712317645914 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 77.48930225910699,
            "unit": "iter/sec",
            "range": "stddev: 0.001475540747264448",
            "extra": "mean: 12.90500715384199 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 78.64872230267305,
            "unit": "iter/sec",
            "range": "stddev: 0.001244028085544677",
            "extra": "mean: 12.714764724995575 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 74.85351541303902,
            "unit": "iter/sec",
            "range": "stddev: 0.0018331295815131063",
            "extra": "mean: 13.359425999995267 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 75.54640774862077,
            "unit": "iter/sec",
            "range": "stddev: 0.001590139049974883",
            "extra": "mean: 13.236896760564461 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 76.95920981733498,
            "unit": "iter/sec",
            "range": "stddev: 0.0012174084140827034",
            "extra": "mean: 12.993896407896212 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 81.30777225701287,
            "unit": "iter/sec",
            "range": "stddev: 0.0008746450739712357",
            "extra": "mean: 12.298947225352729 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 76.34091861215947,
            "unit": "iter/sec",
            "range": "stddev: 0.0013669124718145432",
            "extra": "mean: 13.099135014085636 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 46.669743393175,
            "unit": "iter/sec",
            "range": "stddev: 0.0018935623265330765",
            "extra": "mean: 21.42715873912948 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 48.18888146360487,
            "unit": "iter/sec",
            "range": "stddev: 0.0013919479897842682",
            "extra": "mean: 20.75167486000396 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 47.68853203278573,
            "unit": "iter/sec",
            "range": "stddev: 0.0017118378181455209",
            "extra": "mean: 20.96940202127637 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 45.58115858120477,
            "unit": "iter/sec",
            "range": "stddev: 0.0025106689055676124",
            "extra": "mean: 21.93888946939463 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 72.43489672965221,
            "unit": "iter/sec",
            "range": "stddev: 0.0011324585229474512",
            "extra": "mean: 13.80550045832586 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 69.92951245001817,
            "unit": "iter/sec",
            "range": "stddev: 0.001474299439310515",
            "extra": "mean: 14.300114000004589 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 48.546153132393,
            "unit": "iter/sec",
            "range": "stddev: 0.0017793896760237467",
            "extra": "mean: 20.598954509801064 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 49.394207307390715,
            "unit": "iter/sec",
            "range": "stddev: 0.0012421363511758872",
            "extra": "mean: 20.245288962262038 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 44.98170562890797,
            "unit": "iter/sec",
            "range": "stddev: 0.0015100614782316082",
            "extra": "mean: 22.231260153846623 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 45.079949346507306,
            "unit": "iter/sec",
            "range": "stddev: 0.0013028775131090273",
            "extra": "mean: 22.1828110833376 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 49.53530257612737,
            "unit": "iter/sec",
            "range": "stddev: 0.001168596202734523",
            "extra": "mean: 20.187622725492982 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 46.227880755364524,
            "unit": "iter/sec",
            "range": "stddev: 0.001488178360809038",
            "extra": "mean: 21.63196719512077 msec\nrounds: 41"
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
          "id": "833c4a3577335b31b1e0ce1ed8734567b4d89fca",
          "message": "fix Key access and add deprecation notice (#632)",
          "timestamp": "2023-07-25T21:31:05+02:00",
          "tree_id": "cd9062b20d1ed47015088c1173f1f577d9127677",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/833c4a3577335b31b1e0ce1ed8734567b4d89fca"
        },
        "date": 1690313757846,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 48.40238815134807,
            "unit": "iter/sec",
            "range": "stddev: 0.00018645391858540232",
            "extra": "mean: 20.660137612903068 msec\nrounds: 31"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 61.7817342457153,
            "unit": "iter/sec",
            "range": "stddev: 0.00015271044389637844",
            "extra": "mean: 16.186013750000104 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 50.05381029870963,
            "unit": "iter/sec",
            "range": "stddev: 0.00010614598852545262",
            "extra": "mean: 19.978499019999276 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 62.17590679054073,
            "unit": "iter/sec",
            "range": "stddev: 0.00026690908966638577",
            "extra": "mean: 16.083400333328747 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 51.54633840762851,
            "unit": "iter/sec",
            "range": "stddev: 0.00011624521643225953",
            "extra": "mean: 19.40002007692571 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 60.31854758949975,
            "unit": "iter/sec",
            "range": "stddev: 0.00016007325356703894",
            "extra": "mean: 16.57864852458881 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 51.5130108823742,
            "unit": "iter/sec",
            "range": "stddev: 0.00013347645986740665",
            "extra": "mean: 19.4125713653861 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 60.38395767082916,
            "unit": "iter/sec",
            "range": "stddev: 0.00016597173221010396",
            "extra": "mean: 16.560689934424243 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 36.71566263683417,
            "unit": "iter/sec",
            "range": "stddev: 0.0007845128471903424",
            "extra": "mean: 27.236332621619972 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 53.432169162276665,
            "unit": "iter/sec",
            "range": "stddev: 0.00015500435978125533",
            "extra": "mean: 18.71531730188495 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 36.373788886891845,
            "unit": "iter/sec",
            "range": "stddev: 0.00013509466090722315",
            "extra": "mean: 27.492324297301167 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 54.12509402556137,
            "unit": "iter/sec",
            "range": "stddev: 0.00014230163151225905",
            "extra": "mean: 18.47571848148172 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 46.8496862901695,
            "unit": "iter/sec",
            "range": "stddev: 0.00021545959469117476",
            "extra": "mean: 21.344860108696835 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 54.40438858200151,
            "unit": "iter/sec",
            "range": "stddev: 0.00013777263641637192",
            "extra": "mean: 18.38087011110769 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 39.12342340717019,
            "unit": "iter/sec",
            "range": "stddev: 0.0001783688661855386",
            "extra": "mean: 25.56013541025474 msec\nrounds: 39"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 51.51863047278935,
            "unit": "iter/sec",
            "range": "stddev: 0.0001857916130550816",
            "extra": "mean: 19.41045386538703 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 61.779873788622254,
            "unit": "iter/sec",
            "range": "stddev: 0.00015577315191789824",
            "extra": "mean: 16.186501180327205 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 80.25635484866511,
            "unit": "iter/sec",
            "range": "stddev: 0.00019873051274313472",
            "extra": "mean: 12.460072499998832 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 59.57577921772302,
            "unit": "iter/sec",
            "range": "stddev: 0.0004145224607211188",
            "extra": "mean: 16.78534486885088 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 76.87254629533093,
            "unit": "iter/sec",
            "range": "stddev: 0.0002888530207002568",
            "extra": "mean: 13.008545289474009 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 69.43103459758116,
            "unit": "iter/sec",
            "range": "stddev: 0.00016522632444085692",
            "extra": "mean: 14.402781202900842 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 88.30194139601721,
            "unit": "iter/sec",
            "range": "stddev: 0.00016332319979823635",
            "extra": "mean: 11.324779321840643 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 69.5629662127404,
            "unit": "iter/sec",
            "range": "stddev: 0.00020523792306114967",
            "extra": "mean: 14.375465199999633 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 88.49591818682086,
            "unit": "iter/sec",
            "range": "stddev: 0.0001269373902905338",
            "extra": "mean: 11.299956206894565 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 50.95061301035348,
            "unit": "iter/sec",
            "range": "stddev: 0.00017447297243984605",
            "extra": "mean: 19.626849235293673 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 85.4238127350093,
            "unit": "iter/sec",
            "range": "stddev: 0.00014504659321916527",
            "extra": "mean: 11.706337705881506 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 50.20500238155103,
            "unit": "iter/sec",
            "range": "stddev: 0.00013419452157307097",
            "extra": "mean: 19.918333882351785 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 84.92626564118157,
            "unit": "iter/sec",
            "range": "stddev: 0.00016455628939366767",
            "extra": "mean: 11.774920190475092 msec\nrounds: 84"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 54.42570410661904,
            "unit": "iter/sec",
            "range": "stddev: 0.00016191729049703325",
            "extra": "mean: 18.373671345455023 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 80.35979509368244,
            "unit": "iter/sec",
            "range": "stddev: 0.00013746204244187158",
            "extra": "mean: 12.444033721517242 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 51.52528461995113,
            "unit": "iter/sec",
            "range": "stddev: 0.0002845537257171541",
            "extra": "mean: 19.407947134614947 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 77.4107659861246,
            "unit": "iter/sec",
            "range": "stddev: 0.00016457097010682344",
            "extra": "mean: 12.918099792207764 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 65.55216198523738,
            "unit": "iter/sec",
            "range": "stddev: 0.00020967674201234564",
            "extra": "mean: 15.255026984849168 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 80.68577504912275,
            "unit": "iter/sec",
            "range": "stddev: 0.0001768042591066048",
            "extra": "mean: 12.393758371797066 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 55.66853625033797,
            "unit": "iter/sec",
            "range": "stddev: 0.00015680913436918098",
            "extra": "mean: 17.963468547171093 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 74.50028981632256,
            "unit": "iter/sec",
            "range": "stddev: 0.0002173894525313414",
            "extra": "mean: 13.422766575344326 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 47.483469218790276,
            "unit": "iter/sec",
            "range": "stddev: 0.0007198312397864694",
            "extra": "mean: 21.059960791665944 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 72.08904308842531,
            "unit": "iter/sec",
            "range": "stddev: 0.0002537152941485358",
            "extra": "mean: 13.871733583332317 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 51.438119711506644,
            "unit": "iter/sec",
            "range": "stddev: 0.00014826410708401646",
            "extra": "mean: 19.44083503846081 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 73.12860457747134,
            "unit": "iter/sec",
            "range": "stddev: 0.0002783693757772221",
            "extra": "mean: 13.674539611112301 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 72.98211617742268,
            "unit": "iter/sec",
            "range": "stddev: 0.00015227486014355836",
            "extra": "mean: 13.701986902777067 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 87.36138487257746,
            "unit": "iter/sec",
            "range": "stddev: 0.00022574035961104937",
            "extra": "mean: 11.446704988234426 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 73.50963255370051,
            "unit": "iter/sec",
            "range": "stddev: 0.00019890985222000742",
            "extra": "mean: 13.603659347221964 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 89.01047342144298,
            "unit": "iter/sec",
            "range": "stddev: 0.0002911544259010825",
            "extra": "mean: 11.234632977012073 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 75.78934785018282,
            "unit": "iter/sec",
            "range": "stddev: 0.00015359820925786837",
            "extra": "mean: 13.194466351350028 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 86.14299059657496,
            "unit": "iter/sec",
            "range": "stddev: 0.00023628908237193034",
            "extra": "mean: 11.608605564708126 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 73.69523822437252,
            "unit": "iter/sec",
            "range": "stddev: 0.0001881552914985257",
            "extra": "mean: 13.569397753426077 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 85.82542392654288,
            "unit": "iter/sec",
            "range": "stddev: 0.00016863409393220885",
            "extra": "mean: 11.651559109756219 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 58.354740686115775,
            "unit": "iter/sec",
            "range": "stddev: 0.00022711658936741316",
            "extra": "mean: 17.136568310343428 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 78.68886881752728,
            "unit": "iter/sec",
            "range": "stddev: 0.00034861088795535016",
            "extra": "mean: 12.708277740259732 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 55.8063101617361,
            "unit": "iter/sec",
            "range": "stddev: 0.00019263579445691204",
            "extra": "mean: 17.919120563639332 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 78.43226525225887,
            "unit": "iter/sec",
            "range": "stddev: 0.00019176535268924184",
            "extra": "mean: 12.7498548815814 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 69.68345278089492,
            "unit": "iter/sec",
            "range": "stddev: 0.00024177161849133258",
            "extra": "mean: 14.350609220589158 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 80.31112791201825,
            "unit": "iter/sec",
            "range": "stddev: 0.00019851407831222363",
            "extra": "mean: 12.451574594936723 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 58.31518699609429,
            "unit": "iter/sec",
            "range": "stddev: 0.00025468479921850293",
            "extra": "mean: 17.148191603449302 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 75.61176742789094,
            "unit": "iter/sec",
            "range": "stddev: 0.00027908959759067833",
            "extra": "mean: 13.225454635135664 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 51.78928673095538,
            "unit": "iter/sec",
            "range": "stddev: 0.00018387995846895686",
            "extra": "mean: 19.309012792452346 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 72.09112088613249,
            "unit": "iter/sec",
            "range": "stddev: 0.000173551041970346",
            "extra": "mean: 13.871333774647423 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 55.386226601705054,
            "unit": "iter/sec",
            "range": "stddev: 0.00016689374215887444",
            "extra": "mean: 18.055030309091595 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 74.36237614077649,
            "unit": "iter/sec",
            "range": "stddev: 0.0002645791163050251",
            "extra": "mean: 13.447660657143144 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 83.31779794880634,
            "unit": "iter/sec",
            "range": "stddev: 0.00020228990704619155",
            "extra": "mean: 12.002237512499292 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 80.77554396525586,
            "unit": "iter/sec",
            "range": "stddev: 0.00023202718298362174",
            "extra": "mean: 12.3799847195103 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 82.85448697296803,
            "unit": "iter/sec",
            "range": "stddev: 0.00019686457773413174",
            "extra": "mean: 12.069352385541393 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 81.80679480815799,
            "unit": "iter/sec",
            "range": "stddev: 0.00021460923105109266",
            "extra": "mean: 12.223923481479282 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 81.58031302068679,
            "unit": "iter/sec",
            "range": "stddev: 0.0001830860160703838",
            "extra": "mean: 12.257859316455727 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 79.6169876259005,
            "unit": "iter/sec",
            "range": "stddev: 0.0002211162209949206",
            "extra": "mean: 12.560133582279446 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 80.92271003382078,
            "unit": "iter/sec",
            "range": "stddev: 0.00027705500610761036",
            "extra": "mean: 12.357470475000909 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 78.11040681125752,
            "unit": "iter/sec",
            "range": "stddev: 0.000182630837812556",
            "extra": "mean: 12.802391394738928 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 50.634648007994365,
            "unit": "iter/sec",
            "range": "stddev: 0.0007496703145454968",
            "extra": "mean: 19.74932263461408 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 49.76268772334383,
            "unit": "iter/sec",
            "range": "stddev: 0.0006934366211728012",
            "extra": "mean: 20.09537759615217 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 49.42014034754248,
            "unit": "iter/sec",
            "range": "stddev: 0.00027275356378095094",
            "extra": "mean: 20.234665320001 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 49.02992202984247,
            "unit": "iter/sec",
            "range": "stddev: 0.0002234788791367342",
            "extra": "mean: 20.395708551022 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 81.37957222010006,
            "unit": "iter/sec",
            "range": "stddev: 0.00021916549886825433",
            "extra": "mean: 12.28809605063282 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 80.88085841417994,
            "unit": "iter/sec",
            "range": "stddev: 0.00020291765416909576",
            "extra": "mean: 12.363864820513344 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 53.45168588139244,
            "unit": "iter/sec",
            "range": "stddev: 0.00022347132866745324",
            "extra": "mean: 18.708483811323884 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 52.05513106876278,
            "unit": "iter/sec",
            "range": "stddev: 0.00016922269230078087",
            "extra": "mean: 19.210402115384923 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 45.428765124135104,
            "unit": "iter/sec",
            "range": "stddev: 0.00017863375929498407",
            "extra": "mean: 22.012484760866332 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 45.005436971829454,
            "unit": "iter/sec",
            "range": "stddev: 0.00021256060659204294",
            "extra": "mean: 22.219537622219654 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 48.86219922640771,
            "unit": "iter/sec",
            "range": "stddev: 0.0008250738373825275",
            "extra": "mean: 20.465718200001675 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 47.56256589338626,
            "unit": "iter/sec",
            "range": "stddev: 0.0005612995312909591",
            "extra": "mean: 21.024938020407635 msec\nrounds: 49"
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
          "id": "45fc03c34b18ae66d89a38940d6756d2b9729e6e",
          "message": "Bump version: 6.0.0 → 6.0.1",
          "timestamp": "2023-07-25T21:33:01+02:00",
          "tree_id": "4f24cffe145961bdbb57c3348825ee9168d82c8e",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/45fc03c34b18ae66d89a38940d6756d2b9729e6e"
        },
        "date": 1690313882132,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 47.95192861353724,
            "unit": "iter/sec",
            "range": "stddev: 0.0008138208348398137",
            "extra": "mean: 20.854218566668692 msec\nrounds: 30"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 56.46288232367926,
            "unit": "iter/sec",
            "range": "stddev: 0.0010610592795297909",
            "extra": "mean: 17.710750121954412 msec\nrounds: 41"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 49.959334600419766,
            "unit": "iter/sec",
            "range": "stddev: 0.000928307387312381",
            "extra": "mean: 20.01627939999821 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 55.50628160856245,
            "unit": "iter/sec",
            "range": "stddev: 0.0013356758818477354",
            "extra": "mean: 18.015978931035782 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 47.6982082323394,
            "unit": "iter/sec",
            "range": "stddev: 0.001391037854717558",
            "extra": "mean: 20.96514810638106 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 55.5629026550145,
            "unit": "iter/sec",
            "range": "stddev: 0.001257772660497638",
            "extra": "mean: 17.99761985454428 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 46.525215198563195,
            "unit": "iter/sec",
            "range": "stddev: 0.0024585616618735605",
            "extra": "mean: 21.49372110869639 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 54.33477323149376,
            "unit": "iter/sec",
            "range": "stddev: 0.001169934456662578",
            "extra": "mean: 18.40442023636487 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 34.75944765287701,
            "unit": "iter/sec",
            "range": "stddev: 0.0011079067640909638",
            "extra": "mean: 28.769156805552143 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 49.9981966796254,
            "unit": "iter/sec",
            "range": "stddev: 0.0008202693235913408",
            "extra": "mean: 20.00072135416649 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 34.80015537108875,
            "unit": "iter/sec",
            "range": "stddev: 0.0013040577796232897",
            "extra": "mean: 28.73550388889296 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 50.70541791322922,
            "unit": "iter/sec",
            "range": "stddev: 0.0009752958429075962",
            "extra": "mean: 19.72175836734592 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 46.45970554236201,
            "unit": "iter/sec",
            "range": "stddev: 0.0006529404060537628",
            "extra": "mean: 21.52402793616931 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 51.0295926852136,
            "unit": "iter/sec",
            "range": "stddev: 0.0012229545981140484",
            "extra": "mean: 19.59647230909137 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 37.80610046430231,
            "unit": "iter/sec",
            "range": "stddev: 0.0009038875838823731",
            "extra": "mean: 26.45075762162329 msec\nrounds: 37"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 49.43388340952168,
            "unit": "iter/sec",
            "range": "stddev: 0.0015802163920656434",
            "extra": "mean: 20.229039901958938 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 58.565443736996514,
            "unit": "iter/sec",
            "range": "stddev: 0.0008221392345365485",
            "extra": "mean: 17.07491544827633 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 77.14640019404611,
            "unit": "iter/sec",
            "range": "stddev: 0.000429019988089815",
            "extra": "mean: 12.962367621622047 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 57.090329867902135,
            "unit": "iter/sec",
            "range": "stddev: 0.0011765198934291753",
            "extra": "mean: 17.516101278690098 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 73.72316616623533,
            "unit": "iter/sec",
            "range": "stddev: 0.0008420230740450651",
            "extra": "mean: 13.564257369863105 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 70.14337024305058,
            "unit": "iter/sec",
            "range": "stddev: 0.0005630856860908488",
            "extra": "mean: 14.256514857141106 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 84.59351195927489,
            "unit": "iter/sec",
            "range": "stddev: 0.0006926514909623656",
            "extra": "mean: 11.821237549298356 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 68.09990110626369,
            "unit": "iter/sec",
            "range": "stddev: 0.0006158563210712958",
            "extra": "mean: 14.68430913636117 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 80.59508304920055,
            "unit": "iter/sec",
            "range": "stddev: 0.00146956887257475",
            "extra": "mean: 12.407704814815244 msec\nrounds: 81"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 48.246399476243376,
            "unit": "iter/sec",
            "range": "stddev: 0.0009102692461112555",
            "extra": "mean: 20.72693529166673 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 81.6237323064145,
            "unit": "iter/sec",
            "range": "stddev: 0.0006378321602918854",
            "extra": "mean: 12.251338817073597 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 48.93388772418403,
            "unit": "iter/sec",
            "range": "stddev: 0.0005267203393575327",
            "extra": "mean: 20.4357357755121 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 80.8649173497682,
            "unit": "iter/sec",
            "range": "stddev: 0.0008447764408187343",
            "extra": "mean: 12.366302134146267 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 50.06494698863815,
            "unit": "iter/sec",
            "range": "stddev: 0.0019139424561491268",
            "extra": "mean: 19.97405490565969 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 75.09285576218471,
            "unit": "iter/sec",
            "range": "stddev: 0.0013267738038630972",
            "extra": "mean: 13.316846054795807 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 50.456350174337146,
            "unit": "iter/sec",
            "range": "stddev: 0.0006039088553924796",
            "extra": "mean: 19.819110905659898 msec\nrounds: 53"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 73.23239013226117,
            "unit": "iter/sec",
            "range": "stddev: 0.0008155514208683313",
            "extra": "mean: 13.655159939392288 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 61.80579404763545,
            "unit": "iter/sec",
            "range": "stddev: 0.001170829284823467",
            "extra": "mean: 16.1797128474601 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 71.89563459403027,
            "unit": "iter/sec",
            "range": "stddev: 0.001152886573254063",
            "extra": "mean: 13.909050328947695 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 51.89005084279343,
            "unit": "iter/sec",
            "range": "stddev: 0.0015588120843914046",
            "extra": "mean: 19.271517058821335 msec\nrounds: 51"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 69.98500672092285,
            "unit": "iter/sec",
            "range": "stddev: 0.0012291354362002225",
            "extra": "mean: 14.28877479411655 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 45.819821341945136,
            "unit": "iter/sec",
            "range": "stddev: 0.0007673520759359821",
            "extra": "mean: 21.82461586956393 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 68.27726094528673,
            "unit": "iter/sec",
            "range": "stddev: 0.0015157813655224679",
            "extra": "mean: 14.646164567165922 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 47.95105869440636,
            "unit": "iter/sec",
            "range": "stddev: 0.001833757217053768",
            "extra": "mean: 20.854596899998228 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 70.67395524640952,
            "unit": "iter/sec",
            "range": "stddev: 0.0005468171353607412",
            "extra": "mean: 14.149484014492076 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 71.65132681588553,
            "unit": "iter/sec",
            "range": "stddev: 0.0010082008065228033",
            "extra": "mean: 13.956475677967404 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 78.81498835551014,
            "unit": "iter/sec",
            "range": "stddev: 0.0013067215970962824",
            "extra": "mean: 12.687941987497453 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 74.0430372567614,
            "unit": "iter/sec",
            "range": "stddev: 0.00042439683487476715",
            "extra": "mean: 13.505658830988635 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 83.73002004521805,
            "unit": "iter/sec",
            "range": "stddev: 0.0004871434297426657",
            "extra": "mean: 11.943147743903014 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 67.57987674049518,
            "unit": "iter/sec",
            "range": "stddev: 0.0011484040933084604",
            "extra": "mean: 14.79730428985498 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 79.03052665863841,
            "unit": "iter/sec",
            "range": "stddev: 0.0012127581886427288",
            "extra": "mean: 12.65333842857158 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 68.95237039167677,
            "unit": "iter/sec",
            "range": "stddev: 0.0006480800252023612",
            "extra": "mean: 14.502764652173726 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 80.85633979198268,
            "unit": "iter/sec",
            "range": "stddev: 0.0004840482147268627",
            "extra": "mean: 12.367613999998985 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 54.56476524618021,
            "unit": "iter/sec",
            "range": "stddev: 0.001306322416961794",
            "extra": "mean: 18.326845089285978 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 74.34959146107235,
            "unit": "iter/sec",
            "range": "stddev: 0.0012790713849232284",
            "extra": "mean: 13.449973030767437 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 52.975184457844016,
            "unit": "iter/sec",
            "range": "stddev: 0.0012405372481505462",
            "extra": "mean: 18.87676296428507 msec\nrounds: 56"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 73.98451060287178,
            "unit": "iter/sec",
            "range": "stddev: 0.0005910145094198739",
            "extra": "mean: 13.516342702700584 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 69.9126910960946,
            "unit": "iter/sec",
            "range": "stddev: 0.00043759008607402103",
            "extra": "mean: 14.30355468115947 msec\nrounds: 69"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 76.78278651833868,
            "unit": "iter/sec",
            "range": "stddev: 0.0005491712055163535",
            "extra": "mean: 13.02375239743561 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 56.36033454378626,
            "unit": "iter/sec",
            "range": "stddev: 0.0011750095826386438",
            "extra": "mean: 17.742974879311646 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 70.99276617889822,
            "unit": "iter/sec",
            "range": "stddev: 0.0006808197932606446",
            "extra": "mean: 14.085942185715794 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 47.9146885486835,
            "unit": "iter/sec",
            "range": "stddev: 0.002628177184692145",
            "extra": "mean: 20.870426799997972 msec\nrounds: 50"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 67.65315850120312,
            "unit": "iter/sec",
            "range": "stddev: 0.0006394789457584424",
            "extra": "mean: 14.781275880596413 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 53.17739075311947,
            "unit": "iter/sec",
            "range": "stddev: 0.0008754899854850965",
            "extra": "mean: 18.80498433333415 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 69.93855989122544,
            "unit": "iter/sec",
            "range": "stddev: 0.0008424115577038794",
            "extra": "mean: 14.298264098592929 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 77.25622900634177,
            "unit": "iter/sec",
            "range": "stddev: 0.000478867113567409",
            "extra": "mean: 12.94394009210458 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 75.66979643787593,
            "unit": "iter/sec",
            "range": "stddev: 0.00040040031831014227",
            "extra": "mean: 13.215312410956317 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 77.10924545516505,
            "unit": "iter/sec",
            "range": "stddev: 0.0004700237140753485",
            "extra": "mean: 12.968613479449065 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 76.38018918952274,
            "unit": "iter/sec",
            "range": "stddev: 0.0004313763789269178",
            "extra": "mean: 13.092400144737693 msec\nrounds: 76"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 75.72808973175518,
            "unit": "iter/sec",
            "range": "stddev: 0.000699914871589376",
            "extra": "mean: 13.205139645568908 msec\nrounds: 79"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 75.11046488353439,
            "unit": "iter/sec",
            "range": "stddev: 0.0005040573479849139",
            "extra": "mean: 13.313724013698902 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 77.2202455767073,
            "unit": "iter/sec",
            "range": "stddev: 0.0007313020966271791",
            "extra": "mean: 12.9499717662338 msec\nrounds: 77"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 76.32384501777963,
            "unit": "iter/sec",
            "range": "stddev: 0.0005311140132595918",
            "extra": "mean: 13.102065282049798 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 47.52939153610546,
            "unit": "iter/sec",
            "range": "stddev: 0.0009052266120331189",
            "extra": "mean: 21.03961291489194 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 48.52540047685061,
            "unit": "iter/sec",
            "range": "stddev: 0.0009930857310350679",
            "extra": "mean: 20.607763978724034 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 47.488520183279334,
            "unit": "iter/sec",
            "range": "stddev: 0.0010377910429668902",
            "extra": "mean: 21.05772081632687 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 46.92796152350263,
            "unit": "iter/sec",
            "range": "stddev: 0.0007201253249278814",
            "extra": "mean: 21.309257157892453 msec\nrounds: 38"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 75.5700362788287,
            "unit": "iter/sec",
            "range": "stddev: 0.0007861190236260424",
            "extra": "mean: 13.232757971827981 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 73.76857955239936,
            "unit": "iter/sec",
            "range": "stddev: 0.0006285973520301577",
            "extra": "mean: 13.55590694666527 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 49.588523444224144,
            "unit": "iter/sec",
            "range": "stddev: 0.0016524021932490655",
            "extra": "mean: 20.16595636538308 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 49.561507800295864,
            "unit": "iter/sec",
            "range": "stddev: 0.001363413165169789",
            "extra": "mean: 20.17694869230815 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 43.75927077224656,
            "unit": "iter/sec",
            "range": "stddev: 0.00046104535241269624",
            "extra": "mean: 22.85230037778029 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 43.29068365048013,
            "unit": "iter/sec",
            "range": "stddev: 0.0004303014637489197",
            "extra": "mean: 23.0996583023218 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 45.944265154667825,
            "unit": "iter/sec",
            "range": "stddev: 0.0007034579513904873",
            "extra": "mean: 21.765502106379916 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 45.18608420230994,
            "unit": "iter/sec",
            "range": "stddev: 0.0011822040941501443",
            "extra": "mean: 22.130707222222174 msec\nrounds: 45"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "JackDunnNZ@users.noreply.github.com",
            "name": "Jack Dunn",
            "username": "JackDunnNZ"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "322533cf03dbc01ce10a5725827062ef82148aaf",
          "message": "Update `data_as_image` to return masked values (#635)\n\n* Update `data_as_image` to return masked values\r\n\r\n* Update CHANGES.md",
          "timestamp": "2023-08-21T10:33:11+02:00",
          "tree_id": "18eabb41e1f9c75baa0d9a609daa78ab4740e24e",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/322533cf03dbc01ce10a5725827062ef82148aaf"
        },
        "date": 1692607050904,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 59.51330869175322,
            "unit": "iter/sec",
            "range": "stddev: 0.00013371992557661952",
            "extra": "mean: 16.80296427777961 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 75.07336721666346,
            "unit": "iter/sec",
            "range": "stddev: 0.00013018257862813521",
            "extra": "mean: 13.320303019231535 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 60.15979814029327,
            "unit": "iter/sec",
            "range": "stddev: 0.00016358565746008705",
            "extra": "mean: 16.622396200000367 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 75.0115406005303,
            "unit": "iter/sec",
            "range": "stddev: 0.00014505410465668285",
            "extra": "mean: 13.331281986667136 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 62.267174435394296,
            "unit": "iter/sec",
            "range": "stddev: 0.00015505788719978543",
            "extra": "mean: 16.059826209675798 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 72.3857224536813,
            "unit": "iter/sec",
            "range": "stddev: 0.00017843442342375718",
            "extra": "mean: 13.814879041096637 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 60.94913129075488,
            "unit": "iter/sec",
            "range": "stddev: 0.00012377649113713316",
            "extra": "mean: 16.407124741935178 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 71.24873860883469,
            "unit": "iter/sec",
            "range": "stddev: 0.0001211732745459034",
            "extra": "mean: 14.03533619718009 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 43.60230589109218,
            "unit": "iter/sec",
            "range": "stddev: 0.0007554578815375415",
            "extra": "mean: 22.934566866664202 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 63.080093658327655,
            "unit": "iter/sec",
            "range": "stddev: 0.00014490981459787012",
            "extra": "mean: 15.852861687499775 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 43.129283299614386,
            "unit": "iter/sec",
            "range": "stddev: 0.00013813329866984393",
            "extra": "mean: 23.186102886364004 msec\nrounds: 44"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 64.08122051190435,
            "unit": "iter/sec",
            "range": "stddev: 0.0001385455981892593",
            "extra": "mean: 15.605195906251978 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 55.91317600336091,
            "unit": "iter/sec",
            "range": "stddev: 0.0001662028699395216",
            "extra": "mean: 17.884872072727376 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 64.66195595291705,
            "unit": "iter/sec",
            "range": "stddev: 0.00018539329424447655",
            "extra": "mean: 15.465044093750269 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 47.34702299355367,
            "unit": "iter/sec",
            "range": "stddev: 0.0002541073856690523",
            "extra": "mean: 21.12065208695699 msec\nrounds: 46"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 61.523252866225626,
            "unit": "iter/sec",
            "range": "stddev: 0.00018846125982330988",
            "extra": "mean: 16.254017032785487 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 74.59781416223915,
            "unit": "iter/sec",
            "range": "stddev: 0.00033748517103623845",
            "extra": "mean: 13.40521852054738 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 98.00391004923038,
            "unit": "iter/sec",
            "range": "stddev: 0.0002791824556388099",
            "extra": "mean: 10.203674521737645 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 71.6862327921521,
            "unit": "iter/sec",
            "range": "stddev: 0.0003901248748239973",
            "extra": "mean: 13.949679890410922 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 92.6686975231224,
            "unit": "iter/sec",
            "range": "stddev: 0.0002734665862241712",
            "extra": "mean: 10.79113041111302 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 84.34798082479723,
            "unit": "iter/sec",
            "range": "stddev: 0.00018511408252443534",
            "extra": "mean: 11.855648353659376 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 108.1645442966715,
            "unit": "iter/sec",
            "range": "stddev: 0.00012139205504661224",
            "extra": "mean: 9.245173698113316 msec\nrounds: 106"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 84.22889246584054,
            "unit": "iter/sec",
            "range": "stddev: 0.00010885578064563761",
            "extra": "mean: 11.872410650603712 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 107.27030206709645,
            "unit": "iter/sec",
            "range": "stddev: 0.00013341192415161746",
            "extra": "mean: 9.322244654205507 msec\nrounds: 107"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 61.22557055218093,
            "unit": "iter/sec",
            "range": "stddev: 0.0001546598999530491",
            "extra": "mean: 16.333045016668756 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 103.83391660376222,
            "unit": "iter/sec",
            "range": "stddev: 0.00015659719334770603",
            "extra": "mean: 9.630764519998536 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 61.5244517338102,
            "unit": "iter/sec",
            "range": "stddev: 0.00015576715108129487",
            "extra": "mean: 16.253700306450014 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 103.56713430011479,
            "unit": "iter/sec",
            "range": "stddev: 0.0001239714289074448",
            "extra": "mean: 9.655572752473963 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 65.54683604975224,
            "unit": "iter/sec",
            "range": "stddev: 0.00016441715931321882",
            "extra": "mean: 15.256266515152106 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 96.38355764687954,
            "unit": "iter/sec",
            "range": "stddev: 0.00016650564455479146",
            "extra": "mean: 10.37521361956466 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 62.03937061887002,
            "unit": "iter/sec",
            "range": "stddev: 0.00017049929858175292",
            "extra": "mean: 16.118796661290407 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 94.20515810922457,
            "unit": "iter/sec",
            "range": "stddev: 0.00020252095146520134",
            "extra": "mean: 10.615130000000287 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 79.444975968103,
            "unit": "iter/sec",
            "range": "stddev: 0.00014977802572636607",
            "extra": "mean: 12.587328371796575 msec\nrounds: 78"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 97.45662672090711,
            "unit": "iter/sec",
            "range": "stddev: 0.00020699307964588802",
            "extra": "mean: 10.260974893618728 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 66.40603211306438,
            "unit": "iter/sec",
            "range": "stddev: 0.0002378654180301145",
            "extra": "mean: 15.058872939394691 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 89.65730551987976,
            "unit": "iter/sec",
            "range": "stddev: 0.00020220740165818827",
            "extra": "mean: 11.15358078409204 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 57.89937390298854,
            "unit": "iter/sec",
            "range": "stddev: 0.0002634732016576246",
            "extra": "mean: 17.27134392982415 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 88.75927825143225,
            "unit": "iter/sec",
            "range": "stddev: 0.00018857963199301445",
            "extra": "mean: 11.266427800001447 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 61.64674252731817,
            "unit": "iter/sec",
            "range": "stddev: 0.0002468323020409779",
            "extra": "mean: 16.22145727419189 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 89.60382684858783,
            "unit": "iter/sec",
            "range": "stddev: 0.000195567396983556",
            "extra": "mean: 11.160237627906183 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 88.28709524292788,
            "unit": "iter/sec",
            "range": "stddev: 0.00023732766403832076",
            "extra": "mean: 11.326683670455267 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 105.22546559045013,
            "unit": "iter/sec",
            "range": "stddev: 0.00018365668552495842",
            "extra": "mean: 9.503402948979266 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 87.95931854421173,
            "unit": "iter/sec",
            "range": "stddev: 0.00017711982365560286",
            "extra": "mean: 11.368892080460602 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 105.41435216364651,
            "unit": "iter/sec",
            "range": "stddev: 0.00016648293401451403",
            "extra": "mean: 9.4863742884611 msec\nrounds: 104"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 89.2935526873568,
            "unit": "iter/sec",
            "range": "stddev: 0.0001728364747844074",
            "extra": "mean: 11.19901683720992 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 103.62071704425213,
            "unit": "iter/sec",
            "range": "stddev: 0.0001503534127292893",
            "extra": "mean: 9.650579811882032 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 88.97684875778974,
            "unit": "iter/sec",
            "range": "stddev: 0.0002037926252700564",
            "extra": "mean: 11.238878584272767 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 105.05986564523585,
            "unit": "iter/sec",
            "range": "stddev: 0.0001450768902206954",
            "extra": "mean: 9.518382627451485 msec\nrounds: 102"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 71.17994268156433,
            "unit": "iter/sec",
            "range": "stddev: 0.00024267599609523606",
            "extra": "mean: 14.048901450703205 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 97.15260966435584,
            "unit": "iter/sec",
            "range": "stddev: 0.00022909911717506365",
            "extra": "mean: 10.29308428723442 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 67.07598709905122,
            "unit": "iter/sec",
            "range": "stddev: 0.00025061419064246993",
            "extra": "mean: 14.908464910449968 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 93.58962559121838,
            "unit": "iter/sec",
            "range": "stddev: 0.00024052902253371094",
            "extra": "mean: 10.68494497849376 msec\nrounds: 93"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 85.41476120362537,
            "unit": "iter/sec",
            "range": "stddev: 0.00020025960733964862",
            "extra": "mean: 11.70757824418709 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 97.1026354485841,
            "unit": "iter/sec",
            "range": "stddev: 0.00018930711604246415",
            "extra": "mean: 10.298381659574014 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 70.62030175565725,
            "unit": "iter/sec",
            "range": "stddev: 0.0002703247237381254",
            "extra": "mean: 14.160234028168707 msec\nrounds: 71"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 91.23332104610733,
            "unit": "iter/sec",
            "range": "stddev: 0.00023378199533141775",
            "extra": "mean: 10.960907577776563 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 63.29569722853224,
            "unit": "iter/sec",
            "range": "stddev: 0.00022495632755989246",
            "extra": "mean: 15.798862225807397 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 88.71235904077707,
            "unit": "iter/sec",
            "range": "stddev: 0.0001809591933628629",
            "extra": "mean: 11.272386517647954 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 68.55828646432578,
            "unit": "iter/sec",
            "range": "stddev: 0.00021055722572100246",
            "extra": "mean: 14.586128848484988 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 91.45389179663736,
            "unit": "iter/sec",
            "range": "stddev: 0.00021064355662113777",
            "extra": "mean: 10.934471790699329 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 100.63941845903463,
            "unit": "iter/sec",
            "range": "stddev: 0.00015230697168472384",
            "extra": "mean: 9.936464412371887 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 98.61639032816477,
            "unit": "iter/sec",
            "range": "stddev: 0.00022504780536212066",
            "extra": "mean: 10.140302202020475 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 101.59120902499374,
            "unit": "iter/sec",
            "range": "stddev: 0.00013292285197453828",
            "extra": "mean: 9.843371386140086 msec\nrounds: 101"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 99.76502641593265,
            "unit": "iter/sec",
            "range": "stddev: 0.00013497782054242312",
            "extra": "mean: 10.023552701032497 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 97.24718690604912,
            "unit": "iter/sec",
            "range": "stddev: 0.00025800026247255723",
            "extra": "mean: 10.283073802084411 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 96.65215126838213,
            "unit": "iter/sec",
            "range": "stddev: 0.00016379196317135438",
            "extra": "mean: 10.346381191487565 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 97.85585822089419,
            "unit": "iter/sec",
            "range": "stddev: 0.00016142903215197343",
            "extra": "mean: 10.219112255320038 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 97.45510994555985,
            "unit": "iter/sec",
            "range": "stddev: 0.00021473204475335115",
            "extra": "mean: 10.261134593749036 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 60.225878552209224,
            "unit": "iter/sec",
            "range": "stddev: 0.0007494648984807727",
            "extra": "mean: 16.604157947369913 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 59.54075105301231,
            "unit": "iter/sec",
            "range": "stddev: 0.0008581510702410335",
            "extra": "mean: 16.795219783332033 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 58.895052854142826,
            "unit": "iter/sec",
            "range": "stddev: 0.0002115849386956843",
            "extra": "mean: 16.979354827587315 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 58.65440023814961,
            "unit": "iter/sec",
            "range": "stddev: 0.0002791272270520202",
            "extra": "mean: 17.049019271184815 msec\nrounds: 59"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 97.77703911750974,
            "unit": "iter/sec",
            "range": "stddev: 0.00017072994989331347",
            "extra": "mean: 10.22734998958382 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 93.59123699149066,
            "unit": "iter/sec",
            "range": "stddev: 0.00023645090860491925",
            "extra": "mean: 10.6847610112357 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 63.678382676606475,
            "unit": "iter/sec",
            "range": "stddev: 0.0002526115605799126",
            "extra": "mean: 15.703916430769683 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 62.971947513781586,
            "unit": "iter/sec",
            "range": "stddev: 0.0002144565756929186",
            "extra": "mean: 15.880086919356387 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 54.615838635702225,
            "unit": "iter/sec",
            "range": "stddev: 0.00017792790451221776",
            "extra": "mean: 18.309706945455613 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 53.30517672295721,
            "unit": "iter/sec",
            "range": "stddev: 0.0002007401207410734",
            "extra": "mean: 18.759904037037455 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 56.61965908305115,
            "unit": "iter/sec",
            "range": "stddev: 0.0009215721894473896",
            "extra": "mean: 17.661710017242857 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 56.26541786886823,
            "unit": "iter/sec",
            "range": "stddev: 0.0007901621830151016",
            "extra": "mean: 17.772906305087663 msec\nrounds: 59"
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
          "id": "066878704f841a332a53027b74f7e0a97f10f4b2",
          "message": "Bump version: 6.0.1 → 6.0.2",
          "timestamp": "2023-08-21T13:44:56+02:00",
          "tree_id": "f6759e0332069e9473beb16e9838c0c0c5b31d69",
          "url": "https://github.com/cogeotiff/rio-tiler/commit/066878704f841a332a53027b74f7e0a97f10f4b2"
        },
        "date": 1692618550922,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-equator-full]",
            "value": 58.883884623782386,
            "unit": "iter/sec",
            "range": "stddev: 0.000468474176794942",
            "extra": "mean: 16.98257522222156 msec\nrounds: 36"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int8-dateline-full]",
            "value": 76.17972273895137,
            "unit": "iter/sec",
            "range": "stddev: 0.0002209472875888908",
            "extra": "mean: 13.126852711537778 msec\nrounds: 52"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-equator-full]",
            "value": 59.82103502468479,
            "unit": "iter/sec",
            "range": "stddev: 0.0002722776520994546",
            "extra": "mean: 16.71652788333328 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint8-dateline-full]",
            "value": 76.21100723260302,
            "unit": "iter/sec",
            "range": "stddev: 0.0002730314645363718",
            "extra": "mean: 13.121464159998672 msec\nrounds: 75"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-equator-full]",
            "value": 62.3531833155035,
            "unit": "iter/sec",
            "range": "stddev: 0.00022214264894176061",
            "extra": "mean: 16.037673568966927 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint16-dateline-full]",
            "value": 74.25493060368164,
            "unit": "iter/sec",
            "range": "stddev: 0.0002682754272744963",
            "extra": "mean: 13.467119178082148 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-equator-full]",
            "value": 61.881280568750256,
            "unit": "iter/sec",
            "range": "stddev: 0.00025879237977691135",
            "extra": "mean: 16.15997585714144 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int16-dateline-full]",
            "value": 75.0982993353608,
            "unit": "iter/sec",
            "range": "stddev: 0.00023631504225800248",
            "extra": "mean: 13.315880770273845 msec\nrounds: 74"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-equator-full]",
            "value": 44.69287196930838,
            "unit": "iter/sec",
            "range": "stddev: 0.0007598983151990261",
            "extra": "mean: 22.37493264444323 msec\nrounds: 45"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint32-dateline-full]",
            "value": 63.31026448850128,
            "unit": "iter/sec",
            "range": "stddev: 0.00027688827748205695",
            "extra": "mean: 15.795227015385867 msec\nrounds: 65"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-equator-full]",
            "value": 43.126065251422105,
            "unit": "iter/sec",
            "range": "stddev: 0.0002668481940550191",
            "extra": "mean: 23.187833023255568 msec\nrounds: 43"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int32-dateline-full]",
            "value": 66.03579506119168,
            "unit": "iter/sec",
            "range": "stddev: 0.0003331352984868186",
            "extra": "mean: 15.143302190476481 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-equator-full]",
            "value": 56.133493807246964,
            "unit": "iter/sec",
            "range": "stddev: 0.00042598200488069246",
            "extra": "mean: 17.814675912278556 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float32-dateline-full]",
            "value": 65.40011756672207,
            "unit": "iter/sec",
            "range": "stddev: 0.00043241459527959184",
            "extra": "mean: 15.290492390625854 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-equator-full]",
            "value": 46.197010811017094,
            "unit": "iter/sec",
            "range": "stddev: 0.0002970571757912258",
            "extra": "mean: 21.646422191487755 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-float64-dateline-full]",
            "value": 58.90202053580224,
            "unit": "iter/sec",
            "range": "stddev: 0.0007270214036385012",
            "extra": "mean: 16.977346293106756 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-equator-full]",
            "value": 75.80033490269783,
            "unit": "iter/sec",
            "range": "stddev: 0.0004200735870277206",
            "extra": "mean: 13.19255384931563 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-int64-dateline-full]",
            "value": 101.00046448788233,
            "unit": "iter/sec",
            "range": "stddev: 0.00015213433665638913",
            "extra": "mean: 9.900944565655701 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-equator-full]",
            "value": 72.23954450082314,
            "unit": "iter/sec",
            "range": "stddev: 0.0004636333117902915",
            "extra": "mean: 13.842833684930078 msec\nrounds: 73"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[nodata-uint64-dateline-full]",
            "value": 95.5616132882626,
            "unit": "iter/sec",
            "range": "stddev: 0.00041791460634458107",
            "extra": "mean: 10.464452886364418 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-equator-full]",
            "value": 82.97072427777074,
            "unit": "iter/sec",
            "range": "stddev: 0.00038879994319668563",
            "extra": "mean: 12.052443903613325 msec\nrounds: 83"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int8-dateline-full]",
            "value": 102.75095308653849,
            "unit": "iter/sec",
            "range": "stddev: 0.0003418549342726395",
            "extra": "mean: 9.732269822916232 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-equator-full]",
            "value": 84.64742551613108,
            "unit": "iter/sec",
            "range": "stddev: 0.00023180390665551902",
            "extra": "mean: 11.81370837804668 msec\nrounds: 82"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint8-dateline-full]",
            "value": 109.26076853661436,
            "unit": "iter/sec",
            "range": "stddev: 0.00014983433971608475",
            "extra": "mean: 9.152415943924925 msec\nrounds: 107"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-equator-full]",
            "value": 62.90257611270372,
            "unit": "iter/sec",
            "range": "stddev: 0.00014366040694562847",
            "extra": "mean: 15.897600095237458 msec\nrounds: 63"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint16-dateline-full]",
            "value": 103.10046745086478,
            "unit": "iter/sec",
            "range": "stddev: 0.00018808186783594445",
            "extra": "mean: 9.699277071431087 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-equator-full]",
            "value": 60.39629818152459,
            "unit": "iter/sec",
            "range": "stddev: 0.00038179791278301607",
            "extra": "mean: 16.55730616128892 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int16-dateline-full]",
            "value": 106.31122441485586,
            "unit": "iter/sec",
            "range": "stddev: 0.00014700793116631313",
            "extra": "mean: 9.406344490001572 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-equator-full]",
            "value": 68.08890215269042,
            "unit": "iter/sec",
            "range": "stddev: 0.00014018967564922275",
            "extra": "mean: 14.686681212123004 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint32-dateline-full]",
            "value": 97.96902326229797,
            "unit": "iter/sec",
            "range": "stddev: 0.00025799218312887477",
            "extra": "mean: 10.2073080520834 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-equator-full]",
            "value": 63.55456831986153,
            "unit": "iter/sec",
            "range": "stddev: 0.00037384808565129175",
            "extra": "mean: 15.734510145158024 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int32-dateline-full]",
            "value": 99.08766267913052,
            "unit": "iter/sec",
            "range": "stddev: 0.00009215640187661429",
            "extra": "mean: 10.092073755319454 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-equator-full]",
            "value": 82.25644760147054,
            "unit": "iter/sec",
            "range": "stddev: 0.0002488765552520187",
            "extra": "mean: 12.157101712499951 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float32-dateline-full]",
            "value": 98.90237616851128,
            "unit": "iter/sec",
            "range": "stddev: 0.00026059045148863277",
            "extra": "mean: 10.110980531915489 msec\nrounds: 94"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-equator-full]",
            "value": 66.5515476146384,
            "unit": "iter/sec",
            "range": "stddev: 0.00048630149030921805",
            "extra": "mean: 15.025946590910596 msec\nrounds: 66"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-float64-dateline-full]",
            "value": 89.01591583421242,
            "unit": "iter/sec",
            "range": "stddev: 0.0004282916264048894",
            "extra": "mean: 11.23394609411702 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-equator-full]",
            "value": 56.745744219118876,
            "unit": "iter/sec",
            "range": "stddev: 0.0005474347140704214",
            "extra": "mean: 17.6224669137933 msec\nrounds: 58"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-int64-dateline-full]",
            "value": 88.73328117878681,
            "unit": "iter/sec",
            "range": "stddev: 0.00042458929740090215",
            "extra": "mean: 11.269728637500975 msec\nrounds: 80"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-equator-full]",
            "value": 61.83162129955346,
            "unit": "iter/sec",
            "range": "stddev: 0.0003914890978299047",
            "extra": "mean: 16.172954533333932 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[alpha-uint64-dateline-full]",
            "value": 90.58941616758533,
            "unit": "iter/sec",
            "range": "stddev: 0.00035659220804930454",
            "extra": "mean: 11.038817141177466 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-equator-full]",
            "value": 90.00382116785038,
            "unit": "iter/sec",
            "range": "stddev: 0.00017515536787891093",
            "extra": "mean: 11.110639382022182 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int8-dateline-full]",
            "value": 106.5556758932128,
            "unit": "iter/sec",
            "range": "stddev: 0.0001857738609006483",
            "extra": "mean: 9.384765209524577 msec\nrounds: 105"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-equator-full]",
            "value": 90.30161327349879,
            "unit": "iter/sec",
            "range": "stddev: 0.00026762578109474326",
            "extra": "mean: 11.073999275863153 msec\nrounds: 87"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint8-dateline-full]",
            "value": 108.63884555724466,
            "unit": "iter/sec",
            "range": "stddev: 0.0001460002795838188",
            "extra": "mean: 9.20481062616846 msec\nrounds: 107"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-equator-full]",
            "value": 89.3049093761458,
            "unit": "iter/sec",
            "range": "stddev: 0.0002894597367549647",
            "extra": "mean: 11.197592685392832 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint16-dateline-full]",
            "value": 105.61303507057376,
            "unit": "iter/sec",
            "range": "stddev: 0.00027714582472737446",
            "extra": "mean: 9.468528191920347 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-equator-full]",
            "value": 91.0125547899622,
            "unit": "iter/sec",
            "range": "stddev: 0.00019899225930696777",
            "extra": "mean: 10.98749510227231 msec\nrounds: 88"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int16-dateline-full]",
            "value": 105.78080123524414,
            "unit": "iter/sec",
            "range": "stddev: 0.0001978529814749631",
            "extra": "mean: 9.453511301886595 msec\nrounds: 106"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-equator-full]",
            "value": 70.7065431955349,
            "unit": "iter/sec",
            "range": "stddev: 0.0002915444230819292",
            "extra": "mean: 14.142962656717033 msec\nrounds: 67"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint32-dateline-full]",
            "value": 101.13135690246436,
            "unit": "iter/sec",
            "range": "stddev: 0.00012479509188031136",
            "extra": "mean: 9.888129959182148 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-equator-full]",
            "value": 67.77747027139768,
            "unit": "iter/sec",
            "range": "stddev: 0.00042518465217610023",
            "extra": "mean: 14.75416529999945 msec\nrounds: 70"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int32-dateline-full]",
            "value": 95.83800332529171,
            "unit": "iter/sec",
            "range": "stddev: 0.0002895993545160519",
            "extra": "mean: 10.434274142855596 msec\nrounds: 91"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-equator-full]",
            "value": 85.664095405387,
            "unit": "iter/sec",
            "range": "stddev: 0.000342074731358339",
            "extra": "mean: 11.673502127906843 msec\nrounds: 86"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float32-dateline-full]",
            "value": 98.69137755474868,
            "unit": "iter/sec",
            "range": "stddev: 0.00030667590606781655",
            "extra": "mean: 10.132597444444968 msec\nrounds: 90"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-equator-full]",
            "value": 73.29782074278165,
            "unit": "iter/sec",
            "range": "stddev: 0.0003247033772241811",
            "extra": "mean: 13.642970416667943 msec\nrounds: 72"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-float64-dateline-full]",
            "value": 88.99454045192066,
            "unit": "iter/sec",
            "range": "stddev: 0.0005611681419458138",
            "extra": "mean: 11.236644348315394 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-equator-full]",
            "value": 61.387399928406545,
            "unit": "iter/sec",
            "range": "stddev: 0.0007217157034612907",
            "extra": "mean: 16.289987866667367 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-int64-dateline-full]",
            "value": 91.79755528256939,
            "unit": "iter/sec",
            "range": "stddev: 0.0002485678356012495",
            "extra": "mean: 10.893536292135668 msec\nrounds: 89"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-equator-full]",
            "value": 67.99173002989475,
            "unit": "iter/sec",
            "range": "stddev: 0.00045622562199697984",
            "extra": "mean: 14.70767105882315 msec\nrounds: 68"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[mask-uint64-dateline-full]",
            "value": 89.30973269359802,
            "unit": "iter/sec",
            "range": "stddev: 0.0003369400838228787",
            "extra": "mean: 11.196987941177467 msec\nrounds: 85"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-equator-full]",
            "value": 100.49108490904258,
            "unit": "iter/sec",
            "range": "stddev: 0.0002480511586961053",
            "extra": "mean: 9.951131494949319 msec\nrounds: 99"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int8-dateline-full]",
            "value": 99.9428618500291,
            "unit": "iter/sec",
            "range": "stddev: 0.00023309705564655354",
            "extra": "mean: 10.005717081631767 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-equator-full]",
            "value": 103.13311022202983,
            "unit": "iter/sec",
            "range": "stddev: 0.00022497686642893307",
            "extra": "mean: 9.696207142857933 msec\nrounds: 98"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint8-dateline-full]",
            "value": 100.87405594090198,
            "unit": "iter/sec",
            "range": "stddev: 0.00018634621035820717",
            "extra": "mean: 9.913351759999216 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-equator-full]",
            "value": 99.17646953998876,
            "unit": "iter/sec",
            "range": "stddev: 0.000185549071141916",
            "extra": "mean: 10.083036880000975 msec\nrounds: 100"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint16-dateline-full]",
            "value": 98.54205345522193,
            "unit": "iter/sec",
            "range": "stddev: 0.00026601945043552594",
            "extra": "mean: 10.147951711341246 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-equator-full]",
            "value": 96.97209550375179,
            "unit": "iter/sec",
            "range": "stddev: 0.0002491612314238547",
            "extra": "mean: 10.312244927834014 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int16-dateline-full]",
            "value": 96.08192482969547,
            "unit": "iter/sec",
            "range": "stddev: 0.00023896989418607833",
            "extra": "mean: 10.407784833333563 msec\nrounds: 96"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-equator-full]",
            "value": 59.727420391674265,
            "unit": "iter/sec",
            "range": "stddev: 0.0008795548953635881",
            "extra": "mean: 16.74272877419289 msec\nrounds: 62"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint32-dateline-full]",
            "value": 61.91150487450784,
            "unit": "iter/sec",
            "range": "stddev: 0.000830600595274939",
            "extra": "mean: 16.15208678947411 msec\nrounds: 57"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-equator-full]",
            "value": 61.28351169589283,
            "unit": "iter/sec",
            "range": "stddev: 0.0002860055750369877",
            "extra": "mean: 16.317602766667488 msec\nrounds: 60"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int32-dateline-full]",
            "value": 60.63838282212488,
            "unit": "iter/sec",
            "range": "stddev: 0.00033402745305382376",
            "extra": "mean: 16.491204967213175 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-equator-full]",
            "value": 99.13144249303075,
            "unit": "iter/sec",
            "range": "stddev: 0.00033102311487672825",
            "extra": "mean: 10.087616752578812 msec\nrounds: 97"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float32-dateline-full]",
            "value": 92.72174597797849,
            "unit": "iter/sec",
            "range": "stddev: 0.00032500620816604356",
            "extra": "mean: 10.784956532607799 msec\nrounds: 92"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-equator-full]",
            "value": 65.36653914030897,
            "unit": "iter/sec",
            "range": "stddev: 0.0006046699445959423",
            "extra": "mean: 15.29834703124644 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-float64-dateline-full]",
            "value": 64.00059526953697,
            "unit": "iter/sec",
            "range": "stddev: 0.00045548083964252074",
            "extra": "mean: 15.62485467187491 msec\nrounds: 64"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-equator-full]",
            "value": 54.79012314588168,
            "unit": "iter/sec",
            "range": "stddev: 0.0003179664043743646",
            "extra": "mean: 18.251464727272936 msec\nrounds: 55"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-int64-dateline-full]",
            "value": 55.18600045955793,
            "unit": "iter/sec",
            "range": "stddev: 0.0004090843566910692",
            "extra": "mean: 18.12053766666479 msec\nrounds: 54"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-equator-full]",
            "value": 59.54751475723252,
            "unit": "iter/sec",
            "range": "stddev: 0.0008673734834456341",
            "extra": "mean: 16.79331209836162 msec\nrounds: 61"
          },
          {
            "name": "tests/benchmarks/test_benchmarks.py::test_tile[none-uint64-dateline-full]",
            "value": 58.46433711598694,
            "unit": "iter/sec",
            "range": "stddev: 0.0008686317412775489",
            "extra": "mean: 17.104444338710415 msec\nrounds: 62"
          }
        ]
      }
    ]
  }
}