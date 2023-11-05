import geopandas as gp


LAND_DATASET_DIR = ".\\assets\\ne_10m_land.shp"
MINOR_ISLAND_DATASET_DIR = ".\\assets\\ne_10m_minor_islands.shp"

def main():
    # Land Dataset
    lds = gp.read_file(LAND_DATASET_DIR)
    # Minor Islands Dataset
    mids = gp.read_file(MINOR_ISLAND_DATASET_DIR)

    lgs = lds['geometry']  # Land GeoSereies
    migs = mids['geometry']  # Minor Islands GeoSeries
    
    print(lgs)
    print('====')
    print(migs)


if __name__ == '__main__':
    main()
