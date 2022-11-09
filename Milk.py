"""pscp"""
def main(numa, numb, numc, numd):
    """Milk"""
    free = 0
    total = numd // numa
    total2 = total
    while numb > 0 and total2 >= numb:
        free = (total2 // numb) * numc
        total2 = total2 % numb
        total2 += free
        total += free
    print(total)

main(int(input()), int(input()), int(input()), int(input()))
