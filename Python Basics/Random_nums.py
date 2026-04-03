# Random numbers: Random, Secrets, Numpy random

import random  # They are reproducible so they are not recommended to use for security purposes
import secrets  # The only downside is, it take more time for these algorithms, but generates a tru random number
import numpy as np  # Use to produce arrays


# 1.Random(Pseudo random) can be reproduced:


# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1, 10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1, 10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1, 10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

my_list = list("ABCDEFGHI")
# choose a random element from a sequence
a = random.choice(my_list)
print(a)

# choose k unique random elements from a sequence
a = random.sample(my_list, 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(my_list, k=3)
print(a)

# shuffle list in place
random.shuffle(my_list)
print(my_list)

#Seeding with random
#We can use seed to get same numbers again(reseeding)

random.seed(1)  # here 1 is like name or address of the seed
print(random.random())
print(random.randint(1, 10))


#2. Secrets(Generates true random number):


# random integer in range [0, n).
a = secrets.randbelow(10) # Upper bound, here 10 is not included
print(a)

# return an integer with k random bits.
a = secrets.randbits(5) # Here 5 is k random bits, also highest possible value. k defines that it can have five random binary values
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)


# 3. Numpy:


# Generate nd array with random floats, arrays has size (d0,d1,…,dn)
a = np.random.rand(3)
print(a)

# Generate nd array with random integers in range [a,b) with size n
values = np.random.randint(0, 10, (5,3))
print(values)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)

# numpy random numbers uses different number generator than python random module, and also have different seeding function
np.random.seed(1) # Here we gonna use numpy(np) seed function rather than random
a = np.random.rand(3,3)
print(a)
