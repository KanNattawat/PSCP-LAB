""" PSCP """
def main(frm):
    """ Frame """
    com = "*" + frm + "*"
    frame = len(com)
    print(frame*"*")
    print(com)
    print(frame*"*")
main(input())
