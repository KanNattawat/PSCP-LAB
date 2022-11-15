""" pscp """


def main(num):
    """ main """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return main(num-1) + main(num-2)

print(main(int(input())))
