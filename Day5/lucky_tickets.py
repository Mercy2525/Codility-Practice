# In one city, bus tickets use numbers from 100000 to 999999. Your task is to find the number of lucky tickets between two input tickets' values.
# The ticket is considered to be lucky if the sum of first 3 digits equals to the sum of last 3 digits:
# 123321 is lucky, i.e. 1+2+3 equals to 3+2+1
# 123444 is not lucky, i.e. 1+2+3 doesn't equal to 4+4+4


def lucky_number(alist):
    if sum(alist[:3])==sum(alist[3:]):
        pass
    pass

numb=[1,2,3,3,2,1]
print(sum(numb[:3]))
print(numb[3:])