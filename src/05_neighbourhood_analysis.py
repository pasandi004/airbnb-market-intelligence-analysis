import pandas as pd

listings = pd.read_csv("processed_data/listings_price_cleaned.csv")
listings = listings.dropna(subset=["price"])

neighbourhood_prices = (
    listings.groupby("neighbourhood_cleansed")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("=== TOP 10 MOST EXPENSIVE NEIGHBOURHOODS ===")
print(neighbourhood_prices)