""" PSCP """
def ball_(num):
    """ Ball """
    count = 0
    while num >= 0.01:
        num *= (3/5)
        count += 1
    print(count-1)
ball_(float(input()))
