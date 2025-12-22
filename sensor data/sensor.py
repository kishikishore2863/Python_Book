import random
import  time

for i in range(10):
    temp_c  =25+random.uniform(-2,2)
    print(f"reading {i+1}:{temp_c:.2f} C")
    time.sleep(1)
    