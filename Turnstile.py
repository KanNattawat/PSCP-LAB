"""PSCP"""
def main():
    """main"""
    lst = []
    walk = ""
    count = 0
    while walk != "END":
        walk = input()
        lst.append(walk)
    for i in range(len(lst)-1):
        if lst[0+i] == "C" and lst[1+i] == "P":
            count += 1
    print(count)
main()
