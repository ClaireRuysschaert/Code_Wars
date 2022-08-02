def unique_in_order(iterable):
    list = []
    for letters in iterable:
        if list and list[-1] == letters:
            pass
        else:
            list.append(letters)
    return list
