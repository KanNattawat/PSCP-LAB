"""pscp"""
def main(day, mon):
    """main"""
    if mon == 1 or mon == 10:
        jan_oct(day)
    elif mon == 2 or mon == 3 or mon == 11:
        feb_mar_nov(day)
    elif mon == 4 or mon == 7:
        apr_jul(day)
    elif mon == 5:
        may(day)
    elif mon == 6:
        june(day)
    elif mon == 8:
        aug(day)
    else:
        sep_dec(day)

def jan_oct(day):
    """jan"""
    dic = {"Sunday": [2, 9, 16, 23, 30], "Monday": [3, 10, 17, 24, 31], "Tuesday": [4, 11, 18, 25]\
, "Wednesday": [5, 12, 19, 26], "Thursday": [6, 13, 20, 27], "Friday": [7, 14, 21, 28]\
, "Saturday":[1, 8, 15, 22, 29]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def feb_mar_nov(day):
    """2"""
    dic = {"Sunday": [6, 13, 20, 27], "Monday": [7, 14, 21, 28], "Tuesday": [1, 8, 15, 22, 29]\
, "Wednesday": [2, 9, 16, 23, 30], "Thursday": [3, 10, 17, 24, 31], "Friday": [4, 11, 18, 25]\
, "Saturday":[5, 12, 19, 26]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def apr_jul(day):
    """3"""
    dic = {"Sunday": [3, 10, 17, 24, 31], "Monday": [4, 11, 18, 25], "Tuesday": [5, 12, 19, 26]\
, "Wednesday": [6, 13, 20, 27], "Thursday": [7, 14, 21, 28], "Friday": [1, 8, 15, 22, 29]\
, "Saturday":[2, 9, 16, 23, 30]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def may(day):
    """4"""
    dic = {"Sunday": [1, 8, 15, 22, 29], "Monday": [2, 9, 16, 23, 30]\
, "Tuesday": [3, 10, 17, 24, 31], "Wednesday": [4, 11, 18, 25]\
, "Thursday": [5, 12, 19, 26], "Friday": [6, 13, 20, 27], "Saturday":[7, 14, 21, 28]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def june(day):
    """5"""
    dic = {"Sunday": [5, 12, 19, 26], "Monday": [6, 13, 20, 27], "Tuesday": [7, 14, 21, 28]\
, "Wednesday": [1, 8, 15, 22, 29], "Thursday": [2, 9, 16, 23, 30], "Friday": [3, 10, 17, 24]\
, "Saturday":[4, 11, 18, 25]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def aug(day):
    """6"""
    dic = {"Sunday": [7, 14, 21, 28], "Monday": [1, 8, 15, 22, 29], "Tuesday": [2, 9, 16, 23, 30]\
, "Wednesday": [3, 10, 17, 24, 31], "Thursday": [4, 11, 18, 25], "Friday": [5, 12, 19, 26]\
, "Saturday":[6, 13, 20, 27]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

def sep_dec(day):
    """7"""
    dic = {"Sunday": [4, 11, 18, 25], "Monday": [5, 12, 19, 26], "Tuesday": [6, 13, 20, 27]\
, "Wednesday": [7, 14, 21, 28], "Thursday": [1, 8, 15, 22, 29], "Friday": [2, 9, 16, 23, 30]\
, "Saturday":[3, 10, 17, 24, 31]}
    if day in dic["Sunday"]:
        print("Sunday")
    elif day in dic["Monday"]:
        print("Monday")
    elif day in dic["Tuesday"]:
        print("Tuesday")
    elif day in dic["Wednesday"]:
        print("Wednesday")
    elif day in dic["Thursday"]:
        print("Thursday")
    elif day in dic["Friday"]:
        print("Friday")
    else:
        print("Saturday")

main(int(input()), int(input()))
