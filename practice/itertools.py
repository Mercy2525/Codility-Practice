# from itertools import zip_longest
# #No1
# iterable1 = [1, 2, 3]
# iterable2 = ['a','b']

# result = zip_longest(iterable1, iterable2, fillvalue='NA')
# print(list(result))

# #No2
# from itertools import chain

# iterable1 = [1, 2, 3]
# iterable2 = ['a', 'b', 'c']

# result = chain(iterable2, iterable1)
# print(list(result))

#No3
#from itertools import combinations
# import string

# letters=string.ascii_lowercase

# twos=list(combinations(letters,26))

# for n in twos:
#     values=''.join(list(n))
#     print(values)

import string

def solution(N):
    if N % 2 != 0:
        # If N is odd, reduce it by 1 to make it even
        N -= 1
    
    # Generate the alphabet
    alphabet = string.ascii_lowercase
    
    # Calculate the number of letters needed for each letter to occur N/2 times
    letters_needed = N // 2
    
    # Repeat each letter the required number of times
    result = (alphabet[:letters_needed] * 2)
    
    return result
print(solution(7))
