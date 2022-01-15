import pandas as pd
#import pickle as pk

# Gives a quick description of the data
def describe_data(data: pd.DataFrame) -> pd.DataFrame:
    df = data.describe()
    return df

# Prints the first few rows from the dataset
def show_data_first_rows(data: pd.DataFrame) -> pd.DataFrame:
    df = data.head()
    return df

# Shows percentage of how many missing values are in each column
def null_values_pourcentage(data: pd.DataFrame) -> pd.DataFrame:
    pourcentage = data.isnull().sum()/ data.shape[0]
    return pourcentage