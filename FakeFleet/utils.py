import geopandas as gpd

# Load land boundaries from OpenStreetMap (or shapefile)
land = gpd.read_file("land_polygons.geojson")

def is_in_water(lat, lon):
    point = gpd.GeoSeries([gpd.points_from_xy([lon], [lat])])
    return not land.contains(point).any()

print(is_in_water(37.7749, -122.4194))  # San Francisco (should be False)
print(is_in_water(0.0, -30.0))  # Atlantic Ocean (should be True)
