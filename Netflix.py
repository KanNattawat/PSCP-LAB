""" pscp """
def func1(premium, standard, basic, mobile, xxx):
    """func1"""
    if premium > 0:
        print("Premium x %d" % premium)
    if standard > 0:
        print("Standard x %d"% standard*(standard > 0))
    if basic > 0:
        print("Basic x %d" % basic*(basic > 0))
    if mobile > 0:
        print("Mobile x %d" % mobile*(mobile > 0))
    print("Total = %d THB" % xxx)

def main():
    """main"""
    number_of_screen = int(input())
    number_of_phone = int(input())
    input()
    input()
    watch_tv = input().lower()
    hdo = input().lower()
    ultra = input().lower()

    counter_premium = 0
    counter_standard = 0
    counter_basic = 0
    counter_mobile = 0
    xxx = 0
    while number_of_screen > 0 or number_of_phone > 0:
        if (ultra == "yes" or hdo == "yes" or watch_tv == "yes") \
            and (number_of_screen >= 3 or number_of_phone >= 3):
            xxx += 419
            counter_premium += 1
            number_of_screen -= 4
            number_of_phone -= 4
        elif (hdo == "yes" or watch_tv == "yes") \
            and (number_of_screen >= 2 or number_of_phone >= 2):
            xxx += 349
            counter_standard += 1
            number_of_screen -= 2
            number_of_phone -= 2
        elif watch_tv == "yes" and ultra == "no" and hdo == "no":
            xxx += 279
            counter_basic += 1
            number_of_screen -= 1
            number_of_phone -= 1
        else:
            if ultra == "yes":
                xxx += 419
                counter_premium += 1
                number_of_screen -= 4
                number_of_phone -= 4
            elif hdo == "yes":
                xxx += 349
                counter_standard += 1
                number_of_screen -= 2
                number_of_phone -= 2
            elif watch_tv == "yes":
                xxx += 279
                counter_basic += 1
                number_of_screen -= 1
                number_of_phone -= 1
            else:
                xxx += 99
                counter_mobile += 1
                number_of_screen -= 1
                number_of_phone -= 1
    func1(counter_premium, counter_standard, counter_basic, counter_mobile, xxx)
main()
