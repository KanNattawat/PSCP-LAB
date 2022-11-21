""" pscp """
def main():
    """ main """
    line_1 = input()
    line_2 = input()
    line_3 = input()
    if line_1[0] == line_1[1] == line_1[2] and line_1[0] != '-':
        print(line_1[0], 'WIN')
    elif line_2[0] == line_2[1] == line_2[2] and line_2[0] != '-':
        print(line_2[0], 'WIN')
    elif line_3[0] == line_3[1] == line_3[2] and line_3[0] != '-':
        print(line_3[0], 'WIN')
    elif line_1[0] == line_2[0] == line_3[0] and line_1[0] != '-':
        print(line_1[0], 'WIN')
    elif line_1[1] == line_2[1] == line_3[1] and line_1[1] != '-':
        print(line_1[1], 'WIN')
    elif line_1[2] == line_2[2] == line_3[2] and line_1[2] != '-':
        print(line_1[2], 'WIN')
    elif line_1[0] == line_2[1] == line_3[2] and line_1[0] != '-':
        print(line_1[0], 'WIN')
    elif line_1[2] == line_2[1] == line_3[0] and line_1[2] != '-':
        print(line_1[2], 'WIN')
    else:
        print('DRAW')
main()
