"""pscp"""
 
def main(mmm, nnn):
    """main"""
    lst = []
    lst_sum = []
    for _ in range(mmm):
        lst.append(input().split(" "))
    for i in range(nnn):
        que = 0
        for j in lst:
            que += int(j[i])
        lst_sum.append(que)
    print(max(lst_sum))
 
main(int(input()), int(input()))
