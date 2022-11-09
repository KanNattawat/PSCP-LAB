"""pscp"""

def main(num, word):
    """main"""
    con = 0
    for i in num:
        if i == "1":
            con += 1
    if con % 2 == 0 and word == "Even":
        ans = num + "0"
    elif con % 2 == 0 and word == "Odd":
        ans = num + "1"
    elif con % 2 != 0 and word == "Even":
        ans = num + "1"
    else:
        ans = num + "0"
    print(ans)

main(input(), input())
