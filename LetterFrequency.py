""" pscp """


def main(sentence):
    """ main """
    lst = []
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    for i in sentence:
        lst.append(sentence.count(i))
    print(sentence[lst.index(max(lst))])


main(input())
