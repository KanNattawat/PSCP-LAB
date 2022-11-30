""" PSCP """
def main(num):
    """ Key """
    lst = []
    for i in range(13):
        lst.append(int(num[i]))
    last = int(num) % 1000
    summ = sum(lst)
    summ += last * 10
    if summ < 1000:
        print(summ + 1000)
    elif summ > 9999:
        print(str(summ)[-4:])
    else:
        print(summ)
main(input())
