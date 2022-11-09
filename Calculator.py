"""pscp"""
def main(num):
    """main"""
    ans = 0
    for i in range(1, num+1):
        ans += len(str(i)) + 1
    if num == 1:
        ans = 1

    print(ans)

main(int(input()))
