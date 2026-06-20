import pandas as pd

listings = pd.read_csv("processed_data/listings_price_cleaned.csv")

data = listings.dropna(subset=["review_scores_rating", "price"]).copy()

print("=== REVIEW RATING STATISTICS ===")
print(data["review_scores_rating"].describe())

data["rating_group"] = pd.cut(
    data["review_scores_rating"],
    bins=[0, 3, 4, 4.5, 5],
    labels=["0-3", "3-4", "4-4.5", "4.5-5"]
)

result = (
    data.groupby("rating_group", observed=True)["price"]
    .mean()
)

print("\n=== AVERAGE PRICE BY RATING GROUP ===")
print(result)