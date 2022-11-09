"""pscp"""

def main():
    """main"""
    lst = []
    while True:
        num = int(input())
        if num == 0:
            break
        lst.append(num)
    for i in lst:
        con = 0
        while True:
            if i == 1:
                break
            if i % 2 == 0:
                i /= 2
                con += 1
            else:
                i = (i*3) + 1
                con += 1
        print(con+1)

main()
