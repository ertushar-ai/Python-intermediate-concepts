# Collections: Counter, Namedtuple, Defaultdict, Deque

from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(my_counter.most_common(2)[1])
print(my_counter.most_common(2)[1][1])
print(list(my_counter.elements()))


point = namedtuple("Point", "x,y")
pt = point(1, -4)
print(pt)
print(pt.x,pt.y)


d = defaultdict(int) # return the default value {0}
d['a'] = 1
d['b'] = 2
print(d)

deq = deque()
deq.append(1)
deq.append(2)
deq.appendleft(3)
deq.pop()
deq.popleft()
deq.clear()
deq.extend([4,5,6])
deq.extendleft([7,8,9])
deq.rotate(1)