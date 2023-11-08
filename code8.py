# #Given a number n, return the number of positive odd numbers below n, EASY!

def odd_count(n):
    count=0
    for i in range(n):
        if i%2 !=0:
            count +=1
    return count
print(odd_count(15))