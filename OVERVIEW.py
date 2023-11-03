import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Initialize variables
cumulated_volume_delta = 0
sum_trade_value = 0
total_quantity = 0

# Open and read the CSV file
csv_file = 'TOKENUSDT_SPBL_fills.csv'

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        side = row['side']
        price = float(row['fillPrice'])
        quantity = float(row['fillQuantity'])
        trade_value = price * quantity
        if side == 'Buy':
            cumulated_volume_delta += quantity
        else:
            cumulated_volume_delta -= quantity

        total_quantity += quantity
        sum_trade_value += trade_value

vwap = sum_trade_value / total_quantity
bitget_profit = (0.00605001 - vwap) * cumulated_volume_delta
mkt_val_buyback_time = 671829575 * 0.021635

# table
table = PrettyTable()
table.field_names = ["Metric", "Value"]
table.add_row(["Cumulated Volume Delta (CVD)", round(cumulated_volume_delta)])
table.add_row(["Volume Weighted Average Price (VWAP)", round(vwap, 8)])
table.add_row(["Buyback price", 0.00605001])
table.add_row(["Bitget Loss in USD", round(bitget_profit)])
table.add_row(["Market value of missing coins at announcement in USD", round(mkt_val_buyback_time, 2)])
print(table)

#csv
table_file_name = 'output_table.txt'
with open(table_file_name, 'w') as table_file:
    table_file.write(str(table))
with open(table_file_name, 'r') as table_file:
    print("\n" + table_file.read() + "\n")