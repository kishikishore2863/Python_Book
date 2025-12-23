import os
from os.path import exists
import time
import datetime

# --- Directory and file operations ---
path = os.listdir("../")
print("List of directories:", path)

currentDir = os.getcwd()
print("Current directory:", currentDir)

newDir = os.path.join(currentDir, "kis")
if not exists(newDir):
    os.mkdir(newDir)
    print("Directory created:", newDir)
else:
    print("Directory already exists:", newDir)

os.chdir(newDir)
print("Changed directory to:", os.getcwd())

write = os.open("demo.txt", os.O_WRONLY | os.O_CREAT)
os.write(write, b"Hello from Python!\n")
os.close(write)

# --- Path check ---
if exists(newDir):
    print("Path exists: True")
else:
    print("Path exists: False")

# --- Environment variables ---
print("\nAll environment variables:")
for key, value in os.environ.items():
    print(f"{key} = {value}")

# --- 1. Write a Python program to write current time ---
current_time = time.strftime("%H:%M:%S")
print("\nCurrent Time:", current_time)

# --- 2. Write a Python script using time.localtime() ---
local_time = time.localtime()
print("\nLocal Time:", local_time)

# --- 3. Display current year, month (as name), and day number separately ---
now = datetime.datetime.now()
print("\nCurrent Year:", now.year)
print("Current Month (name):", now.strftime("%B"))
print("Current Day:", now.day)

# --- 4. Display various date and time formats ---
print("\nVarious date and time formats:")
print("a. Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("b. Current year:", now.strftime("%Y"))
print("c. Month of the year:", now.strftime("%B"))
print("d. Week of the year:", now.strftime("%U"))
print("e. Weekday of the week:", now.strftime("%A"))
print("f. Day of month:", now.strftime("%d"))
print("g. Day of week:", now.strftime("%w"))


#write a python program to convert a string to datetime
#sample String :jul 1 2014 2:43PM
#expected output: 2014-07-01 14:43:00
#[hint : use determine..strtime( to parse the string ]



