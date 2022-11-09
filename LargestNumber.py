""" PSCP """
def cal_(num1, num2, num3):
    """ Cal & Print """
    ans = num1 + num2 + num3
    ans = main((num1 + num3 + num2), ans)
    ans = main((num2 + num1 + num3), ans)
    ans = main((num2 + num3 + num1), ans)
    ans = main((num3 + num2 + num1), ans)
    ans = main((num3 + num1 + num2), ans)
    print(int(ans))

def main(val_1, val_2):
    """ Main """
    if val_1 > val_2:
        return val_1
    return val_2
cal_(input(), input(), input())
