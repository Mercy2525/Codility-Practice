# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements>
# move_zeros([1,0,1,2,0,1,3])# returns[1,1,2,1,3,0,0]


def move_zeros(lst):
    without_zeros=[]
    with_zeros=[]
    for num in lst:
        if num==0:
            with_zeros.append(num)
        else:
            without_zeros.append(num)
    without_zeros.extend(with_zeros)
    return without_zeros


#OR

import itertools
def move_zeros(lst):
    without_zeros=[]
    with_zeros=[]
    for num in lst:
        if num==0:
            with_zeros.append(num)
        else:
            without_zeros.append(num)
    all=list(itertools.chain(without_zeros,with_zeros))
    return all
#print(move_zeros([1,0,1,2,0,1,3]))

