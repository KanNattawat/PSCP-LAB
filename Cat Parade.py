"""pscp"""

def main():
    """main"""
    lst_cat = []
    loca = []
    con_cat = []
    while True:
        cat = input()
        if cat == "END":
            break
        elif cat == "IT'S A DOG":
            lst_cat.pop()
            continue
        elif cat.count(", ") != 0:
            lst_cat.extend(cat.split(", "))
        else:
            lst_cat.append(cat)
    pre_lst = lst_cat[:]
    lst_cat = list(set(lst_cat))
    lst_cat.sort()
    for i in lst_cat:
        loca.append(pre_lst.index(i)+1)
        con_cat.append(pre_lst.count(i))
    print(loca)
    print(con_cat)
    print(lst_cat)
    # for i in range(len(lst_cat)):
        # print(lst_cat[i], loca[i], con_cat[i])

main()
