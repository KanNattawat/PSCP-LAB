""" pscp """
def main(loca_a, loca_b, loca_c):
    """ main """
    print(max(loca_b - loca_a, loca_c - loca_b) - 1)
main(int(input()), int(input()), int(input()))
