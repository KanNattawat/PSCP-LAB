"""pscp"""
def main():
    """main"""
    while True:
        num = input()
        if num == "0":
            break
        while len(num) != 1:
            ans = 0
            for i in num:
                ans += int(i)
            num = str(ans)
        ans = num
        print(ans)

main()
