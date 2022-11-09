"""pscp"""
def main(can1, prins, can2, finger):
    """pringles"""
    deep = len(prins)-1
    picked = (prins[:finger]).count(")")
    if not prins.count(")"):
        print(picked, "None.", can1, prins, can2, sep="\n")
    elif finger >= deep:
        print(picked, "None.", can1, (" "*finger)+"|", can2, sep="\n")
    else:
        print(picked, "There are still some left.", can1, \
(" "*finger)+(prins[finger:]), can2, sep="\n")
main(input(), input(), input(), int(input()))
