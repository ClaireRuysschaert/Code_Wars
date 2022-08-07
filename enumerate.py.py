mystr = "abcd"

count = 0
for letter in mystr:
    print("Loop number ", count, "current letter :", letter)
    count += 1

# With enumerate
for index, letter in enumerate(mystr):
    print("Loop number ", index, "current letter :", letter)


print("Here are details of enumerate")
# Detail of enumerate
for the_enumerate_tuple in enumerate(mystr, start=1):
    print(the_enumerate_tuple)  # Tuple containing the counter and the letter
    print(the_enumerate_tuple[0])  # The counter
    print(the_enumerate_tuple[1])  # The letter
