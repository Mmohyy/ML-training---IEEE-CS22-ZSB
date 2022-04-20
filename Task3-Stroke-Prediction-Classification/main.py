import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('healthcare-dataset-stroke-data.csv');

#drop id
data.drop("id", axis=1, inplace=True)

#fill empty and unknown
temp1 = (data['stroke'] == 1) & (data['smoking_status'] == 'Unknown')
data.loc[temp1, 'smoking_status'] = 'formerly smoked'

temp2 = (data['stroke'] == 0) & (data['smoking_status'] == 'Unknown')
data.loc[temp2, 'smoking_status'] = 'never smoked'

data['bmi'].fillna(data['bmi'].mean(), inplace=True)


#text to numrics
data['gender'].replace('Male', 0, inplace=True)
data['gender'].replace('Female', 1, inplace=True)
data['gender'].replace('Other', 1, inplace=True) 

data['ever_married'].replace('Yes', 1, inplace=True)
data['ever_married'].replace('No', 0, inplace=True)

data['Residence_type'].replace('Urban', 0, inplace=True)
data['Residence_type'].replace('Rural', 1, inplace=True)

data['work_type'].replace('Private', 0, inplace=True)
data['work_type'].replace('Self-employed', 1, inplace=True)
data['work_type'].replace('Govt_job', 2, inplace=True)
data['work_type'].replace('children', 3, inplace=True)
data['work_type'].replace('Never_worked', 4, inplace=True)

data['smoking_status'].replace('formerly smoked', 0, inplace=True)
data['smoking_status'].replace('never smoked', 1, inplace=True)
data['smoking_status'].replace('smokes', 2, inplace=True)


#split
X = data.drop('stroke', axis=1).values
y = data['stroke'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LogisticRegression()
lr.fit(X_train, y_train)
predict = lr.predict(X_test)
print(classification_report(y_test, predict))
