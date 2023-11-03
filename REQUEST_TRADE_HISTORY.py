import requests
import csv
import os
import time

base_url = "https://api.bitget.com/api/spot/v1/market/fills-history?symbol=TOKENUSDT_SPBL"
csv_file = os.path.join(os.getcwd(), "TOKENUSDT_SPBL_fills.csv") 
def get_most_recent_tradeId(csv_file):
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            last_line = None

            for line in csv_reader:
                last_line = line

            if last_line:
                return int(last_line[1])  #trade id is second column 
    except (FileNotFoundError, ValueError, FileNotFoundError, StopIteration):
        return None

#get the last trade id form the file for later
last_tradeId = get_most_recent_tradeId(csv_file) +1

# store the seen trade id's to not store duplicates because their endpoints are shite
seen_trade_ids = set()

while True:
    # build req
    url = f"{base_url}&tradeId={last_tradeId}&limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # list data
        trade_data = []

        # looping
        for trade in data['data']:
            trade_id = trade['tradeId']
            
            #no write dupliucates
            if trade_id in seen_trade_ids:
                continue

            seen_trade_ids.add(trade_id)

            ticker = trade['symbol']
            side = trade['side']
            fill_price = trade['fillPrice']
            quantity = trade['fillQuantity']
            timestamp_unix = int(trade['fillTime'])

            #build df
            trade_data.append([ticker, trade_id, side, fill_price, quantity, timestamp_unix])

        if trade_data:
            last_tradeId = max(trade_data, key=lambda x: x[1])[1]

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(trade_data)

        print(f"Data has been written to {csv_file}")
        print(f"Updated last_tradeId: {last_tradeId}")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

    time.sleep(60)