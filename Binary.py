"""pscp"""

def main(base10):
    """main"""
    ans = ""
    if base10 == 0:
        return print("0")
    while True:
        if base10 == 0:
            break
        if base10 % 2 != 0:
            base10 //= 2
            ans += "1"
        else:
            base10 //= 2
            ans += "0"
    print(ans[-1::-1])

main(int(input()))
