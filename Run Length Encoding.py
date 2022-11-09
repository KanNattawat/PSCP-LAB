""" PSCP """
def main(word):
    """ Main """
    count = 1
    for i in range(len(word)-1):
        ans = i
        if word[0+i] == word[1+i]:
            count += 1
            continue
        print(str(count)+word[0+i], end="")
        count = 1
    if len(word) == 1:
        print(str(count)+word)
        return
    print(str(count)+word[1+ans], end="")

main(input())
