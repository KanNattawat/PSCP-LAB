"""pscp"""

def main(txt):
    """main"""
    new_txt = txt
    symbols = list("""`~!@#$%^&*()_-+={[}|:;"'<,>.?/""")
    for i in symbols:
        new_txt = new_txt.replace(i, "")
    for i in txt:
        if i.isnumeric():
            new_txt = new_txt.replace(i, "")
    lst = new_txt.split(" ")
    for i in lst:
        if len(i) > 6:
            print(i, end=" ")

main(input())
