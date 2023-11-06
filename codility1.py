# Task
# Create a function that always returns True for every item in a given list. However, if an element is the word 'flick', switch to always returning the opposite boolean value.
# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.
# https://www.codewars.com/kata/64fbfe2618692c2018ebbddb


# def switch_flick(str):
#     result=[]
#     flick=True
#     for i in str:
#         if i=='flick':
#             result.append(not flick)
#         else:
#             result.append(flick)
#     return result

def switch_flick(lst):
    result = []
    flick = True
    for item in lst:
        if item == 'flick':
            flick=not flick
        result.append(flick)
        
    return result

print(switch_flick(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))
print(switch_flick(['flick', 'chocolate', 'adventure', 'sunshine']))
    