'''PSCP Program'''
def main():
    '''8433-Milk v2 18/11/2022'''
    price_per_bottle, every_x, free = float(input()), int(input()), int(input())
    every_y, free_y, money = int(input()), int(input()), float(input())
    milk = money//price_per_bottle
    bottle_x = milk
    bottle_y = milk
    while bottle_x >= every_x and every_x != 0:
        got_free = (bottle_x // every_x) * free
        milk += got_free
        bottle_x -= (bottle_x // every_x) * every_x
        bottle_x += got_free
    while bottle_y >= every_y and every_y != 0:
        got_free = (bottle_y // every_y) * free_y
        milk += got_free
        bottle_y -= (bottle_y // every_y) * every_y
        bottle_y += got_free
    print(int(milk))

main()
