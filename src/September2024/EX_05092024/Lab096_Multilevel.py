# Multilevel Inheritance

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    pass

son_obj = Son()
son_obj.bhk1()
son_obj.bhk2()

father_obj = Father()
father_obj.bhk1()

gradfather_obj = GrandFather()
gradfather_obj.bhk1()
#gradfather_obj.bhk2()