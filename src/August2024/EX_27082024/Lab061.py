# ✅ Understanding Decorators in Python
# two parts
# wrapper & call
def my_decorator(func):
    def wrapper():
        print("before function is call")
        print("ready with ingredient")
        func()
        print("After function is call")
        print("serve")

    return wrapper()


@my_decorator
def cooking_food():
    print("cooking")
