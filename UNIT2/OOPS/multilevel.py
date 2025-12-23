class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(self.brand)
        print(self.model)

    def __str__(self):
        return f"{super().__str__()}, Model: {self.model}"

class SportsCar(Car):
    def __init__(self, brand, model, topSpeed):
        super().__init__(brand, model)
        self.topSpeed = topSpeed

    def display_info(self):
        super().display_info()
        print(self.topSpeed)

    def __str__(self):
        return f"{super().__str__()}, Top Speed: {self.topSpeed}"

ferrari = SportsCar("ferrari", "f480", "340km/h")
