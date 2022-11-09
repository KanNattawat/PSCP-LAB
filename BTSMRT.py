"""pscp"""
def main(day, age, hight):
    """ MAIN """
    if age < 14 and hight < 90:
        print("FREE")
    elif day == 'Children Day' and age < 14 and hight <= 140:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")
main(input(), float(input()), float(input()))
