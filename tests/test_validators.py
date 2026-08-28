from validators import is_location_valid, is_distance_valid

def test_is_location_valid():

    place = {'name': 'point', 'latitude': '-90', 'longitude': '180'}

    assert is_location_valid(place)

def test_is_location_not_valid():

    place = {'name': 'point', 'latitude': '50'}

    assert not is_location_valid(place)

def test_is_location_name_not_valid():

    place = {'name': None, 'latitude': '-87', 'longitude': '110'}

    assert not is_location_valid(place)

def test_is_distance_valid():

    distance = 123

    assert is_distance_valid(distance)

def test_is_distance_not_valid():

    distance = 'avv'

    assert not is_distance_valid(distance)

