""" pscp """


def main(isbn):
    """ main """
    ans = 0
    count_down = 10
    isbn = isbn.replace('-', '')
    isbn = isbn.replace(' ', '')
    isbn = list(map(int, isbn))
    for i in isbn:
        if count_down == 1:
            break
        ans += i * count_down
        count_down -= 1
    ans = -ans % 11

    if ans == isbn[-1]:
        print('Yes')
    elif ans == 10:
        print('No', 'X')
    else:
        print('No', ans)


main(input())
