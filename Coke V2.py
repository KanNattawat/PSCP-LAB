""" pscp """


def main():
    """ main """
    old_price = int(input())
    cap_cnt = int(input())
    new_price = int(input())
    cap_needed = int(input())

    if cap_cnt == 0:
        print(old_price*cap_needed)
        quit()
    if cap_needed == 0:
        print(0)
        quit()

    howmany = (cap_needed - 1)
    loop_cnt = howmany // cap_cnt
    cap_left = howmany % cap_cnt
    price_loop = (old_price*(cap_cnt-1)) + new_price

    ans = old_price + (loop_cnt * price_loop) + \
        (cap_left * old_price)
    print(ans)


main()
