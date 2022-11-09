""" PSCP """
def main(size, pos, message):
    """ Align """
    if pos == "left":
        print(message)
    elif pos == "center" and size % 2 == 0 and len(message) % 2 != 0:
        space = (size - len(message)) / 2
        print(" " * int(space+1) + message)
    elif pos == "center" and size % 2 != 0 and len(message) % 2 == 0:
        space = (size - len(message)) / 2
        print(" " * int(space+1) + message)
    elif pos == "center":
        space = (size - len(message)) / 2
        print(" " * int(space) + message)
    else:
        space = (size - len(message))
        print(" " * int(space) + message)
main(int(input()), input(), input())
