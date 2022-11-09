""" pscp """

def main(num):
    """ main """
    lst_kabata = ["bakka", "ka", "ba", "ta"]
    for _ in range(num):
        txt = input()
        if txt.count("baka") != 0:
            print("no")
            continue
        for i in lst_kabata:
            txt = txt.replace(i, "")
        if txt == "":
            print("yes")
        else:
            print("no")

main(int(input()))
