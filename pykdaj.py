""" fibnal00 """


def main():
    month = int(input())
    cost = float(input())
    max_unit = float(input())
    new_cost = float(input())
    free = float(input())
    lst = []

    for i in range(month):
        unit = float(input())
        if unit > max_unit:
            more = unit - max_unit
            total = max_unit*cost + (more*new_cost)
        else:
            total = unit * cost
        if total <= free:
            total = 0
        else:
            total = total
        lst.append(total)
    print(sum(lst))


main()
