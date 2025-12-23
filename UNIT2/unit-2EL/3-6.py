#A Transport class stores fare_per_km as a class variable.
# Each trip object stores distance and passenger_name.
# A class method updates fare_per_km.
# A static method checks if distance is valid.
# Compute fares before and after the update.



class Transport:
    fare_per_km = 10

    def __init__(self, passenger_name, distance):
        self.passenger_name = passenger_name
        self.distance = distance

    @classmethod
    def update_fare(cls, new_fare):
        cls.fare_per_km = new_fare

    @staticmethod
    def is_valid_distance(d):
        return d > 0

t1 = Transport("Kishore", 12)
t2 = Transport("Amit", 25)
t3 = Transport("Rita", 7)

print(t1.passenger_name, t1.distance, Transport.fare_per_km, t1.distance * Transport.fare_per_km)
print(t2.passenger_name, t2.distance, Transport.fare_per_km, t2.distance * Transport.fare_per_km)
print(t3.passenger_name, t3.distance, Transport.fare_per_km, t3.distance * Transport.fare_per_km)

Transport.update_fare(15)

print(t1.passenger_name, t1.distance, Transport.fare_per_km, t1.distance * Transport.fare_per_km)
print(t2.passenger_name, t2.distance, Transport.fare_per_km, t2.distance * Transport.fare_per_km)
print(t3.passenger_name, t3.distance, Transport.fare_per_km, t3.distance * Transport.fare_per_km)