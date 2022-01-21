from kedro.pipeline import Pipeline, node

from .nodes.data_prep import edit_date_column
from .nodes.data_prep import data_train_test
from .nodes.data_classification import RandomForest
from .nodes.data_classification import LogisticRegressionFunc
from .nodes.data_classification import DecisionTree
from .nodes.models_evaluation import RandomForest_evaluation, RandomForest_report
from .nodes.models_evaluation import LogisticRegression_evaluation, LogisticRegression_report
from .nodes.models_evaluation import DecisionTree_evaluation, DecisionTree_report


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
            node(
                name = 'df_random_forest_evaluation',
                func = RandomForest_evaluation,
                inputs = ['model_rf', 'X_test', 'y_test'],
                outputs = 'random_forest_evaluation_plot',
            ),
            node(
                name = 'df_random_forest_report',
                func = RandomForest_report,
                inputs = ['model_rf', 'X_test', 'y_test'],
                outputs = 'random_forest_report_plot',
            ),
            node(
                name = 'df_logistic_regression_evaluation',
                func = LogisticRegression_evaluation,
                inputs = ['model_lr', 'X_test', 'y_test'],
                outputs = 'logistic_regression_evaluation_plot',
            ),
            node(
                name = 'df_logistic_regression_report',
                func = LogisticRegression_report,
                inputs = ['model_lr', 'X_test', 'y_test'],
                outputs = 'logistic_regression_report_plot',
            ),
            node(
                name = 'df_decision_tree_evaluation',
                func = DecisionTree_evaluation,
                inputs = ['model_dt', 'X_test', 'y_test'],
                outputs = 'decision_tree_evaluation_plot',
            ),
            node(
                name = 'df_decision_tree_report',
                func = DecisionTree_report,
                inputs = ['model_dt', 'X_test', 'y_test'],
                outputs = 'decision_tree_report_plot',
            ),
        ]
    )
