"""Grade III"""
def main(num):
    """ beom gun """
    count = 0
    for _ in range(num):
        gra = float(input())
        if 95 <= gra < 100:
            count += 4
        elif 90 <= gra < 95:
            count += 3.5
        elif 85 <= gra < 90:
            count += 3
        elif 80 <= gra < 85:
            count += 2.5
        elif 75 <= gra < 80:
            count += 2
        elif 70 <= gra < 75:
            count += 1.5
        elif 65 <= gra < 70:
            count += 1
        elif 60 <= gra < 65:
            count += 0.5
        elif 0 <= gra < 60:
            count += 0
    ala = count/num
    print("%.2f" %ala)
main(int(input()))
