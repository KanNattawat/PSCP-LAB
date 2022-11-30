""" pscp """
def main(num):
    """ main """
    lst = []
    lst_ans = []
    for i in range(num):
        lst.append(int(input()))
    for i in lst:
        lst_2 = {number for number in range(1, i+1) if i % number == 0}
        lst_ans.append(lst_2)
    ans = set.intersection(*lst_ans)
    print(max(list(ans)))

main(int(input()))
