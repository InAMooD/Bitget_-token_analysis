import csv

# Input and output file names
input_file = '_rawTOKENUSDT_SPBL_fills.csv'
output_file = 'TOKENUSDT_SPBL_fills.csv'

data = []
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

data.sort(key=lambda x: int(x['fillTime']))

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
