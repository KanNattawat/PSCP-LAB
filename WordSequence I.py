"""pscp"""

def main(word):
    """main"""
    num = len(word)
    for i in range(1, num+1):
        print(word[0:i])

main(input())
