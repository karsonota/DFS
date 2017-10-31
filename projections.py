import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score


# Filename containing data for training/testing.  
fileName = None

# split data into train and test datasets
testAmount = .3
data = pd.read_excel(fileName)
train, test = train_test_split(data, test_size = testAmount) # randomized split of data into test & train

# Actual results from past examples - will need to determine what these are
yTrain = None
yTest = None


#Grid Search to train and validate model
forest = RandomForestRegressor() #Constructor for basic model
parameters = {'n_estimators': [x for x in range(5, 15)], # Hyperparameters to grid search over
              'max_features': ['auto', 'sqrt', 'log2'],
              'njobs': [-1, 1],
              'oob_score': [True, False],
              'bootstrap', [True, False]
              } 
clf = GridSearchCV(forest, parameters) 
clf.fit(train, yTrain) # Perform grid search over hyperparameters using cross validation
forest = RandomForestRegressor(clf.best_params_) # Construct the model with the best hyperparameters
forest.fit(train, yTrain) # Train the Model


# Get important values from the model
features = train.columns
featureImportances = forest.feature_importances_


# Score outcomes for test Data
predictions = forest.predict(test)
score = forest.score(test, yTest) #determine how good the model is


# Predict outcomes for unseen data




    
