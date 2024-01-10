import string

def solution(N):
    # if N < 26:
    #     return "Input N should be at least 26 for all letters to be included equally."
    
    # if N > 26 * 2:
    #     return "Input N should not exceed 52 for each letter to occur at most twice."
    
    # num_letters = N // 2
    # letters = string.ascii_lowercase[:num_letters]
    # result = ''.join([letter * 2 for letter in letters])
    letters = string.ascii_lowercase[:N]
    result = ''.join([letters[i % N] for i in range(N)])
    
    return result

print(solution(3))
