import sys
import json
import os

for line in sys.stdin:
    try:
        # Extract stock symbol from the HDFS file path
        file_path = os.environ["map_input_file"]
        symbol = file_path.split("/")[-2]  # Path is like /stock/input/IBM/stock_IBM_123.json
        
        data = json.loads(line.replace("'", "\""))
        time_series = data["Time Series (5min)"]
        
        for timestamp in time_series:
            date = timestamp.split(" ")[0]
            high = float(time_series[timestamp]["2. high"])
            low = float(time_series[timestamp]["3. low"])
            close = float(time_series[timestamp]["4. close"])
            print(f"{symbol},{date}\t{high}\t{low}\t{close}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
