"""pscp"""
 
def main(txt):
    """main"""
    num = ""
    lst = []
    ans = 0
    for i in txt:
        if i.isnumeric():
            num += i
        else:
            lst.append(num)
            num = ""
    lst.append(num)
    for i in lst:
        if i != "":
            ans += int(i)
    print(ans)
 
main(input())
