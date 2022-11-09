"""pscp"""

def main(num):
    """main"""
    lst = []
    for _ in range(num):
        lst.clear()
        num2 = int(input())
        for _ in range(num2):
            numxy = input()
            con = numxy.split(" ")
            con = [int(x) for x in con]
            lst.append(con)
        lst.sort(key=lambda lst: lst[1], reverse=True)
        lst.sort(key=sum)
        for i in lst:
            print(*i)

main(int(input()))
