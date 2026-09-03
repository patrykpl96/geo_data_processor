from exporters import export_to_geojson
from shapely.geometry import Point
import geopandas as gpd

def test_export_to_geojson(tmp_path):

    output_path = tmp_path / "result.geojson"

    data = { "name" : ["Warszawa"],
             "geometry" : [Point(21.0122, 52.2297)]
            }

    gdf = gpd.GeoDataFrame(data, geometry="geometry", crs="EPSG:4326")

    gdf_projected = gdf.to_crs("EPSG:2180")

    export_to_geojson(gdf_projected, output_path)

    assert output_path.exists()

    saved_gdf = gpd.read_file(output_path)

    assert len(saved_gdf) == 1
    assert saved_gdf["name"].iloc[0] == "Warszawa"
    assert saved_gdf.crs.to_string() == "EPSG:4326"
