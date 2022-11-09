""" pscp """
def func1(win_a, winb, my_input):
    """Compare winner function"""
    return win_a >= my_input or winb >= my_input

def func2(win_a, winb):
    """Check if not deal mode"""
    return abs(win_a - winb) >= 2

def main():
    """Main function"""
    my_input = input() + " "
    win_a = 0
    winb = 0
    round_a = 0
    round_b = 0
    my_str = ""
    con = 0
    my_bool = False
    while len(my_input) != 0:
        for text in my_input:
            if func1(win_a, winb, 25) \
                and func2(win_a, winb) and con <= 3:
                my_bool = True
                break
            if func1(win_a, winb, 15) \
                and func2(win_a, winb) and con == 4:
                my_bool = True
                break
            if text == "A":
                win_a = win_a + 1
            elif text == "B":
                winb = winb + 1
            my_str = my_str + text
        con = con + 1
        if win_a > winb:
            round_a = round_a + 1
        else:
            round_b = round_b + 1
        if con <= 5:
            print("Set %d: A (%d) | B (%d)"%(con, win_a, winb))
        my_input = my_input.replace(my_str, "", 1)
        if con >= 4 and my_bool and round_a-round_b != 0 \
            or (abs(round_a-round_b) == 3):
            print("A won %d:%d set"\
               %(round_a, round_b)*(round_a > round_b)+\
                  "B won %d:%d set"\
                %(round_b, round_a)*(round_a < round_b))
            break
        #Set to default at all!
        my_bool = False
        win_a = 0
        winb = 0
        my_str = ""
    if not my_bool:
        print("The game has not finished yet.")
main()
