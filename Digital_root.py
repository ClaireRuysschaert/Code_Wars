def digital_root(n):
    add_numbers = 0
    for numbers in str(n):
        add_numbers += int(numbers)
    print(add_numbers)

    if len(str(add_numbers)) == 1:
        return add_numbers
    else:
        return digital_root(add_numbers)
