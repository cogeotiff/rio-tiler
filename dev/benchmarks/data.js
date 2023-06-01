window.BENCHMARK_DATA = {
  "lastUpdate": 1685602108018,
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
      }
    ]
  }
}