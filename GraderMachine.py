""" PSCP """
def main():
    """ Grader Machine """
    low = abs(int(input()))
    high = abs(int(input()))
    con = 0
    print("pass : ", end="")
    if high >= low:
        for i in range(low, high+1):
            if i % 2 == 0:
                print(i, "", end="")
                con += i
    elif high < low:
        for i in range(low, high-1, -1):
            if i % 2 == 0:
                print(i, "", end="")
                con += i
    print("\n", "Sum : ", con, sep="")
main()
