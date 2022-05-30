
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBRegressor
from pressure_model.config.core import config
from pressure_model.preprocessing.features import SImputer

pressure_pipe = Pipeline(steps=[
        ("imputer", SImputer(variables=config.model_config.features_with_na,
                             strategy=config.model_config.num_imputation_strategy )),

        ("scaler", MinMaxScaler()),

        ("model", XGBRegressor(random_state=config.model_config.random_state))
])
