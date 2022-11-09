""" PSCP """
def main():
    """ [Pre] LeftArrow """
    wide = int(input())
    hight_1 = int(input())
    hight_2 = (hight_1 // 2) + 1
    hight_free = (hight_1 // 2)
    while hight_2 != 0:
        hight_2 = hight_2 - 1
        print((" " * hight_2) + ("*" * wide))
    while hight_2 != hight_free:
        hight_2 = hight_2 + 1
        print((" " * hight_2) + ("*" * wide))
main()
