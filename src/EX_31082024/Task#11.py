class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def walk(self):
        print("Slowly")

    def talk(self):
        print("Too Much")

    def __init__(self, name, age, address, phone, eid):
        print("create employee class")
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.eid = eid

E1 = Employee("Prachi", 28, "MH", 845236512, 1546879)
print(E1.name)
print(E1.age)
print(E1.address)
print(E1.phone)
print(E1.eid)
E1.walk()
E1.talk()


E2 = Employee("Pradnya", 25, "GOA", 586545236523, 458236)
print(E2.name, E2.age, E2.address, E2.phone, E2.eid)
E2.walk()
E2.talk()



