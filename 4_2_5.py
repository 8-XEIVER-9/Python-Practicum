def to_string(*args, sep=" ", end="\n"):
    strings = list(map(str, args))
    return sep.join(strings) + end