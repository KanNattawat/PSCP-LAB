""" pscp """


def gcd_euclidean_recursion(num1, num2):
    """ main """
    if num2 == 0:  # base case
        return num1
    else:
        # different arguments
        return gcd_euclidean_recursion(num2, num1 % num2)


print(gcd_euclidean_recursion(int(input()), int(input())))
