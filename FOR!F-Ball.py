""" PSCP """
def main(word):
    """ FOR!F-Ball """
    ans1 = "b"
    ans2 = "1"
    ans3 = "2"
    for i in word:
        if i == "A":
            ans1, ans2 = ans2, ans1
        elif i == "B":
            ans2, ans3 = ans3, ans2
        else:
            ans1, ans3 = ans3, ans1
    ans = ans1 + ans2 + ans3
    print(ans.find("b")+1)

main(input())
