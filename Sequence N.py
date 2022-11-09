""" PSCP """
def seq_(num):
    """ Sequence N """
    left = 0
    right = num - 3
    print("*" + " " * (num-2) + "*")
    while left != num - 2:
        print("*" + " " * left + "*" + " " * right + "*")
        left += 1
        right -= 1
    print("*" + " " * (num-2) + "*")
seq_(int(input()))
