""" PSCP """
def main(text):
    """ Main """
    con = 0
    for i in range(len(text)-1, -1, -1):
        print(" "*i, end="")
        con += 1
        for j in range(con):
            print(text[0+j], end="")
        print()
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            print(text[j], end="")
        print()
main(input())
