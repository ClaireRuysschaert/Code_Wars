def pig_it(text):
    list = text.split()
    new_list = []
    for word in list:   
        if word.isalpha() == False:
            new_list.append(word)
        else : 
            new_word = word[1:] + word[0] + "ay"
            new_list.append(new_word)
    final_list = ' '.join(new_list)
    return final_list
            

            

pig_it('Hello world !')
