"""pscp"""
def main():
    """main"""
    menu = []
    while True:
        course = input()
        if course == "DONE":
            break
        elif course == "CLOSED":
            return print("Full Course: [] Reversed: []")
        elif course == "SOMETHING'S WRONG":
            menu.clear()
            continue
        elif course[0:10:] == "Can't do: ":
            menu.remove(course[10::])
        else:
            text = course.split(" #")
            if text[1].isnumeric():
                menu.insert(int(text[1])-1, text[0])
            else:
                menu.append(text[0])
    print("Full Course: " + str(menu), end=" ")
    menu.reverse()
    print("Reversed: " + str(menu))

main()

# """pscp"""

# def main():
#     """main"""
#     lst = []
#     lst_n = []
#     preloca = ""
#     while True:
#         menu = input()
#         if menu[-1] == "N":
#             lst_n.append(menu[0:-3])
#             continue
#         if menu[0:9] == "Can't do:":
#             lst.pop(lst.index(menu[10:]))
#             continue
#         if menu == "DONE" or menu == "CLOSED":
#             if menu == "CLOSED":
#                 print("Full Course: [] Reversed: []")
#                 return
#             break
#         if menu == "SOMETHING'S WRONG":
#             lst.clear()
#             lst_n.clear()
#             continue
#         lst.append(menu[0:-3])
#         if menu[-1] == preloca:
#             lst[-1], lst[-2] = lst[-2], lst[-1]
#         preloca = menu[-1]
#     lst.extend(lst_n)
#     print("Full Course:", lst, end=" ")
#     lst.reverse()
#     print("Reversed:", lst)

# main()
