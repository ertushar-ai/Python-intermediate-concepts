# Tuple: Ordered, Immutable, Allows duplicate elements

my_tuple = ("Max", 28, "Netherlands")
my_tuple2 = ("a", "p", "p", "l", "e")
a = [1, 2, 3, 4, 5, 6, 7, 8]

item = my_tuple[2]

print(my_tuple2.count("p"))
print(my_tuple2.index("p"))

my_list = list(my_tuple2)  # can be done vice-versa

slice = a[1:3]

name, age, country = my_tuple
print(name)
print(age)
print(country)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)