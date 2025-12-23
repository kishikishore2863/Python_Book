class  Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)

    def display(self):
        print("BRAND:", self.brand)
        print("MODEL:",self.model)


myCar = Car("BMW","THE M2")
print(myCar.display())



