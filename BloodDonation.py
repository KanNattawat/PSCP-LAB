""" pscp """


def main(age, weight, donate_cnt):
    """ main """
    ans = "No"
    if age == 17 or age in range(60, 71):
        contest = input()
    if age in range(17, 71):
        if weight >= 45:
            if donate_cnt == 0 and age <= 55 or donate_cnt != 0:
                if age == 17 or age in range(60, 71):
                    if contest == "True":
                        ans = "Yes"
                elif age in range(18, 60):
                    ans = "Yes"

    print(ans)


main(int(input()), int(input()), int(input()))
