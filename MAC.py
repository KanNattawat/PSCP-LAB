"""pscp"""

def main(address):
    """main"""
    err = "abcdefABCDEF0123456789"
    con1 = 0
    con2 = 1
    con_sym = 2
    ans1 = False
    ans2 = False
    ans3 = False
    dot1 = 0
    dot2 = 1
    dot3 = 2
    dot4 = 3
    qqq = 0
    if len(address) != 17 and len(address) != 14:
        print("ERROR")
        return
    if address[2] == "-" or address[2] == ":":
        qqq += address.count("-")
        qqq += address.count(":")
        if qqq != 5:
            print("ERROR")
            return
        for _ in range(qqq+1):
            if address[con1] not in err or address[con2] not in err:
                print("ERROR")
                return
            con1 += 3
            con2 += 3
    elif address[4] == ".":
        qqq += address.count(".")
        if qqq != 2:
            print("ERROR")
            return
        for _ in range(3):
            if address[dot1] not in err or address[dot2] not in err or address[dot3] not in err \
or address[dot4] not in err:
                print("ERROR")
                return
            dot1 += 5
            dot2 += 5
            dot3 += 5
            dot4 += 5
    else:
        print("ERROR")
        return
    main2(address, con_sym, ans1, ans2, ans3)

def main2(address, con_sym, ans1, ans2, ans3):
    """main2"""
    if address[2] == "-" or address[2] == ":":
        for _ in range(5):
            if address[2] == "-":
                ans1 = True
                if address[con_sym] != "-":
                    print("ERROR")
                    return
            elif address[2] == ":":
                ans2 = True
                if address[con_sym] != ":":
                    print("ERROR")
                    return
            con_sym += 3
    else:
        ans3 = True
        con_sym += 2
        for _ in range(2):
            if address[con_sym] != ".":
                print("ERROR")
                return
            con_sym += 5

    if ans1:
        print("VALID 1")
    elif ans2:
        print("VALID 2")
    elif ans3:
        print("VALID 3")

main(input())
