""" pscp """


def main(hour, minute):
    """ main """
    minute *= 6
    hour *= 30
    print((hour + (minute/12)) >= minute and (hour + (minute/12)) - minute < 6)


main(int(input()), int(input()))
