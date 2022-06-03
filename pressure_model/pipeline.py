from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from pressure_model.config.core import config
from pressure_model.preprocessing.features import SImputer

pressure_pipe = Pipeline(
    steps=[
        (
            "imputer",
            SImputer(
                variables=config.model_config.features_with_na,
                strategy=config.model_config.num_imputation_strategy,
            ),
        ),
        ("scaler", MinMaxScaler()),

        ("model", SVR(
            C=config.model_config.C,
            kernel=config.model_config.kernel,
            degree=config.model_config.degree,
            epsilon=config.model_config.epsilon
        )),
    ]
)
