from itertools import zip_longest
#No1
iterable1 = [1, 2, 3]
iterable2 = ['a','b']

result = zip_longest(iterable1, iterable2, fillvalue='NA')
print(list(result))

#No2
from itertools import chain

iterable1 = [1, 2, 3]
iterable2 = ['a', 'b', 'c']

result = chain(iterable2, iterable1)
print(list(result))

#No3

