class Animal:
        def __init__(self):
            self.name = "kishi"

        def __del__(self):
            print("deleted by dunder function")

a = Animal()
print(a)
del a
print(a)