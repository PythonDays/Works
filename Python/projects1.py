# Import the necessary modules
import pandas as pd
import numpy as np

# Read in the data
data = pd.read_csv('data.csv')

# Split the data into features and labels
X = data.drop('label', axis=1)
y = data['label']

# Split the data into train and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train, y_train)
#Make predictions on the test data

predictions = clf.predict(X_test)
#Evaluate the model

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
