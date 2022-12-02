""" pscp """


def main():
    """ main """
    while True:
        otp = input()
        if otp == '0':
            break
        num_count_list = [otp.count(str(i)) for i in range(10)]
        if len(otp) == 4 and num_count_list.count(2) == 1:
            print('Valid')
        elif len(otp) == 6 and (num_count_list.count(2) == 2 or num_count_list.count(3) == 1):
            print('Valid')
        elif len(otp) == 8 and (num_count_list.count(2) == 3 or num_count_list.count(3) == 2):
            print('Valid')
        else:
            print('Invalid')
        # print(num_count_list)


main()
