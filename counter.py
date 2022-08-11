from collections import Counter

def valid_parentheses(string):
    #collection.counter 
    #compter parenthèses ouvertes et fermées 
    counter = Counter(string)

    if counter['('] ==0 and counter[')'] ==0:
        return True
    elif counter['('] == counter[')']:
        return True
    else:
        return False