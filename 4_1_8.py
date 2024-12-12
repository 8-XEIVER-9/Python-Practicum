def is_palindrome(line):
    if isinstance(line, int):
        line = str(line)
    if isinstance(line, tuple):
        line = list(line)
    return line == line[::-1]
