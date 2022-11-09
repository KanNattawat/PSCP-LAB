"""pscp"""

def main(base10):
    """main"""
    lst = []
    if base10 == 0:
        return print("0")
    while True:
        if base10 == 0:
            break
        if base10 % 2 != 0:
            base10 //= 2
            lst.append("1")
        else:
            base10 //= 2
            lst.append("0")
    lst.reverse()
    ans = "".join(lst)
    print(ans)

main(int(input()))
