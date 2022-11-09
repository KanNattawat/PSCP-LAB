""" pscp """
def main():
    """ main """
    concon = int(input())
    for _ in range(concon):
        minute = float(input())
        lst = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(lst)):
            if sum(lst[:i+1]) > minute:
                break
            i += 1
        print(i)

main()
