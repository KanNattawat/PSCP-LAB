"""pscp"""
 
def main(num):
    """main"""
    ans = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                ans = True
                break
    if num == 0 or num == 1:
        print("No")
    elif ans:
        print("No")
    else:
        print("Yes")
 
main(int(input()))
