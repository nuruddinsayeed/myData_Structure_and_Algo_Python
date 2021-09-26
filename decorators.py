import time
import datetime


def decorator_function(funnc):
    """takes a function and return another function"""

    def wrapper(*args, **kwargs):
        print("Started function 1")
        funnc(*args, **kwargs)
        print("Ended function 1")

    return wrapper


@decorator_function
def hello(message, me):
    print(message, me)


hello("Hello", "world")


def count_time(func):
    """Decorate a function"""

    def wrapper():
        before = time.time()
        func()
        print(f"Time Took For Second function: {time.time() - before}")

    return wrapper


@count_time
def delay():
    time.sleep(2)


delay()


def log(func):
    """Decorate a function and write data to a file"""

    def wrapper(*args, **kwargs):
        with open("decorators_function_log.txt", "a") as file:
            file.write("\nthird function called with attribute " + " ".join([str(arg) for arg in args]) + "at " +
                       str(datetime.datetime.now()))

            val = func(*args, **kwargs)   # it returns the value that provided functions returns
            return val

    return wrapper


@log
def run(a, b, c=4):
    return a+b+c


print(run(1, 5, 3))