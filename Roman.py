""" pscp """


def main():
    """ main """
    roman_list = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    roman_input = input()
    cnt = 0
    for i, j in enumerate(roman_input):
        if (i + 1) == len(roman_input) or roman_list[j] >= roman_list[roman_input[i+1]]:
            cnt += roman_list[j]
        else:
            cnt -= roman_list[j]
    print(cnt)


main()
