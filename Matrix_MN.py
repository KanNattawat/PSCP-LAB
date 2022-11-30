""" pscp """


def main(line, row):
    """ main """
    lst = []
    for _ in range(line * row):
        lst.append(int(input()))
    for i in range(line):
        for i in range(row):
            print(lst[i], end=" ")

        del lst[:row]
        print()


main(int(input()), int(input()))
