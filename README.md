![Test](./images/Aviation-Safety.png)

# Machine Learning in Aviation 

**Authors**: [Robert Reynoso](mailto:robert@birdstop.io)

## Overview

With my background in aeronautics I wanted to apply my new Machine Learning (ML) skills to my passion and industry. Using data provided by the National Transportation Safety Board (NTSB), I wanted to discover if ML can help in increasing safety or provide more insights into the factors that contribute to a safe flight. 

## Business Problem

Using ML specifically supervised learning. 
Can we use classification algorithms to classify past aviation accidents as fatal or non-fatal based on features of that accident?


## Data

* In the industry, data can be obtained and requested through the FAA and NTSB.

* The data set used in this project was provided by the NTSB and pulled from Kaggle.

## Methods

* Data Wrangling & EDA Was conducted using Seaborn, Matplotlib, Pandas, and Numpy.

* Model Construction

Given the business problem, a binary classification was used. Model creation was used using the python Sci-kit learn library.
Using a function to test multiple models. 7 final models were used. KNN, logistic regression, decision tree, random forest, naive bayes, adaboost, and gradient boosting. The best perfoming out of the 7 models was random forest. 

* Preprocessing pipelines

Test-Train-Split was utilized to set aside the test set, with a 20% test size.

GridSearchCV was utilized to perform a 5 fold cross validation over the selected parameters.


* Performance metrics

Accuracy score was utilized for the models.


## Results
* From Analysis 1, the most popular movie genres from 2010 - 2019 have been Drama, Comedy, and Documentary

* From Analysis 2, the most monetarily successful release dates have been December and June.

* From Analysis 3, the top 50 movie studios in the U.S. have been Buena Vista and Universal Studios.  


### Analysis 1
![graph1](./images/analysis_1.png)

![graph1](./images/analysis_2.png)

![graph1](./images/analysis_3.png)

## Conclusions

Given these analysis, 3 recommendations can be made:
1. In order to maximize revenue a studio should consider making movies within in the Drama, Comedy, and Documentary genres.

2. In order to maximize revenue a studio should consider releasing films in either December or June.

3. In order to maximize revenue a new studio should consider doing further research into Buena Vista and Universal Studios. In order to understand why these studios have been more successful than other studios in the U.S.

* The business problem for this project is a report on the movie industry that will allow Microsoft producers to make informed decisions in the creation of their new movie studio. 

* A successful film in the U.S. is one that yields maximum profit.

* Thus using these 3 analysis a producer can begin to make informed decisions into creating a new movie studio. 

## Next Steps

Further analysis could produce more accurate and current insights:

* Merging more data sets could yield more accurate information

* Design a new label for movies with multiple genres. Yielding more data, rather than dropping movies with multiple genres. 

* New investigation into what specifically made the top 50 studios more successful than other studios in the U.S.


## For More Information

Please review our full analysis in [our Jupyter Notebook](./Movie_Analysis.ipynb) or our [presentation](./Movie_Analysis.pdf).

For any additional questions, please contact **Robert Reynoso & robert@birdstop.io**

## Repository Structure



```
├── README.md                           <- The top-level README for reviewers of this project
├── Movie_Analysis.ipynb                <- Narrative documentation of analysis in Jupyter notebook
├── Movie_Analysis.pdf                  <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
