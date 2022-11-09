""" PSCP """
def main():
    """ Sequence VIII """
    num = int(input())
    for i in range(1, num+1):
        for j in range(num-i):
            print("  ", end=" ")
        for j in range(1, i):
            print("%02d" %j, end=" ")
        for i in range(i, 0, -1):
            print("%02d" %i, end=" ")
        print()
main()
