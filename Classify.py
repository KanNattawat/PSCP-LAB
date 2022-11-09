""" pscp """
import json
def main():
    """ main """
    lst_student_id = []
    lst_info = []
    while True:
        student_id = input()
        if student_id == "END":
            break
        lst_student_id.append(student_id)
    for i in lst_student_id:
        lst_info.append({i[0:2]: i[2:4]})
    # lst_info.sort(key=int(.value))
    print(lst_info)

main()
