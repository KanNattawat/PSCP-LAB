""" PSCP """
def main():
    """ pointincircle """
    num_x = float(input())
    num_y = float(input())
    num_r = float(input())
    num_xn = float(input())
    num_yn = float(input())
    if ((((num_x - num_xn) ** 2) + ((num_y - num_yn) ** 2)) ** 0.5) <= num_r:
        print("True")
    else:
        print("False")
main()
