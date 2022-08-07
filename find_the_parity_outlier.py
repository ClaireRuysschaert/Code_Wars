def find_outlier(integers):
    even_list=[]
    odd_list=[]
    for element in integers:
        if (element % 2) ==0:
            even_list.append(element)
        else:
            odd_list.append(element)
    
    # Si la liste paire est plus longue : return impaire et inverse
    if len(even_list) > len(odd_list):
        return odd_list[0]
    else : 
        return even_list[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))