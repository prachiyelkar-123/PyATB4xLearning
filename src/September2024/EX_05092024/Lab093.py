# Inheritance

class father:

    key = "2BHK"

    def car(self):
        print("father car", "Aulto", self.key)


class son(father):
    pass

son_obj = son()
son_obj.car()