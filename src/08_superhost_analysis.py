import pandas as pd

listings = pd.read_csv("processed_data/listings_price_cleaned.csv")

data = listings.dropna(
    subset=[
        "host_is_superhost",
        "price"
    ]
)

result = (
    data.groupby("host_is_superhost")["price"]
    .mean()
)

print("=== AVERAGE PRICE BY SUPERHOST STATUS ===")
print(result)