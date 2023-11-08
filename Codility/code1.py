# In an even word, each letter occurs an even number of times.

# Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.

# Examples:

# 1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).

# 2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).

# 3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S is made only of lowercase letters (a−z).



def even_word(S):
    char_count=0
    for char in set(S):
        x=S.count(char)
        if x%2 != 0:
            char_count+=1
        else:
            char_count==0
    return char_count

print(even_word('acbcbba'))

