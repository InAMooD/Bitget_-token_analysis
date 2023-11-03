import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('TRADE_BY_TRADE.csv')
data_points = data['Data Points']
vwap = data['Volume Weighted Average Price (VWAP)']
bitget_loss = data['Bitget Loss in USD']
fig, ax1 = plt.subplots()
ax1.plot(data_points, vwap, color='tab:blue', label='VWAP')
ax1.set_xlabel('Trade cnt')
ax1.set_ylabel('VWAP', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax2 = ax1.twinx()
ax2.plot(data_points, bitget_loss, color='tab:red', label='Bitget Loss')
ax2.set_ylabel('Bitget Loss in USD', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
lines = lines_1 + lines_2
labels = labels_1 + labels_2
ax1.legend(lines, labels, loc='upper right')
plt.title("VWAP and Bitget Loss over Data Points")
plt.show()
