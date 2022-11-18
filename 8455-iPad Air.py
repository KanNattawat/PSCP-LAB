'''PSCP Program'''
def main():
    '''8455-iPad Air 18/11/2022'''
    colors, storage = ('Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue'), ('64', '256')
    conectivity, pricing = ('Wi-Fi', 'Wi-Fi + Cellular'), ((19900, 24900), (24400, 29400))
    choice = [input() for _ in range(3)]
    try:
        print(pricing[conectivity.index(choice[2])][storage.index(choice[1])]
              if choice[0] in colors else 'Not Available')
    except (ValueError, IndexError) as _:
        print('Not Available')
main()
