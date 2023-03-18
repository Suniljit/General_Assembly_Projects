### Project Title:
Digitalizing our Marketing and Branding Infringement Checks

### Problem Description:
We, Super Heroes Media Incorporated, are a marketing and branding agency that works with both Disney and Warner Bros for superhero movie franchises, namely the Marvel Cinematic Universe (MCU) for Disney and DC Extended Universe (DCEU) for Warner Bros. As we are representing two clients both working in the same field, it is important to maintain a distinct brand for both MCU and DCEU. By distinct brand, we mean to ensure that there is no misunderstanding when there is discussion or advertising for super hero characters (e.g. When Captain America is mentioned, he should be correctly assosicated to MCU. Similarly, Superman should be associated to DCEU). If a mistake is made during one of our advertising campaign, it could result in an expensive lawsuit from either Disney or Warner Bros.    

As a way to ensure a clear brand and prevent mixing characters or overlapping information between MCU and DCEU, we will be creating a classification model using posts from Reddit.

### Dataset:
We'll be scraping posts from the following two subreddits:
* r/marvelstudios for MCU
* r/DC_cinematic for DCEU 

We used the Pushshift API to scrap 1000 posts from each subreddit.

### Project Overview:
In this project, we'll be employing the 6 step data science process:  
1. Define the Problem
2. Obtain the Data
3. Explore the Data
4. Model the Data
5. Evaluate the Data
6. Answer the Problem  

### Exploratory Data Analysis (EDA)
For this project, we took an iterative approach between cleaning the data and conducting our EDA. Basically, we cleaned the data, performed EDA, then went back to clean it further, before conducting EDA again.  

Through the exploratory data analysis, we will be looking into the following:
* Word count in the post title and post text
* Most frequently occuring words  

**Word Count in the Post Title and Post Text**  
From the figures below, we can see that both distributions have a right skew, as would be expected. 
![](https://github.com/Suniljit/General_Assembly_Projects/blob/main/project_3/images/word_length.png)

**Most Frequently Occuring Words**
Quite a few common and giveaway words were identified when looking at the most frequently occuring words. Hence, they were included into our stopword list and removed to increase the quality of the data. After this cleaning process, we can observe that the words observed for both MCU and DCEU are very distinct.

### Modelling
In this project, there were two key steps in our modelling process:
1. Vectorization
2. Application of Classification Algorithm

**Vectorization**
There were two vectorizers used in our modelling:
1. Count Vectorizer
Converts a collection of text documents into a matrix of token counts
2. TF-IDF Vectorizer
Similar to Count Vectorizer, but also tells us which words are important to one document, relative to all other documents.

**Classification Algorithms**
1. Naive Bayes
The Naive Bayes model is a probabilistic classifier based on Bayes' theorem. It heavily relies on one simplifying assumption, which is that we assume our features are indepedent from one another. 

2. Logistic Regression
The logistic regression gives us the probability of a feature being in each class by using a link function to "bend" of line of best fit into a curve of best fit to match the values we're interested in. This link funciton is known as the logit link.

3. K-Nearest Neighbors
The KNN model is a non-parametric method that uses the nearest neighbor's classification to assign a class membership. 

4. Random Forest
The Random Forest Classifier is an emsemble method that combines the predictions of other smaller models. Each of the smaller model is a decision tree. 

5. Support Vector Machine
The Support Vector Machine is a classification model that predicts the categorical vairables. They belong to a wider class of models called discriminant models. 

### Model Evaluation
The table below summarizes the scores for all the models trained and tested. 

|Model   | Model Type          |Training Accuracy |Test Accurary | Specificity | Recall | Precision | F1     | ROC AUC |
|------------|---------------------|----|----------|-------------|--------|-----------|--------|---------|
|Model 0     |Dummy Classifier     |0.5133|0.4898    |0.5152       |0.4672  |0.5193     |0.4919  |0.5      |
|Model 1     |Naive Bayes (Cvec)   |0.8998|0.8837|0.9177|0.8533| 0.9208|0.8858| 0.95|
|Model 2     |Naive Bayes (TF-IDF) |0.893| 0.8510|0.8745|0.8301|0.8811|0.8545|0.94|
|Model 3     |Logistic Regression (Cvec)|0.9264|0.8122|0.8182|0.8069|0.8327|0.8196|0.93|
|Model 4     |Logistic Regression (TF-IDF)|0.8684|0.802|0.708|0.8842|0.7736|0.8252|0.91|
|Model 5     |KNN Classifier (Cvec)|0.7778|0.6959|0.8571|0.5521|0.8125|0.6575|0.82|
|Model 6     |KNN Classifier (TF-IDF)|0.7117|0.6612|0.71|0.6178|0.7049|0.6584|0.77|
|Model 7     |Random Forest (Cvec)|0.8187|0.7939|0.9351|0.668|0.9202|0.774|0.91|
|Model 8     |Random Forest (TF-IDF)|0.8098|0.8061|0.9697|0.6602|0.9607|0.7826|0.92|
|Model 9     |Support Vector Machine (Cvec)|0.9298|0.7959|0.8225|0.7722|0.8299|0.8|0.9|
|Model 10    |Support Vector Machine (TF-IDF)|0.9652|0.8347|0.8442|0.8263|0.856|0.8409|0.91|

For our current problem statement, where our aim is to achieve correct branding, it is important to high a high accuracy and ROC AUC score. This is because a high accuracy score ensures that most of the predictions (both for Marvel and DCEU) are correct. A high ROC AUC score will also ensure that both distributions are seperated well.  

By looking at the scores above, we can see that Model 1 (Naive Bayes with CountVectorizer) best fits our scoring criteria. Apart from the above, Model 1 also has a good fit to the data. In comparison, almost all the other models have overfitted. 

### Conclusion
To recap, our problem statement was to create a model that could differentiate between the two stated brands (MCU and DCEU). In this project, we scraped data from the following two subreddits: r/marvelstudios and r/DC_cinematic. We then trained a relatively accurate multinomial naive bayes model that can predict the correct MCU or DCEU classification with an accuracy of 88%. 

### Recommendations
Due to the nature of the problem statement, where mistakes could result in expensive lawsuits, it is important to further increase the accuracy and useability of the model. Furthermore, the model is trained using the most recent 1000 posts. As such, the model might not be able to recognize older content that is not currently being talked about in reddit. The following improvements could be considered:

**Increase Accuracy**
1. Try other models (e.g. decision trees, bagging, boosting, other more complex models)
2. Remove more common words to ensure that both classifications have a distinct set of words
3. Clean the data further as currently certain distinct words from one classification is being recognized by the other classification (e.g. the name Waller is recognized as a word associated to Marvel, when it is clearly a distinct character in DECU)

**Increase Useability**
1. Train the model on older data, possibly going as far back to when MCU and DECU originated
2. Train the model from different sources (e.g. facebook, twitter, other forums)
3. Consider using data from Marvel and DC comics to cover heroes that have not been released under MCU and DCEU

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