""" pscp """
def main(item_locate):
    """ main """
    pre = 0
    ans = 0
    item_locate = item_locate.split(' ')
    for i in item_locate:
        i = int(i)
        if i > pre:
            ans += i
        pre = i
    print(ans)
main(input())
