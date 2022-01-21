from kedro.pipeline import Pipeline, node

from .nodes.countries_vaccinations_visualisation import country_total_vaccination
#from .nodes.scatterplot_matrix_visualisation import scatterplot_matrix
from .nodes.world_countries_vaccination_visualisation import world_total_vaccination
def create_pipeline(**kwargs):
    return Pipeline(
        [
            # data preprocess
            node(
                func=country_total_vaccination,
                inputs=["US_data"],
                outputs="us_total_vaccination_plot",
                name="us_total_vaccination_node",
            ),
            node(
                func=country_total_vaccination,
                inputs=["Mexico_data"],
                outputs="mexico_total_vaccination_plot",
                name="mexico_total_vaccination_node",
            ),
            node(
                func=country_total_vaccination,
                inputs=["Canada_data"],
                outputs="canada_total_vaccination_plot",
                name="canada_total_vaccination_node",
            ),
            node(
                func=country_total_vaccination,
                inputs=["UK_data"],
                outputs="uk_total_vaccination_plot",
                name="uk_total_vaccination_node",
            ),
            node(
                func=country_total_vaccination,
                inputs=["China_data"],
                outputs="china_total_vaccination_plot",
                name="china_total_vaccination_node",
            ),
            node(
                func=country_total_vaccination,# visualiser le totale de vaccination dans China avec le dataset de base !
                inputs=["China_data_1"],
                outputs="china_total_vaccination_1_plot",
                name="china_total_vaccination_1_node",
            ),
            node(
                func=country_total_vaccination,
                inputs=["India_data"],
                outputs="india_total_vaccination_plot",
                name="india_total_vaccination_node",
            ),
            #node(
            #    func=scatterplot_matrix,
            #    inputs=["missingValues_deleted"],
            #    outputs="scatterplot_matrix_plot",
            #    name="scatterplot_matrix_node",
            #),
            node(
                func=world_total_vaccination,
                inputs=["world_countries_1"],
                outputs="world_total_vaccination_1_plot",
                name="world_total_vaccination_1_node",
            ),
            node(
                func=world_total_vaccination,
                inputs=["world_countries_2"],
                outputs="world_total_vaccination_2_plot",
                name="world_total_vaccination_2_node",
            ),

        ]
    )
