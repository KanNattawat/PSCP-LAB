""" pscp """
import math
def main(day):
    """ main """
    ans = 0
    for _ in range(day):
        hrs = float(input())
        if hrs % 1 != 0:
            hrs = math.floor(hrs)
            hrs += 1
        ans += hrs*8720
    print("%d" %ans)
main(int(input()))
