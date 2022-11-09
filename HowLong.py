""" PSCP """
def main():
    """ HowLong """
    num = abs(int(input()))
    con = 1
    while num // 10 > 0:
        con += 1
        num = num // 10
    print(con)
main()
