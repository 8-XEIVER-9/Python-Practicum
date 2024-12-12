from itertools import chain, permutations, product

cards = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
nominals = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
card = input()
nominal = input()
nominals.remove(nominal)
table = product(nominals, cards.values())
triplets = permutations(table, 3)
triplets = [triplet for triplet in triplets if cards[card] in chain.from_iterable(triplet)]
sorted_combinations = sorted(triplets)
for combination in sorted_combinations[:10]:
    print(', '.join(f'{nominal} {card}' for nominal, card in combination))