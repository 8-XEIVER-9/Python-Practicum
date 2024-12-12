prev_lines = []


def modern_print(line):
    if line not in prev_lines:
        print(line)
        prev_lines.append(line)