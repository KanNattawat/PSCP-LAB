"""pscp"""

def main(num_list):
    """main"""
    con = 0
    num_list = num_list.split(" ")
    num_list.reverse()
    for i in num_list:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            print(i)
            con = 1
    if con == 0:
        print("Nope")

main(input())
