import math

def nb_year(p0 : int, percent : float, aug : int, p : int):
    # p0 = initial population
    # percent = increase percent of population
    # aug = inhabitants coming or leaving each year
    # p = final population
    number_of_years = 0
    px = p0
    while px < p :
        px = math.floor(px + px * (percent/100) + aug)
        number_of_years += 1
    return number_of_years

# math.floor -> arrondir à l'inférieur (chiffre)
# round -> arrondir au plus proche (chiffre, nombre après la virgule)
# Quand on ne sait pas combien de fois il faut itérer = while -> variable +1 