""" PSCP """
def cross(small, big, goal):
    """ input """
    if big * 5 + small < goal or goal // 5 * 5 + small < goal and goal < big * 5:
        print(-1)
    elif goal == small + big * 5:
        print(small)
    else:
        if big * 5 >= goal:
            smalluse = goal % 5
            print(smalluse)
        else:
            smalluse = goal - big * 5
            print(smalluse)
 
 
cross(int(input()), int(input()), int(input()))
