'''RuleofThree'''
def main():
    '''RuleofThree'''
    num = int(input())
    con = 0
    p_ans = 0
    w_ans = 0
    for _ in range(1, num+1):
        pirce = float(input())
        size = float(input())
        if size/pirce > con:
            con = size/pirce
            p_ans = pirce
            w_ans = size
        if size/pirce == con:
            if pirce < p_ans:
                con = size/pirce
                p_ans = pirce
                w_ans = size
    print('%.2f %.2f' %(p_ans, w_ans), end=' ')

main()
