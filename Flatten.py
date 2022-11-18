""" pscp """
import json

def main(nested_list):
    """ main """
    lst = []
    for i in nested_list:
        if isinstance(i, list):
            lst += main(i)
        else:
            lst.append(i)
    lst.sort(reverse=True)
    return lst

print(main(json.loads(input())))
