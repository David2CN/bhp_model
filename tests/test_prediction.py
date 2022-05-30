import math

import numpy as np

from pressure_model.predict import make_prediction


def test_predictions(sample_input_data):
    # Given
    expected_first_prediction_value = 0
    expected_no_predictions = 743

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64) | isinstance(
        predictions[0], np.float32
    )
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=10)
