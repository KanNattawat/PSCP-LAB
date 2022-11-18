"""pscp"""


def main(num):
    """main"""
    ans = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                ans = True
                break
    if num == 0 or num == 1:
        print("NO")
    elif ans:
        print("NO")
    else:
        print("YES")


main(int(input()))
