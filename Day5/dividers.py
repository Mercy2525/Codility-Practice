# Find all the dividers!
# You are given a list of prime numbers (e.g. [5, 7, 11]) and a list of their associated powers (e.g. [2, 1, 1]). The product of those primes at their specified power forms a number x (in our case x = 5^2 * 7^1 * 11^1 = 1925).

# Your goal is to find all of the dividers for this number!
# To do so, you have to multiply each prime number, from its power 0 to its power p in the power list, to every other prime, from their power 0 to their associated power p.

# Each result of those products is a divider of x!

# In our example: [1, 5, 7, 11, 25, 35, 55, 77, 175, 275, 385, 1925]

# Once you find those dividers, sort them in ascending order, and VOILA!

# import math

# def get_dividers(values, powers):
#     prod_powers=[]
#     for val,pow in zip(values,powers):
#         prod_powers.append(val**pow)
#     product=math.prod(prod_powers)


#     dividers=[]
#     for i in range(1,product+1):
#         if product%i==0:
#             dividers.append(i)
#     return dividers
            

# print(get_dividers([5, 7, 11],[2, 1, 1]))




# Don't forget to sort your result list!
import math
def get_dividers(values, powers):
    product=math.prod([value**power for value,power in zip(values,powers)])
    return [i for i in range(1,product+1) if product%i==0]

  


print(get_dividers([5, 7, 11],[2, 1, 1]))










# garden=['Tractor','Cows','Maize']
# levels=[1,2,4,]

# for gar,lev in zip(garden,levels):
#     if lev==1:
#         print(gar)