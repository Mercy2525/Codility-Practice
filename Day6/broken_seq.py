def find_missing_number(sequence):
    num_list=sequence.split()
    if not num_list:
        return 0
    
    digit_list=[]
 
    for num in num_list:
        if not num.isnumeric():
            return 1
        else:
            digit_list.append(int(num))
            
    sequence1=set(digit_list)
    expected_sequence=set(range(1,max(digit_list)+1))
    missing_values=list(expected_sequence-sequence1)
    
    if not missing_values:
        return 0
    return min(missing_values)

print(find_missing_number("" ))