import requests
import time
from hdfs import InsecureClient

# Configuration
API_KEY = "ABCD1234"  # Replace with your key
STOCKS = ["IBM", "AAPL", "GOOGL", "MSFT", "AMZN"]  # 5 stocks
HDFS_BASE_PATH = "/stock/input"
HDFS_CLIENT = InsecureClient("http://localhost:9870", user="your_username")

def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

def save_to_hdfs(symbol, data):
    timestamp = int(time.time())
    hdfs_path = f"{HDFS_BASE_PATH}/{symbol}/stock_{symbol}_{timestamp}.json"
    with HDFS_CLIENT.write(hdfs_path, encoding="utf-8") as writer:
        writer.write(str(data))
    print(f"Saved {symbol} data to HDFS")

if __name__ == "__main__":
    while True:
        for symbol in STOCKS:
            data = fetch_stock_data(symbol)
            save_to_hdfs(symbol, data)
            time.sleep(12)  # 5 stocks * 12s = 60s (stay within API limits)
        time.sleep(300)  # Fetch all 5 stocks every 5 minutes
