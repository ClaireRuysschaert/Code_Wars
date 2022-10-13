def high_and_low(numbers):
    num_list = numbers.split(" ")
    for element in range(0, len(num_list)):
        num_list[element] = int(num_list[element])
    sort_list = sorted(num_list)
    return f'{sort_list[-1]} {sort_list[0]}'

high_and_low("1 2 3")