import pandas as pd


#Subsets United States data from the original data set.
#changes the total_vaccinations column from string elements to integer elements.
def US_data(data: pd.DataFrame) -> pd.DataFrame:
    us_df = data.loc[data["pays"] == "United States"]
    pd.to_numeric(us_df["vaccinationsTotales"])
    return us_df