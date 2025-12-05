#A Car class stores a warranty_years class variable.
# Each car stores model and mileage.
# A class method updates warranty_years.
# A static method checks if mileage falls within a safe limit.
# Show that all cars reflect the new warranty value.

class Car:
    warranty_years = 3

    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    @classmethod
    def update_warranty(cls, years):
        cls.warranty_years = years

    @staticmethod
    def is_safe_mileage(m):
        return m <= 50000

c1 = Car("Honda", 42000)
c2 = Car("Toyota", 38000)
c3 = Car("Ford", 61000)

Car.update_warranty(5)

print(c1.model, c1.mileage, Car.warranty_years, Car.is_safe_mileage(c1.mileage))
print(c2.model, c2.mileage, Car.warranty_years, Car.is_safe_mileage(c2.mileage))
print(c3.model, c3.mileage, Car.warranty_years, Car.is_safe_mileage(c3.mileage))