""" pscp """


def main(money, interest, year):
    """ main """
    for _ in range(year):
        money += money * (interest/100)
    print("%.2f" % money)


main(int(input()), float(input()), int(input()))
