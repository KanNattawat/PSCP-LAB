'''PSCP Program'''
def main():
    '''8438-Sort 18/11/2022'''
    num_lst = []
    num = input()
    while num != 'END':
        num_lst.append(int(num))
        num = input()
    for i in range(len(num_lst)):
        for j in range(0, len(num_lst) - i - 1):
            if num_lst[j] > num_lst[j+1]:
                num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
    print(*num_lst, sep='\n')
main()
