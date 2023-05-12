# Progress Report 3
## Topic Modeling of Academic Journals

## Requirements
|S/N| Question| Answer|
|---|--------|-------|
|1. |Do you have data fully in hand and if not, what blockers are you facing?|Data collected|
|2. |Have you done a full EDA on all of your data?| Yes, but i need to touch it up for the presentation|
|3. |Have you begun the modeling process? How accurate are your predictions so far?|(a) 3 models completed, 1 to go. <br><br> (b) Still fine-tuning the results. Looking at coherence model/score to help with identifying the number of topics and keywords i should use|
|4. |What blockers are you facing, including processing power, data acquisition, modeling difficulties, data cleaning, etc.? How can we help you overcome those challenges?|(a) Seems like Bertopic needs cloud to support the processing. <br><br> (b) Also having difficulty with fine tuning the LDA model to get meaningful insight|
|5. |Have you changed topics since your lightning talk? Since you submitted your Problem Statement? If so, do you have the necessary data in hand (and the requisite EDA completed) to continue moving forward?| Removed text classification component as most articles comprise of the 3 labels i wanted to use. Hence, its not possible to do text classification|
|6. |What is your timeline for the next week and a half? What do you have to get done versus what would you like to get done?|Refer to outstanding work below|
|7. |What topics do you want to discuss during your 1:1?|(a) Need help with removing certain stopwords. <br><br> (b) Any tips on choosing the number of topics and key words for topic modeling?|

## Oustanding Work
* Can't seem to remove the stop words "model" and "based" - **NEED TAs HELP**
* BERTopic (kills my kernal. need cloud i think)
* Fine tune the stop words to make the keywords in each topic distinct
* Evaluate the key words and create a proper topic label using domain knowledge and reading the top few articles for each topic
* Topic evaluation with visualizations, distributions and trending
* Recommendations for the organization
* Create dashboard
* Touch up on the EDA for presentation slides
* Create slides and prepare for presentation

## EDA Guidelines
|S/N| Question| Answer|
|---|---------|-------|
|1.|Identify the data types you are working with.| Text and dates|
|2.|Examine the distributions of your data, numerically and/or visually.| (a) Word frequency and document length. <br><br> (b) To look at the the trends and the distributions of the model output|
|3. | Identify outliers.| Nil|
|4. | Identify missing data and look for patterns of missing data.| Nil|
|5. | Describe how your EDA will inform your modeling decisions and process.| (a) EDA of initial data helps to identify stop words. <br><br> (b) EDA of model output will help to make decisions for the organization|