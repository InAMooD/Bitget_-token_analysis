import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('step_6_output.csv')
data = data.sort_values('Data Points')
timestamp = data['Data Points']
cvd = data['Cumulated Volume Delta (CVD)']
vwap = data['Volume Weighted Average Price (VWAP)']
lowest_cvd_index = cvd.idxmin()
lowest_cvd_value = cvd[lowest_cvd_index]
lowest_vwap_value = vwap[lowest_cvd_index]

plt.figure(figsize=(10, 6))
plt.plot(timestamp, cvd, marker='o', linestyle='--', linewidth=1)
plt.title('CVD by Timestamp')
plt.xlabel('Trade count')
plt.ylabel('Cumulated Volume Delta')
plt.grid(True)

tooltip_text = f'Lowest CVD: {lowest_cvd_value:.5f}\nCorresponding VWAP: {lowest_vwap_value:.8f}'
plt.text(timestamp.min(), cvd.min(), tooltip_text, fontsize=10, verticalalignment='bottom', horizontalalignment='left', bbox=dict(facecolor='white', alpha=0.7))
plt.show()
