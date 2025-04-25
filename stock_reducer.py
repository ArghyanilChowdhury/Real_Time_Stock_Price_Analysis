import sys

current_key = None
highs = []
lows = []
closes = []

for line in sys.stdin:
    key, values = line.strip().split("\t")
    high, low, close = map(float, values.split("\t"))
    
    if key != current_key:
        if current_key:
            symbol, date = current_key.split(",")
            max_high = max(highs)
            min_low = min(lows)
            avg_close = sum(closes) / len(closes)
            print(f"{symbol}\t{date}\t{max_high}\t{min_low}\t{avg_close:.2f}")
        
        current_key = key
        highs = [high]
        lows = [low]
        closes = [close]
    else:
        highs.append(high)
        lows.append(low)
        closes.append(close)

# Process the last key
if current_key:
    symbol, date = current_key.split(",")
    max_high = max(highs)
    min_low = min(lows)
    avg_close = sum(closes) / len(closes)
    print(f"{symbol}\t{date}\t{max_high}\t{min_low}\t{avg_close:.2f}")
