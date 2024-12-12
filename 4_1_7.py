def can_eat(hor, fig):
    hor_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    dx = fig[0] - hor[0]
    dy = fig[1] - hor[1]
    return (dx, dy) in hor_moves
