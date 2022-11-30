""" pscp """


def main(evidence_1, evidence_2, evidence_3):
    """ main """
    ghost_evidence_dic = {
        "EMF Level 5": ["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"],
        "Ghost Writing": ["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"],
        "Fingerprints": ["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"],
        "Spirit Box": ["Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"],
        "Freezing Temperatures": ["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"],
        "Ghost Orb": ["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"],
        "No evidence": ["Banshee", "Demon", "Jinn", "Mare", "Oni", \
"Phantom", "Poltergeist", "Revenant", "Shade", "Spirit", "Wraith", "Yurei"]
        }
    ans = set.intersection(set(ghost_evidence_dic[evidence_1]), \
set(ghost_evidence_dic[evidence_2]), set(ghost_evidence_dic[evidence_3]))
    ans = list(ans)
    ans.sort()
    if ans == list():
        print("Not yet discovered")
    else:
        print(*ans, sep="\n")


main(input(), input(), input())
