"""pscp"""

def main():
    """main"""
    old_price = int(input())
    cap = int(input())
    new_price = int(input())
    want = int(input())
    pay = old_price * want
    dif = old_price - new_price
    if cap == 0:
        print(pay)
    elif cap < want:
        inspec_cap = (want // cap)
        if want % cap == 0:
            inspec_cap -= 1
        for _ in range(inspec_cap):
            pay -= dif
        print(pay)
    else:
        print(pay)

main()
