""" pscp """


def main(str1, str2):
    """ main """
    ans = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(str1)):
        # print(str1[i], str2[i])
        if str1[i] == str2[i]:
            continue
        lst = []
        dex_str1 = abc.index(str1[i])
        dex_str2 = abc.index(str2[i])
        way1 = abs(dex_str1 - dex_str2)
        way2 = (abc[dex_str1::-1] + abc[-1:dex_str1:-1]).index(str2[i])
        way3 = (abc[dex_str1:] + abc[:dex_str2+1]).index(str2[i])
        lst.extend([way1, way2, way3])
        ans += min(lst)

    print(ans)


main(input(), input())
