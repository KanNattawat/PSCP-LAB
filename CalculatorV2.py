""" pscp """


def main():
    """ main """
    num = int(input())
    cnt = len(str(num))
    cnt_1 = 1
    cnt_9 = 9
    ans = 0

    if num == 1:
        print(1)
        quit()
    for i in range(1, cnt):
        con = (cnt_9 - cnt_1)+1
        ans += con * i
        cnt_1 = int(str(cnt_1) + "0")
        cnt_9 = int(str(cnt_9) + "9")

    cnt_ans = ((num - cnt_1) + 1) * cnt
    total = (ans + cnt_ans) + num
    print(total)


main()
