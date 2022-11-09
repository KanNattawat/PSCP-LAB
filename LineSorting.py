"""pscp"""

def main(num):
    """main function"""
    lst = list()
    for _ in range(num):
        my_str = input()
        lst.append(my_str)
    lst.sort(key=len)
    for i in lst:
        print(i)

main(int(input()))
