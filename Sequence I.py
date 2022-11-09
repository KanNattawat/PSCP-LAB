""" PSCP """
def main():
    """ Sequence I """
    num = int(input())
    for _ in range(1, num+1):
        for numy in range(1, num+1):
            print(numy, end=" ")
        print()
main()
