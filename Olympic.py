""" pscp """

def main(cnt_input):
    """ main """
    lst_country = []
    dic_gold = {}
    dic_silver = {}
    dic_bronze = {}
    dic_total = {}
    for _ in range(cnt_input):
        stats = input()
        lst_country.append(stats[0:3])
        dic_gold.update({stats[0:3]:int(stats[4])})
        dic_silver.update({stats[0:3]:int(stats[6])})
        dic_bronze.update({stats[0:3]:int(stats[8])})
        dic_total.update({stats[0:3]:int(stats[4])+int(stats[6])+int(stats[8])})

main(int(input()))
