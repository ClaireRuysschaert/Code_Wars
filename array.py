def array_diff(a:list, b:list):
    # Compare list 
    # Add only in list c the values that are not equal and return
    c = []
    for element in a:
        if element in b : 
            pass
        else :
            c.append(element)
    return c
