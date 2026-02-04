class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "no specific sound"

class Bird(Animal):
    legs = 2
    def __init__(self,name,category):
        self.category = category
        super().__init__(name)

    def speak(self):
        return "quck quck"

    @classmethod
    def cm(cls):
        print(cls.legs)

class Cat(Animal):
    legs=4

    def __init__(self,name,colour):
        super().__init__(name)
        self.colour = colour

    def speak(self):
        return "meow"

someAnimal = Animal("Some Animal")
tom = Cat("Tom","Blue")
quacker = Bird("Quacker","Duck")

print(someAnimal.speak())
print(tom.speak())
print(quacker.speak())

Bird.cm()