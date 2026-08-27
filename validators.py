

def is_location_valid(location):


    try:
        latitude = float(location["latitude"])
        longitude = float(location["longitude"])

        return -90 <= latitude <=90 and -180 <= longitude <= 180

    except ValueError:
        return False

def is_distance_valid(distance):

    try:
        distance = float(distance)

        return distance > 0
    except ValueError:
        return False




