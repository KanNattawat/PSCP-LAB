""" PSCP """
def main():
    """ Sequence I """
    num = int(input())
    numk = 1
    for _ in range(1, num+1):
        for _ in range(1, num+1):
            print(numk, end=" ")
            numk = numk+1
        print()
main()
