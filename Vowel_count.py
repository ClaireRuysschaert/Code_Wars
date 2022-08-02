def get_count(sentence):
    count = 0
    for letters in sentence : 
        if letters in "aeiouAEIOU":
            count += 1
        else:
            pass
    return count
    