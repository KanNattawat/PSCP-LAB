"""pscp"""

def main(sen):
    """main"""
    con = True
    lst = []
    lst_ans = []
    my_str = ""
    for i in sen:
        lst.append(i)
    for i in lst:
        if lst.count(i) % 2 != 0 and i not in my_str:
            lst_ans.append(i)
            my_str += i
            con = False
    if con:
        print("fully paired")
    else:
        for i in lst_ans:
            print(i, end="")

main(input())
