# Strings : Ordered, Immutable , text representation

my_string = "Hello World"
name = "John"
new_string = "        Hello new"
my_string1 = "Hello,World"
variable = "Tim"

char = my_string[2]
substring = my_string[6:]

concat = my_string[:6] + name

new_string = new_string.strip()

print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title())
print(my_string.startswith("Hello"))
print(my_string.endswith("World"))
print(my_string.find("o"))
print(my_string.count("o"))
print(my_string.replace("World", "Universe"))

my_list = my_string1.split(",")
new_string1 = "".join(my_list)
print(new_string1)

print("The variable is", variable)
my_string2 = (
    "The variable is %s" % variable
)  # %d for integers, %f for floats, %s for stings
print(my_string2)
print("The variable is {}".format(variable))
print(f"The variable is {variable}")