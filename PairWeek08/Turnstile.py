"""PSCP"""
def main():
    xxx = 0
    con = 0
    conp = 0
    lst = []
    while xxx != "END":
        xxx = input()
        lst.append(xxx)
        for i in range(0, len(lst)+1):
            if xxx == "C":
                if lst[con+i] == "P":
                    conp += 1
            con += 1
    print(conp)
main()
