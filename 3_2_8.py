lt_por = {}
n = int(input())
for _ in range(n):
    l_d = input().split()
    name = l_d[0]
    for i in range(1, len(l_d)):
        if l_d[i] not in lt_por:
            lt_por[l_d[i]] = [name]
        else:
            lt_por[l_d[i]].append(name)
porridge = input()
if porridge in lt_por:
    print("\n".join(sorted(lt_por[porridge])))
else:
    print("Таких нет")