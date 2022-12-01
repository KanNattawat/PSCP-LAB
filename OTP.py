""" pscp """


def main():
    """ main """
    while True:
        check = 0
        stop = []
        otp = input()
        if otp == '0':
            break
        for i in otp:
            if otp.count(i) == 2 and i not in stop:
                check += 2
                stop.append(i)
            elif otp.count(i) == 3 and i not in stop:
                check += 3
                stop.append(i)
        if len(otp) == 4:
            if check == 2:
                print('Valid')
            else:
                print('Invalid')
        elif len(otp) == 6:
            if check == 4 or check == 3:
                print('Valid')
            else:
                print('Invalid')
        else:
            if check == 6:
                print('Valid')
            else:
                print('Invalid')


main()
