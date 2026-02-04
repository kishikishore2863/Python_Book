class Animal:
    def sound(self):
        print("makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog brakes")


d = Dog()
d.sound()
        