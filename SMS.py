"""pscp"""


def checking(botton):
    """ botton """
    if botton == 2:
        txt = "ABC"
    elif botton == 3:
        txt = "DEF"
    elif botton == 4:
        txt = "GHI"
    elif botton == 5:
        txt = "JKL"
    elif botton == 6:
        txt = "MNO"
    elif botton == 7:
        txt = "PQRS"
    elif botton == 8:
        txt = "TUV"
    else:
        txt = "WXYZ"

    return txt


def main(botton_count):
    """main"""
    ans = ""
    for _ in range(botton_count):
        botton = int(input())
        press_count = int(input())
        if botton == 1:
            for _ in range(press_count):
                ans = ans[:-1]
            continue
        char_string = checking(botton)
        cnt = 0
        for _ in range(press_count):
            if cnt > len(char_string) - 1:
                cnt = 0
            txt = char_string[cnt]
            cnt += 1
        ans += txt
    if ans == "":
        print("null")
    else:
        print(ans)


main(int(input()))
