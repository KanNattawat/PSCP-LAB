""" pscp """

def main(txt):
    """ main """
    nnn = False
    txt = txt.replace(".", "")
    lst = txt.split(" ")
    lst_ans = []
    for i in lst:
        con = 0
        i22 = i.lower()
        con += i22.count("a")
        con += i22.count("e")
        con += i22.count("i")
        con += i22.count("o")
        con += i22.count("u")
        if con >= 2:
            lst_ans.append(i)
            nnn = True
    lst_ans.sort()
    if nnn:
        for i in lst_ans:
            print(i)
    else:
        print("Nope")

main(input())
