"""pscp"""

def main(num):
    """main"""
    for _ in range(num):
        year = input()
        if year[:4] == "B.E.":
            year = int(year[5::]) - 543
            if year < 0:
                ans = "ERROR"
        else:
            year = int(year[5::])
        if year < 0:
            print(ans)
        else:
            ans = year // 100
            if year % 100 != 0:
                ans += 1
            print(ans)

main(int(input()))
