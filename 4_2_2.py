def make_matrix(size, value=0):
    if isinstance(size, int):
        width, height = size, size
    else:
        width, height = size
    return [[value for _ in range(width)] for _ in range(height)]
