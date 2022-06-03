import typing as t

import numpy as np
import pandas as pd

from pressure_model import __version__ as _version
from pressure_model.config.core import config
from pressure_model.preprocessing.data_manager import load_pipeline
from pressure_model.preprocessing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_pressure_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _pressure_pipe.predict(
            X=validated_data[config.model_config.features]
        )

        results = {
            "predictions": [pred for pred in predictions],  # type: ignore
            "version": _version,
            "errors": errors,
        }

    return results

