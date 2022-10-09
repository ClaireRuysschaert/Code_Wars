source1 = {"A": 1, "B": 2, "C": 3} 
source2 = {"A": [1], "B": [2], "C": [3]}
# fonction qui merge 2 dict en ajoutant les doublons d'object dans une liste
# fonction ajoute des valeurs dans une liste de clefs communes
# dont overrride the data

def merge(*dict_tuple):
    # For ech dictionaries in the tuple
    # For each key, value, add to a final dict
    # If the key is already added to the final dict, create a list of all the values
    final_dict = {}
    for dictionaries in dict_tuple:
        for key, value in dictionaries.items():
            if key in final_dict:
                if type(final_dict[key]) != list:
                    final_dict[key]= [final_dict[key]]
                if type(value) == list:
                    final_dict[key] = final_dict[key] + value
                else:
                    final_dict[key].append(value)
            else :
                final_dict[key] = [value]
    return final_dict

print(merge(source1, source2))
