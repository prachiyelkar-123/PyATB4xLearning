
class my_class:

    public_var = "i am public"
    __password = "abc123"
    _private = "pri_var"


object = my_class()

print(object.public_var)
#print(object.__password)
print(object._private)