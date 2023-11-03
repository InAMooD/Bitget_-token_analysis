import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sorted_bitget_candlestick_data.csv')
timestamp = data['Timestamp']
close = data['Close']
timestamp = pd.to_datetime(timestamp, unit='ms')

plt.figure(figsize=(10, 6))
plt.plot(timestamp, close, label='Close Price', color='blue')
plt.title('Close Price Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.savefig('step_2_ohlc_chart.png')
plt.show()
