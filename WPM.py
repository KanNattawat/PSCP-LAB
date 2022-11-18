""" pscp """


def main(age_range, wpm):
    """ main """
    if age_range == "Kids":
        if wpm < 11:
            print("Very Slow")
        elif wpm in range(11, 21):
            print("Slow")
        elif wpm in range(21, 31):
            print("Average")
        elif wpm in range(31, 41):
            print("Fast")
        else:
            print("Very Fast")
    else:
        main2(wpm)


def main2(wpm):
    """ main2 """
    if wpm < 26:
        print("Very Slow")
    elif wpm in range(26, 36):
        print("Slow/Beginner")
    elif wpm in range(36, 46):
        print("Intermediate/Average")
    elif wpm in range(46, 66):
        print("Fast/Advanced")
    elif wpm in range(66, 81):
        print("Very Fast")
    else:
        print("Insane")

main(input(), int(input()))
