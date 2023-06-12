## Project Title:
Topic Modeling of Academic Journals (Model-Based Systems Engineering)

### Problem Description:
Due to the increasing complexity of engineering projects, there is a growing trend to adopt Model-Based Systems Engineering (MBSE) over the traditional Document-Based Systems Engineering (DBSE). However, as Systems Engineering is a large field and there are limited resourses availablity to work ont he adoption of MBSE, our organization needs to prioritize which aspect of MBSE to implement. However, as this is still an emerging field, we are unaware of the best approach to take or what aspects of MBSE are available and applicable for our context. <br>

By applying topic modeling to the abstracts of academic research articles and conference papers on MBSE, our organization can be better equiped to implement MBSE where it is most impactful. <br>

In particular, we will use topic modeling to try to address the following three points:
1. Identification of organizational enterprise goals
2. Where to focus R&D research efforts
3. Identify latest trends in the field

### Dataset:
Our data was collected from the below three sources: <br>
1. [Institute of Electrical & Electronics Engineers (IEEE) - 384 articles](https://ieeexplore.ieee.org/Xplore/home.jsp)
2. [International Council on Systems Engineering (INCOSE) - 257 articles](https://incose.onlinelibrary.wiley.com)
3. [Science Direct - 210 articles](https://www.sciencedirect.com)

### Exploratory Data Analysis (EDA)
After cleaning the data, and removing stop words as well as commons words such as "model", "based", "systems" and "engineering" that appear in every article, we took a look at the unigrams and bigrams to draw some insight. Interesting terms such as "digital twin", "verification & validation" and "product development" were observed. <br>
![](https://github.com/Suniljit/General_Assembly_Projects/blob/main/capstone_project/images/unigrams.png)
![](https://github.com/Suniljit/General_Assembly_Projects/blob/main/capstone_project/images/bigrams.png)

### Topic Modeling
We then proceeded with the unsupervised modeling process by trying out three different models: Latent Dirichlet Allocation (LDA), Hierachical Dirichlet Process (HDP) and BERTopic <br>

Overall, BERTopic performed the best in gaining insights into the topics and themes in the academic articles. By using a process to generalize the topics identified by BERTopic, we were able to identify 8 topics to use. We then used domain knowledge to look through the key words and top few article abstracts to generate a proper topic label for each topic <br>

Below are the top 10 key words for each topic and the assigned labels

|Topic| Top 10 Key Words for Topic| Topic Label Using Domain Knowledge|
|-----|---------------------------|-----------------------------------|
|0| cubesat, vehicle, spacecraft, satelite, requirement, nasa, modeling, submarine, payload, electric vehicle| Application of MBSE in Projects|
|1| sysml, modeling, simulation, modeling language, uml, language sysml, diagram, modeling language sysml, software, specification| Modeling language for MBSE|
|2| ontology, research, reuse, paper, industry, knowledge, semantic, tool, modeling, database| Adoption of MBSE and its Evaluation Metrics|
|3| development, product development, production, process, manufacturing, industrial, iot, product line, toolchain, development process| Product Development Process Using MBSE|
|4| reliability, safety analysis, fmea, fault tree, design safety, safety artifact, medical device, reliability analysis, failure mode, safety critical| Safety Assurance Using MBSE|
|5| mechatronic, inspection, inspection equipment, production scheduling, modeling, constraint, business rule, validation, property verification, mechatronic product| Validation & Verification Using MBSE|
|6| requirement, design, engineer, specification, hcd, wfrequirements, text-based requirement, cm process, property-based requirement, methodology| MBSE for Requirements Specification|
|7| digital twin, cyber, resilience, mbsecps, simplexity test-bed, security threat, vulnerability, twin technology, risk assessment, cpg| MBSE for Digital Twin and Cybersecurity|

We also too a look at the trends of the topics over the last 10 years and identified the following trends:
1. Despite Topic 4 (System Assurance using MBSE) have only 4 months of data in 2023, there has been a lot of interest in the field lately
2. Prior to 2016, Topic 7 (MBSE for Digital Twin and Cybersecurity) had zero articles. In 2016, a lot of interest in the topic was picked up.
![](https://github.com/Suniljit/General_Assembly_Projects/blob/main/capstone_project/images/trends.png)

### Topic Insights
By looking at the keywords and top few article abstracts for each other, we have also summarized each topic with its capabilities as well as identified stakeholder in the organization.

|Topic| Topic Label| Topic Summary| Identified Stakeholder|
|-----|------------|--------------|-----------------------|
|0|Application of MBSE in Projects| Real-life examples of MBSE application <br><br> Aerospace, NASA, Electric Vehicles, Navel| EV-Electric Charging Pte Ltd subsidiary recently set up|
|1|Modeling Language for MBSE| One of three pillars of MBSE <br><br> Systems Modeling Langauge (SysML)| All users, to learn language and modeling best practices|
|2|Adoption of MBSE and Evaluation Metrics| Guide adoption process <br><br> Evaluation metrics for ROI| Core MBSE Team performing R&D to adopt MBSE in the Org|
|3|Product Development Process using MBSE| Product Development <br><br> Manufacturing| Fare Systems Team performing in-house product development|
|4|Safety Assurance using MBSE| Safety Analysis <br><br> Reliability <br><br> Failure Mode| Safety Assurance Team performing and reviewing safety and reliability analysis for new projects|
|5|Validation & Verification using MBSE| V&V of product <br><br> Inspection of equipment| Project Teams in charge of ensuring project delivery|
|6| MBSE for Requirements Specification| Design Requirements Specification <br><br> Change Management| Engineering Teams in charge of specifying requirements for new projects|
|7| MBSE for Digital Twin and Cybersecurity| Digital Twin <br><br> Cyber Resilience <br><br> Vulnerability Assessment <br><br> Security| Cybersecurity & Project Teams delivering critical information infrastructure|

### Classification Modeling
To ensure that the work done here remains relevant moving forward, we also trained a Naive Bayes classification model to label new published articles. <br>

The Naive Bayes model is a probabilistic classifier based on Bayes' theorem. It heavily relies on one simplifying assumption, which is that we assume our features are indepedent from one another. 

By using the Macro Average F1 score of 76% as our evaluation metric, we can conclude that the model performs relatively well, given the small dataset that we have. 


### Recommendations
Based on the insights and trends observed, we would make the following recommendations for the short-term and long-term.

**Short-Term**

As the core MBSE team only has the capacity to engage one stakeholder at a time, we would recommend to engage the Systems Assurance Team based on the following points:
1. Current trends show that Systems Assurance is picking in the MBSE space
2. Our teams share the same Director, which makes it easier to collaborate and overcome inertia to implement new things
3. The nature of systems assurance has significant impact, given the importance of our MRT lines. This makes the ROI even more attractive

**Long-Term**

We have now identified the capabilites of MBSE as well as the relevant stakeholders that could be engaged and could benefit from the implementation of MBSE. We can use this information to engage our management to properly plan at the organizational level for the adoption of MBSE.

### Future Works
We have also identified the following two tasks to perform as part of our future works to improve this project, namely:

1. Breaking Down Topic 0
CUrrently, Topic 0 (Application of MBSE in Projects) is generic for project implementation. We would like to break it down into specific domains such as aerospace, naval, electric vehicles, NASA,etc. This would be beneficial to domain specific stakeholders as they can view articles specific to their field.

2. Creating a Front-End for the Classification Model
We would like to create a front-end implementation of the classification model. This would allow us to quickly pre-process and label newly published without having to open our jupyter notebooks.

### Directory Structure
```
capstone_project  
|__ code  
|   |__ 01_Data_Collection.ipynb     
|   |__ 02_Data_Cleaning_and_Initial_Data_Exploration.ipynb     
|   |__ 03_Preprocessing_and_EDA.ipynb  
|   |__ 04_Modelling_Model_Evaluation_Conclusion.ipynb     
|__ data    
|   |__ dceu_clean.csv  
|   |__ dceu.csv  
|   |__ marvel_clean.csv  
|   |__ marvel.csv  
|   |__ x_test.pkl  
|   |__ x_train.pkl  
|   |__ y_test.pkl    
|   |__ y_train.pkl  
|__ images    
|   |__ frequently_occuring_words_clean.png  
|   |__ frequently_occuring_words_unclean.png  
|   |__ word_length.png 
|__ Digitalizing our Marketing and Branding Infringement Checks.pdf  
|__ README.md  
```