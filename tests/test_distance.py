from mlproject.distance import haversine

48.865070, 2.380009, 41.40338, 2.17403
def test_haversine():
    assert type(haversine(48.865070, 2.380009, 41.40338, 2.17403)) == float
