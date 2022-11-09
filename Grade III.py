"""Grade III"""
import math
def main(num):
    """ beom gun """
    count = 0
    for _ in range(num):
        score = float(input())
        if score >= 95:
            count += 4
        elif score >= 90:
            count += 3.5
        elif score >= 85:
            count += 3
        elif score >= 80:
            count += 2.5
        elif score >= 75:
            count += 2
        elif score >= 70:
            count += 1.5
        elif score >= 65:
            count += 1
        elif score >= 60:
            count += 0.5
    count /= num
    count *= 100
    count = math.floor(count)
    count /= 100
    print("%.2f" %count)
main(int(input()))
