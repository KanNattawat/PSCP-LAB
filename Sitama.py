"""pscp"""
def main():
    """main"""
    ex1 = int(input())
    ex2 = int(input())
    ex3 = int(input())
    ex4 = int(input())
    do1 = int(input())
    do2 = int(input())
    do3 = int(input())
    do4 = int(input())
    do1 = ex1 / do1
    do2 = ex2 / do2
    do3 = ex3 / do4
    do4 = ex4 / do3

    for _ in range(4):
        if do1 <= do2:
            do1, do2 = do2, do1
        if do2 <= do3:
            do2, do3 = do3, do2
        if do3 <= do4:
            do3, do4 = do4, do3

    print(int(do1+0.999999999))

main()
