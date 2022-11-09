""" pscp """

def main(str1, str2):
    """ main """
    ans = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        dex_str1 = abc.find(str1[i])
        dex_str2 = abc.find(str2[i])
        print(dex_str1)
        print(dex_str2)
        if abs(dex_str1 - dex_str2) < dex_str1 - abc[26:].find(str2[i]) + 27:
            ans += abs(dex_str1 - dex_str2)
        else:
            ans += dex_str1 - abc[26:].find(str2[i]) + 1

    print(ans)
    print(dex_str1 - abc[26:].find(str2[i]))

main(input(), input())
