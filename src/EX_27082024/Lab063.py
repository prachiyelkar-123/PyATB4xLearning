import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start time")
        func()
        end_time = time.time()
        print("end time")
        print(f"time taken by function {start_time - end_time}")

    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this fucntion")
    time.sleep(2) # wait for 2 seconds


@time_decorator
def test_ui_2():
    print("Add a function, time taken by this fucntion")
    time.sleep(5)