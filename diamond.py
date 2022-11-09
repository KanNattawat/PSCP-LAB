"""pscp"""
def main(num):
    """main"""
    cut = num //2
    for i in range(num):
        for j in range(num):
            if i == cut or i + j == cut or j - i == cut or i - j == cut or\
                 j == num - i + cut - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main(int(input()))
