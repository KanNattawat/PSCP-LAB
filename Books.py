"""pscp"""
def main(book, page, numx, numy):
    """main"""
    while book > 0:
        for i in range(page):
            read = (numx+i) / (numy+i)
        book -= 1
main(int(input()), int(input()), int(input()), int(input()))