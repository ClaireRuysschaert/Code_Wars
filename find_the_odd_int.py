# dans une liste d'int, trouver l'occurence impaire

# pour chaque element  de la liste, vérifier combien de fois il occure

list = [1,1,2,2,2,3,3]

def find_it(list):
    for integers in list:
        occurences = list.count(integers)
        if (occurences%2) != 0:
            return integers

find_it(list)
