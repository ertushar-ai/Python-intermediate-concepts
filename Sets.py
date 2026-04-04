# Sets: Unordered, Mutable, No duplicates

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
a = frozenset({1,2,3,4,5,6}) # Can not be modified
print(a)

print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

setA = setB # modify anyone of these, the second will be modified by itself
setA = setB.copy() # modify anyone of these, the second will not be modified
setA = set(setB) # OR

u = odds.union(evens)  # Return a new set with elements from the set and all others.
i = odds.intersection(primes)  # Return a new set with elements common to the set and all others.
d = setA.difference(setB)  # Return a new set with elements in the set that are not in the others.
sd = setA.symmetric_difference(setB)  # Return a new set with elements in either the set or other but not both.


setA.add(4)
setA.update(setB)
setA.intersection_update(setB)  # Update the set, keeping only elements found in it and all others.
setA.difference_update(setB) # Update the set, removing elements found in others.
setA.symmetric_difference_update(setB) # Update the set, keeping only elements found in either set, but not in both

setA.remove(3)
setA.discard(3)
setA.clear()