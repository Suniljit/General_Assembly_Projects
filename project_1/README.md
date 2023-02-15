### Problem Title:
Does Rainy Weather Increase Healthcare Cases?

### Problem Description:
There is a general consensus that during rainy seasons, people tend to fall sick more (e.g. flu). Furthermore, the wet environment could increase the likelyhood of road accidents and create an environment for mosquitoes to breed, resulting in an increase in dengue cases. If the above statement is true, analyzing the climate data in Singapore would allow healthcare professionals to identify peak periods where more staff and other resources such as hospital bed and medication would be needed. Advertising campaigns to get a flu jab can be made timely as well information campaigns to remind residents to ensure there are no mosquito breeding grounds formed. 

### Dataset:
*Flu and Dengue Data* <br>
    * [Number of Flu and Dengue cases from 2012 to 2020](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2020/weekly-infectious-diseases-bulletin)<br>
    * [Number of Flu and Dengue cases in 2021](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2021)<br>
    * [Number of Flu and Dengue cases in 2022](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2022)<br>

*Road Accident (Injuries and Fatalities)*<br>
    * [Number of accidents from 2008 to 2021](https://www.police.gov.sg/media-room/statistics)<br>

*Climate Data* <br>
    * [Monthly number of rain days from 1982 to 2022](../data/rainfall-monthly-number-of-rain-days.csv)<br>
    * [Monthly total rainfall in mm from 1982 to 2022](../data/rainfall-monthly-total.csv)<br>
    * [Relative Humidity](https://data.gov.sg/dataset/relative-humidity-monthly-mean)<br>
    * [Monthly Mean Shunshine Hours](https://data.gov.sg/dataset/sunshine-duration-monthly-mean-daily-duration)<br>
    * [Surface Air Temperature](https://data.gov.sg/dataset/surface-air-temperature-mean-daily-minimum)<br>

### Project Overview:
In this project, we'll be looking at three focus points:
1. Number of Flu cases in a month (as MOH does not report the number of flu cases, we will use the number of Acute Upper Respiratory cases as a proxy, as the largest contrbuting factor to this figure is the flu)
    * The assumption here is that wet weather provides an environment for the flu to spread, thus increasing the number of flu cases. We will compare the flu numbers with climate data to determine if this assumption is correct.

2. Number of Dengue cases in a month
    * The assumption here is that during a period of wet weather, puddles of stagnant waters can form, which provides mosquitos with a breeding ground. This increaes the number of mosquitos, thus causing a dengue outbreak. We will compare the dengue case numbers with climate data to determine if this assumption is correct. 

3. Road Accidents in a month (Injuries and Fatalities)
    * The assumption here is the wet weather will make road more slippery and reduce visibility for drivers, thus increasing the number of accidents on the road. We will compare the road accident numbers with climate data to determine if this assumption is correct. 

We will try to look for correlation between these three focus points and the monthly total rainfall and monthly number of rainy days. Where applicable, we will also look at the correlation of the focus points to relative humidity, sunshine hours and air temperature

### Analysis of Flu Cases:
The amount of flu cases over the months exhibit a somewhat normal distribution. Through our analysis, we found that:
1. No observable link is found between the monthly total rainfall and monthly number of rainy days to flu cases.
2. However, there is usually a spike in flu cases in January and July compared to other months, hence further investigation looking at other possible factors is warranted.
3. Looking at the long term trend, the number of flu cases has been decreasing. However, with a closer look, the flu cases were actually rather flat, but significantly dropped in 2020 and 2021. This could be attributed to lock downs and mask wearing due to covid-19.

### Analysis of Dengue Cases:
The amount of dengue cases over the months exhibit a right skewed distribution. Through our analysis, we found that:
1. No observable link is found between the monthly total rainfall and monthly number of rainy days to dengue cases.
2. A lot of variance is observed during June and July, meaning that there are quite a few years with spikes in dengue cases during these months. Further investigation is recommneded to identify the cause.
3. The long term trend shows that the number of dengue cases has been increasing. Hence, more investigation into the cause is advised. 

### Analysis of Road Accident Cases:
The amount of road accidents over the months exhibit a left skewed distribution. Through our analysis, we found that:
1. The only observable link is found between the monthly total rainfall and monthly number of rainy days to road accident cases is that there is a decrease in all three attributes during Febuary. However, on the months with higher rainfall and rainy days (e.g. December and January), there is no increase in the number of road accidents. Hence, we cannot conclude that total rainfall and more rainy days affects the number of road accidents.
2. The number of road accidents has been on a declining trend. Hence, more investigation into other factors causing this is advised.

### Conclusion:
Based on the exploratory data analysis performed, no strong link can be found between climate data (specifically total rainfall per month and number of rainy days per month) to the number of flu cases, dengue cases and accident cases per month. As such, there is no evidence of a need to stock up on resources such as medication, vaccination and hospital staff during the rainy season. Similarly, no evidence is found to justify that running advertising campaigns before and during the rainy season would affect the number of flu, dengue and accident cases. 