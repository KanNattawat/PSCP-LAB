""" PSCP """
def con1(vir):
    """ Con1 """
    lsts = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "{", "}", \
"[", "]", "|", "\\", "/", ":", ";", "\"", "'", "<", ">", ",", ".", "?"]
    for j in range(31):
        if vir.find(lsts[0+j]) != -1:
            print("Invalid")
            return
    con2(vir)

def con2(vir):
    """ Con2 """
    for k in range(len(vir)-1):
        if vir[1+k] == " ":
            print("Invalid")
            return
    con3(vir)

def con3(vir):
    """ Con3 """
    if vir[0].isnumeric():
        print("Invalid")
    else:
        con4(vir)

def con4(vir):
    """ Con4 """
    if vir == "if" or vir == "else" or vir == "elif" or vir == "while" or vir == "for" or \
vir == "True" or vir == "False" or vir == "continue" or vir == "break" or vir == "return" or \
vir == "is" or vir == "in" or vir == "and" or vir == "or" or vir == "from" or vir == "as" or \
vir == "pass" or vir == "not" or vir == "def" or vir == "None":
        print("Invalid")
    else:
        print("Valid")

def main(con):
    """ Main """
    lst = []
    for i in range(con):
        lst.append(input())
    for i in range(con):
        con1(lst[0+i])
main(int(input()))
