class Person:
    # Class Variables
    # Instance variables
    # name = "Amit" # hardcoded value
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


amit = Person("amit")
Prachi = Person("Prachi")
print(amit.name)
print(Prachi.name)
print("Who is walking with the object pramod -> ", Prachi.walk())