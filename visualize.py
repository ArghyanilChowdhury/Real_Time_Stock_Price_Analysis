from hdfs import InsecureClient
import matplotlib.pyplot as plt
import pandas as pd

# Fetch data from HDFS
client = InsecureClient("http://localhost:9870", user="your_username")
with client.read("/stock/output/part-00000") as reader:
    data = reader.read().decode("utf-8")

# Parse into DataFrame
rows = [line.strip().split("\t") for line in data.strip().split("\n")]
df = pd.DataFrame(rows, columns=["Symbol", "Date", "High", "Low", "Close"])
df["Date"] = pd.to_datetime(df["Date"])
df["High"] = df["High"].astype(float)
df["Low"] = df["Low"].astype(float)
df["Close"] = df["Close"].astype(float)

# Plot for each stock
plt.figure(figsize=(12, 8))
symbols = df["Symbol"].unique()

for symbol in symbols:
    symbol_df = df[df["Symbol"] == symbol].sort_values("Date")
    plt.plot(symbol_df["Date"], symbol_df["Close"], label=symbol, linestyle="-", marker="o")

plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.title("Daily Closing Prices for 5 Stocks")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("multi_stock_trends.png")
plt.show()
