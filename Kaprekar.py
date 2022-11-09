"""pscp"""
def main(num):
    """main"""
    prei = "-1"
    full = ""
    con = 0
    while True:
        for i in num:
            if int(i) > int(prei):
                full += i
            prei = i
        break
    print(full)
main(input())
