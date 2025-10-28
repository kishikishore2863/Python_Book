#10. Define is_leap(year) that returns True if the year is a leap year. Loop through 2000–2025 and print leap years.
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

for year in range(2000, 2026):
    if is_leap(year):
        print(year)



