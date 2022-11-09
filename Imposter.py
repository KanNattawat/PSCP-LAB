""" pscp """
import json
def main():
    """ main """
    dic_total = {}
    dic_dead = {}
    while True:
        data = input()
        if data == "Start":
            break
        xxx = json.loads(data)
        dic_total.update(xxx)
    while True:
        data = input()
        if data == "End":
            break
        dic_dead[data] = dic_total[data]
        dic_total.pop(data)
    con = list(dic_total.values()).count("Impostor")
    print(con, "Impostor Remains")
    print("***Alive***")
    for key, value in sorted(dic_total.items()):
        print(key, ":", value)
    print("***Dead***")
    for key, value in sorted(dic_dead.items()):
        print(key, ":", value)
main()
