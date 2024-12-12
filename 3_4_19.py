from itertools import product
logic = input()
var = {ex for ex in logic.split() if len(ex) == 1}
print(*sorted(var), "F")
s_var = sorted(var)
exec(f'for {", ".join(s_var)} in product([0, 1], repeat={len(var)}):\n   print({", ".join(s_var)}, int(eval(logic)))')