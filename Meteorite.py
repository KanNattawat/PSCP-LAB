"""sdfsdf"""
 
def main():
    """sdfsfd"""
    my_a = float(input())
    my_b = int(input())
    my_c = float(input())
    shoot_missle = 0
    enemy = 1
    weight = my_a
 
    while weight >= my_c:
 
        for _ in range(enemy):
            #print(f"enemy = {enemy} i = {i}")
            shoot_missle += 1
            enemy += my_b - 1
 
        weight = my_a/enemy
 
    print(shoot_missle)
 
main()
