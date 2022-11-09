""" PSCP """
def main(word):
    """ Main """
    scorea = 0
    scoreb = 0
    con1 = 0
    con2 = 2
    ran = len(word) / 2
    for _ in range(int(ran)):
        if word[con1:con2] == "SP" or word[con1:con2] == "PR" or word[con1:con2] == "RS":
            scorea += 1
        elif word[con1:con2] == "PS" or word[con1:con2] == "RP" or word[con1:con2] == "SR":
            scoreb += 1
        con1 += 2
        con2 += 2
    condi_(scorea, scoreb)

def condi_(scorea, scoreb):
    """ Print """
    if scorea > scoreb:
        print("A win %d-%d" %(scorea, scoreb))
    elif scoreb > scorea:
        print("B win %d-%d" %(scoreb, scorea))
    elif scorea == scoreb:
        print("DRAW", scorea)

main(input())
