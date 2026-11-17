import pandas as pd
import geopandas as gpd

if __name__ == "__main__" : 
    df = pd.DataFrame(
        [
            {
            "ville": "Paris",
            "latitude": 48.85,
            "longitude": 2.35,
            "population": 2_100_000,
        },
        {
            "ville": "Marseille",
            "latitude": 43.30,
            "longitude": 5.37,
            "population": 870_000,
        },
        {
            "ville": "Lyon",
            "latitude": 45.76,
            "longitude": 4.84,
            "population": 520_000,
        },
        {
            "ville": "Lille",
            "latitude": 50.63,
            "longitude": 3.06,
            "population": 235_000,
        },
        {
            "ville": "Brest",
            "latitude": 48.39,
            "longitude": -4.49,
            "population": 140_000,
        },
        {
            "ville": "Strasbourg",
            "latitude": 48.57,
            "longitude": 7.75,
            "population": 290_000,
        },
        {
            "ville": "Nice",
            "latitude": 43.70,
            "longitude": 7.27,
            "population": 345_000,
        },
        {
            "ville": "Perpignan",
            "latitude": 42.70,
            "longitude": 2.90,
            "population": 120_000,
        },
        ]
    )
    print(df)

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
        crs="EPSG:4326"
    )
    df_l93 = gdf.to_crs("EPSG:2154")

    # Extraction des géométries
    paris_4326 = gdf.loc[gdf["ville"] == "Paris", "geometry"].item()
    marseille_4326 = gdf.loc[gdf["ville"] == "Marseille", "geometry"].item()

    paris_l93 = df_l93.loc[df_l93["ville"] == "Paris", "geometry"].item()
    marseille_l93 = df_l93.loc[df_l93["ville"] == "Marseille", "geometry"].item()

    # 1) Calcul dans EPSG:4326 (WGS 84)
    dist_4326 = paris_4326.distance(marseille_4326)

    # 2) Calcul dans EPSG:2154 (Lambert 93)
    dist_l93 = paris_l93.distance(marseille_l93)

    print(f"Distance EPSG:4326 : {dist_4326:.4f} (unités du CRS)")
    print(f"Distance EPSG:2154 : {dist_l93:.2f} m  (~ {dist_l93 / 1000:.2f} km)")
        
