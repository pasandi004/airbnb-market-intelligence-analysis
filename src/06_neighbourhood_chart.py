import pandas as pd
import matplotlib.pyplot as plt

listings = pd.read_csv("processed_data/listings_price_cleaned.csv")
listings = listings.dropna(subset=["price"])

top10 = (
    listings.groupby("neighbourhood_cleansed")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top10.plot(kind="bar")

plt.title("Top 10 Most Expensive Neighbourhoods")
plt.ylabel("Average Price ($)")
plt.xlabel("Neighbourhood")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visuals/top10_neighbourhoods.png")
plt.show()