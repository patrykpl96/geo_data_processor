from shapely.geometry import Point
import geopandas as gpd


def create_point(location):

    x = float(location["longitude"])
    y = float(location["latitude"])

    punkt = Point(x,y)

    return punkt

def create_geodataframe(locations, crs):

    gdf = gpd.GeoDataFrame(locations, geometry = "geometry", crs = crs)

    return gdf