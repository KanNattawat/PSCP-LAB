"""FizzBuzz"""
def find_fuzz():
    """beom gun"""
    iii = int(input())
    for _ in range(1, iii+1):
        if _ %5 != 0 and _ %3 != 0:
            print(_)
        elif _ %3 == 0 and _%5 == 0:
            print("FizzBuzz")
        elif _ %3 == 0:
            print("Fizz")
        elif _ %5 == 0:
            print("Buzz")
find_fuzz()
