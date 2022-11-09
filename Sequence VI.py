""" PSCP """
def main():
    """ Sequence VI """
    num = int(input())
    for i in range(1, num+1):
        for numy in range(1, i+1):
            print(numy, end=" ")
        print()
main()
