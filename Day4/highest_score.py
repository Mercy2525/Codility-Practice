# def high(x):
#     splitted_str=x.split(' ')

#     import string
#     letters=string.ascii_lowercase
#     score_list=[]
#     for word in splitted_str:
#         score=0
#         for letter in word:
#             if letter in letters:
#                 score+=letters.index(letter)+1
#         score_list.append(score)

#     highest_score = max(score_list) 

#     highest_scoring_word = ""
#     for word, score in zip(splitted_str, score_list):
#         if score == highest_score:
#             highest_scoring_word = word
#             break

#     return (highest_scoring_word)





# #Demonstrate zip
# names=['Mercy','Mary','Joel','John']
# letters=[1,2]
# for word,letter in zip(names,letters):
#         print(word,letter)
#         # if letter==max(letters):
#         #     print(word)

import string
# alphabet=string.ascii_letters
# print(alphabet.index('a')+1)

def high(x):
    sum_of_letters=[]
    splitted_value=x.split()

    alphabet=string.ascii_lowercase

    for word in splitted_value:
        count=1
        for letter in word:
            if letter in alphabet:
                count+=(alphabet.index(letter))
        sum_of_letters.append(count)
    
    for word,number in zip(splitted_value,sum_of_letters):
        if number==max(sum_of_letters):
            return word
        

print(high('what time are we climbing up the volcano'))



    