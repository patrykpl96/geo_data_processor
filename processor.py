def remove_duplicates(valid_locations):


    seen_coordinates = set()
    unique_locations = []

    for location in valid_locations:
        coordinates = (location["latitude"], location["longitude"])
        if coordinates not in seen_coordinates:
            unique_locations.append(location)
            seen_coordinates.add(coordinates)

    return unique_locations

def get_nearby_locations(gdf, reference_point, max_distance):

    nearby_locations = []
    for index, row in gdf.iterrows():
        distance = round(reference_point.distance(row["geometry"]), 2)
        if distance <= max_distance and distance != 0:
            row["distance"] = distance
            nearby_locations.append(row)

    return nearby_locations

def get_location_point(gdf, location_name):

    location = gdf[gdf["name"].str.lower() == location_name.lower().strip()]
    if location.empty:
        return None

    location_point = location.iloc[0].geometry

    return location_point





