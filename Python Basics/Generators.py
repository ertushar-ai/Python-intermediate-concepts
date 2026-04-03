import sys # nothing to do with generators just for difference
# Basics:
# Generators are very memory efficient, saves a lot if memory while working on large data


def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

value = next(g)  # Print first value of g, runs until 1 and pauses there
print(value)

value = next(g)  # Print next value of g i.e. 2, runs until 2 and pauses there
print(value)

value = next(g)  # Print next value of g i.e. 3, runs until 3 and pauses there
print(value)

for i in g:  # iterates over g
    print(i)


print(sum(g))  # Prints sum of yields
print(sorted(g))  # Prints sorted list of yields


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)  # Counts starting in this as well, so there a three number and one "Staring" so it's 4

value = next(cd)  # prints start, pauses and remembers the current state(Starting)
print(next(cd))  # prints start, pauses and remembers the current state, also update the number (3)
print(next(cd))  # prints start, pauses and remembers the current state, also update the number(2)
print(next(cd))  # prints start, pauses and remembers the current state, also update the number(1)
print(next(cd))  # this will throw an error saying "StopIteration"


# Difference between regular lists and generators

def first_n(n): # Normal function using list to get first n numbers
    nums = []
    num = 0
    while num < n:
        nums.append(n)
        num += 1
    return nums


def first_n_gen(n): # using generator to get first n numbers
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_n(100000))) # here we can see the size is 800984
print(sys.getsizeof(first_n_gen(100000))) # here we can see the size is 200, so generators are very memory efficient

# Example
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# Generator expression example

my_generator = (i for i in range(10) if i % 2 == 0)
for i in my_generator:
    print(i)
    