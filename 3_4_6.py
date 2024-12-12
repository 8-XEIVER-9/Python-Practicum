from itertools import product

cards = ["пик", "треф", "бубен", "червей"]
cards.remove(input())
nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
for nominal, card in product(nominals, cards):
    print(nominal, card)