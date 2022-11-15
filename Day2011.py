""" pscp """


def main(day, month):
    """ main """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayofyear = sum(days[:month-1]) + day
    daynum = dayofyear % 7
    daynames = ['Friday', 'Saturday', 'Sunday',
                'Monday', 'Tuesday', 'Wednesday', 'Thursday']

    return daynames[daynum]


print(main(int(input()), int(input())))
