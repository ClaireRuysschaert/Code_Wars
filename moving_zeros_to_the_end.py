def move_zeros(lst):
    list_wt_zero = []
    list_zero = []
    for element in lst : 
        if element == 0:
            list_zero.append(element)
        else : 
            list_wt_zero.append(element)
    final_list = list_wt_zero + list_zero
    return final_list

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))