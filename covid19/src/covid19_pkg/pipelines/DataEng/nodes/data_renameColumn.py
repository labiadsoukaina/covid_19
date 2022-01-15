import pandas as pd

def rename_column(data: pd.DataFrame) -> pd.DataFrame:

    data.columns = ['pays', 'date', 'vaccinationsTotales']
    return data