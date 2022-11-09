'''ProgressiveTax'''
def main():
    '''ProgressiveTax'''
    my_mon = int(input())
    tot = 0
    if my_mon > 4000000:
        twee = my_mon - 4000000
        my_mon -= twee
        tot += twee * (35/100)
    if my_mon > 2000000:
        twee = my_mon - 2000000
        my_mon -= twee
        tot += twee * (30/100)
    if my_mon > 1000000:
        twee = my_mon - 1000000
        my_mon -= twee
        tot += twee * (25/100)
    if my_mon > 750000:
        twee = my_mon - 750000
        my_mon -= twee
        tot += twee * (20/100)
    if my_mon > 500000:
        twee = my_mon - 500000
        my_mon -= twee
        tot += twee * (15/100)
    if my_mon > 300000:
        twee = my_mon - 300000
        my_mon -= twee
        tot += twee * (10/100)
    if my_mon > 150000:
        twee = my_mon - 150000
        my_mon -= twee
        tot += twee * (5/100)
    if my_mon > 0:
        pass
    print(int(tot))

main()
