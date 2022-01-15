import pandas as pd

#Subsets United States data from the original data set.
#changes the total_vaccinations column from string elements to integer elements.

def US_data(data: pd.DataFrame) -> pd.DataFrame:
    us_df = data.loc[data["pays"] == "United States"]
    pd.to_numeric(us_df["vaccinationsTotales"])
    return us_df

def Mexico_data(data: pd.DataFrame) -> pd.DataFrame:
    mexico_df = data.loc[data["pays"] == "Mexico"]
    pd.to_numeric(mexico_df["vaccinationsTotales"])
    return mexico_df

def Canada_data(data: pd.DataFrame) -> pd.DataFrame:
    canada_df = data.loc[data["pays"] == "Canada"]
    pd.to_numeric(canada_df["vaccinationsTotales"])
    return canada_df

def UK_data(data: pd.DataFrame) -> pd.DataFrame:
    uk_df = data.loc[data["pays"] == "United Kingdom"]
    pd.to_numeric(uk_df["vaccinationsTotales"])
    return uk_df

def India_data(data: pd.DataFrame) -> pd.DataFrame:
    india_data = data.loc[data["pays"] == "India"]
    pd.to_numeric(india_data["vaccinationsTotales"])
    return india_data

def China_data(data: pd.DataFrame) -> pd.DataFrame:
    china_df = data.loc[data["pays"] == "China"]
    pd.to_numeric(china_df["vaccinationsTotales"])
    return china_df

def world_countries(us_data: pd.DataFrame, mexico_data: pd.DataFrame, canada_data: pd.DataFrame, uk_data: pd.DataFrame, china_data: pd.DataFrame, india_data: pd.DataFrame) -> pd.DataFrame:
    world_countries = pd.concat([us_data, mexico_data, canada_data, uk_data, china_data, india_data], axis = 0)
    return world_countries
