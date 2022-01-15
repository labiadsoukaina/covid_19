import pandas as pd

#Drops the missing values in the dataframe
def delete_missingValues(data: pd.DataFrame) -> pd.DataFrame:
    df = data.dropna()
    return df

#This line puts two columns in dataframe and drops rows with NA values.
def delete_naValues(data: pd.DataFrame) -> pd.DataFrame:
    df = data[["country","date","total_vaccinations"]]
    return df


