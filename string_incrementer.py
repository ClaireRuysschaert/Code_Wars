def increment_string(message):
    str_list = []
    number_list = []

    for element in message : 
        if element.isalpha():
            str_list.append(element)
        elif element.isdecimal(): 
            number_list.append(element)
        else:
            str_list


    if len(number_list) == 0:
        int_all_number = 1
    else: 
        int_all_number = int(''.join(number_list)) + 1

    str_sum=str(int_all_number)
    str_sum = '0'*(len(number_list) - len(str_sum)) + str_sum
    new_string = ''.join(str_list) + str_sum
    return new_string

print(increment_string("foo3]\\885191"))