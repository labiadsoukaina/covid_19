from sklearn import preprocessing
from sklearn.model_selection import  train_test_split
import pandas as pd

#edit date column to float values
def edit_date_column(data: pd.DataFrame) -> pd.DataFrame:
    number = preprocessing.LabelEncoder()
    data_date_edited = data.copy()
    data_date_edited['date'] = number.fit_transform(data_date_edited.date)
    return data_date_edited

def data_train_test(data:pd.DataFrame) :
    X_train, X_test, y_train, y_test=train_test_split(data.drop('pays',axis=1),data['pays'],test_size=0.2,stratify=data['pays'])
    return X_train, X_test, y_train, y_test
