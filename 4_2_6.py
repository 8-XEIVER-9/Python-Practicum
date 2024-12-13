rec = {
    'Эспрессо': {'coffee': 1},
    'Капучино': {"coffee": 1, "milk": 3},
    'Макиато': {"coffee": 2, "milk": 1},
    'Кофе по-венски': {"coffee": 1, "cream": 2},
    'Латте Макиато': {"coffee": 1, "milk": 2, "cream": 1},
    'Кон Панна': {"coffee": 1, "cream": 1}
}

in_stock = {}


def order(*drinks):
    global in_stock, rec

    for drink in drinks:
        if all(rec[drink][ingredient] <= in_stock[ingredient] for ingredient in rec[drink]):
            for ingredient, amount in rec[drink].items():
                in_stock[ingredient] -= amount
            return drink

    return "К сожалению, не можем предложить Вам напиток"