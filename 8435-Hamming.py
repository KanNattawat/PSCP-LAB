'''PSCP Program'''
def main(txt1, txt2, count):
    '''8435-Hamming 18/11/2022'''
    for i, j in enumerate(txt1):
        count += 1 if j != txt2[i] else 0
    print(count)

main(input(), input(), 0)
