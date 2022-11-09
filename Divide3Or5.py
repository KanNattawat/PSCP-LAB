"""pscp"""

def main(num):
    """main"""
    lst = []
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
    print(sum(lst))

main(int(input()))
