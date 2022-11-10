""" PSCP """


def main(num):
    """ main """
    ans = 0

    for i in range(1, num+1):
        can_divide = 0
        for val in range(1, i+1):
            if i % val == 0:
                can_divide += 1

        if can_divide == 2:
            ans += 1

    print(ans)


main(int(input()))
