import pandas as pd

listings = pd.read_csv("processed_data/listings_price_cleaned.csv")

result = (
    listings["neighbourhood_cleansed"]
    .value_counts()
    .head(10)
)

print("=== TOP 10 NEIGHBOURHOODS BY NUMBER OF LISTINGS ===")
print(result)