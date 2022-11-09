""" PSCP """
def main(lev, wod):
    """ Christmas Tree """
    for i in range(1, lev+1):
        for _ in range(lev-i):
            print(" ", end="")
        for _ in range(1, i):
            print("*", end="")
        for i in range(i, 0, -1):
            print("*", end="")
        print()
    for i in range(1, wod+1):
        print(" " * (lev - 2), end="")
        print("---")
main(int(input()), int(input()))
