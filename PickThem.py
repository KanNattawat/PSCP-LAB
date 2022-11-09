"""pscp"""
import json
def main(lst):
    """main"""
    con = True
    lst = json.loads(lst)
    for i in lst:
        if i % 2 == 0:
            print(i)
            con = False
    if con:
        print("Nope")

main(input())
