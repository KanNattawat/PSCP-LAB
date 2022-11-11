""" pscp """


def main():
    """ main """
    countries = dict()
    for _ in range(int(input())):
        xxx = input().split(" ")
        countries[xxx[0]] = tuple(map(int, xxx[1:]))
    countries_sort = sorted(
        countries.items(), key=lambda a: sum(a[1]), reverse=True)
    countries_sort.sort(key=lambda a: a[0])
    countries_sort.sort(key=lambda a: a[1], reverse=True)
    rank = 0
    keep = 0
    old = 0
    for country, score in countries_sort:
        score_sum = sum(score)
        score = " ".join(map(str, score))
        if score != old:
            rank += keep
            keep = 0
            rank += 1
        elif rank != 0:
            keep += 1
        print(rank, country, score, score_sum)
        old = score


main()
