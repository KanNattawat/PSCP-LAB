""" PSCP """
def main():
    """ BootSequence """
    num = int(input())
    lst = []
    for i in range(1, num+1):
        lst.append(i)
    print(*lst, sep="_")

main()
