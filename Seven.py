""" PSCP """
def main():
    """ Seven """
    num = int(input())
    ans = num % 4
    if ans == 1:
        print(7)
    elif ans == 2:
        print(9)
    elif ans == 3:
        print(3)
    elif ans == 0:
        print(1)
main()
