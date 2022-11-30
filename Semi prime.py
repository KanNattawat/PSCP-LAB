""" pscp """


def is_prime(num):
    """ is_prime """
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def main():
    """ main """
    amount = int(input())
    primes = []
    for num in range(1, amount+1):
        if is_prime(num):
            primes.append(num)
    value = 0
    for i in range(len(primes)):
        prime1 = primes[i]
        for prime2 in primes[i:]:
            if prime1*prime2 <= amount:
                value += 1
    print(value)


main()
