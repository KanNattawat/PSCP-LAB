"""pscp"""

def main(my_input):
    """main"""
    lst = []
    my_input = my_input.replace(" ", "")
    lst.extend(my_input)
    for i in range(2):
        index_sun = lst.find("S")
    if index_sun >= 1 and index_sun != 8:
        print("Hot:", lst[index_sun-1], lst[index_sun+1])
        if index_sun <= 3:
            print("Cool:", lst[-1])
        elif index_sun > 3 and index_sun != 4:
            print("Cool:", lst[0])
        elif index_sun == 4:
            print("Cool:", lst[0], lst[-1])
    elif index_sun == 0:
        print("Hot:", lst[index_sun+1])
        print("Cool:", lst[-1])
    elif index_sun == 8:
        print("Hot:", lst[index_sun-1])
        print("Cool:", lst[0])

main(input())
