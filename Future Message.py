""" PSCP """
def fut_(message):
    """ Future Message """
    if message.isnumeric():
        print("Number")
    elif message.isupper():
        print("Uppercase")
    elif message.islower():
        print("Lowercase")
    elif message.istitle():
        print("Title")
    elif message.isspace():
        print("Space")
    else:
        print("Other")
fut_(input())
