def square_digits(num):
    total_square = ""
    for numbers in str(num):
        square = int(numbers) * int(numbers)
        total_square += str(square)
    return int(total_square)
