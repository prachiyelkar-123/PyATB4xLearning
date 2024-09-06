#Hierarchical
class Father:
    def BHK1(self):
        print("1BHK")

class Prachi(Father):
    def BHK2(self):
        print("2BHK")

class Pradnya(Father):
    def BHK3(self):
        print("3BHK")

class Alka(Father):
    def no_house(self):
        print("NO house")

prachi = Prachi()
prachi.BHK1()
prachi.BHK2()

pradnya = Pradnya()
pradnya.BHK1()
pradnya.BHK3()

alka = Alka()
alka.BHK1()
