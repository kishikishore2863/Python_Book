#A utility class uses a static method to check if a year is a leap year.
# You must run this for five sample years.

class Utility:
    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

years = [1996, 2000, 1900, 2024, 2023]

for y in years:
    print(y, "→", Utility.is_leap(y))