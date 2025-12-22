import pickle


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person(name={self.name},age={self.age})"
person =Person('kishikishore',25)

with open('person.pkl','wb')as file:
    pickle.dump(person,file)
with open('person.pkl','rb') as file:
    loaded_person = pickle.load(file)
print("Loaded Person",loaded_person)
