""" PSCP """
def main():
    """ Stepper II """
    in_m = int(input())
    in_n = int(input())
    if in_m > in_n:
        for i in range(in_m, in_n-1, -1):
            print(i)
    else:
        for i in range(in_m, in_n+1):
            print(i)
main()
