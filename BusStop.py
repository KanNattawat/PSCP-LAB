""" pscp """

def main():
    """ main """
    capacity = int(input())
    stop = int(input())
    passenger_str = []
    passennger_num = []
    home = 0
    for _ in range(stop):
        bus = input().split()
        passenger_str.append(bus)
    passenger_str.sort(key=lambda i: int(i[0]))
    for i in passenger_str:
        stage_bus_stop = int(i[0])
        if len(passennger_num) != 0:
            passenger_of_list_integer2 = passennger_num.copy()
            for arrive in passennger_num:
                if arrive == stage_bus_stop:
                    passenger_of_list_integer2.remove(arrive)
                    home += 1
            passennger_num = passenger_of_list_integer2
        for j in range(1, len(i)):
            if len(passennger_num) == capacity:
                break
            if stage_bus_stop < int(i[j]):
                passennger_num.append(int(i[j]))
    print(home)

main()
