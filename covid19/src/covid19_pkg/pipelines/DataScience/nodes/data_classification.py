from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

def RandomForest(x_train, y_train):
    model_rf = RandomForestClassifier()
    model_rf.fit(x_train, y_train)
    return model_rf
    #ypred_rf = model_rf.predict(x_test)
    #confusion_matrix(y_test, ypred_rf)

def LogisticRegressionFunc(x_train, y_train):
    model_lr = LogisticRegression(solver='liblinear')
    model_lr.fit(x_train, y_train)
    return model_lr
    #ypred_lr = model_lr.predict(x_test)
    #confusion_matrix(y_test, ypred_lr)

def DecisionTree(x_train, y_train):
    model_dt = DecisionTreeClassifier()
    model_dt.fit(x_train, y_train)
    return model_dt
    #ypred_dt = model_dt.predict(x_test)
    #confusion_matrix(y_test, ypred_dt)