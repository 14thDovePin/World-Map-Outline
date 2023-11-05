from shapely import Polygon, MultiPolygon

import geopandas as gp
import matplotlib.pyplot as plt


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

    # Pull polygons from Land.
    for polygon in lgs:
        if type(polygon) is Polygon:
            polygons.append(polygon)
        else:
            for i in polygon.geoms:
                polygons.append(i)

    # Pull polygons from Minor Islands.
    if include_minor:
        for polygon in migs:
            if type(polygon) is Polygon:
                polygons.append(polygon)
            else:
                for i in polygon.geoms:
                    polygons.append(i)

    # Convert Polygon coordinates into x and y series.
    final = []
    for polygon in polygons:
        coordinates = polygon.exterior.coords
        x, y = [], []

        for cord in coordinates:
            x.append(cord[0])
            y.append(cord[1])

        poly_cords = (x, y)
        final.append(poly_cords)

    print(f'Total Polygons: {len(polygons)}')
    if not include_minor: print('Excluded Minor Islands')

    print('Plotting Polygons..')
    for i in final:
        plt.fill(
            i[0],
            i[1],
            edgecolor='black',
            linewidth=0.05
            )
    print('Polygons Plotted')
    plt.show()


if __name__ == '__main__':
    main(False)
