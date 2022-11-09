"""pscp"""
def main(number, loca):
    """main"""
    ppp = len(number)
    if ppp == 9:
        if loca == "Domestic":
            print(number[0], number[1:5], number[5:10])
        else:
            print("+66", number[1:5], number[5:10])
    else:
        if loca == "Domestic":
            print(number[0:2], number[2:6], number[6:10])
        else:
            print("+66"+number[1], number[2:6], number[6:10])
main(input(), input())
