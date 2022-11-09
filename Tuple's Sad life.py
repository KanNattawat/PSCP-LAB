"""pscp"""

def main(num_str, num):
    """kfc"""
    con = 0
    index_ = 0
    num_str = num_str.replace(" ", "")
    for i in num_str:
        if i == num:
            index_ = con
            break
        con += 1
    count_ = num_str.count(str(num))

    for i in range(count_):
        for _ in range(count_):
            print(index_, end=" ")
        print()

main(input(), input())
