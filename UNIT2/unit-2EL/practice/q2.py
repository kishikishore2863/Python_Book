class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print("car started")

c = Car("bmw")
c.start()
