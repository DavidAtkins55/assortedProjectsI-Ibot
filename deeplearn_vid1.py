import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

file_path = '/Users/nathancassells/Documents/Code/python/notes:other/avocado.csv'
#stereamlit does not seem suitable for this application
new = pd.read_csv(file_path)

bins = (0.90, 1.10, 1.30, float('inf'))
g_names = ['cheap', 'average', 'expensive']
new = new.assign(data=pd.cut(new['AveragePrice'], bins=bins, labels=g_names))
label_quality = LabelEncoder()
new['data'] = label_quality.fit_transform(new['data'])
print(new)

print(sns.countplot(new['data']))
X = new('data', axis=1)
y = new['data']
#machine learning part

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

rfc = RandomForestClassifier
rfc.fit(X_train, Y_train)
pred_rfc = rfc.predict(X_test)