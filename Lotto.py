"""pscp"""
def main():
    """MAIN"""
    won1 = input()
    last2 = input()
    front3_1 = input()
    front3_2 = input()
    last3_1 = input()
    last3_2 = input()
    my_lot = input()
    ans = 0
    if my_lot == won1:
        ans += 6000000
    elif int(my_lot) == int(won1) - 1 or int(my_lot) == int(won1) + 1:
        ans += 100000
    if my_lot[-2::] == last2:
        ans += 2000
    if my_lot[:3] == front3_1 or my_lot[:3] == front3_2:
        ans += 4000
    if my_lot[-3::] == last3_1 or my_lot[-3::] == last3_2:
        ans += 4000
    print(ans)

main()
