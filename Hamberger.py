""" PSCP """
def main():
    """ Hamburger """
    bread_1 = int(input())
    bread_2 = int(input())
    bread = "|"
    meat = "**"
    print((bread * bread_1) + (meat * bread_1) + (meat * bread_2) + (bread * bread_2))
main()
