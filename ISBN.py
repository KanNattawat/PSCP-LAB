""" pscp """


def main(isbn):
    """ main """
    ans = 0
    count_down = 10
    isbn = isbn.replace('-', '')
    isbn = isbn.replace(' ', '')
    check = isbn[-1]
    isbn = isbn[:-1]
    isbn = list(map(int, isbn))
    for i in isbn:
        if count_down == 1:
            break
        ans += i * count_down
        count_down -= 1
    ans = -ans % 11

    if str(ans) == check or check == 'X' and ans == 10:
        print('Yes')
    elif ans == 10 and check != 'X':
        print('No', 'X')
    else:
        print('No', ans)


main(input())
