""" PSCP """
def main():
    """ Distinguish """
    num = int(input())
    if num > 180:
        print("You're hit the door edge.")
    elif num <= 180:
        print("Nothing happens.")
main()
