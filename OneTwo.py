""" pscp """

def main(num):
    """ main """
    s_1 = "1"
    s_2 = "2"
    pre = ""
    ans = ""
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        for _ in range(num-2):
            ans = s_2 + s_1
            pre = s_1
            s_1 = s_2
            s_2 = s_2 + pre
        return ans

print(main(int(input())))
