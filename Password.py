""" pscp """
import hashlib


def main(password):
    """ main """
    ans = hashlib.sha512(password.encode())
    print((ans.hexdigest()).upper())


main(input())
