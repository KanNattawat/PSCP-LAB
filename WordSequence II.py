""" pscp """


def main(word_1, word_2):
    """ main """
    con = len(word_1)
    if len(word_1) > len(word_2):
        con = len(word_1)
    else:
        con = len(word_2)
    for i in range(con+1):
        print(word_2[:i] + word_1[i:])


main(input(), input())
