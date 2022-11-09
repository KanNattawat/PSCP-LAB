""" pscp """


def main(num_1, num_2):
    """ main """
    lst = []
    for i in range(1, 100001):
        if num_1 % i == 0 and num_2 % i == 0:
            lst.append(i)
    print(max(lst))


main(int(input()), int(input()))
