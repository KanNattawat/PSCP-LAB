""" pscp """
def main(bit):
    """ main """
    invert = ''
    for i in bit:
        if i == '1':
            invert += '0'
        else:
            invert += '1'
    if invert.count('1') != 0:
        print(invert[invert.index('1'):])
main(input())
