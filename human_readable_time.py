# Fonction qui traduit les secondes en h, min, sec

# 1h = 60 min
# 1min = 60 sec
# tout diviser par 60 

def make_readable(total_seconds):
    min = 0
    hours = 0
    int_seconds = int(total_seconds)

    if int_seconds < 60:
        sec = total_seconds
    else:
        sec = int_seconds % 60
        min = int((int_seconds - (int_seconds % 60))/60)

        if min >= 60:
            hours = int((int(min) - (int(min) % 60))/60)
            min = int(min)%60
    
    if len(str(sec)) < 2:
        sec = '0' + str(sec)
    if len(str(min)) < 2:
        min = '0' + str(min)
    if len(str(hours)) < 2:
        hours = '0' + str(hours)
    
    return f'{hours}:{min}:{sec}'   

make_readable('0')
