### Problem Title:
Does Rainy Weather Increase Healthcare Cases

### Problem Description:
There is a general consensus that during rainy seasons, people tend to fall sick more (e.g. flu). Furthermore, the wet environment could increase the likelyhood of road accidents and create an environment for mosquitoes to breed, resulting in an increase in dengue cases. If the above statement is true, analyzing the climate data in Singapore would allow healthcare professionals to identify peak periods where more staff and other resources such as hospital bed and medication would be needed. Advertising campaigns to get a flu jab can be made timely as well information campaigns to remind residents to ensure there are no mosquito breeding grounds formed. 

### Dataset:
*Flu and Dengue Data*
[Number of Flu and Dengue cases from 2012 to 2020](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2020/weekly-infectious-diseases-bulletin)
[Number of Flu and Dengue cases in 2021](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2021)
[Number of Flu and Dengue cases in 2022](https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2022)

*Road Accident (Injuries and Fatalities)*
[Number of accidents from 2008 to 2021](https://www.police.gov.sg/media-room/statistics)

*Climate Data*
[Monthly number of rain days from 1982 to 2022](../data/rainfall-monthly-number-of-rain-days.csv)

[Monthly total rainfall in mm from 1982 to 2022](../data/rainfall-monthly-total.csv)

[Relative Humidity](https://data.gov.sg/dataset/relative-humidity-monthly-mean)

[Monthly Mean Shunshine Hours](https://data.gov.sg/dataset/sunshine-duration-monthly-mean-daily-duration)

[Surface Air Temperature](https://data.gov.sg/dataset/surface-air-temperature-mean-daily-minimum)


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
The amount of flu cases over the months exhibit a somewhat normal distribution. In our analysis, we plot the below two scatterplots to look for correlation:
1. No. of flu cases per month vs total rainfall per month
* No correlation is observed and the no. of flu cases generally averages between 80,000 cases per month regardless of the total rainfall. 
2. No. of flu cases per month vs no. of rainy days
* No correlation is observed and the no. of flu cases generally averages between 80,000 cases per month regardless of the no. of rainy days. 
3. January and July have a higher amount of flu cases every year, which could indicate the flu season. However, no similar trend is observed with the total rainfall and number of rainy days, hence there is no observable link.
4. The long term trend of flu cases seems to be on a downtrend. However, this could be due to the lockdowns and mask wearing due to covid-19.

- The correlation between flu cases and relative humidity, sunshine hours and air temperature was also calcuated and no strong correlation was found. 

### Analysis of Dengue Cases:
The amount of dengue cases over the months exhibit a right skewed distribution. In our analysis, we plot the below two scatterplots to look for correlation:
1. No. of dengue cases per month vs total rainfall per month
* No correlation is observed and the number of dengue cases generally averages around 500 to 1,000 cases per month regardless of total rainfall. 
2. No. of dengue cases per month vs no. of rainy days
* No correlation is observed and the no. of dengue cases generally averages around 500 to 1,000 cases per month regardless of the no. of rainy days. 
3. A lot of varience is observed in the number of dengue cases during June and July. No similar trend is observed in the total rainfall and number of rainy days. Hence, there is no observable link. 
4. The number of dengue cases seems to be increasing on the long term trend. 

- The correlation between dengue cases and relative humidity, sunshine hours and air temperature was also calcuated and no strong correlation was found. 

### Analysis of Road Accident Cases:
The amount of road accidents over the months exhibit a left skewed distribution. In our analysis, we plot the below two scatterplots to look for correlation:
1. No. of road accidents per month vs total rainfall per month
* No correlation is observed and the number of road accidents generally averages around 600 to 700 cases per month regardless of total rainfall. 
2. No. of road accidents per month vs no. of rainy days
* No correlation is observed and the number of road cases generally averages between 600 to 700 cases per month regardless of the no. of rainy days. 

- The correlation between road accidents and relative humidity, sunshine hours and air temperature was also calcuated and no strong correlation was found. 

### Conclusion:
Based on the exploratory data analysis performed, no strong link can be found between climate data (specifically total rainfall per month and number of rainy days per month) to the number of flu cases, dengue cases and accident cases per month. As such, there is no evidence of a need to stock up on resources such as medication, vaccination and hospital staff during the rainy season. Similarly, no evidence is found to justify that running advertising campaigns before and during the rainy season would affect the number of flu, dengue and accident cases. 