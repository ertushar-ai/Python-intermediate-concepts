# Dictionary: Key-Value pairs, Unordered, Mutable

my_dict = {"name": "Max", "age": 28, "country": "Netherlands"}
my_dict2 = dict(name="Emily", age=27, country="Italy")
my_dict3 = {3: 9, 6: 36, 9: 81}

value = my_dict["name"]
value1 = my_dict3[3]

my_dict["email"] = "max@xyz.com"
my_dict.update(my_dict2)

for key in my_dict:
    print(key)  # OR
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)

del my_dict["name"]
my_dict.pop("age")
my_dict.popitem()

my_dict_cpy = my_dict  # modify anyone of these, the second will be modified by itself
my_dict_cpy2 = my_dict.copy()  # modify anyone of these, the second will not be modified
my_dict_cpy3 = dict(my_dict)  # OR