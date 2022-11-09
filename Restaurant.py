"""pscp"""
def main(numa, numb, numc, numd):
    """main"""
    # totalprice = numa
    totalprice = numa + numd
    percent = (100 - numc) / 100
    # con = totalprice * percent
    # ans = abs(con - numa)
    # if con > numa:
    #     print("No %.3f" %ans)
    # elif con < numa and numa + numd >= numb:
    #     print("Yes %.3f" %ans)
    # else:
    #     print("Yes")
    if totalprice >= numb:
        offer = totalprice * percent
    else:
        offer = totalprice
    totalprice = numa
    if totalprice >= numb:
        unoffer = totalprice * percent
    else:
        unoffer = totalprice
    totalprice = numa + numd
    con = abs(unoffer - offer)
    if offer < unoffer:
        print("Yes %.3f" %con)
    elif offer > unoffer:
        print("No %.3f" %con)
    else:
        print("Yes")

main(float(input()), float(input()), float(input()), float(input()))
