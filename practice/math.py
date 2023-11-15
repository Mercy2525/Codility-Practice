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

# def distinct(seq):
#     new_list=[]
    
#     for num in seq:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list

# print(distinct([1, 2, 1, 1, 3, 2]))

list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
            { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
            ] 



def find_senior(lst): 
    age_list=[]
    for dev in lst:
        age_list.append(dev['age'])
        if dev['age']== max(age_list):
            return dev


