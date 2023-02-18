### Project Title:
Anatomy of a Resale HDB Flat: An Analysis on HDB Resale Prices and its Factos for Predictions

### Problem Description:
4 in 5 Singapores own or will own HDB flats. As it's one of the most expensive purchases people will make, it is important to be able to accurate price these flats. Furthermore, with delays to BTO flats due to covid, more young buyers are entering the resale market instead. To give us an edge, we will also be identifying the factors that make a HDB flat desirable by employing a linear regression model. The model will solve our problem by:
* Predicting the price
* Having interpretable and quantifiable coefficients to identify the price factors

### Dataset:
We'll be using a dataset provided by kaggle (https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/overview), which contains over 150,000 transactions and 77 features. 

### Project Overview:
In this project, we'll be employing the 6 step data science process:  
1. Define the Problem
2. Obtain the Data
3. Explore the Data
4. Model the Data
5. Evaluate the Data
6. Answer the Problem  

### Exploratory Data Analysis
Through the exploratory data analysis, we will identify features to use in the model and also engineer features we require. We will also identify features that have multi-collinearity or outliers, assess and deal with them.   

The first step we took in this process was to eliminate features we don't intend to use by employing domain knowledge and common sense. After cleaning up the data, we looked at the correlation of the features to identify multi-collinearity and addressed highly correlated features one-by-one. Next, we looked at outliers and through data visualizations, determined if they need to be dropped or if it would be justifiable to keep them.   

Lastly, we perform exploratory visualizations to answer the following questions we had.  

1. Which flat types are being sold the most?
By looking at the data and visualization, we assessed that most of the flats types on sale are 3 room, 4 room, 5 room and executive flats. 

2. How does the floor area affect the resale price?
By plotting a scatterplot, we can see that there is a direct correlation betwen the floor area and the resale price. As the size of the flat increases, the resale price increases appropriately. We can also see that most flat types have a consistent floor area. 

3. Which flat model is most popular for the resale market?
The Model A and Improved flat models are the most popular in the resale market. 

4. Which towns command the highest mean reslae price?
Bukit Timah has the highest mean resale price. This area is also known to have a lot of landed property, hence it is an estate where the rich live in.

5. How has the mean prices of flats changed over the years?
There was a dip in the resale price in 2013 due to cooling measures introduced by the Singapore Government. From 2020 onwards, the steep increase in price could be attributed to the pandemic, where a lot of Build-to-Order (BTO) projects were delayed and couples purchased flats in the resale market instead. 

6. Are there any months where there were significantly more sales?
There are a significant amount of sales consistently throughout the year. However, the most sales happen in March. Perhaps this could be attributed to the anticipation of performance bonuses being paid out in April. 


### Modelling
In this project, we are using the Linear Regression model. Rather than simply using one model, we created five. First was the base model with mean price to use as a comparison. Next, we had a vanilla linear regression model. Lastly, we applied regulazation (Ridge, Lasso, Elastic Net)to the linear regression. Looking at the results and coefficients of the models, we found that the Lasso model performed best, giving a RSME value of 47,559. We also confirmed that the model did not overfit as the training and validation datasets provided similar RSME values. As such, we used it as our production model. By applying the model to unseen data on kaggle, we achieved a RSME score of 47,659 on kaggle. 


### Insights and Conclusion
We'll cover the insights in three sections:

#### Top 5 features that add the most value to a home
The top 5 features identified are:
1. Floor area
2. Years left in the lease
3. Floor of the flat
4. Hawker Nearest Distance
5. MRT Nearest Distance  

The top three features are not surprising as they are commonly associated to house pricing. However, the 4th and 5th features are interesting to note. 

**Hawker Nearest Distance**
The high score probably represents the food culture in Singapore, where takeout is readily available at an affordable price and also shows the love of food here. Clearly, buyers are willing to pay a premium to be located near a Hawker Centre. With the work from home culture trending due to the pandemic, we can assume that Hawker Centres will continue to be a key factor as white collar workers working at home might not have the time to cook their lunch.  

**MRT Nearest Distance**
This coefficient stresses the unique situation in Singaore, where cars are incredibly unaffordable due to the high COE price. Due to that, majority of the public are forced to take the cheap and reliable public transportation network, primarily the MRT. Hence, it makes sense that people who require to travel daily for work or school would be willing to pay a higher price for the convenience of being located near an MRT station.

#### Top 2 features that hurt the value of a home the most
Compared to the features that significantly increase the price of flats, there are only two groups of features that significantly hurt the value of a flat. There are:
1. Town
2. Transaction Year 

**Town**   
It is natural for the location of the estate to affect the resale price. Some locations are more convenient and better developed compared to others. From the model, we can see that towns like Bukit Merah, Marine Parade, Queenstown and Bishan are able to command higher prices compared to other lcoations. Inversely, we can see that towns such as Woodlands, Jurong West, Bukit Panjang, Choa Chu Kang, Sembawang and Yishun have negative effects to the price. A clear observation here is that towns in the West and North are not favored, possibly due to them being out of the way and far away from the central area of the island. 

**Transaction Year**  
From the coefficients for the different transaction years, we can see that certain years have a strong negative effect on the resale prices. In particular, the period between 2015 to 2019 had a big negative effect. One possible explanation for this is the property cooling measures that were introduced in 2013 which kept property prices down. 

#### Other features of note
**Primary and Secondary School Distance**    
It is interesting to note that the distance to schools are not significant features, despite families moving homes to ensure their kids are eligible for good schools. One possible explanation here is that families might only need the school of their choice within the town. Distance might not be important to them due to the efficient, reliable and safe public transport network available. 

**Flat Types and Models**  
Flat types and models do not seem to be strong indicators for the resale price. One explanation for this could be that most buyers would rather look at the size of the flat (i.e. floor area) and use that to determine their needs. However, one interesting coefficient to note is on the feature for flat model DBSS, which has a rather high coefficient. This could be due to the flat model's unique characteristics compared to a traditional HDB. The DBSS (Developed by Sellers) flat was introduced in 2005 and discontinued in 2011. These flats were build by private developers and sold by HDB. What seperates the DBSS flat from condos and HDBs was that they were developed as condo apartments, but without the facilities a condo would have (e.g. pool, gym, etc). One assumption here could be that buyers are keen to live in a condo apartment, but are unwilling to pay for the extra facilities that come with a condo, especially since there are many such public facilities available for cheap. Since this flat model is discontinued, it's availablitiy is lacking, which could also drive up its price. 

**Bus Stop Nearest Distance**  
It is interesting that the model penalized the bus stop nearest distance coefficient to zero. This means that the model has deemed this feature having no impact on the price of the flat. This could be because buyers are more focused on purchasing flats near MRT stations, as shown by the strong coefficient on MRT nearest distance. This is also in line with the Land Transport Authority's plan to continue beefing up the MRT network to ensure that majority of flats are located walking distnace to an MRT station. With the ease of access and convenience of the MRT network, buses might not be a favored option, especially since bus timing might not be regular due to being affected by traffic conditions.  

### Future Recommendations
Based on the results and its analysis, the following improvements could also be made on the model in the future:
* The distance to important amenitites could be misleading as there might not be a direct route. Hence, we can consider using travel time instead
* We can consider the  number of new flats that finish their minimum occupancy period (MOP) per year. This gives us a sensing of how many new flats are entering the resale market that year, affecting the supply.
* The model has shown that the number of years remaining in the lease is a very significant feature. We also know that the value of a house appreciate over time, but eventually the value could start to decrease due to the depreciation of the lease. We should investigate further at which point does the depreciation become significant and starts lowering the price of the flat

### Directory Structure
```
project-2  
|__ code  
|   |__ 01_EDA_Cleaning_and_Feature_Engineering.ipynb     
|   |__ 02_Exploratory_Visualizations.ipynb     
|   |__ 03_Preprocessing_and_Modelling.ipynb  
|   |__ 04_Production_Model_and_Insights.ipynb     
|__ datasets  
|   |__ kaggle_sub.csv  
|   |__ lasso_model.pkl  
|   |__ sample_sub_reg.csv  
|   |__ standard_scaler.pkl  
|   |__ test_cleaned.csv  
|   |__ test.csv  
|   |__ train_cleaned.csv  
|   |__ train.csv  
|__ An Analysis on HDB resale prices and its factors for predictions.pdf  
|__ README.md  
```
