import random
import time
import csv
with open('sensor_reading.csv', 'w', newline='')as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','temp_c'])
    for i in range(50):
        ts = time.time()
        temp_c = 25+random.uniform(-2,2)
        writer.writerow([ts,f"{temp_c:.2f}"])
        print(ts,temp_c)
        time.sleep(0.5)
