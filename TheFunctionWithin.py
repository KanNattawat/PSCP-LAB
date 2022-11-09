""" PSCP """
def main():
    """ TheFunctionWithin """
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    num_x = (num_a + num_b)*2
    num_y = (num_a + num_c)*2
    num_y2 = (num_a - num_c)*2
    num_z = ((((num_d**2)*2)**4)*3) - (((num_d**2)*2)**3) + (((((num_d**2)*2)**2)*2) + 10)
    num_1 = (((num_z + num_x)**2) - (num_x*num_y2) + (num_y2**2))
    num_2 = ((((num_a - num_b)*2)**4)*3) - (((num_a - num_b)*2)**3) + \
        ((2*((num_a - num_b)*2)**2)) + 10
    num_3 = (((((num_c*2)*2)*2)*2)*2)
    num_4 = num_d ** 8
    print((2*num_a)*2)
    print(((((num_a - num_b)*2)**4)*3) - (((num_a - num_b)*2)**3) + \
        ((2*((num_a - num_b)*2)**2)) + 10)
    print(((num_z + num_x)**2) - (num_x*num_y) + (num_y**2))
    print(((num_1**2) + (num_2**2) - (num_3**2)) / ((num_4**2) - (2*(num_1 * num_4)) + (2*num_1)))
main()
