from shapely import Polygon, MultiPolygon

import geopandas as gp


LAND_DATASET_DIR = ".\\assets\\ne_10m_land.shp"
MINOR_ISLAND_DATASET_DIR = ".\\assets\\ne_10m_minor_islands.shp"

def main(include_minor=True):
    # Land Dataset
    lds = gp.read_file(LAND_DATASET_DIR)
    # Minor Islands Dataset
    mids = gp.read_file(MINOR_ISLAND_DATASET_DIR)

    lgs = lds['geometry']  # Land GeoSereies
    migs = mids['geometry']  # Minor Islands GeoSeries

    polygons = []

    for polygon in lgs:
        if type(polygon) is Polygon:
            polygons.append(polygon)
        else:
            for i in polygon.geoms:
                polygons.append(i)

    if include_minor:
        for polygon in migs:
            if type(polygon) is Polygon:
                polygons.append(polygon)
            else:
                for i in polygon.geoms:
                    polygons.append(i)

    print(len(polygons))


if __name__ == '__main__':
    main()
