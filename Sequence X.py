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
    main2(num)
 
def main2(num):
    """ main2 """
    for i in range(1, num):
        for _ in range(1, i+1):
            print("  ", end=" ")
        for j in range(1, num-i+1):
            print("%02d" %j, end=" ")
        for j in range(num-i-1, 0, -1):
            print("%02d" %j, end=" ")
        print()
main()
