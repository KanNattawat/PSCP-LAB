"""Pad Thai"""


def main():
    """Pad Thai"""
    food = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
            "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]

    taste = ["Sweet", "Sour", "Salty"]
    lst_not_food = []
    lst_food = []
    lst_taste = []

    while 1:
        wear = input()
        if wear == "Cook":
            break
        elif wear not in food:
            lst_not_food.append(wear)
            continue
        lst_food.append(wear)
    while 1:
        wear = input()
        if wear == "End":
            break
        lst_taste.append(wear)

    if lst_not_food != []:
        print("This is not Pad Thai!!!")
    elif set(lst_food) != set(food):
        print("This is bad!")
    elif set(lst_taste) != set(taste):
        print("Not Bad...")
    else:
        print("Delicious!")


main()
