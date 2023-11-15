# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements


def unique_in_order(sequence):
#     split_values=sequence.split()
    
    another_list=[]
    
    for n in sequence:
        if n not in another_list:
            another_list.append(n)
    return another_list


# list1='ABBCcAD'
list1=[1, 2, 2, 3, 3]
list2 = []
for i, n in enumerate(list1):
    if i < len(list1) - 1 and n != list1[i + 1]:
        list2.append(n)

        print(list2)