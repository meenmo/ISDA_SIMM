# ISDA SIMM
This is an implementation of ISDA Standard Initial Margin Model (a.k.a. [ISDA SIMM™](https://www.isda.org/category/margin/isda-simm/)) version 2.3 & 2.4 to calculate the initial margin of uncleared over-the-counter derivatives in Python. The implementation is soley based on the official [ISDA SIMM Methodology Documents](https://www.isda.org/a/CeggE/ISDA-SIMM-v2.4-PUBLIC.pdf).

비청산 장외파생상품 개시증거금 ISDA SIMM 산출 Python 엔진입니다


## Getting Started
  - Place your [CRIF](https://www.isda.org/a/owEDE/risk-data-standards-v1-36-public.pdf) file under the folder "CRIF" with all columns needed for the calculation
  - Run main.py

## Results Example
|     SIMM Total     |    Add-On   |  Product Class  |  SIMM_ProductClass  |  Risk Class  |    SIMM_RiskClass    |  Risk Measure  |    SIMM_RiskMeasure   |
|:------------------:|:-----------:|:---------------:|:-------------------:|:------------:|:--------------------:|:--------------:|:---------------------:|
|    16,111,268,937  | 816,400,002 |    Commodity    |        289,586,229  |   Commodity  |         289,586,229  |    Curvature   |        34,987,138     |
|                    |             |                 |                     |              |                      |      Delta     |       171,187,064     |
|                    |             |                 |                     |              |                      |      Vega      |        83,412,026     |
|                    |             |      Credit     |     13,774,076,995  |  CreditNonQ  |     11,473,625,787   |    Curvature   |             36,291    |
|                    |             |                 |                     |              |                      |      Delta     |   11,472,297,989      |
|                    |             |                 |                     |              |                      |      Vega      |          1,291,507    |
|                    |             |                 |                     |    CreditQ   |      3,933,746,616   |    BaseCorr    |          9,044,453    |
|                    |             |                 |                     |              |                      |    Curvature   |             33,042    |
|                    |             |                 |                     |              |                      |      Delta     |     3,922,360,448     |
|                    |             |                 |                     |              |                      |      Vega      |          2,308,673    |
|                    |             |                 |                     |    Equity    |          34,785,002  |    Curvature   |                    -  |
|                    |             |                 |                     |              |                      |      Delta     |        34,785,002     |
|                    |             |                 |                     |              |                      |      Vega      |                    -  |
|                    |             |                 |                     |      FX      |           7,064,086  |    Curvature   |                    -  |
|                    |             |                 |                     |              |                      |      Delta     |          7,064,086    |
|                    |             |                 |                     |              |                      |      Vega      |                    -  |
|                    |             |                 |                     |     Rates    |         192,531,632  |    Curvature   |                    -  |
|                    |             |                 |                     |              |                      |      Delta     |       192,531,632     |
|                    |             |                 |                     |              |                      |      Vega      |                    -  |
|                    |             |      Equity     |        464,520,787  |    Equity    |         235,482,184  |    Curvature   |          6,262,663    |
|                    |             |                 |                     |              |                      |      Delta     |       158,843,566     |
|                    |             |                 |                     |              |                      |      Vega      |        70,375,955     |
|                    |             |                 |                     |     Rates    |         330,171,266  |    Curvature   |                    -  |
|                    |             |                 |                     |              |                      |      Delta     |       330,171,266     |
|                    |             |                 |                     |              |                      |      Vega      |                    -  |
|                    |             |     RatesFX     |        766,684,924  |      FX      |          25,589,599  |    Curvature   |          9,061,235    |
|                    |             |                 |                     |              |                      |      Delta     |        11,926,343     |
|                    |             |                 |                     |              |                      |      Vega      |          4,602,021    |
|                    |             |                 |                     |     Rates    |         759,126,165  |    Curvature   |               1,947   |
|                    |             |                 |                     |              |                      |      Delta     |       759,108,218     |
|                    |             |                 |                     |              |                      |      Vega      |             16,000    |
## Warning
If you intend to implement this for any commercial purpose, reach out to ISDA SIMM™ (isdalegal@isda.org) to obtain a proper liscense. You can find futher details [here](https://www.isda.org/2021/04/08/isda-simm-licensing-faq/).
