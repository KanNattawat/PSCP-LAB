""" pscp """


def main(digit_in_string):
    """ main """
    digit_in_string = digit_in_string.split(" ")
    if digit_in_string[0][-1] == "n" and digit_in_string[0] != "seven" \
            or digit_in_string[0] == "twelve":
        ans = 2
    elif digit_in_string[0][-1] == "y":
        ans = 2
    else:
        ans = 1

    if len(digit_in_string) >= 2:
        if digit_in_string[1] == "hundred":
            ans = 3
        elif digit_in_string[1] == "thousand":
            ans = 4
    print(ans)


main(input())
