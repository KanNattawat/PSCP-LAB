"""pscp"""
def main(num):
    """main"""
    for i in range(1, num+1):
        name = input()
        if i == num:
            print(name+"_"+str(num), end="")
        elif i%2 == 0:
            print(name+"-"*i, end="")
        else:
            print(name+"*"*i, end="")
main(int(input()))
