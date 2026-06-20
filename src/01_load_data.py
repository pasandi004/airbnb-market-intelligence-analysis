import pandas as pd

# Load listings dataset
listings = pd.read_csv("raw_data/listings.csv.gz")

print("=== DATASET SHAPE ===")
print(listings.shape)

print("\n=== DATASET INFO ===")
listings.info()

print("\n=== TOP 20 MISSING VALUES ===")
print(listings.isnull().sum().sort_values(ascending=False).head(20))