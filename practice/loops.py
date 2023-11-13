#While loop

# i=0
# while i<5:
#     i+=1
#     print(f"{i}." + "*"*i )#+ " Loops are awesome" + "*"*i*2)
   
  
# def mainFunction(number):
#     divisors = []
#     for i in range(1, number+1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors
# print(mainFunction(5))

# print(5**2)

# def get_dividers(values, powers):
#     for value,power in zip(values,powers):
#         print(value**power) 

# print(get_dividers([5, 7, 11],[2, 1, 1]))

# import math

# print(math.prod([2, 3, 4]))

# list1 =  [
#   { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
#   { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
#   { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
#   { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
#   ]

# list2 = [
#             { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' }
#             ]
# for mydict in list2:
# #mydict.setdefault('hello','hi')
#     mydict['name']='Joel'
#     print(mydict)

# def all_continents(lst): 
#     all=[]
#     all_continents = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}

#     for x in lst:          
#         all.append(x['continent'])
#     all=set(all)     
            
            
#     return all==all_continents


# def all_continents_present(devs):
#     # List of all continents
#     all_continents = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}
    
#     # Extract unique continents from the list of developers
#     unique_continents = set(dev['continent'] for dev in devs)
    
#     # Check if all continents are present
#     return unique_continents == all_continents

        
# print(all_continents(list1))
# print(all_continents(list2))


# list1 = [
#           { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
#           { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
#           { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
#           { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
#         ]
        
# list2 = [
#           { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
#           { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
#         ]
        

# def count_developers(lst):
#     count=0
#     for developers in lst:            
#         if developers['language'] == 'JavaScript' and developers['continent'] =='Europe':
#             count+=1

#     return count
            
                
# # print(count_developers(list1))   
    
list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
]

def greet_developers(lst): 
    for developer in lst:
        greeting = f"Hi {developer['firstName']}, what do you like most about {developer['language']}?"
        developer['greeting'] = greeting
        
    
    return lst

def greet_developers(lst): 
    for developer in lst:
        greeting =  f"Hi {developer['firstName']}, what do you like the most about {developer['language']}?"
        developer['greeting'] = greeting
        
    return lst
  
  #'greeting': 'Hi Sofia, what do you like most about Java?'
    
    
print(greet_developers(list1))

#Hi < firstName here >, what do you like the most about < language here >?