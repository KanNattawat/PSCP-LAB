'''Inflation'''
def inflation(price, num_years):
    '''inflation'''
    for _ in range(num_years):
        price += price * 381 // 10000
    print("%d.%02d" %(price//100, price%100))

inflation(int(float(input()) * 100), int(input()))
