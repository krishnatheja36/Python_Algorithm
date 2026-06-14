# Python Cheat Sheet
*Last updated: 2026-05-26  22:40*

---

## Imports

```python
from abc import ABC, abstractmethod
from collections import  defaultdict
from collections import Counter
from collections import Counter, deque
from collections import defaultdict
from collections import defaultdict, deque
from collections import deque
import collections
import heapq
from itertools import combinations
from itertools import combinations, permutations
from itertools import permutations
import math
from p0_linkedlist_helper import *
from pathlib import Path
from q0_helper_tree_dfs_utility import *
from queue import deque
import sys
```

---

## Quick Reference

```python
# -- heapq  (min-heap by default)
import heapq
heapq.heapify(lst)                           # convert list → heap in-place          O(n)
heapq.heappush(heap, val)                    # push val                               O(log n)
heapq.heappop(heap)                          # pop & return smallest                  O(log n)
heapq.nlargest(k, iterable)                  # k largest elements                     O(n log k)
heapq.nsmallest(k, iterable)                 # k smallest elements                    O(n log k)
heap[0]                                      # peek smallest without popping          O(1)
heapq.heappush(heap, -val)                   # max-heap trick: negate values
heapq.heappush(heap, (priority, item))       # heap of tuples — sorts by first element

# -- collections.Counter
from collections import Counter
ctr = Counter("aabbbc")                      # Counter({'b':3,'a':2,'c':1})
ctr['x']                                     # 0  (no KeyError)
ctr.most_common(2)                           # [('b',3), ('a',2)]  top-k
ctr.most_common()[:-k-1:-1]                  # k least common
list(ctr.elements())                         # ['a','a','b','b','b','c']
ctr.total()                                  # sum of all counts
ctr1 + ctr2                                  # merge (keep positives)
ctr1 & ctr2                                  # intersection (min of counts)
ctr1 | ctr2                                  # union (max of counts)

# -- collections.defaultdict
d = defaultdict(int)                         # missing key → 0
d = defaultdict(list)                        # missing key → []
d = defaultdict(set)                         # missing key → set()
d = defaultdict(lambda: -1)                  # missing key → -1

# -- collections.deque
dq = deque([1, 2, 3])
dq.append(4)      / dq.appendleft(0)        # add to right/left        O(1)
dq.pop()          / dq.popleft()            # remove from right/left   O(1)
dq[0]             / dq[-1]                  # peek left / right         O(1)
dq.rotate(k)                                 # rotate right k steps
deque(maxlen=k)                              # fixed-size sliding window

# -- String
s.isalnum() / s.isalpha() / s.isdigit()
s.upper() / s.lower()
s.strip() / s.lstrip() / s.rstrip()
s.split(sep)    /    sep.join(lst)
s.startswith(p) /    s.endswith(p)
s.find(sub)                                  # index or -1
s.replace(old, new)
ord('a')                                     # 97  — char → int
chr(97)                                      # 'a' — int → char
ord(c) - ord('a')                            # 0-25 index for lowercase

# -- List & Sorting
lst.sort()                                   # in-place                 O(n log n)
lst.sort(reverse=True)
lst.sort(key=lambda x: x[1])
sorted(lst)                                  # returns new list
lst[::-1]                                    # reversed copy
lst.append(x)                                # O(1) amortized
lst.pop()    / lst.pop(i)                    # O(1) / O(n)
[0] * n                                      # list of n zeros
[[0]*n for _ in range(m)]                    # 2D grid  (NOT [[0]*n]*m)

# -- bisect  (binary search on sorted list)
import bisect
bisect.bisect_left(lst, x)                   # leftmost index to insert x
bisect.bisect_right(lst, x)                  # rightmost index to insert x
i = bisect.bisect_left(lst, x)
found = i < len(lst) and lst[i] == x

# -- Set
s = set()
s.add(x) / s.discard(x)                     # discard is silent if missing
x in s                                       # O(1) lookup
s1 & s2 / s1 | s2 / s1 - s2 / s1 ^ s2
frozenset(lst)                               # immutable set (hashable, dict key safe)

# -- Dict
d.get(key, default)
d.setdefault(key, default)                   # set if missing, return value
d.items() / d.keys() / d.values()
d.pop(key, default)
{k: v for k, v in d.items() if v > 0}
sorted(d.items(), key=lambda x: x[1])        # sort by value

# -- Built-ins
enumerate(lst)          / enumerate(lst, start=1)
zip(a, b)               / zip(*matrix)       # pair / transpose
min(lst) / max(lst)     / sum(lst)
any(iterable) / all(iterable)
divmod(a, b)                                 # (quotient, remainder)
pow(base, exp, mod)                          # fast modular exponentiation

# -- math
math.inf  /  float('inf')
math.floor(x) / math.ceil(x) / math.sqrt(x)
math.log(x) / math.log(x, base)
math.gcd(a, b) / math.lcm(a, b)
math.comb(n, k)                              # n choose k
math.perm(n, k)

# -- itertools
combinations(lst, r)                         # r-length combos, no repeat
permutations(lst, r)                         # r-length perms, order matters
product(lst, repeat=2)                       # cartesian product
list(accumulate([1,2,3]))                    # [1, 3, 6]  prefix sums
accumulate(lst, max)                         # running max
zip_longest(a, b, fillvalue='-')             # pad shorter iterable

# -- Lambda, map, filter, reduce
square  = lambda x: x ** 2
pairs.sort(key=lambda x: x[1])
people.sort(key=lambda p: (p['age'], p['name']))  # multi-key sort

doubled  = list(map(lambda x: x * 2, numbers))
integers = list(map(int, ['1','2','3']))
evens    = list(filter(lambda x: x % 2 == 0, numbers))
product  = reduce(lambda x, y: x * y, [1,2,3,4,5])   # 120

# -- Comprehensions & Generators
squares  = [x**2 for x in range(10)]
even_sq  = [x**2 for x in range(10) if x % 2 == 0]
flat     = [x for sub in [[1,2],[3,4]] for x in sub]
squared  = {x: x**2 for x in range(5)}
unique   = {len(w) for w in words}
total    = sum(x**2 for x in range(1_000_000))       # generator — no list built
first    = next(x for x in numbers if x % 2 == 0)

def fibonacci():                             # generator function
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# -- Error Handling
try:
    result = a / b
except ZeroDivisionError:
    return None
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    pass                                     # runs only if NO exception
finally:
    pass                                     # ALWAYS runs — cleanup

class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

# -- Dunder Methods
def __repr__(self):  return f"Obj('{self.name}')"    # for devs  (repr)
def __str__(self):   return f"{self.name}"            # for users (print)
def __len__(self):   return len(self.items)
def __contains__(self, item): return item in self.items
def __eq__(self, other):      return self.name == other.name
def __lt__(self, other):      return len(self) < len(other)
def __add__(self, other):     return Obj(self.items + other.items)

# -- Type Hints
from typing import Optional
def process(data: list[int], label: Optional[str] = None) -> dict[str, int]: ...
value: int | str = 0                        # Union (Python 3.10+)

# -- Context Managers
with open('file.txt', 'r') as f:
    data = f.read()

class Timer:
    def __enter__(self):
        import time; self.start = time.time(); return self
    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start:.3f}s")
        return False                         # False = don't suppress exceptions

# -- re (Regular Expressions)
import re
re.search(pattern, string)                  # first match anywhere
re.findall(pattern, string)                 # list of all matches
re.sub(pattern, repl, string)               # replace matches
r'\d+'    # digits    r'\w+'  # word chars    r'\s+' # whitespace
# capture groups
pattern = r'(\d+\.\d+\.\d+\.\d+).*"(\w+) (\S+) HTTP.*" (\d+) (\d+)'
m = re.search(pattern, line)
if m: ip, method, endpoint, status, size = m.groups()

# -- Decorators
@property                                    # method behaves like attribute
@staticmethod                               # utility, no self/cls
@classmethod                                # receives class; factory methods
@dataclass                                  # auto-generates __init__, __repr__, __eq__

class Example:
    name: str
    tags: list = field(default_factory=list)  # mutable default

# -- OOP — Four Pillars (see g0_oops/ for full examples)
self.name   = name                          # public
self._value = value                         # protected (convention)
self.__pin  = 1234                          # private (name mangled → _Class__pin)

class Child(Parent):
    def __init__(self, x, y): super().__init__(x); self.y = y
    def method(self):         super().method()

for obj in [Dog(), Cat()]: obj.speak()      # polymorphism

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass           # subclasses MUST implement

# -- Data Structure Templates
class ListNode:
    def __init__(self, val=0, next=None): self.val = val; self.next = next

def build_list(arr):
    head = curr = ListNode(arr[0])
    for v in arr[1:]: curr.next = ListNode(v); curr = curr.next
    return head

def to_list(head):
    out = []
    while head: out.append(head.val); head = head.next
    return out

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val; self.neighbors = neighbors or []

# -- Histogram (4 lines, know cold)
from collections import Counter
def histogram(data):
    freq = Counter(data)
    for key in sorted(freq.keys()):
        print(f"{key:>4} | {'#' * freq[key]} ({freq[key]})")
```

---

## When to Use What

| Tool              | Use When                                     |
|-------------------|----------------------------------------------|
| `@property`       | Method should behave like attribute          |
| `@staticmethod`   | Utility function, no self/cls needed         |
| `@classmethod`    | Need access to class, factory methods        |
| `@abstractmethod` | Force subclasses to implement (with ABC)     |
| `lambda`          | Simple one-liner, used as argument           |
| `map()`           | Apply function to every element              |
| `filter()`        | Keep elements that pass a test               |
| `reduce()`        | Fold list into single value                  |
| Generator         | Large data, memory efficiency matters        |
| Context manager   | Resource cleanup (files, connections)        |
| `@dataclass`      | Simple data container class                  |
| `ABC`             | Enforce interface contract on subclasses     |

---

## Edge Cases to Always Mention

```python
if not nums: return []            # empty input
if len(nums) == 1: return ...     # single element
# all same elements:  [1,1,1,1]
# already sorted / reverse sorted
# negative numbers:   [-1,-2,0,1]
if nums is None: return None      # None check
```

