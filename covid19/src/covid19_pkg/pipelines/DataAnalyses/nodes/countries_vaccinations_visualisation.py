import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from kedro.extras.datasets.matplotlib import MatplotlibWriter


def country_total_vaccination(data: pd.DataFrame) -> MatplotlibWriter:
    x = data["date"]
    y = data["vaccinationsTotales"]

    plt.figure(figsize = (20,6))
    plt.title("Total de vaccinations")
    sns.scatterplot(x,y)
    ax = plt.gca()
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    plt.xticks(np.arange(0, len(x), step = 5), rotation = 45)
    plt.xlabel("Date")
    plt.ylabel("Vaccinations totales")

    return plt

