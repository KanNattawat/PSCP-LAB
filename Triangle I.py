""" PSCP """
def tria():
    """ Triangle I """
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 > num2 and num1 > num3:
        if int(num1**2) == int(num2**2 + num3**2):
            print("Yes")
        else:
            print("No")
    elif num2 > num1 and num2 > num3:
        if int(num2**2) == int(num1**2 + num3**2):
            print("Yes")
        else:
            print("No")
    elif num3 > num1 and num3 > num2:
        if int(num3**2) == int(num1**2 + num2**2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
tria()
