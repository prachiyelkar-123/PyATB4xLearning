# Multiple Inheritance

class Father:
    def father_money(self):
        print(5)

    def home(self):
        print("1bhk")

class Mother:
    def mother_money(self):
        print(6)

    def home(self):
        print("2bhk")

class Son(Mother, Father):
    pass


s = Son()
s.mother_money()
s.father_money()
s.home()