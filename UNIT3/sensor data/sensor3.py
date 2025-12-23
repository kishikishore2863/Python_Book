import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sensor_reading.csv')
df['timestamp'] = pd.to_numeric(df['timestamp'],errors='coerce')
df['timestamp'] = pd.to_datetime(df['timestamp'],unit='s')
plt.figure()
plt.plot(df['timestamp'],df['temp_c'])
plt.xlabel('Time')
plt.ylabel('Temperature(C)')
plt.title('Raw sensor values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()