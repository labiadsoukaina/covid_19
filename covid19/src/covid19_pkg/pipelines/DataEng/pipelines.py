from kedro.pipeline import Pipeline, node

from .nodes.data_preprocess import describe_data
from .nodes.data_preprocess import show_data_first_rows
from .nodes.data_preprocess import null_values_pourcentage

from .nodes.data_cleansing import delete_missingValues
from .nodes.data_cleansing import delete_naValues

from .nodes.data_renameColumn import rename_column

from .nodes.data_resize import limit_data_size

#from .nodes.data_cleansing import US_data
#from .nodes.data_cleansing import US_data
#from .nodes.data_cleansing import US_data
#from .nodes.data_cleansing import US_data
#from .nodes.data_cleansing import US_data
#from .nodes.data_cleansing import US_data

def create_pipeline(**kwargs):
    return Pipeline(
        [
            # data preprocess
            node(
                func=describe_data,
                inputs=["data_input"],
                outputs="data_describe",
                name="describe_data_node",
            ),
            node(
                func=show_data_first_rows,
                inputs=["data_input"],
                outputs="data_first_rows",
                name="data_first_rows_node",
            ),
            node(
                func=null_values_pourcentage,
                inputs=["data_input"],
                outputs="missingValues_pourcentage",
                name="missingValues_pourcentage_node",
            ),
            # data cleansing
            node(
                func=delete_missingValues,
                inputs=["data_input"],
                outputs="missingValues_deleted",
                name="delete_missingValues_node",
            ),
            node(
                func=null_values_pourcentage,
                inputs=["missingValues_deleted"],
                outputs="missingValues_pourcentage_after_deletingMissingVal",
                name="missingValues_pourcentage_after_deletingMissingVal_node",
            ),
            node(
                func=delete_naValues,
                inputs=["missingValues_deleted"],
                outputs="naValues_deleted",
                name="naValues_deleted_node",
            ),
            # data renameColumn
            node(
                func=rename_column,
                inputs=["naValues_deleted"],
                outputs="data_renamed_column",
                name="data_renamed_column_node",
            ),
            # data resize
            node(
                func=limit_data_size,
                inputs=["data_renamed_column", "params:limit_size"],
                outputs="resized_data",
                name="resized_data_node",
            ),
        ]
    )
