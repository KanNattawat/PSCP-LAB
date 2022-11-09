'''FourDirections'''
def main(message):
    '''Directions'''
    txt1 = ''
    txt2 = ''
    txt3 = ''
    txt4 = ''
    txt5 = ''
    for i in message:
        if i == 'U':
            txt1 += '  *   '
            txt2 += ' ***  '
            txt3 += '* * * '
            txt4 += '  *   '
            txt5 += '  *   '
        if i == 'D':
            txt1 += '  *   '
            txt2 += '  *   '
            txt3 += '* * * '
            txt4 += ' ***  '
            txt5 += '  *   '
        if i == 'L':
            txt1 += '  *   '
            txt2 += ' *    '
            txt3 += '***** '
            txt4 += ' *    '
            txt5 += '  *   '
        if i == 'R':
            txt1 += '  *   '
            txt2 += '   *  '
            txt3 += '***** '
            txt4 += '   *  '
            txt5 += '  *   '
    print(txt1)
    print(txt2)
    print(txt3)
    print(txt4)
    print(txt5)

main(input())
