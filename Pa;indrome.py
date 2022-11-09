""" pscp """
def main():
    """ main """
    my_str = int(input())
    time = input()
    con = 0
    while con != my_str:
        xxx = "%02d" % (int(time[-2:]) + 1)
        hours = time[0:2].replace(":", "")
        if int(xxx) % 60 == 0 and int(xxx) != 0:
            xxx = "00"
            yyy = int(hours) + 1
            hours = str(yyy)
        if int(hours) % 24 == 0:
            hours = "0"
        time = hours + ":" + xxx
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            con = con + 1
            print(time)

main()
