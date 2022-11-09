""" FoodGrade I """
def input_first():
    """ main """
    ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12 = infunc_first()
    inans1 = ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8+ch9+ch10+ch11+ch12
    return inans1

def input_second():
    """ main """
    ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23, ch24 = infunc_second()
    inans2 = ch13+ch14+ch15+ch16+ch17+ch18+ch19+ch20+ch21+ch22+ch23+ch24
    return inans2

def infunc_first():
    """ inputfunc """
    ch1 = check(int(input()))
    ch2 = check(int(input()))
    ch3 = check(int(input()))
    ch4 = check(int(input()))
    ch5 = check(int(input()))
    ch6 = check(int(input()))
    ch7 = check(int(input()))
    ch8 = check(int(input()))
    ch9 = check(int(input()))
    ch10 = check(int(input()))
    ch11 = check(int(input()))
    ch12 = check(int(input()))
    return ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12

def infunc_second():
    """ inputfunc """
    ch13 = check(int(input()))
    ch14 = check(int(input()))
    ch15 = check(int(input()))
    ch16 = check(int(input()))
    ch17 = check(int(input()))
    ch18 = check(int(input()))
    ch19 = check(int(input()))
    ch20 = check(int(input()))
    ch21 = check(int(input()))
    ch22 = check(int(input()))
    ch23 = check(int(input()))
    ch24 = check(int(input()))
    return ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23, ch24

def check(chgrams):
    """ checking """
    if 50 <= chgrams <= 70:
        count = int(1)
        return count
    else:
        count = int(0)
        return count

print(input_first() + input_second())
