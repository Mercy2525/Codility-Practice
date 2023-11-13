def passed(lst):
    demerit_points=[number for number in lst if number<=18]

    return 'No pass scores registered.' if len(demerit_points)==0  else round(sum(demerit_points)/len(demerit_points)) 
   
            

print(passed([19,16,8,11,25,10,29,22,23]))
print(passed([10,10,10,18,20,20]))
print(passed([3,22,9,13,20,18,2,14,20,8,23,12,7,21,21,19,20,11,18,7,13,22,11,20,9]))
print(passed([21,22,24]))