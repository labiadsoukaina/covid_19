from kedro.pipeline import Pipeline, node

from .nodes.data_preprocess import describe_data
from .nodes.data_preprocess import show_data_first_rows
from .nodes.data_preprocess import null_values_pourcentage

from .nodes.data_cleansing import delete_missingValues
from .nodes.data_cleansing import delete_naValues

from .nodes.data_renameColumn import rename_column

from .nodes.data_resize import limit_data_size

from .nodes.data_subsets import US_data
from .nodes.data_subsets import Mexico_data
from .nodes.data_subsets import Canada_data
from .nodes.data_subsets import UK_data
from .nodes.data_subsets import China_data
from .nodes.data_subsets import India_data
from .nodes.data_subsets import world_countries
from .nodes.data_subsets import world_countries_for_data_science

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
            # data subsets
            node(
                func=US_data,
                inputs=["resized_data"],
                outputs="US_data",
                name="US_data_node",
            ),
            node(
                func=Mexico_data,
                inputs=["resized_data"],
                outputs="Mexico_data",
                name="Mexico_data_node",
            ),
            node(
                func=Canada_data,
                inputs=["resized_data"],
                outputs="Canada_data",
                name="Canada_data_node",
            ),
            node(
                func=UK_data,
                inputs=["resized_data"],
                outputs="UK_data",
                name="UK_data_node",
            ),
            node(
                func=China_data,
                inputs=["resized_data"],
                outputs="China_data",
                name="China_data_node",
            ),
            node(
                func=India_data,
                inputs=["resized_data"],
                outputs="India_data",
                name="India_data_node",
            ),
            node(
                func=world_countries,
                inputs=["US_data", "Mexico_data", "Canada_data", "UK_data", "China_data", "India_data"],
                outputs="world_countries_1",
                name="world_countries_1_node",
            ),
            # créer China_data à partir du dataSet da base pour avoir toutes les infos
            node(
                func=delete_naValues,
                inputs=["data_input"],
                outputs="data_input_1",
                name="data_input_1_node",
            ),
            node(
                func=rename_column,
                inputs=["data_input_1"],
                outputs="data_input_2",
                name="data_input_2_node",
            ),
            node(
                func=China_data,
                inputs=["data_input_2"],
                outputs="China_data_1",
                name="China_data_1_node",
            ),

            # Créer le world_countries file avec China_data_1
            node(
                func=world_countries,
                inputs=["US_data", "Mexico_data", "Canada_data", "UK_data", "China_data_1", "India_data"],
                outputs="world_countries_2",
                name="world_countries_2_node",
            ),
            node(
                func=world_countries_for_data_science,
                inputs=["world_countries_2"],
                outputs="world_countries_ds",
                name="world_countries_ds_node",
            ),
        ]
    )
