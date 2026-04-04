import functools


# Basics of Decorators:
# A decorator function takes another function as argument, wraps its behavior inside
# an inner function, and returns the wrapped function.
def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def print_name():  # prints name
    print("Alex")


print_name()

print()  # prints space

# Now wrap the function by passing it as argument to the decorator function
# and assign it to itself -> Our function has extended behavior!
print_name = start_end_decorator(print_name)
print_name()

# OR


def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@start_end_decorator  # Decorator
def print_name():  # prints name
    print("Alex")


print_name()


# Decorators with arguments:


def start_end_decorator(func):
    @functools.wraps(func)  # You need functools imported to use this
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_end_decorator
def add_5(x):
    return x + 5


result = add_5(10)
print(result)


# The final template for own decorators:


# import functools # you have to import 'functools we already did so it's commented out.


def my_decorator(func):
    @functools.wraps(func)  # You need functools imported to use this
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result

    return wrapper


# Decorators with arguments:


def repeat(num_times):
    def decorator_repeat(func):  # Decorator function
        @functools.wraps(func)  # You need functools imported to use this
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet("Alice")