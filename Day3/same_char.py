# DESCRIPTION:
# Write a function that will check if two given characters are the same case.
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# Examples
# 'a' and 'g' returns 1
# 'A' and 'C' returns 1
# 'b' and 'G' returns 0
# 'B' and 'g' returns 0
# '0' and '?' returns -1
# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b

import string

def check(y,z):
    if y in string.ascii_letters and z in string.ascii_letters:
        if (y in string.ascii_lowercase and z in string.ascii_lowercase) or (y in string.ascii_uppercase and z in string.ascii_uppercase):
            return 1
        else:
            return 0
    else:
        return -1
    

# a.isalpha,a.islower,a.isupper

#OR

def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        return 0
    return -1