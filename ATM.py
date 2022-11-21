""" pscp """
def main(start_money):
    """ main """
    while True:
        used = input()
        if used == 'END':
            break
        if start_money - int(used[2:]) <= 0 and used[0] == 'W':
            start_money = 0
        elif used[0] == 'D':
            start_money += int(used[2:])
        else:
            start_money -= int(used[2:])
    print(start_money)
main(int(input()))
