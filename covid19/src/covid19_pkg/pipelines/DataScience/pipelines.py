from kedro.pipeline import Pipeline, node

from .nodes.data_prep import edit_date_column
from .nodes.data_prep import data_train_test
from .nodes.data_classification import RandomForest
from .nodes.data_classification import LogisticRegressionFunc
from .nodes.data_classification import DecisionTree


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                name = 'df_edit_date_column',
                func = edit_date_column,
                inputs = ['world_countries_ds'],
                outputs = 'world_countries_date_column_edited',
            ),
            node(
                name = 'df_train_test_data',
                func = data_train_test,
                inputs = ['world_countries_date_column_edited'],
                outputs = ['X_train', 'X_test', 'y_train', 'y_test'],
            ),
            node(
                name = 'df_random_forest',
                func = RandomForest,
                inputs = ['X_train', 'y_train'],
                outputs = 'model_rf',
            ),
            node(
                name = 'df_logistic_regression',
                func = LogisticRegressionFunc,
                inputs = ['X_train', 'y_train'],
                outputs = 'model_lr',
            ),
            node(
                name = 'df_decision_tree',
                func = DecisionTree,
                inputs = ['X_train', 'y_train'],
                outputs = 'model_dt',
            ),
        ]
    )
