# Take input and create a class in python

class person:

    def __init__(self):
        self.name = input("enter name:\n")
        self.age = input("enter age:\n")


    def display_function(self):
       # print(self.name)
       # print(self.age)
        print(f"name is {self.name}",p f"age is {self.age}")


person1 = person()

person1.display_function()
