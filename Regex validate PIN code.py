def validate_pin(pin):
    if pin.isnumeric() == False:
        return False 
    elif len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False