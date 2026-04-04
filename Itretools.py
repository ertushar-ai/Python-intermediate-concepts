# Itertools: Product, Permutation, Combination, Accumulate, Groupby, and Infinite iterators

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
c = [3]
prod = product(a, c, repeat=2)
print(list(prod))

d = [1, 2, 3]
perm = permutations(d)
print(list(perm))
perm = permutations(d, 2)
print(list(perm))


e = [1, 2, 3, 4]
comb = combinations(e, 2)  # here 2 is length, no repetitions
print(list(comb))
comb_wr = combinations_with_replacement(e, 2)  # here 2 is length, with repetitions
print(list(comb_wr))


acc = accumulate(e)
print(e)
print(list(acc))  # sums the elements


def smaller_than_3(x):
    return x < 3


group_obj = groupby(e, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

for i in count(10):  # here 10 is starting value
    print(i)  # print i infinite times and plus +1 every time, infinite loop
    if i == 15:  # stop condition
        break
Count = 0
for i in cycle(d):  # infinitely cycles through the list "d"
    print(i)
    Count += 1
    if Count == 7:  # stop condition
        break

for i in repeat(1, 4):  # infinite loop to print 1, here 4 means the limit
    print(i)