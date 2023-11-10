# import math

# num=math.trunc(38.89)
# print(num)

# a=32.8493
# b=a*100
# c=math.trunc(b)
# d=c/100
# print(d)

# x=round(32.8493,2)
# print(x)

def distinct(seq):
    new_list=[]
    
    for num in seq:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(distinct([1, 2, 1, 1, 3, 2]))
