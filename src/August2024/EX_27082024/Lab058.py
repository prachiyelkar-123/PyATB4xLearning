#Function Scope
marks= 10 # almost work like a global varibale
def myfunction():

    print(marks)

myfunction()

def total():
    a=45  # local variable, within the function
    print(a)

total()