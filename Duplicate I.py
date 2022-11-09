"""pscp"""

def main(num_m, num_n):
    """main"""
    lst_m = []
    lst_n = []
    ans = []
    for _ in range(num_m):
        lst_m.append(int(input()))
    for _ in range(num_n):
        lst_n.append(int(input()))
    for i in lst_m:
        if i in lst_n:
            ans.append(i)
    ans.sort(reverse=True)
    if ans != []:
        for i in ans:
            print(i)
    else:
        print("Nope")

main(int(input()), int(input()))
