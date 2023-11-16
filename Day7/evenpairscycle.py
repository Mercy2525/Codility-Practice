# EvenPairsOnCycle
# You are given N numbers on a circle, described by an array A. Find the maximum number of neighbouring pairs whose sums are even. One element can belong to only one pair.

# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns the maximum number of neighbouring pairs whose sums are even.

# Examples:
# 1. Given A = [4, 2, 5, 8, 7, 3, 7], the function should return 2. We can create two pairs with even sums: (A[0], A[1]) and (A[4], A[5]). Another way to choose two pairs is: (A[0], A[1]) and (A[5], A[6]).

# Picture illustrates the first example.
# 2. Given A = [14, 21, 16, 35, 22], the function should return 1. There is only one qualifying pair: (A[0], A[4]).

# Picture illustrates the second example.
# 3. Given A = [5, 5, 5, 5, 5, 5], the function should return 3. We can create three pairs: (A[0], A[5]), (A[1], A[2]) and (A[3], A[4]).

# Picture illustrates the third example.
# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000].


# def solution(A):
#     # Split the array into pairs---> One element can only be contained in one pair
#     # Find the sum of each pair, if even, increment the count.
#     # Return the count
#     count = 0
    
    
#     pairs = [A[i:i + 2] for i in range(0, len(A), 2)]
#     print(pairs)
    
#     # else:
#     #     pairs = []

#     for pair in pairs:
#         if sum(pair) % 2 == 0:
#             count += 1
#     return count

# print(solution([5, 6, 5, 6, 4, 9, 7]))
# # arr = [1,2,4,2,8,6]

# first_element = [arr[0]]

# reversed_elements = list(reversed(arr[1:]))
# reversed_circle = first_element + reversed_elements

# print(f"Initial Array: {arr}")
# print(f"First Element: {first_element}")
# print(f"Reversed list: {reversed_elements}")

# print(f"Reversed Circle: {reversed_circle}")


def solution(A):
    n = len(A)
    even_count = 0

    for i in range(n):
        if A[i] % 2 == 0 and A[(i + 1) % n] % 2 == 0:
            even_count += 1

    return even_count

# Examples
print(solution([4, 2, 5, 8, 7, 3, 7]))  # Output: 2
print(solution([14, 21, 16, 35, 22]))    # Output: 1
print(solution([5, 5, 5, 5, 5, 5]))      # Output: 3
