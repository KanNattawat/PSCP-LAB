""" pscp """

def main(line):
    """ main """
    ans = 0
    for _ in range(line):
        txt = input()
        ans += len(txt) - txt.count(" ")
    print(ans)

main(int(input()))
