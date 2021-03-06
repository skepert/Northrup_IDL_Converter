# Northrup_IDL_Converter
Convert raw .dat files from Northrup IDL software into csv file

We want to take the .dat files from Paul Northrup's IDL software, strip out anything that isn't element data, and convert them into csv format. 
Input files will look something like this:

#  ROI    Min   Max    Mean     Sigma    Median     Mode
I0  905,192.6  927,346.1  916,730.1  2,967.2  916,862.6  911,592.8
I0_raw  997,990.0  1,020,140.0  1,009,527.6  2,967.2  1,009,660.0  1,009,455.0
IT  -7,861.1  6,789.3  81.9  2,116.5  143.7  -1,295.8
IT_raw  119,070.0  133,720.0  127,012.3  2,116.5  127,075.0  126,800.0
T  999,965.7  1,000,078.5  1,000,018.9  11.8  1,000,019.1  1,000,019.7
T_raw  49,998,284.0  50,003,924.0  50,000,948.0  590.3  50,000,956.0  50,000,984.0
pin_ES1  -140.0  1,934.8  828.4  340.5  799.9  725.1
pin_ES1_raw  18,855.0  20,930.0  19,823.3  340.5  19,795.0  19,810.0
OutputCount (mca1)  39,475.0  52,660.0  44,793.2  2,258.9  44,482.5  43,830.0
OutputCount (mca2)  38,560.0  51,655.0  44,541.4  2,452.5  44,545.0  44,845.0
OutputCount (mca3)  36,270.0  48,205.0  41,695.1  2,371.2  41,652.5  42,495.0
OutputCount (mca4)  36,445.0  48,230.0  40,874.2  2,153.0  40,572.5  39,770.0
OutputCount (mca5)  38,700.0  51,350.0  43,513.7  2,122.4  43,172.5  41,470.0
OutputCount (mca6)  40,830.0  53,345.0  45,937.6  2,114.9  45,690.0  46,245.0
OutputCount (mca7)  40,925.0  53,215.0  46,753.3  2,260.0  46,660.0  46,300.0
OutputCount (mca8)  0.0  0.0  0.0  0.0  0.0  0.0
Si Ka (mca1)  0.0  60.0  19.5  9.9  20.0  15.0
Si Ka (mca2)  0.0  65.0  20.1  10.1  20.0  20.0
Si Ka (mca3)  0.0  65.0  19.9  10.2  20.0  20.0
Si Ka (mca4)  0.0  50.0  18.7  9.7  20.0  15.0
Si Ka (mca5)  0.0  60.0  22.1  10.4  20.0  20.0
Si Ka (mca6)  0.0  70.0  24.8  11.2  25.0  20.0
Si Ka (mca7)  0.0  65.0  22.8  10.7  20.0  20.0
Si Ka (mca8)  0.0  0.0  0.0  0.0  0.0  0.0
K Ka (mca1)  45.0  220.0  109.6  25.3  110.0  95.0
K Ka (mca2)  45.0  220.0  118.9  26.3  120.0  125.0
K Ka (mca3)  35.0  190.0  97.3  23.1  95.0  95.0
K Ka (mca4)  20.0  200.0  92.3  23.1  90.0  95.0
K Ka (mca5)  35.0  225.0  117.2  26.9  115.0  105.0
K Ka (mca6)  40.0  205.0  111.2  25.9  110.0  110.0
K Ka (mca7)  45.0  215.0  117.5  25.4  115.0  105.0
