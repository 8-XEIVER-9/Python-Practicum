from itertools import chain, combinations, product

cards = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
nominals = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
card = input()
nominal = input()
prev = input()
nominals.remove(nominal)
table = product(nominals, cards.values())
triplets = combinations(table, 3)
triplets = [triplet for triplet in triplets if cards[card] in list(chain.from_iterable(triplet))]
triplets.sort()
prev_appeared = 0
for triplet in triplets:
    if prev_appeared:
        print(', '.join(f'{nominal} {card}' for nominal, card in triplet))
        break
    if ', '.join(f'{nominal} {card}' for nominal, card in triplet) == prev:
        prev_appeared = 1