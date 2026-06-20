import pandas as pd

# Load dataset
listings = pd.read_csv("raw_data/listings.csv.gz")

print("=== BEFORE CLEANING ===")
print("Rows:", len(listings))

# Check duplicate records
duplicates = listings.duplicated().sum()
print("Duplicate Rows:", duplicates)

# Remove duplicates
listings = listings.drop_duplicates()

print("\n=== AFTER DUPLICATE REMOVAL ===")
print("Rows:", len(listings))

# Missing values in important columns
important_columns = [
    "price",
    "room_type",
    "neighbourhood_cleansed",
    "review_scores_rating"
]

print("\n=== Missing Values ===")
print(listings[important_columns].isnull().sum())

# Save cleaned dataset
listings.to_csv(
    "processed_data/listings_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")