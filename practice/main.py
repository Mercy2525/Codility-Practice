
# msg='welcome to Python 101: Strings'
# #1 Welcome Ring To Tyler

# new=msg[18]+' '+msg[0:7]+''+msg[7:10]+msg[7:9]+msg[12]+msg[2]+msg[1]+msg[25]
# print(new.title())
# print(new[::-1].title())

# print(msg.find('to'))


# friends=['Mary','Abel','John']
# #friends.sort(reverse=True)
# # friends.reverse()
# # friends.pop(1)
# new_fr=friends.copy()

# print(friends)


sentence="Panda has 48 apples and loses 4"
# # sentence=sentence.split()
# numbers=[]

import re
nums=re.findall(r'\d+', sentence)#returns a list, secondvalis a string
all=[int(num) for num in nums]
print(all[0]-all[1])
# for val in sentence:
#     numbers.append(int(val))
# print(numbers)
    
        
# # print(int(sentence[2])+int(sentence[6]))

num="1,2"
#print(type(num))

splitted_num=num.split(',')
print(len(splitted_num))




    
