""" PSCP """
def main():
    """ Sequence VI """
    num = int(input())
    for numi in range(1, num+1):
        for numy in range(1, numi+1):
            print(numy, end=" ")
        print()
    for numi in range(num):
        for numy in range(1, num-numi):
            print(numy, end=" ")
        print()
main()
