""" PSCP """
def func_a(val_a, val_b):
    """ Elo A """
    return 1/(1+10**((val_b - val_a)/400))

def func_b(val_a, val_b):
    """ Elo B """
    return 1/(1+10**((val_a - val_b)/400))

def main(val_a, val_b):
    """Elo Main"""
    xxx = input()
    if xxx == 'A':
        print("%.2f" %func_a(val_a, val_b))
    else:
        print('%.2f' %func_b(val_a, val_b))
main(int(input()), int(input()))
