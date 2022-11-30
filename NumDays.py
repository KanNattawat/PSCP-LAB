""" pscp """
def main():
    """ main """
    day_1 = int(input())
    mon_1 = int(input()) - 1
    day_2 = int(input())
    mon_2 = int(input()) - 1
    ans = 0
    mon_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mon_2 < mon_1:
        mon_1, mon_2 = mon_2, mon_1
        day_1, day_2 = day_2, day_1
    if mon_1 != mon_2:
        for i in range(day_1, mon_list[mon_1] + 1):
            ans += 1
        for i in range(1, mon_list[mon_2] + 1):
            if i == day_2:
                break
            ans += 1
    else:
        ans = abs(day_1 - day_2)

    if ans == 0:
        print("Impossible")
    else:
        print(ans)

main()
