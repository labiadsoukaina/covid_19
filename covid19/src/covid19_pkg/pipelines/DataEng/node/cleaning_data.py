import pandas as pd
import logging

logger = logging.getLogger(__name__)


def df_pipeline_extract(csvfile_name: pd.DataFrame):
    print(csvfile_name.size)
    return csvfile_name

