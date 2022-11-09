""" pscp """


def main(temp, temp_unit, newunit_temp):
    """ main """
    if temp_unit == "F":
        temp = (temp - 32) / 1.8
    elif temp_unit == "K":
        temp = temp - 273.15
    elif temp_unit == "R":
        temp = temp / 1.8 - 273.15

    if newunit_temp == "F":
        ans = temp * 1.8 + 32
    elif newunit_temp == "K":
        ans = temp + 273.15
    elif newunit_temp == "R":
        ans = (temp + 273.15) * 1.8
    else:
        ans = temp

    print("%.2f" %ans)


main(float(input()), input(), input())
