""" pscp """


def main():
    """ main """
    student_lst = []
    pre_year = 0
    while True:
        student_info = input()
        if student_info == "END":
            break
        student_lst.append(student_info[:4])
    for i in sorted(set(student_lst)):
        year = i[:2]
        if pre_year != year:
            print(year, int(i[2:4]), student_lst.count(i))
        else:
            print("--", int(i[2:4]), student_lst.count(i))
        pre_year = year


main()
