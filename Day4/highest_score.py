def high(x):
    splitted_str=x.split(' ')

    import string
    letters=string.ascii_lowercase
    score_list=[]
    for word in splitted_str:
        score=0
        for letter in word:
            if letter in letters:
                score+=letters.index(letter)+1
        score_list.append(score)

    highest_score = max(score_list) 

    highest_scoring_word = ""
    for word, score in zip(splitted_str, score_list):
        if score == highest_score:
            highest_scoring_word = word
            break

    return (highest_scoring_word)

#Demonstrate zip
names=['Mercy','Mary']
letters=[1,2,4,5]
for word,letter in zip(names,letters):
        #print(word,letter)
        if letter==1:
            print(word)