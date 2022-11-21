""" pscp """


def main(color_1, color_2):
    """ main """
    base = ['Red', 'Yellow', 'Blue']
    if color_1 in base and color_2 in base:
        if color_1 == 'Yellow' and color_2 == 'Red' or color_1 == 'Red' and color_2 == 'Yellow':
            print('Orange')
        elif color_1 == 'Yellow' and color_2 == 'Blue' or color_1 == 'Blue' and color_2 == 'Yellow':
            print('Green')
        elif color_1 == 'Red' and color_2 == 'Blue' or color_1 == 'Blue' and color_2 == 'Red':
            print('Violet')
        else:
            print(color_1)
    else:
        print('Error')


main(input(), input())
