""" pscp """
def main(number, count):
    """ main """
    for i in range(1, number+1):
        if check(i):
            count += 1
    print(count)

def check(var_i):
    """ check """
    if var_i % 2 == 0:
        var_i = var_i / 2
    if var_i % 2 == 0:
        return False
    for j in range(3, int(var_i**0.5 + 1)):
        if var_i % j == 0:
            var_i = var_i / j
        if var_i % j == 0:
            return False
    return True
main(int(input()), 0)
