""" pscp """


def main(txt):
    """ main """
    lst = list(set(txt))
    lst.sort()
    lst.sort(key=lambda i: i.isupper())
    for i in lst:
        ans = ""
        for i_cnt in range(txt.count(i)):
            if i_cnt % 5 == 0 and i_cnt != 0 and i_cnt != txt.count(i):
                ans += "|"
            ans += "-"
        print(i, ":", ans)


main(input())
