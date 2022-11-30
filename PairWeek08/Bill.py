"""pscp"""
def main(num):
    """bill"""
    service = num*(10/100)
    if service < 50:
        service = 50
        ans = (num + service + ((service + num)*(7/100)))
        print("%.2f" %ans)
    elif 50 <= service <= 1000:
        ans = (num + service + ((service + num)*7/100))
        print("%.2f" %ans)
    else:
        service = 1000
        ans = (num + service + ((service + num)*7/100))
        print("%.2f" %ans)
main(int(input()))
