from loader import load_locations

def test_load_locations(tmp_path):

    file_path = tmp_path / "locations.csv"

    file_path.write_text(
        "name,latitude,longitude\n"
        "Warszawa,52.2297,21.0122\n",
        encoding="utf-8" )

    result = load_locations(file_path)

    assert result == [{
    "name": "Warszawa",
    "latitude": "52.2297",
    "longitude": "21.0122"
    }]

def test_load_locations_load_many_rows(tmp_path):

    file_path = tmp_path / "locations.csv"

    file_path.write_text(
        "name,latitude,longitude\n"
        "Warszawa,52.2297,21.0122\n"
        "Kraków,50.0647,19.9450\n"
        "Gdańsk,54.3520,18.6466\n",
        encoding="utf-8"
    )

    result = load_locations(file_path)

    assert len(result) == 3

def test_load_locations_empty_data(tmp_path):

    file_path = tmp_path / "locations.csv"

    file_path.write_text("", encoding="utf-8")

    result = load_locations(file_path)

    assert result == []

