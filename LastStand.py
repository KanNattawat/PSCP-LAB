"""pscp"""
import json

def main(lst):
    """main"""
    lst = json.loads(lst)
    for i in lst:
        i = str(i)
        print(i[-1::])

main(input())
