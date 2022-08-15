# fonction which increments a string, to create a new string

import re

def str_incrementer(txt):
    matching_digits = re.findall('\d+$', txt)
    
    if matching_digits:
        new_string = txt[0:-len(matching_digits[0])]
        str_matching_digits = ''.join(matching_digits)
        addition = int(str_matching_digits) + 1 
        new_string += '0'*(len(matching_digits[0])-len(str(addition))) + str(addition)
    else:
        new_string = txt
        new_string += '1'
    
    return new_string

str_incrementer('foo0042')