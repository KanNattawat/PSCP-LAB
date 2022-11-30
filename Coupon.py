""" pscp """
def main(price, coupon_1, coupon_2):
    """ main """
    coupon_1 = coupon_1.split(' ')
    coupon_2 = coupon_2.split(' ')
    coupon_1 = list(map(float, coupon_1))
    coupon_2 = list(map(float, coupon_2))
    discount_1 = (price - coupon_1[0])
    discount_2 = (price * (100 - coupon_2[0])) / 100
    if coupon_1[1] <= price and coupon_2[1] <= price:
        if discount_1 < discount_2:
            print('1', discount_1)
        elif discount_2 < discount_1:
            print('2', discount_2)
        elif discount_1 == discount_2 and coupon_1[1] == coupon_2[1]:
            print('1', discount_1)
        elif discount_1 == discount_2 and coupon_1[1] > coupon_2[1]:
            print('2', discount_2)
        elif discount_1 == discount_2 and coupon_1[1] < coupon_2[1]:
            print('1', discount_1)
    elif coupon_1[1] >= price:
        print('1', discount_1)
    elif coupon_2[1] >= price:
        print('2', coupon_2)
    else:
        print('Nope')

main(int(input()), input(), input())
