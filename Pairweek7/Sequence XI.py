""" PSCP """
def seq_(num):
    """ Sequence XI """
    con = 0
    for k in range(1, num):
        print("%02d" %k)
    for i in range(1, num+1):
        print("%02d" %i, end=" ")
        con += 1
    for j in range(num-1, 0, -1):
        print("%02d" %j, end=" ")
        con += 1
    print()
    # for i in range(num+1):
    #     print()
    line2_(num, con)


def line2_(num, con):
    for i in range(1, num):
        for j in range(con):
            print(i, end" ")
seq_((int(input())))