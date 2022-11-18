""" pscp """


def main(times, count):
    """ main """
    for i in range(6, times, 2):
        count += i if perfect_num(i) else 0
    print(count)


def perfect_num(num):
    '''Check if num is perfect'''
    return num == (num > 1) + sum(i+num//i for i in range(2, int(num**0.5)+1) if num % i == 0)


main(int(input()), 0)
