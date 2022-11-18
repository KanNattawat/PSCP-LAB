""" pscp """


def main(num_x, num_y, num_a, num_z):
    """ main """
    can_use = num_z // num_x
    cant_use = num_z % num_x
    if num_z % num_x == 0:
        ans = num_a * (num_y*can_use)
    else:
        ans = num_a * (num_y*can_use+cant_use)
    print(ans)

main(int(input()), int(input()), int(input()), int(input()))
