""" PSCP """
def main():
    """ SumOfNumber """
    toa = int(input())
    num = 0
    ans = 0
    while True:
        num = int(input())
        if num == -1:
            break
        ans += num
        if ans == toa:
            break
    print(ans)
main()
