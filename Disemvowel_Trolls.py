def disemvowel(string_):
    without_vowel = ""
    for letters in string_:
        if not letters in "aeiouAEIOU":
            without_vowel += letters
        else:
            pass
    return(without_vowel)
