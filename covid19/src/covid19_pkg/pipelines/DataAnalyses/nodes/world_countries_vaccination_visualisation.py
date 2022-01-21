import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from kedro.extras.datasets.matplotlib import MatplotlibWriter


def world_total_vaccination(data: pd.DataFrame) -> MatplotlibWriter:

    x = data['date']
    y = data['vaccinationsTotales']
    hue = data['pays']

    # Scatterplot
    plt.figure(figsize = (12,6))
    plt.title("Total de vaccination par pays")
    sns.scatterplot(x , y , hue)
    ax = plt.gca()
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    plt.xticks(np.arange(0, 0, step = 5), rotation = 45)
    plt.xlabel("Date")
    plt.ylabel("Vaccinations totales")
    #plt.legend()

    return plt