# DESCRIPTION:
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!
# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"

# https://www.codewars.com/kata/6512b3775bf8500baea77663

import string

def gimme_the_letters(sp):
    letters=(string.ascii_letters)
    variable=sp.split('-')
    start_letter,end_letter=variable[0],variable[1]
    start_index,end_index=letters.index(start_letter),letters.index(end_letter)

    return letters[start_index:end_index+1]

print(gimme_the_letters('a-z'))


# a='a-b'
# print(a.split('-'))
# letters=(string.ascii_lowercase)
# index=(letters.index('z'))
# print(letters[index])

# phone=[1,2,4,6,7]
# print(phone[1:5])



