def make_list(length, value=None):
    if value is None:
        return [0] * length
    else:
        return [value] * length