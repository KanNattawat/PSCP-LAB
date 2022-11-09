""" PSCP """
def main(word):
    """ Decode """
    num = "0"
    for i in word:
        if i.isnumeric():
            num = num + i
        else:
            ans = i
            print(ans * int(num), end="")
            num = "0"

main(input())
