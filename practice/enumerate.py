friends=['Tabby','Tosh','Mercy','Jesse']

for i,friend in enumerate(friends,51): #can include a start value
    print(friend)

# print(list(enumerate(friends)))


# for friend in enumerate(enumerate(friends,51),-100): #can include a start value
#     print(friend)

# for num,letter in enumerate('python',start=5):
#     print(num,letter)

print(range(5))



def nato(word):
    dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    
    letters= [dictionary[letter.upper()] for letter in word]
    return ' '.join(letters)


print(nato('hi'))