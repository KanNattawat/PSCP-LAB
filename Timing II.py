""" PSCP """
def main():
    """ Timing II """
    sec = int(input())
    minn = sec//60
    sec = sec%60
    hour = minn//60
    minn = minn%60
    day = hour//24
    hour = hour%24
    if day <= 9999:
        print("%04d:%02d:%02d:%02d" %(day, hour, minn, sec))
    elif day > 9999:
        print("ERR_:__:__:__")
main()
