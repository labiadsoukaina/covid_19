import pandas as pd
import numpy as np
import seaborn as sns
from kedro.extras.datasets.matplotlib import MatplotlibWriter


def scatterplot_matrix(data: pd.DataFrame) -> MatplotlibWriter:

    data['total_vacc'] = np.log10(data['total_vaccinations'])
    data['people_vacc'] = np.log10(data['people_vaccinated'])
    data['people_fully_vacc'] = np.log10(data['people_fully_vaccinated'])
    data['daily_vacc'] = np.log10(data['daily_vaccinations'])

    #drop the original nontransformed columns
    #data = data.drop(columns = ['total_vaccinations','people_vaccinated','people_fully_vaccinated', 'daily_vaccinations'])


    covid_features = data[['date', 'total_vacc', 'people_vacc' , 'people_fully_vacc' , 'daily_vacc']]
    sns.set_theme(style="ticks")
    sns.pairplot(covid_features)


    return sns

