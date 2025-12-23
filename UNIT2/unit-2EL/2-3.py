# A temperature class uses a class method to convert Fahrenheit to Celsius.
# You must create an instance through this method and print the converted value.

class Temperature:

    def __init__(self,celsius):
        self.celsius = celsius
    @classmethod
    def from_fahreheits(cls,fahrenheit):
        celsius = (fahrenheit - 32)*5/9
        return celsius


t = Temperature.from_fahreheits(98.6)

print(f"Temperature in Celsius: {t:.2f}c")