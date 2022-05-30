
def test_features(sample_input_data):

    assert sample_input_data["AVG_ANNULUS_PRESS"].iat[0] == 0.0
    assert sample_input_data["AVG_WHT_P"].iat[0] == 0.0
    assert sample_input_data["DP_CHOKE_SIZE"].iat[0] == 0.0
    assert sample_input_data["DAYS_1STPRD"].iat[0] == 0
