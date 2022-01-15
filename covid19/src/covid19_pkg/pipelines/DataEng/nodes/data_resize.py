import pandas as pd
import logging

logger = logging.getLogger(__name__)


def limit_data_size(data: pd.DataFrame, limit_size: int) -> pd.DataFrame:

    if limit_size is None:
        logger.warning("Aucune taille limite n'est précisée, toute la donnée va être utilisée.")
        return data

    return data.head(limit_size)
