import csv

buy_cvd = 0
sell_cvd = 0

total_fill_quantity = 0
total_fees_usd = 0

file_name = "TOKENUSDT_SPBL_fills.csv"
fee_percentage = 0.002  

with open(file_name, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        side = row['side']
        fill_quantity = float(row['fillQuantity'])
        fill_price = float(row['fillPrice'])

        fees_usd =( fill_quantity * 0.001 ) * 0.00600501
        total_fees_usd += fees_usd

        if side == 'Buy':
            buy_cvd += fill_quantity
        elif side == 'Sell':
            sell_cvd += fill_quantity

        total_fill_quantity += fill_quantity

with open("table.txt", "w") as output_file:
    print("Cumulative Volume Delta for Buys:", buy_cvd, file=output_file)
    print("Cumulative Volume Delta for Sells:", sell_cvd, file=output_file)
    print("cvd total", buy_cvd - sell_cvd, file=output_file)
    print("Total fillQuantity:", total_fill_quantity, file=output_file)
    print("Total Fees Generated in USD:", total_fees_usd, file=output_file)

print("Output has been saved to 'table.txt'.")
