""" PSCP """
def main():
    """ Sequence I """
    num = int(input())
    k = 1
    for numx in range(1, num+1):
        for numy in range(1, num+1):
            print(k, end=" ")
            k = k+1
        print()
main()
