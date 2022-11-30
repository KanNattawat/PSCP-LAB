""" pscp """
import hashlib


def main():
    """ main """
    encrypted = input()
    for number in range(0, 100000):
        value = str("%05d" % (number))
        hashing = hashlib.sha512(value.encode())
        if str(hashing.hexdigest()).upper() == encrypted:
            print("%05d" % (number))


main()
