""" PSCP """
def main(num):
    """ Key """
    summ = 0
    for i in num:
        summ += int(i)
    multi = int(num[-3:]) * 10
    ans = summ + multi
    if ans > 9999:
        ans = str(ans)
        ans = ans[1:]
    elif ans < 1000:
        ans += 1000
    print(ans)

main(input())
