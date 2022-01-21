import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix,classification_report

def RandomForest_evaluation(model_rf, x_test, y_test):
    ypred_rf=model_rf.predict(x_test)
    sns.heatmap(confusion_matrix(y_test, ypred_rf), annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    return plt

def RandomForest_report(model_rf, x_test, y_test):
    ypred_rf=model_rf.predict(x_test)
    report = classification_report(y_test, ypred_rf)
    return report

def LogisticRegression_evaluation(model_lr, x_test, y_test):
    ypred_lr=model_lr.predict(x_test)
    sns.heatmap(confusion_matrix(y_test, ypred_lr), annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    return plt

def LogisticRegression_report(model_lr, x_test, y_test):
    ypred_lr=model_lr.predict(x_test)
    report = classification_report(y_test, ypred_lr)
    return report

def DecisionTree_evaluation(model_dt, x_test, y_test):
    ypred_dt=model_dt.predict(x_test)
    sns.heatmap(confusion_matrix(y_test, ypred_dt), annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    return plt

def DecisionTree_report(model_dt, x_test, y_test):
    ypred_dt=model_dt.predict(x_test)
    report = classification_report(y_test, ypred_dt)
    return report

