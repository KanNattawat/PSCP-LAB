"""pscp"""

def main(num):
    """main"""
    avg = 0
    lst = []
    lst_score = []
    lst_ans = []
    prepre = 0
    for _ in range(num):
        xxx = input()
        lst.append(xxx)
        lst_score.append(float(xxx[9:]))
        avg += float(xxx[9:])
    avg = abs(avg / num)
    for i in lst_score:
        lst_ans.append(abs(avg - i))
    inin = lst_ans.index(min(lst_ans))
    print(lst[inin])

main(int(input()))
