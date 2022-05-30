from typing import Dict, List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class SImputer(BaseEstimator, TransformerMixin):
    """A simple imputer for numerical variables."""

    def __init__(self, variables: List[str], strategy: str = "median"):

        self.variables = variables
        self.strategy = strategy
        self.fill_value: Dict[str, str] = {}

    def fit(self, X: pd.DataFrame, y: pd.Series = None):

        for col in self.variables:
            if self.strategy == "median":
                self.fill_value[col] = X[col].median()
            elif self.strategy == "mean":
                self.fill_value[col] = X[col].mean()
        return self

    def transform(self, X: pd.DataFrame):

        df = X.copy()
        for col in self.variables:
            df[col] = df[col].fillna(self.fill_value[col])
        return df
