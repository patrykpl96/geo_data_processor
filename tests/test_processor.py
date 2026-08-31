from shapely.geometry import Point
import geopandas as gpd
from processor import get_location_point, get_nearby_locations, remove_duplicates

data = {
    "name": ["Warszawa", "Kraków", "Gdańsk", "PunktA", "Warszawa"],
    "geometry": [
        Point(21.0122, 52.2297),
        Point(19.9450, 50.0647),
        Point(18.6466, 54.3520),
        Point(21.0001, 52.2137),
        Point(21.0122, 52.2297)
    ]
}

gdf = gpd.GeoDataFrame(data, geometry="geometry", crs="EPSG:4326")

gdf_projected = gdf.to_crs("EPSG:2180")

def test_get_location_point_returns_correct_point():

    result = get_location_point(gdf, "Kraków")

    assert result == Point(19.9450, 50.0647)

def test_get_location_point_is_empty():

    result = get_location_point(gdf, "Wrocław")

    assert result is None

def test_get_location_point_lower():

    result = get_location_point(gdf, "gDańSK")

    assert result == Point(18.6466, 54.3520)

def test_get_location_point_strip():

    result = get_location_point(gdf, "  Warszawa  ")

    assert result == Point(21.0122, 52.2297)

def test_get_nearby_location():

    reference_point = get_location_point(gdf_projected, "warszawa")

    points = get_nearby_locations(gdf_projected, reference_point, 5000)

    assert len(points) == 1
    assert points[0]["name"] == "PunktA"

def test_get_nearby_location_distance():

    reference_point = get_location_point(gdf_projected, "warszawa")

    points = get_nearby_locations(gdf_projected, reference_point, 5000)

    assert points[0]["distance"] <= 5000
    assert points[0]["distance"] > 0

def test_remove_duplicates():

    locations = [
        {"name": "Firma A", "latitude": "50", "longitude": "20"},
        {"name": "Firma A", "latitude": "50", "longitude": "20"}
    ]
    result = remove_duplicates(locations)

    assert len(result) == 1

def test_remove_duplicates_different_names_same_coordinates():

    locations = [
        {"name": "Firma A", "latitude": "50", "longitude": "20"},
        {"name": "Firma B", "latitude": "50", "longitude": "20"}
    ]

    result = remove_duplicates(locations)

    assert len(result) == 2

def test_remove_duplicates_same_names_different_coordinates():

    locations = [
        {"name": "Firma A", "latitude": "50", "longitude": "20"},
        {"name": "Firma A", "latitude": "50", "longitude": "21"}
    ]

    result = remove_duplicates(locations)

    assert len(result) == 2

def test_remove_duplicates_empty_list():

    locations = []

    result = remove_duplicates(locations)

    assert result == []




