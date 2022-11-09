""" pscp """
import math


def main(temp):
    """ main """
    temp = math.floor(temp)
    if temp in range(36, 38):
        print("No Fever")
    elif temp in range(38, 39):
        print("Mild Fever")
    elif temp in range(39, 40):
        print("High Fever")
    else:
        print("Very High Fever")


main(float(input()))
