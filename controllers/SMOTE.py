from dataclasses import dataclass
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from sklearn.utils import resample
from imblearn.over_sampling import KMeansSMOTE
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# ---------------------- preprocesing data ----------------------
data = pd.read_csv('models\\creditcard.csv', sep= ',')
data = data.drop(['Time', 'Amount'], axis=1)
X = data.iloc[:, data.columns != 'Class'].sample(n=100000, random_state=0)
y = data.iloc[:, data.columns == 'Class'].sample(n=100000, random_state=0)

# Getting the amounts grouped by frauds or not
# gb = data.groupby('Class').agg(
#     transactions=('Class', 'count'),
#     total_revenue=('Amount', 'sum'),
# ).round(2)
# print(gb)



#taking just a part of data to developpe
# X = X.to_numpy()
# y = y.to_numpy()
# y = y.flatten()
print("dataset loader")

# NOTE: DataFrames are allowed with sklearn

# ---------------------- random data generation ---------------------- (FOR TESTS ONLY)
# print(y.head)
# print(X.head)
# showing original data
# X, y = make_classification(n_classes=2, class_sep=0.5,
#     weights=[0.05, 0.95], n_informative=2, n_redundant=0, flip_y=0,
#     n_features=2, n_clusters_per_class=1, n_samples=1000, random_state=10)


print("---------------------- Splitting the data ----------------------")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)		#Dividing dataset with test_set <- 0.3*data
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)			# all data features except Class
# X_test = sc.fit_transform(X_test)			# Class feature


# ---------------------- Plotting imbalance ---------------------- Problem with the graph

# Using PCA to have a clear plot 
# pca = PCA(n_components=3)
# pca.fit(X_train)
# data_pca = pca.transform(X_train)
# data_pca = pd.DataFrame(data_pca)
# data_pca['Class'] = y_train

# Xax = data_pca.iloc[:,0]
# Yax = data_pca.iloc[:,1]
# Zax = data_pca.iloc[:,2]

# cdict = {0:'red',1:'green'}
# labl = {0:'Not Fraud',1:'Fraud'}
# marker = {0:'*',1:'o'}
# alpha = {0:.3, 1:.5}


# fig = plt.figure(figsize=(7,5))
# ax = fig.add_subplot(111, projection='3d')
# for key, grp in data_pca.groupby(['Class']):
#     ax.scatter(grp.iloc[:,0], grp.iloc[:,1], grp.iloc[:,2], marker=marker[key], label=labl[key])

# ax.legend()
# plt.savefig('imbalance.png')
# plt.show()

print("---------------------- Balancing Data ----------------------")

over_sample = RandomOverSampler(random_state=0)
X_train, y_train = over_sample.fit_resample(X_train,y_train)

pca = PCA(n_components=3)
pca.fit(X_train)
data_pca = pca.transform(X_train)
data_pca = pd.DataFrame(data_pca)
data_pca['Class'] = y_train

Xax = data_pca.iloc[:,0]
Yax = data_pca.iloc[:,1]
Zax = data_pca.iloc[:,2]

cdict = {0:'red',1:'green'}
labl = {0:'Not Fraud',1:'Fraud'}
marker = {0:'*',1:'o'}
alpha = {0:.3, 1:.5}

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
for key, grp in data_pca.groupby(['Class']):
    ax.scatter(grp.iloc[:,0], grp.iloc[:,1], grp.iloc[:,2], marker=marker[key], label=labl[key])

ax.legend()

plt.savefig('over-sample.png')


# ---------------------- ML models ----------------------
print("training")

# MLPClassifier Application
model = MLPClassifier(hidden_layer_sizes=(200,))
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

print(accuracy_score(y_test, y_predict))
print(classification_report(y_test, y_predict))

# NOTE : SVM -> SVC not efficient in this case
# SVM Application
# model = SVC()
# model.fit(X_train, y_train)
# y_predict = model.predict(X_test)

# print(accuracy_score(y_test, y_predict))
# print(classification_report(y_test, y_predict))

plt.show()