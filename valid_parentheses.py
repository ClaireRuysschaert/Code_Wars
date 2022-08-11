def valid_parentheses(string):
   # stocker dans une variable le compte des parenthèses ouvertes / fermées
   # si '(' = +1 et si ')' = -1
   # dès que la variable atteint -1 -> False (mais pendant le compte ?? = if à la fin de la boucle ??)
   # à la fin forcément = 0
    count = 0
    for element in string:
        if element == '(':
            count += 1
        elif element == ')':
            count -= 1
        if count == -1:
            return False
    if count == 0:
        return True
    else : 
        return False    

    

print(valid_parentheses('hi())('))

