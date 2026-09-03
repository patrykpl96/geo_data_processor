from loader import load_locations
from validators import is_location_valid, is_distance_valid
from processor import remove_duplicates, get_nearby_locations, get_location_point
from geometry import create_point, create_geodataframe
from exporters import export_to_geojson

def main():

    locations = load_locations("data/locations.csv")

    valid_locations = [location for location in locations if is_location_valid(location)]

    unique_locations = remove_duplicates(valid_locations)

    for location in unique_locations:
        location["geometry"] = create_point(location)

    gdf = create_geodataframe(unique_locations, "EPSG:4326")


    gdf_projected = gdf.to_crs("EPSG:2180")

    name = input("Podaj nazwę lokalizacji: ")

    point = get_location_point(gdf_projected, name)

    if point is None:
        print("Nie znaleziono lokalizacji")
    else:
        distance = input("Podaj maksymalną odległość w metrach ")
        if is_distance_valid(distance):
            distance = float(distance)
            points = get_nearby_locations(gdf_projected, point, distance)
            if not points:
                print("Brak wyników")
            else:
                for row in points:
                    print(f'{row["name"]}-  {row["distance"]} m ')

                result_gdf = create_geodataframe(points, "EPSG:2180")
                export_to_geojson(result_gdf, "data/processed/search_results.geojson")

        else:
            print("Niepoprawne dane")


if __name__ == "__main__":
    main()






















