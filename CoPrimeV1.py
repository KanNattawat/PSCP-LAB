""" main """


def main():
    """ main """
    num_1 = int(input())
    num_2 = int(input())
    gcd = 1
    for i in range(1, num_1 + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
    if gcd == 1:
        print("YES")
        print(gcd)
    else:
        print("NO")
        print(gcd)


main()
