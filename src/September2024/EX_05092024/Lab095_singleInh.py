class mother:
    key = ("1home")

    def home(self):
        print("mother home", self.key)

    def mother_gold(self):
        print("dimond")


class daughter(mother):
    pass


daughter_obj = daughter()
daughter_obj.home()
daughter_obj.mother_gold()