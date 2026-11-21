-- Archive central energies and uncertainties in electron volts. No fitted thresholds.
import Batch11Kernel
namespace ElementPaper.Batch11
set_option maxRecDepth 8192
set_option maxHeartbeats 10000000

def priorThrough10 : List (List Rat) :=
  [[13.598434599702],
   [24.587389011, 54.4177655282],
   [5.391714996, 75.640097, 122.45435913],
   [9.322699, 18.21115, 153.896205, 217.71858459],
   [8.298019, 25.15483, 37.93059, 259.374379, 340.2260225],
   [11.260288, 24.383143, 47.88778, 64.49352, 392.09056, 489.99320779],
   [14.53413, 29.60125, 47.4453, 77.4735, 97.8901, 552.06741, 667.0461377],
   [13.618055, 35.12112, 54.93554, 77.4135, 113.899, 138.1189, 739.32697, 871.4099138],
   [17.42282, 34.97081, 62.70798, 87.175, 114.249, 157.16311, 185.1868, 953.8983, 1103.1175302],
   [21.564541, 40.96297, 63.4233, 97.19, 126.247, 157.934, 207.271, 239.097, 1195.8082, 1362.199256]]

theorem priorThrough10Window : priorThrough10.all (centralTest nitrogen carbon) = true := by
  decide +kernel

def priorThrough20 : List (List Rat) :=
  [[5.13907696, 47.28636, 71.62, 98.936, 138.404, 172.23, 208.504, 264.192, 299.856, 1465.0992, 1648.702285],
   [7.646236, 15.035271, 80.1436, 109.2654, 141.33, 186.76, 225.02, 265.924, 327.99, 367.489, 1761.8049, 1962.663889],
   [5.985769, 18.82855, 28.447642, 119.9924, 153.8252, 190.49, 241.76, 284.64, 330.21, 398.65, 442.005, 2085.97693, 2304.140359],
   [8.15168, 16.34585, 33.493, 45.14179, 166.767, 205.279, 246.57, 303.59, 351.28, 401.38, 476.273, 523.415, 2437.65805, 2673.177958],
   [10.486686, 19.76949, 30.20264, 51.44387, 65.02511, 220.43, 263.57, 309.6, 372.31, 424.4, 479.44, 560.62, 611.741, 2816.90868, 3069.842145],
   [10.36001, 23.33788, 34.86, 47.222, 72.5945, 88.0529, 280.954, 328.794, 379.84, 447.7, 504.55, 564.41, 651.96, 706.994, 3223.78057, 3494.188518],
   [12.967633, 23.81364, 39.8, 53.24, 67.68, 96.94, 114.2013, 348.306, 400.851, 456.7, 530.0, 591.58, 656.3, 750.23, 809.198, 3658.34366, 3946.29179],
   [15.7596119, 27.62967, 40.735, 59.58, 74.84, 91.29, 124.41, 143.4567, 422.6, 479.76, 540.4, 619.0, 685.5, 755.13, 855.5, 918.375, 4120.66559, 4426.22407],
   [4.34066373, 31.625, 45.8031, 60.917, 82.66, 99.44, 117.56, 154.87, 175.8174, 503.67, 565.6, 631.1, 714.7, 786.3, 860.92, 967.7, 1034.542, 4610.80714, 4934.04979],
   [6.11315547, 11.871719, 50.91316, 67.2732, 84.34, 108.78, 127.21, 147.24, 188.54, 211.275, 591.6, 658.2, 728.6, 817.2, 894.0, 973.7, 1086.8, 1157.726, 5128.8576, 5469.86358]]

theorem priorThrough20Window : priorThrough20.all (centralTest nitrogen carbon) = true := by
  decide +kernel

def priorThrough30 : List (List Rat) :=
  [[6.56149, 12.79977, 24.756839, 73.4894, 91.95, 110.68, 137.99, 158.08, 180.03, 225.18, 249.798, 687.36, 757.7, 833.2, 926.5, 1008.6, 1093.5, 1213.1, 1287.957, 5674.9036, 6033.75643],
   [6.82812, 13.5755, 27.49171, 43.26717, 99.299, 119.533, 140.68, 170.5, 192.1, 215.92, 265.07, 291.5, 787.67, 864.0, 944.5, 1042.5, 1130.2, 1220.3, 1346.3, 1425.257, 6249.0226, 6625.81023],
   [6.746187, 14.634, 29.3111, 46.709, 65.28165, 128.125, 150.72, 173.55, 206.0, 230.5, 254.8, 308.5, 336.274, 896.0, 977.2, 1062.9, 1165.2, 1258.9, 1354.2, 1486.7, 1569.656, 6851.3112, 7246.12624],
   [6.76651, 16.486305, 30.959, 49.16, 69.46, 90.6349, 160.29, 184.76, 209.5, 244.5, 270.8, 296.7, 354.7, 384.163, 1011.6, 1097.2, 1188.0, 1294.8, 1394.5, 1495.1, 1634.1, 1721.183, 7481.8624, 7894.80289],
   [7.434038, 15.63999, 33.668, 51.21, 72.41, 95.604, 119.203, 195.5, 221.89, 248.6, 286.1, 314.4, 343.6, 402.95, 435.172, 1133.7, 1224.1, 1320.3, 1430.9, 1537.2, 1643.2, 1788.7, 1879.873, 8140.7864, 8571.95438],
   [7.9024681, 16.19921, 30.651, 54.91, 75.0, 98.985, 124.9671, 151.06, 233.6, 262.1, 290.9, 330.8, 361.0, 392.2, 456.2, 489.312, 1262.7, 1357.8, 1460.0, 1575.6, 1687.0, 1798.4, 1950.4, 2045.759, 8828.1864, 9277.6886],
   [7.88101, 17.0844, 33.5, 51.27, 79.5, 102.0, 128.9, 157.8, 186.14, 275.4, 305.32, 336.1, 378.5, 410.0, 441.1, 511.96, 546.588, 1397.2, 1504.5, 1606.0, 1724.0, 1844.0, 1960.8, 2119.4, 2218.876, 9544.1817, 10012.1297],
   [7.639878, 18.168838, 35.187, 54.92, 76.06, 108.0, 132.0, 162.0, 193.2, 224.7, 319.5, 351.6, 384.5, 429.3, 462.8, 495.4, 571.07, 607.02, 1540.1, 1646.0, 1758.0, 1880.0, 2008.1, 2130.5, 2295.6, 2399.259, 10288.8848, 10775.3948],
   [7.72638, 20.29239, 36.841, 57.38, 79.8, 103.0, 139.0, 166.0, 198.0, 232.2, 265.33, 367.0, 401.0, 436.0, 483.1, 518.7, 552.8, 632.5, 670.608, 1690.5, 1800.0, 1918.0, 2044.0, 2179.4, 2307.3, 2479.1, 2586.954, 11062.4309, 11567.6237],
   [9.394197, 17.96439, 39.7233, 59.573, 82.6, 108.0, 133.9, 173.9, 203.0, 238.0, 274.4, 310.8, 417.6, 453.4, 490.6, 540.0, 577.8, 613.3, 697.5, 737.366, 1846.8, 1961.0, 2085.0, 2214.0, 2358.0, 2491.5, 2669.9, 2781.996, 11864.9401, 12388.9427]]

theorem priorThrough30Window : priorThrough30.all (centralTest nitrogen carbon) = true := by
  decide +kernel

def priorThrough40 : List (List Rat) :=
  [[5.999302, 20.51514, 30.72576, 63.241, 86.01, 112.7, 140.8, 169.9, 211.0, 244.0, 280.0, 319.0, 356.0, 471.2, 508.8, 548.3, 599.8, 640.0, 677.0, 765.7, 807.308, 2010.0, 2129.0, 2258.0, 2391.0, 2543.9, 2683.0, 2868.0, 2984.426, 12696.5581, 13239.5029],
   [7.899435, 15.93461, 34.0576, 45.7155, 90.5, 115.9, 144.9, 176.4, 212.5, 252.1, 286.0, 326.0, 367.0, 407.0, 527.9, 567.3, 609.1, 662.8, 706.7, 744.0, 837.1, 880.44, 2178.2, 2304.0, 2439.0, 2575.0, 2737.1, 2881.9, 3074.0, 3194.293, 13557.4218, 14119.4457],
   [9.78855, 18.5892, 28.349, 50.15, 62.77, 121.19, 147.0, 180.0, 213.0, 247.0, 296.0, 333.0, 375.0, 418.0, 460.0, 587.6, 628.8, 672.9, 728.9, 774.0, 814.0, 911.7, 956.79, 2356.9, 2486.0, 2626.0, 2766.0, 2938.0, 3088.1, 3287.0, 3411.643, 14447.6799, 15028.9251],
   [9.752368, 21.196, 31.697, 42.947, 68.3, 81.83, 155.327, 184.0, 219.0, 255.0, 291.0, 342.9, 383.0, 426.0, 473.0, 517.0, 650.5, 693.4, 739.8, 798.0, 845.8, 887.0, 989.6, 1036.36, 2540.7, 2674.0, 2820.0, 2964.0, 3146.0, 3301.8, 3507.0, 3636.526, 15367.493, 15968.1075],
   [11.81381, 21.591, 34.871, 47.782, 59.595, 87.39, 103.03, 192.61, 224.0, 261.0, 301.0, 338.0, 393.0, 436.0, 481.0, 530.0, 577.0, 716.3, 761.0, 809.8, 870.0, 920.8, 963.0, 1070.6, 1119.17, 2731.4, 2869.0, 3021.0, 3169.0, 3361.0, 3523.1, 3735.0, 3868.986, 16317.014, 16937.1497],
   [13.9996055, 24.35984, 35.838, 50.85, 64.69, 78.49, 109.13, 125.802, 233.0, 268.0, 308.0, 350.0, 391.0, 446.0, 492.0, 540.0, 591.0, 640.0, 785.316, 831.6, 882.8, 945.0, 999.0, 1042.0, 1155.0, 1205.23, 2928.9, 3072.0, 3228.0, 3380.0, 3584.0, 3752.0, 3971.0, 4109.083, 17296.424, 17936.2405],
   [4.1771281, 27.28954, 39.247, 52.2, 68.44, 82.9, 98.67, 132.79, 150.628, 277.12, 313.1, 356.0, 400.0, 443.0, 502.0, 550.0, 601.0, 654.0, 706.0, 857.0, 905.3, 958.9, 1024.0, 1080.0, 1125.0, 1242.5, 1294.57, 3133.3, 3281.0, 3443.0, 3600.0, 3815.0, 3988.0, 4214.0, 4356.865, 18305.886, 18965.5484],
   [5.69486745, 11.0302765, 42.88353, 56.28, 70.7, 88.0, 104.0, 121.21, 158.33, 177.3, 324.07, 362.0, 408.0, 454.0, 499.0, 562.0, 612.0, 665.0, 722.0, 774.0, 932.0, 982.1, 1038.0, 1105.0, 1165.0, 1211.0, 1333.4, 1387.19, 3344.7, 3497.0, 3664.0, 3830.0, 4053.0, 4232.0, 4465.0, 4612.397, 19345.59, 20025.2673],
   [6.21726, 12.2236, 20.52441, 60.6072, 75.35, 91.39, 110.02, 128.12, 145.64, 185.7, 205.814, 374.04, 414.0, 463.0, 512.0, 559.0, 624.0, 677.0, 733.0, 790.0, 847.0, 1010.0, 1061.9, 1120.2, 1190.0, 1253.0, 1300.0, 1427.6, 1483.12, 3562.9, 3720.0, 3892.0, 4060.0, 4299.0, 4484.0, 4724.0, 4875.731, 20415.719, 21115.588],
   [6.634126, 13.13, 23.17, 34.41836, 80.348, 96.38, 112.0, 133.7, 153.0, 172.02, 214.9, 236.252, 426.0, 470.0, 520.0, 573.0, 622.0, 690.0, 745.0, 803.0, 863.0, 922.0, 1092.0, 1144.7, 1205.4, 1277.0, 1344.0, 1392.0, 1525.1, 1582.37, 3788.0, 3950.0, 4127.0, 4300.0, 4553.0, 4744.0, 4991.0, 5146.935, 21516.471, 22236.712]]

theorem priorThrough40Window : priorThrough40.all (centralTest nitrogen carbon) = true := by
  decide +kernel

def priorThrough50 : List (List Rat) :=
  [[6.75885, 14.32, 25.04, 37.611, 50.5728, 102.069, 119.1, 136.0, 159.2, 180.0, 200.28, 246.1, 268.59, 482.5, 530.0, 581.0, 636.0, 688.0, 758.0, 816.0, 877.0, 940.0, 1000.0, 1176.0, 1230.6, 1293.7, 1368.0, 1439.0, 1488.0, 1625.9, 1684.97, 4020.1, 4187.0, 4369.0, 4540.0, 4815.0, 5011.0, 5265.0, 5426.066, 22648.046, 23388.85],
   [7.09243, 16.16, 27.13, 40.33, 54.417, 68.82704, 125.638, 143.6, 164.12, 186.3, 209.3, 230.28, 279.1, 302.6, 544.0, 591.0, 646.0, 702.0, 758.0, 829.0, 890.0, 953.0, 1019.0, 1082.0, 1263.0, 1319.6, 1385.1, 1462.0, 1537.0, 1587.0, 1730.1, 1790.93, 4259.0, 4430.0, 4618.0, 4800.0, 5084.0, 5287.0, 5548.0, 5713.194, 23810.653, 24572.213],
   [7.11938, 15.26, 29.55, 41.0, 57.0, 72.0, 88.0, 150.0, 169.0, 189.9, 214.0, 239.0, 262.08, 311.0, 338.55, 604.0, 655.0, 713.0, 773.0, 829.0, 904.0, 968.0, 1032.0, 1102.0, 1166.0, 1354.0, 1411.6, 1479.5, 1559.0, 1638.0, 1689.0, 1838.0, 1900.28, 4505.0, 4681.0, 4874.0, 5060.0, 5361.0, 5570.0, 5838.0, 6008.391, 25004.531, 25787.047],
   [7.3605, 16.76, 28.47, 45.0, 59.0, 76.0, 93.0, 110.0, 178.41, 198.0, 219.9, 245.0, 271.0, 295.9, 348.0, 376.25, 670.0, 723.0, 784.0, 845.0, 905.0, 981.0, 1048.0, 1115.0, 1187.0, 1253.0, 1447.0, 1506.7, 1577.0, 1659.0, 1743.0, 1794.0, 1949.0, 2013.04, 4758.0, 4939.0, 5136.0, 5330.0, 5647.0, 5861.0, 6137.0, 6311.721, 26229.888, 27033.564],
   [7.4589, 18.08, 31.06, 42.0, 63.0, 80.0, 97.0, 115.1, 135.0, 207.51, 228.0, 252.1, 277.0, 306.0, 331.58, 389.3, 415.97, 739.0, 794.0, 857.0, 921.0, 984.0, 1061.0, 1131.0, 1202.0, 1274.0, 1344.0, 1544.0, 1604.9, 1677.6, 1763.0, 1851.0, 1903.0, 2063.0, 2129.22, 5018.0, 5203.0, 5406.0, 5600.0, 5940.0, 6161.0, 6444.0, 6623.262, 27486.979, 28312.031],
   [8.336839, 19.43, 32.93, 46.0, 61.0, 84.1, 101.0, 120.0, 141.0, 159.9, 238.57, 260.0, 286.0, 311.0, 342.0, 369.1, 427.0, 457.5, 810.0, 869.0, 933.0, 1000.0, 1065.0, 1145.0, 1218.0, 1290.0, 1366.0, 1438.0, 1644.0, 1706.2, 1781.3, 1869.0, 1962.0, 2016.0, 2181.0, 2248.87, 5284.0, 5475.0, 5683.0, 5880.0, 6242.0, 6469.0, 6759.0, 6943.097, 28776.032, 29622.678],
   [7.576234, 21.4844, 34.8, 49.0, 65.0, 82.0, 106.0, 125.0, 145.1, 167.0, 188.0, 271.46, 294.0, 321.0, 347.0, 381.0, 408.43, 469.0, 500.87, 885.0, 946.0, 1013.0, 1082.0, 1149.0, 1231.0, 1308.0, 1382.0, 1460.0, 1535.0, 1747.0, 1810.5, 1888.0, 1979.0, 2077.0, 2131.0, 2302.0, 2371.99, 5558.0, 5753.0, 5966.0, 6170.0, 6551.0, 6785.0, 7082.0, 7271.298, 30097.314, 30965.78],
   [8.99382, 16.908313, 37.468, 51.0, 67.9, 87.0, 105.0, 130.1, 150.0, 173.0, 195.0, 218.0, 305.0, 329.0, 358.0, 385.0, 421.0, 452.6, 513.0, 546.19, 963.0, 1026.0, 1095.0, 1167.0, 1237.0, 1320.0, 1401.0, 1477.0, 1558.0, 1635.0, 1852.0, 1917.9, 1998.0, 2091.0, 2195.0, 2250.0, 2427.0, 2498.62, 5839.0, 6039.0, 6257.0, 6460.0, 6869.0, 7109.0, 7414.0, 7607.95, 31451.07, 32341.587],
   [5.7863558, 18.87041, 28.04415, 55.45, 69.3, 90.0, 109.0, 130.1, 156.0, 178.0, 201.0, 226.0, 249.0, 341.0, 368.0, 396.0, 425.0, 462.0, 497.1, 560.0, 593.38, 1043.0, 1109.0, 1181.0, 1255.0, 1328.0, 1413.0, 1496.0, 1575.0, 1659.0, 1738.0, 1961.0, 2028.5, 2111.0, 2207.0, 2317.0, 2373.0, 2555.0, 2628.77, 6126.0, 6331.0, 6554.0, 6770.0, 7196.0, 7442.0, 7754.0, 7953.14, 32837.593, 33750.404],
   [7.343918, 14.63307, 30.506, 40.74, 77.03, 94.0, 112.9, 135.0, 156.0, 184.0, 208.0, 232.0, 258.0, 282.0, 379.0, 407.0, 437.0, 466.0, 506.0, 537.0, 608.0, 642.35, 1127.0, 1195.0, 1269.0, 1347.0, 1421.0, 1508.0, 1596.0, 1676.0, 1763.0, 1844.0, 2074.0, 2142.1, 2227.0, 2326.0, 2443.0, 2499.0, 2687.0, 2762.49, 6421.0, 6631.0, 6859.0, 7080.0, 7531.0, 7790.0, 8103.0, 8306.95, 34257.148, 35192.501]]

theorem priorThrough50Window : priorThrough50.all (centralTest nitrogen carbon) = true := by
  decide +kernel

def Antimony : List (Option Energy) :=
  [some ⟨1.047401,(some 0.000019)⟩, some ⟨8.608389,(some 0.000012)⟩, some ⟨16.626,(some 0.025)⟩, some ⟨25.3235,none⟩,
   some ⟨43.804,(some 0.025)⟩, some ⟨55.0,(some 0.1)⟩, some ⟨99.51,(some 0.05)⟩, some ⟨117.0,(some 2.0)⟩,
   some ⟨139.0,(some 2.1)⟩, some ⟨162.0,(some 2.2)⟩, some ⟨185.0,(some 2.2)⟩, some ⟨214.0,(some 2.4)⟩,
   some ⟨238.0,(some 2.5)⟩, some ⟨265.0,(some 3.0)⟩, some ⟨292.0,(some 3.0)⟩, some ⟨317.0,(some 3.0)⟩,
   some ⟨420.0,(some 3.0)⟩, some ⟨447.0,(some 3.0)⟩, some ⟨479.0,(some 3.0)⟩, some ⟨510.0,(some 3.0)⟩,
   some ⟨552.0,(some 4.0)⟩, some ⟨584.0,(some 4.0)⟩, some ⟨657.0,(some 4.0)⟩, some ⟨693.26,(some 0.24)⟩,
   some ⟨1214.0,(some 4.0)⟩, some ⟨1285.0,(some 4.0)⟩, some ⟨1360.0,(some 4.0)⟩, some ⟨1441.0,(some 4.0)⟩,
   some ⟨1518.0,(some 4.0)⟩, some ⟨1606.0,(some 4.0)⟩, some ⟨1698.0,(some 4.0)⟩, some ⟨1781.0,(some 4.0)⟩,
   some ⟨1869.0,(some 4.0)⟩, some ⟨1954.0,(some 4.0)⟩, some ⟨2190.0,(some 5.0)⟩, some ⟨2266.0,(some 5.0)⟩,
   some ⟨2349.0,(some 5.0)⟩, some ⟨2428.0,(some 5.0)⟩, some ⟨2567.0,(some 4.0)⟩, some ⟨2654.0,(some 4.0)⟩,
   some ⟨2815.0,(some 4.0)⟩, some ⟨2900.0,(some 0.5)⟩, some ⟨6714.0,(some 4.0)⟩, some ⟨6929.0,(some 4.0)⟩,
   some ⟨7167.0,(some 4.0)⟩, some ⟨7390.0,(some 4.0)⟩, some ⟨7887.0,(some 4.0)⟩, some ⟨8140.0,(some 4.0)⟩,
   some ⟨8455.0,(some 4.0)⟩, some ⟨8669.48,(some 0.04)⟩, some ⟨35710.03,(some 0.025)⟩, some ⟨36668.183,(some 0.012)⟩]

theorem AntimonyBoxCalls : labels Antimony =
    [some .outside, some .inside, some .missing, some .missing] ++ List.replicate 47 (some .inside) := by decide +kernel

def AntimonyOrdinary := Antimony.tail.filterMap (fun e => e.map Energy.e)
theorem AntimonyOrdinaryCalls :
    AntimonyOrdinary.length = 51 ∧ centralTest nitrogen cesium AntimonyOrdinary = true ∧
    ((AntimonyOrdinary.zip AntimonyOrdinary.tail).zipIdx.filterMap fun ((a,b),i) =>
      if outside a b then some (i+1) else none) = [] := by decide +kernel

def Tellurium : List (Option Energy) :=
  [some ⟨1.970875,(some 0.000007)⟩, some ⟨9.009808,(some 0.000006)⟩, some ⟨18.6,(some 0.4)⟩, some ⟨27.84,(some 0.04)⟩,
   some ⟨37.4155,(some 0.0012)⟩, some ⟨59.3,(some 0.9)⟩, some ⟨69.1,(some 2.0)⟩, some ⟨124.2,(some 0.06)⟩,
   some ⟨143.0,(some 2.1)⟩, some ⟨167.0,(some 2.2)⟩, some ⟨191.1,(some 2.2)⟩, some ⟨215.0,(some 2.4)⟩,
   some ⟨245.0,(some 2.5)⟩, some ⟨272.0,(some 3.0)⟩, some ⟨299.0,(some 3.0)⟩, some ⟨328.0,(some 3.0)⟩,
   some ⟨354.0,(some 3.0)⟩, some ⟨461.0,(some 3.0)⟩, some ⟨491.0,(some 3.0)⟩, some ⟨522.0,(some 3.0)⟩,
   some ⟨555.0,(some 4.0)⟩, some ⟨599.0,(some 4.0)⟩, some ⟨633.0,(some 4.0)⟩, some ⟨709.0,(some 4.0)⟩,
   some ⟨746.12,(some 0.25)⟩, some ⟨1304.0,(some 4.0)⟩, some ⟨1377.0,(some 4.0)⟩, some ⟨1455.0,(some 4.0)⟩,
   some ⟨1538.0,(some 4.0)⟩, some ⟨1618.0,(some 4.0)⟩, some ⟨1707.0,(some 4.0)⟩, some ⟨1803.0,(some 4.0)⟩,
   some ⟨1889.0,(some 4.0)⟩, some ⟨1979.0,(some 4.0)⟩, some ⟨2066.0,(some 5.0)⟩, some ⟨2309.0,(some 5.0)⟩,
   some ⟨2386.0,(some 5.0)⟩, some ⟨2472.0,(some 5.0)⟩, some ⟨2552.0,(some 4.0)⟩, some ⟨2700.0,(some 4.0)⟩,
   some ⟨2788.0,(some 4.0)⟩, some ⟨2954.0,(some 4.0)⟩, some ⟨3041.0,(some 0.5)⟩, some ⟨7022.0,(some 4.0)⟩,
   some ⟨7243.0,(some 4.0)⟩, some ⟨7485.0,(some 4.0)⟩, some ⟨7714.0,(some 4.0)⟩, some ⟨8240.0,(some 4.0)⟩,
   some ⟨8499.0,(some 4.0)⟩, some ⟨8821.0,(some 4.0)⟩, some ⟨9040.83,(some 0.04)⟩, some ⟨37196.52,(some 0.03)⟩,
   some ⟨38177.74,(some 0.015)⟩]

theorem TelluriumBoxCalls : labels Tellurium =
    [some .inside] ++ List.replicate 51 (some .inside) := by decide +kernel

def TelluriumOrdinary := Tellurium.tail.filterMap (fun e => e.map Energy.e)
theorem TelluriumOrdinaryCalls :
    TelluriumOrdinary.length = 52 ∧ centralTest nitrogen cesium TelluriumOrdinary = true ∧
    ((TelluriumOrdinary.zip TelluriumOrdinary.tail).zipIdx.filterMap fun ((a,b),i) =>
      if outside a b then some (i+1) else none) = [] := by decide +kernel

def Iodine : List (Option Energy) :=
  [some ⟨3.0590465,(some 0.0000036)⟩, some ⟨10.451236,(some 0.000025)⟩, some ⟨19.13126,(some 0.00012)⟩, some ⟨29.57,(some 0.025)⟩,
   some ⟨40.357,(some 0.025)⟩, some ⟨51.52,(some 0.04)⟩, some ⟨74.4,(some 0.4)⟩, some ⟨87.61,(some 0.06)⟩,
   some ⟨150.81,(some 0.1)⟩, some ⟨171.0,(some 2.2)⟩, some ⟨197.0,(some 2.2)⟩, some ⟨220.9,(some 2.4)⟩,
   some ⟨247.0,(some 2.5)⟩, some ⟨279.0,(some 3.0)⟩, some ⟨307.0,(some 3.0)⟩, some ⟨335.0,(some 3.0)⟩,
   some ⟨365.0,(some 3.0)⟩, some ⟨393.0,(some 3.0)⟩, some ⟨505.0,(some 3.0)⟩, some ⟨535.0,(some 3.0)⟩,
   some ⟨569.0,(some 4.0)⟩, some ⟨601.0,(some 4.0)⟩, some ⟨649.0,(some 4.0)⟩, some ⟨683.0,(some 4.0)⟩,
   some ⟨762.0,(some 4.0)⟩, some ⟨800.8,(some 0.4)⟩, some ⟨1397.0,(some 4.0)⟩, some ⟨1472.0,(some 4.0)⟩,
   some ⟨1553.0,(some 4.0)⟩, some ⟨1639.0,(some 4.0)⟩, some ⟨1720.0,(some 4.0)⟩, some ⟨1812.0,(some 4.0)⟩,
   some ⟨1911.0,(some 4.0)⟩, some ⟨1999.0,(some 4.0)⟩, some ⟨2093.0,(some 5.0)⟩, some ⟨2181.0,(some 5.0)⟩,
   some ⟨2431.0,(some 5.0)⟩, some ⟨2510.0,(some 5.0)⟩, some ⟨2598.0,(some 4.0)⟩, some ⟨2680.0,(some 4.0)⟩,
   some ⟨2836.0,(some 4.0)⟩, some ⟨2926.0,(some 4.0)⟩, some ⟨3096.0,(some 4.0)⟩, some ⟨3185.5,(some 0.5)⟩,
   some ⟨7337.0,(some 4.0)⟩, some ⟨7563.0,(some 4.0)⟩, some ⟨7811.0,(some 4.0)⟩, some ⟨8044.0,(some 4.0)⟩,
   some ⟨8601.0,(some 4.0)⟩, some ⟨8867.0,(some 4.0)⟩, some ⟨9196.0,(some 4.0)⟩, some ⟨9421.1,(some 0.04)⟩,
   some ⟨38717.0,(some 0.03)⟩, some ⟨39721.549,(some 0.017)⟩]

theorem IodineBoxCalls : labels Iodine =
    [some .inside] ++ List.replicate 52 (some .inside) := by decide +kernel

def IodineOrdinary := Iodine.tail.filterMap (fun e => e.map Energy.e)
theorem IodineOrdinaryCalls :
    IodineOrdinary.length = 53 ∧ centralTest nitrogen cesium IodineOrdinary = true ∧
    ((IodineOrdinary.zip IodineOrdinary.tail).zipIdx.filterMap fun ((a,b),i) =>
      if outside a b then some (i+1) else none) = [] := by decide +kernel

def Xenon : List (Option Energy) :=
  [none, some ⟨12.1298437,(some 0.0000015)⟩, some ⟨20.975,(some 0.004)⟩, some ⟨31.05,(some 0.04)⟩,
   some ⟨42.2,(some 0.2)⟩, some ⟨54.1,(some 0.5)⟩, some ⟨66.703,(some 0.007)⟩, some ⟨91.6,(some 0.5)⟩,
   some ⟨105.9778,(some 0.0025)⟩, some ⟨179.84,(some 0.12)⟩, some ⟨202.0,(some 2.2)⟩, some ⟨229.02,(some 0.2)⟩,
   some ⟨255.0,(some 2.5)⟩, some ⟨281.0,(some 3.0)⟩, some ⟨314.0,(some 3.0)⟩, some ⟨343.0,(some 3.0)⟩,
   some ⟨374.0,(some 3.0)⟩, some ⟨404.0,(some 3.0)⟩, some ⟨434.0,(some 3.0)⟩, some ⟨549.0,(some 3.0)⟩,
   some ⟨582.0,(some 4.0)⟩, some ⟨616.0,(some 4.0)⟩, some ⟨650.0,(some 4.0)⟩, some ⟨700.0,(some 4.0)⟩,
   some ⟨736.0,(some 4.0)⟩, some ⟨818.0,(some 4.0)⟩, some ⟨857.0,(some 0.4)⟩, some ⟨1493.0,(some 4.0)⟩,
   some ⟨1571.0,(some 4.0)⟩, some ⟨1653.0,(some 4.0)⟩, some ⟨1742.0,(some 4.0)⟩, some ⟨1826.0,(some 4.0)⟩,
   some ⟨1919.0,(some 4.0)⟩, some ⟨2023.0,(some 4.0)⟩, some ⟨2113.0,(some 5.0)⟩, some ⟨2209.0,(some 5.0)⟩,
   some ⟨2300.0,(some 5.0)⟩, some ⟨2556.0,(some 5.0)⟩, some ⟨2637.0,(some 4.0)⟩, some ⟨2726.0,(some 4.0)⟩,
   some ⟨2811.0,(some 4.0)⟩, some ⟨2975.0,(some 4.0)⟩, some ⟨3068.0,(some 4.0)⟩, some ⟨3243.0,(some 4.0)⟩,
   some ⟨3333.8,(some 0.5)⟩, some ⟨7660.0,(some 4.0)⟩, some ⟨7889.0,(some 4.0)⟩, some ⟨8144.0,(some 4.0)⟩,
   some ⟨8382.0,(some 4.0)⟩, some ⟨8971.0,(some 4.0)⟩, some ⟨9243.0,(some 4.0)⟩, some ⟨9581.0,(some 4.0)⟩,
   some ⟨9810.37,(some 0.04)⟩, some ⟨40271.73,(some 0.03)⟩, some ⟨41299.892,(some 0.019)⟩]

theorem XenonBoxCalls : labels Xenon =
    [none] ++ List.replicate 53 (some .inside) := by decide +kernel

def XenonOrdinary := Xenon.tail.filterMap (fun e => e.map Energy.e)
theorem XenonOrdinaryCalls :
    XenonOrdinary.length = 54 ∧ centralTest nitrogen cesium XenonOrdinary = true ∧
    ((XenonOrdinary.zip XenonOrdinary.tail).zipIdx.filterMap fun ((a,b),i) =>
      if outside a b then some (i+1) else none) = [] := by decide +kernel

def Cesium : List (Option Energy) :=
  [some ⟨0.471626,(some 0.000025)⟩, some ⟨3.89390572743,(some 0.00000000017)⟩, some ⟨23.15745,(some 0.00006)⟩, some ⟨33.195,(some 0.004)⟩,
   some ⟨43.0,(some 1.7)⟩, some ⟨56.0,(some 1.9)⟩, some ⟨69.1,(some 2.0)⟩, some ⟨82.9,(some 2.0)⟩,
   some ⟨110.1,(some 0.6)⟩, some ⟨125.61,(some 0.09)⟩, some ⟨213.3,(some 2.5)⟩, some ⟨233.0,(some 2.4)⟩,
   some ⟨261.0,(some 2.5)⟩, some ⟨289.0,(some 3.0)⟩, some ⟨316.0,(some 3.0)⟩, some ⟨352.0,(some 3.0)⟩,
   some ⟨382.0,(some 3.0)⟩, some ⟨413.0,(some 3.0)⟩, some ⟨445.0,(some 3.0)⟩, some ⟨476.0,(some 3.0)⟩,
   some ⟨597.0,(some 4.0)⟩, some ⟨629.0,(some 4.0)⟩, some ⟨666.0,(some 4.0)⟩, some ⟨700.0,(some 4.0)⟩,
   some ⟨753.0,(some 4.0)⟩, some ⟨791.0,(some 4.0)⟩, some ⟨875.0,(some 4.0)⟩, some ⟨916.1,(some 0.5)⟩,
   some ⟨1592.0,(some 4.0)⟩, some ⟨1672.0,(some 4.0)⟩, some ⟨1757.0,(some 4.0)⟩, some ⟨1848.0,(some 4.0)⟩,
   some ⟨1936.0,(some 4.0)⟩, some ⟨2029.0,(some 4.0)⟩, some ⟨2137.0,(some 5.0)⟩, some ⟨2230.0,(some 5.0)⟩,
   some ⟨2329.0,(some 5.0)⟩, some ⟨2422.0,(some 5.0)⟩, some ⟨2683.0,(some 4.0)⟩, some ⟨2767.0,(some 4.0)⟩,
   some ⟨2859.0,(some 4.0)⟩, some ⟨2945.0,(some 4.0)⟩, some ⟨3118.0,(some 4.0)⟩, some ⟨3214.0,(some 4.0)⟩,
   some ⟨3392.0,(some 4.0)⟩, some ⟨3485.0,(some 4.0)⟩, some ⟨7989.0,(some 4.0)⟩, some ⟨8224.0,(some 4.0)⟩,
   some ⟨8484.0,(some 4.0)⟩, some ⟨8726.0,(some 4.0)⟩, some ⟨9350.0,(some 4.0)⟩, some ⟨9629.0,(some 4.0)⟩,
   some ⟨9974.0,(some 4.0)⟩, some ⟨10208.78,(some 0.05)⟩, some ⟨41861.08,(some 0.04)⟩, some ⟨42913.144,(some 0.02)⟩]

theorem CesiumBoxCalls : labels Cesium =
    [some .outside, some .outside] ++ List.replicate 53 (some .inside) := by decide +kernel

def CesiumOrdinary := Cesium.tail.filterMap (fun e => e.map Energy.e)
theorem CesiumOrdinaryCalls :
    CesiumOrdinary.length = 55 ∧ centralTest nitrogen cesium CesiumOrdinary = true ∧
    ((CesiumOrdinary.zip CesiumOrdinary.tail).zipIdx.filterMap fun ((a,b),i) =>
      if outside a b then some (i+1) else none) = [1] := by decide +kernel

/-- The newly met upper endpoint is attained by the first ordinary cesium crossing. -/
theorem cesiumWitness : CesiumOrdinary[1]! / CesiumOrdinary[0]! = cesium ∧
    ¬ (6 < CesiumOrdinary[1]! / CesiumOrdinary[0]!) ∧
    outside CesiumOrdinary[0]! CesiumOrdinary[1]! = true := by decide +kernel

theorem previousWitnesses :
    let n := priorThrough10[6]!
    let c := priorThrough10[5]!
    n[5]!/n[4]! = nitrogen ∧ outside n[4]! n[5]! = false ∧
    c[4]!/c[3]! = carbon ∧ outside c[3]! c[4]! = true := by decide +kernel

def historical := (priorThrough10 ++ priorThrough20 ++ priorThrough30 ++ priorThrough40 ++ priorThrough50).flatMap (fun e => e.zip e.tail)
def beforeCesium := historical ++ ([AntimonyOrdinary, TelluriumOrdinary, IodineOrdinary, XenonOrdinary] : List (List Rat)).flatMap (fun e => e.zip e.tail)
def expanded := beforeCesium ++ CesiumOrdinary.zip CesiumOrdinary.tail

theorem historicalAndExpandedCount : historical.length=1225 ∧ beforeCesium.length=1431 ∧ expanded.length=1485 := by decide +kernel

theorem windowHydrogenTin (c : Rat) : Fits historical c ↔ nitrogen ≤ c ∧ c < carbon := by
  apply sharpWindow historical (97.8901,552.06741) (64.49352,392.09056) <;> decide +kernel

theorem windowHydrogenXenon (c : Rat) : Fits beforeCesium c ↔ nitrogen ≤ c ∧ c < carbon := by
  apply sharpWindow beforeCesium (97.8901,552.06741) (64.49352,392.09056) <;> decide +kernel

theorem windowHydrogenCesium (c : Rat) : Fits expanded c ↔ nitrogen ≤ c ∧ c < cesium := by
  apply sharpWindow expanded (97.8901,552.06741) (3.89390572743,23.15745) <;> decide +kernel

theorem cutoffSixFirstFailsWithCesium : Fits beforeCesium 6 ∧ ¬ Fits expanded 6 := by
  rw [windowHydrogenXenon, windowHydrogenCesium]
  decide +kernel

#print axioms agreesAtAnyCut
#print axioms sharpWindow
#print axioms orderedEndpoints
#print axioms priorThrough10Window
#print axioms priorThrough20Window
#print axioms priorThrough30Window
#print axioms priorThrough40Window
#print axioms priorThrough50Window
#print axioms AntimonyBoxCalls
#print axioms AntimonyOrdinaryCalls
#print axioms TelluriumBoxCalls
#print axioms TelluriumOrdinaryCalls
#print axioms IodineBoxCalls
#print axioms IodineOrdinaryCalls
#print axioms XenonBoxCalls
#print axioms XenonOrdinaryCalls
#print axioms CesiumBoxCalls
#print axioms CesiumOrdinaryCalls
#print axioms cesiumWitness
#print axioms previousWitnesses
#print axioms historicalAndExpandedCount
#print axioms windowHydrogenTin
#print axioms windowHydrogenXenon
#print axioms windowHydrogenCesium
#print axioms cutoffSixFirstFailsWithCesium

end ElementPaper.Batch11
