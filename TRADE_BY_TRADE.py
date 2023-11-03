import csv
import pandas as pd
from datetime import datetime, timedelta

#df
data = {
    "Data Points": [],
    "Cumulated Volume Delta (CVD)": [],
    "Volume Weighted Average Price (VWAP)": [],
    "Buyback price": [],
    "Bitget Loss in USD": [],
    "Time Elapsed (HH:MM:SS)": []  #calc time
}

#init
cumulated_volume_delta = 0
sum_trade_value = 0
total_quantity = 0
first_timestamp = None  # initialise ts

csv_file = 'TOKENUSDT_SPBL_fills.csv'

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for i, row in enumerate(csv_reader):
        side = row['side']
        price = float(row['fillPrice'])
        quantity = float(row['fillQuantity'])
        trade_value = price * quantity
        timestamp_ms = int(row['fillTime'])  #convert
        timestamp = datetime.utcfromtimestamp(timestamp_ms / 1000)  # CONVER
        if first_timestamp is None:
            first_timestamp = timestamp

        if side == 'Buy':
            cumulated_volume_delta += quantity
        else:
            cumulated_volume_delta -= quantity

        total_quantity += quantity
        sum_trade_value += trade_value

        # here we calculate Cthe data for every datapoint / every trade data points
        if (i + 1) % 1 == 0:
            vwap = sum_trade_value / total_quantity
            bitget_profit = (0.00605001 - vwap) * cumulated_volume_delta
            mkt_val_buyback_time = 671829575 * 0.021635

            # calculate time elapsed since the trade
            time_elapsed = timestamp - first_timestamp
            time_elapsed_str = str(time_elapsed) 

            #build data
            data["Data Points"].append(i + 1)
            data["Cumulated Volume Delta (CVD)"].append(round(cumulated_volume_delta))
            data["Volume Weighted Average Price (VWAP)"].append(round(vwap, 8))
            data["Buyback price"].append(0.00605001)
            data["Bitget Loss in USD"].append(round(bitget_profit))
            data["Time Elapsed (HH:MM:SS)"].append(time_elapsed_str)

table = pd.DataFrame(data)
vwap = sum_trade_value / total_quantity
bitget_profit = (0.00605001 - vwap) * cumulated_volume_delta
mkt_val_buyback_time = 671829575 * 0.021635
print("Final Cumulated Volume Delta (CVD):", round(cumulated_volume_delta))
print("Final Volume Weighted Average Price (VWAP):", round(vwap, 8))
print("Final Buyback price: 0.00605001")
print("Final Bitget Loss in USD:", round(bitget_profit))

print(table)
print(table.head(10))
table.to_csv('step_6_output.csv', index=False)
