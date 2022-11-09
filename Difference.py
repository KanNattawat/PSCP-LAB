"""pscp"""

def main(num_n, num_m):
    """main"""
    set_n = set()
    set_m = set()
    for _ in range(num_n):
        set_n.add(int(input()))
    for _ in range(num_m):
        set_m.add(int(input()))
    for i in set_m:
        if i not in set_n:
            continue
        set_n.discard(i)
    set_n = sorted(set_n)
    print(*set_n)

main(int(input()), int(input()))
