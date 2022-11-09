"""pscp"""
def main(numa, numb, numc, numd):
    """main"""
    d_set = numb + numc
    p_set = numa * numb
    numset = numd // d_set
    left = numd - d_set * numset
    if left >= numb:
        numset += 1
        left = 0
    t_price = numset * p_set + left * numa
    t_donut = numset * d_set + left
    print(t_price, t_donut)
main(int(input()), int(input()), int(input()), int(input()))
