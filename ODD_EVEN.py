""" PSCP """
def input_():
    """ input """
    num_in = int(input())
    is_odd(num_in)

def is_odd(num_in):
    """ Calculate """
    if num_in%2 == 0:
        print("False")
    else:
        print("True")
input_()
