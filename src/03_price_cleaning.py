import pandas as pd

# Load cleaned dataset
listings = pd.read_csv("processed_data/listings_cleaned.csv")

print("=== PRICE COLUMN BEFORE CLEANING ===")
print(listings["price"].head())

# Remove $ and commas
listings["price"] = (
    listings["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert to numeric
listings["price"] = pd.to_numeric(
    listings["price"],
    errors="coerce"
)

print("\n=== PRICE COLUMN AFTER CLEANING ===")
print(listings["price"].head())

print("\n=== PRICE STATISTICS ===")
print(listings["price"].describe())

# Save dataset
listings.to_csv(
    "processed_data/listings_price_cleaned.csv",
    index=False
)

print("\nPrice cleaning completed successfully!")