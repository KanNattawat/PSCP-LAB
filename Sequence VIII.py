""" PSCP """
def main():
    """ Sequence VIII """
    num = int(input())
    for i in range(num):
        for j in range(num-i-1):
            print("  ", end=" ")
        for j in range(i+1):
            print("%02d" %int(j+1), end=" ")
        print()
main()
