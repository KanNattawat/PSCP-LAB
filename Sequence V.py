# """ PSCP """
# def main():
#     """ Sequence V """
#     num = int(input())
#     count = 0
#     for i in range(num, 0, -1):
#             print(i, end=" ")
#             count += 1
#             if count == 7:
#                 print()
# main()

""" PSCP """
def main():
    """ Sequence I """
    num = int(input())
    for _ in range(num):
        for _ in range(0, 7):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
main()
