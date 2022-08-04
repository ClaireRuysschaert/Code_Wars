def spin_words(sentence):
    words = sentence.split()
    final_sentence = ""
    # Check the lenght of each word of the list "words"
    for word in words : 
        if len(word) > 5:
            final_sentence += word[::-1] + " "
            #inverser l'ordre des lettres
        else:
            final_sentence += word + " "
    return final_sentence.strip()
