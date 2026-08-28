

def is_location_valid(location):

    try:
        if not isinstance(location["name"], str):
            return False

        if not location["name"].strip():
            return False

        latitude = float(location["latitude"])
        longitude = float(location["longitude"])

        return -90 <= latitude <=90 and -180 <= longitude <= 180

    except (ValueError,  KeyError):
        return False

def is_distance_valid(distance):

    try:
        if isinstance(distance, bool):
            return False

        distance = float(distance)

        return distance > 0
    except (ValueError, TypeError):
        return False




