""" pscp """
def main():
    """ main """
    distance = float(input())
    con = int(input())
    value = []
    runner = []
    for _ in range(con):
        player = input().split(" ")
        value.append(player)
    value2 = value.copy()
    value.sort(key=lambda i: float(i[0]), reverse=True)
    for i in value:
        runner.append((distance-float(i[1]))/float(i[0]))
    print(value2.index(value[runner.index(min(runner))])+1)

main()
