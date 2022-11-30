""" PSCP """
def main(lev, wod):
    for i in range(lev, 0, -1):
        print("#" * i, end="")
    for i in range(1, lev+1):
        for k in range(i, i+2):
            print("*" * k, end="")
        print()
main(int(input()), int(input()))