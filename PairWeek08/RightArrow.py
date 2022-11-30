''' Right arrow '''
def main():
    ''' input and print'''
    val_k = int(input())
    val_n = int(input())
    new_n = int((val_n-1)/2)
    line = 0
    while line != new_n+1:
        print(' '*line + '*'*val_k)
        line += 1
    for i in range(new_n, 0, -1):
        print(' '*(i-1) + '*'*val_k)
main()
