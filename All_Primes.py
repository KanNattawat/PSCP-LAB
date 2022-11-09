"""pscp"""

def isprime(num):
    """isprime function"""
    con = 0
    if num > 1:
        for i in range(1, num+1):
            if i % i == 0 and i % 1 == 0:
                con += 1
    print(con)

isprime(int(input()))
