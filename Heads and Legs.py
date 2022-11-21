""" pscp """


def main(head, leg):
    """ main """
    rabbit, left = divmod(leg - 2 * head, 2)
    bird = head - rabbit
    if bird >= 0 and rabbit >= 0 and left == 0:
        print(rabbit, bird)
    else:
        print("Impossible")


main(int(input()), int(input()))
