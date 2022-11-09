"""pscp"""

def main():
    """main"""
    message = input().replace("<", "$<").replace(">", ">$").split("$")
    check = list(filter(lambda x, ok="<": ok not in x, message))
    value = ' '.join(check)
    print(value.split())

main()
