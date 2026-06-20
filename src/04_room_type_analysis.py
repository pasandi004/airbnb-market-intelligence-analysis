import pandas as pd

# Load dataset
listings = pd.read_csv("processed_data/listings_price_cleaned.csv")

# Remove rows with missing prices
listings = listings.dropna(subset=["price"])

# Average price by room type
room_prices = (
    listings.groupby("room_type")["price"]
    .mean()
    .sort_values(ascending=False)
)

print("=== AVERAGE PRICE BY ROOM TYPE ===")
print(room_prices)