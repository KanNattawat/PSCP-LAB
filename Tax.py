""" pscp """


def main(car_age, engine_size):
    """ main """
    ans = 0
    for i in range(1, engine_size + 1):
        if i in range(1, 601):
            ans += 0.5
        elif i in range(601, 1801):
            ans += 1.5
        else:
            ans += 4
    if car_age > 5:
        print("%.2f" % discount(car_age, ans))
    else:
        print("%.2f" % ans)


def discount(car_age, ans):
    """ discount """
    if car_age == 6:
        return (90 * ans) / 100
    elif car_age == 7:
        return (80 * ans) / 100
    elif car_age == 8:
        return (70 * ans) / 100
    elif car_age == 9:
        return (60 * ans) / 100
    else:
        return ans / 2


main(int(input()), int(input()))
