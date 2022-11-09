'''SequenceXXX'''
def main():
    '''SequenceXXX'''
    aaa = int(input())
    bbb = int(input())
    for i in range(aaa):
        if i == 0 or i == aaa-1:
            for _ in range(bbb):
                print("*" * aaa, end=" ")
            print()
        else:
            for _ in range(bbb):
                for j in range(aaa):
                    if i == j or j == 0 or j == aaa-1 or j == aaa-1-i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()

main()
