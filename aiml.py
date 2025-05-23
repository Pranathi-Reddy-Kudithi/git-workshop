import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import seaborn as sns
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,AdaBoostClassifier,StackingClassifier
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,ConfusionMatrixDisplay,classification_report

df=pd.read_csv(r"C:\Users\chinm\aiml\Titanic-Dataset.csv")

X=df.drop(columns=['Survived'])

Y=df[['Survived']]

le=LabelEncoder()
for column in X.columns:
    if X[column].dtype=='object':
        X[column]=le.fit_transform(X[column].astype(str))
imputer=SimpleImputer(strategy='mean')
X=imputer.fit_transform(X)
X=pd.DataFrame(X)
Y=pd.DataFrame(Y)
scaler=StandardScaler()
X=scaler.fit_transform(X)
#split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#Logistic Regression
'''lr=LogisticRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
print(f"Accuracy:{accuracy},Precision:{precision},Recall:{recall}")

cm=confusion_matrix(y_test,y_pred)

disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("logistic regression")
plt.show()'''

#Naive Bayes
'''model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
print(f"Accuracy:{accuracy},Precision:{precision},Recall:{recall}")

cm=confusion_matrix(y_test,y_pred)
disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("Naive Bayes")
plt.show()'''

#DecisionTreeClassifier
'''dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)
y_pred=dt.predict(X_test)

accuracy_dt=accuracy_score(y_test,y_pred)
precision_dt=precision_score(y_test,y_pred)
recall_dt=recall_score(y_test,y_pred)
classification_dt=classification_report(y_test,y_pred)
print(f"Decision Tree Classifier:\nAccuracy:{accuracy_dt},Precision:{precision_dt},Recall:{recall_dt}")


cm=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(10,15))
plot_tree(dt,max_depth=4)
plt.show()

rt=RandomForestClassifier(n_estimators=100,random_state=42)
rt.fit(X_train,y_train)
y_rt_pred=rt.predict(X_test)
accuracy_rt=accuracy_score(y_test,y_rt_pred)
precision_rt=precision_score(y_test,y_rt_pred)
recall_rt=recall_score(y_test,y_rt_pred)
print(f"Random Forest Classifier:\nAccuracy:{accuracy_rt},Precision:{precision_rt},Recall:{recall_rt}")

bg=BaggingClassifier(estimator=LogisticRegression(),n_estimators=50,random_state=42)
bg.fit(X_train,y_train)
y_bg_pred=bg.predict(X_test)
accuracy_bg=accuracy_score(y_test,y_bg_pred)
precision_bg=precision_score(y_test,y_bg_pred)
recall_bg=recall_score(y_test,y_bg_pred)
print(f"Bagging Classifier:\nAccuracy:{accuracy_bg},Precision:{precision_bg},Recall:{recall_bg}")

boost=AdaBoostClassifier(n_estimators=50,random_state=42)
boost.fit(X_train,y_train)
y_boost_pred=boost.predict(X_test)
accuracy_boost=accuracy_score(y_test,y_boost_pred)
precision_boost=precision_score(y_test,y_boost_pred)
recall_boost=recall_score(y_test,y_boost_pred)
print(f"Boosting Classifier:\nAccuracy:{accuracy_bg},Precision:{precision_bg},Recall:{recall_bg}")

stack=StackingClassifier(estimators=[
    ('dt',DecisionTreeClassifier()),
    ('svm',SVC(probability=True)),
    ('rt',RandomForestClassifier())
],final_estimator=LogisticRegression(),cv=5)
stack.fit(X_train,y_train)
y_stack_pred=stack.predict(X_test)
accuracy_stack=accuracy_score(y_test,y_stack_pred)
precision_stack=precision_score(y_test,y_stack_pred)
recall_stack=recall_score(y_test,y_stack_pred)
print(f"Stacking Classifier:\nAccuracy:{accuracy_stack},Precision:{precision_stack},Recall:{recall_stack}")

data_df={
    "Model":["Decision Tree","Random Forest","Bagging","Boosting","Stacking"],
    "Accuracy":[accuracy_dt,accuracy_rt,accuracy_bg,accuracy_boost,accuracy_stack]
}
plt.figure(figsize=(15,16))
sns.barplot(x="Model",y="Accuracy",data=data_df,palette='viridis')
plt.title("Decision vs Ensemble")
plt.show()'''

#SVM
'''digits=datasets.load_digits()
X_digit=digits.images.reshape((len(digits.images),-1))
Y_digit=digits.target
X_train_y,X_test_y,y_train_y,y_test_y=train_test_split(X_digit,Y_digit,test_size=0.2,random_state=42)
model=SVC(kernel='rbf',gamma=0.001,C=100.0)
model.fit(X_train_y,y_train_y)
y_pred=model.predict(X_test_y)
print(f"Accuracy:{accuracy_score(y_test_y,y_pred)}")
print("Classification Matrix/n",classification_report(y_test_y,y_pred))

plt.figure(figsize=(15,16))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(X_test_y[i].reshape(8,8),cmap='grey')
    plt.title(f'pred:{y_pred[i]}')
    plt.axis('off')
plt.show()'''

iris=datasets.load_iris()
X_iris=iris.data
Y_iris=iris.target
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(X_iris)
labels=kmeans.labels_
print("confusion matrix (clusters vs labels)",confusion_matrix(Y_iris,labels))
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_iris)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.scatter(X_pca[:,0],X_pca[:,1],c=labels,cmap='viridis',s=50)
plt.title("K means clustering (predicted vs actual)")
plt.xlabel("pc 1")
plt.ylabel("pc 2")

plt.subplot(1,2,2)
plt.scatter(X_pca[:,0],X_pca[:,1],c=Y_iris,cmap='viridis',s=50)
plt.title("Actual labels")
plt.xlabel('pca 1')
plt.ylabel('pca 2')

plt.show()





