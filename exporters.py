from pathlib import Path

def export_to_geojson(gdf, output_path):

    gdf = gdf.to_crs("EPSG:4326")

    folder = Path(output_path).parent
    folder.mkdir(parents=True, exist_ok=True)

    gdf.to_file(output_path, driver="GeoJSON")



