# user define
# 1. The can't return -> non return
# 2. No Return Type and with Argument
# 3. No Return Type and with Default Argument
# 4. Argument + return Type


# 1. The can't return -> non return
def greet_to():
    print("Hello")


result = greet_to()
print(result)


# 2. No Return Type and with Argument

def greet_to_parents(Mother):
    print("hi", Mother)


greet_to_parents("Mother")


# 3. No Return Type and with Default Argument
def Say_hello_to(name="Friend"):
    print("hello", name.upper())


Say_hello_to()
Say_hello_to("Prajakta")


def multi_default_name(name1="prachi", name2="prajakta", name3="alka"):
    print("multi names", name1, name2, name3)


multi_default_name(name1="pradnya", name2="ekanth")
multi_default_name()


# 4. Argument + return Type

def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")

print(result)

def sum_of_the_num(num1, num2, num3):
    return num1 + num2 - num3

result = sum_of_the_num(num1=30, num2=10, num3=10)
print(result)

