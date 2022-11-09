""" PSCP """
def main():
    """ Sequence II """
    num = int(input())
    count1 = 0
    count2 = 1
    for _ in range(num):
        print(count2, end=" ")
        count2 += 3 + count1
        count1 += 2
main()
