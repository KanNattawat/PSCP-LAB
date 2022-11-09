"""pscp"""
def main(line1, line2, line3, line4, line5):
    """ main """
    maxx = max(len(line1), len(line2), len(line3), len(line4), len(line5))
    frame = "*"*maxx+"****"
    print(frame)
    print("* "+line1+" "*(maxx-len(line1)+1)+"*")
    print("* "+line2+" "*(maxx-len(line2)+1)+"*")
    print("* "+line3+" "*(maxx-len(line3)+1)+"*")
    print("* "+line4+" "*(maxx-len(line4)+1)+"*")
    print("* "+line5+" "*(maxx-len(line5)+1)+"*")
    print(frame)
main(input().strip(" "), input().strip(" "), input().strip(" "), \
input().strip(" "), input().strip(" "))
