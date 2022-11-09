""" PSCP """
def input_():
    """ SurprisingVote """
    total = float(input())
    h_score = float(input())
    left = (total - h_score) / 2 + 2
    if h_score < left:
        print("Not surprising")
    else:
        print("Surprising")
input_()
