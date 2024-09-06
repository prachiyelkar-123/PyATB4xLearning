class father:

    key = "2BHK"

    def car(self):
        print("father car", "Aulto", self.key)


class son(father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def banglow(self):
        print("4BHK")

father_obj = father()

father_obj.car()
#father_obj.home()


son_obj = son()
son_obj.car()
son_obj.home()
son_obj.banglow()
