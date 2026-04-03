# Lists: Ordered, Mutable, Allow duplicate elements

my_list = ["apple", "banana", "coconut", "cherry"]
my_list1 = [5, 2, 9, 44, 5, 26, 7]

my_list.insert(1, "lemon")
my_list.append("peach")
my_list.reverse()
new_list2 = "".join(my_list)

item = my_list.pop(1)
my_list.remove("apple")
my_list.clear()
del my_list1[1]

my_list1.sort()
new_list = sorted(my_list1)

my_list2 = [5] * 5
my_list3 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list1 = my_list2 + my_list3

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[1:4]
c = a[::2]

list_cpy = my_list  # modify anyone of these, the second will be modified by itself
list_cpy2 = (
    my_list.copy
)  # modify anyone of these, the second will be modified by itself
list_cpy3 = list(my_list)  # OR
list_cpy4 = my_list[:]

square = [i * i for i in my_list1]  # list comprehension to take square of numbers