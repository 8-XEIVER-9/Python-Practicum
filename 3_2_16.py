ans = set()
while (line := input()):
    lt = line.split()
    if "зайка" in lt and len(lt) > 1:
        for i in range(len(lt)):
            if lt[i] == "зайка":
                if i == 0:
                    ans.add(lt[i + 1])
                elif i == len(lt) - 1:
                    ans.add(lt[len(lt) - 2])
                else:
                    ans.add(lt[i + 1])
                    ans.add(lt[i - 1])
    else:           
        continue
print("\n".join(ans))    