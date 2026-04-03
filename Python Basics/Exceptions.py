# Errors and Exceptions

# try:
    # code you want to run
# except:
    # executed if error occurs
# else:
    # executed if no error
# finally:
    # always executed

x = -5
if x < 0:
    raise Exception("x should be positive")

assert x >= 0, "x is not positive"

try:
    a = 5 / 0
# except:
#     print('An error occurred')
# except Exception as e:
#     print(e)
except ZeroDivisionError as e:
    print(e, "You cannot divide by zero!")
else:
    print("Everything works perfectly!")
finally:
    print("I work every time no matter what =)")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def value_test(x):
    if x > 100:
        raise ValueTooHighError("Input value is too high!")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)


try:
    value_test(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e, e.message, e.value)