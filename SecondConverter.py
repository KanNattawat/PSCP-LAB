"""pscp"""
def main(sec, insec, inmin, inhr):
    """secondconverter"""
    mins = sec // insec
    sec = sec % insec
    hrs = mins // inmin
    mins = mins % inmin
    hrs = hrs % inhr
    print("%d:%d:%d" %(hrs, mins, sec))
main(int(input()), int(input()), int(input()), int(input()))#หรbือ okok gขอบคุณมากๆๆๆๆ
