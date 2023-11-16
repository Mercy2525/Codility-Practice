# CreateLongestSpike
# ```Task description
# We will call a sequence of integers a spike if they first increase (strictly) and then decrease (also strictly, including the last element of the increasing part). For example (4, 5, 7, 6, 3, 2) is a spike, but (1, 1, 5, 4, 3) and (1, 4, 3, 5) are not. Note that the increasing and decreasing parts always intersect, e.g.: for spike (3, 5, 2) sequence (3, 5) is an increasing part and sequence (5, 2) is a decreasing part, and for spike (2) sequence (2) is both an increasing and a decreasing part.

# Your are given an array A of N integers. Your task is to calculate the length of the longest possible spike, which can be created from numbers from array A. Note that you are NOT supposed to find the longest spike as a sub-sequence of A, but rather choose some numbers from A and reorder them to create the longest spike.

# Write a function:

# def solution(A)

# which, given an array A of integers of length N, returns the length of the longest spike which can be created from the numbers from A.

# Examples:

# Given A = [1, 2], your function should return 2, because (1, 2) is already a spike.

# Given A = [2, 5, 3, 2, 4, 1], your function should return 6, because we can create the following spike of length 6: (2, 5, 4, 3, 2, 1).

# Given A = [2, 3, 3, 2, 2, 2, 1], your function should return 4, because we can create the following spike of length 4: (2, 3, 2, 1) and we cannot create any longer spike. Note that increasing and decreasing parts should be strictly increasing/decreasing and they always intersect.
# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000].```

# def solution(A):
#     #first sort in asc order
#     sorted_list=sorted(A)

#     first_element=[sorted_list[0]]
    
#     new_list=sorted(A[1:],reverse=True)
  
#     both=first_element+new_list
   
#     spike=[]
#     prev=None

#     for n in both:
#         if n !=prev:
#             spike.append(n)
#             prev=n
#     return len(spike)

# print(solution([1]))
# print(solution([1, 2]))
# print(solution([2, 5, 3, 2, 4, 1]))
# print(solution([2, 3, 3, 2, 2, 2, 1]))

def solution(A):
    n=len(A)

    if len<=2:
        return n
    
    m_s_l=2

    for i in range(1,n-1):
        pass
    