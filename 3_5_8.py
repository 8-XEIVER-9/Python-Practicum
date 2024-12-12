f1 = input()
f2 = input()
ans = input()

with open(f1, "r", encoding="UTF-8") as first:
    set1 = set([word for word in first.read().split()])

with open(f2, "r", encoding="UTF-8") as second:
    set2 = set([word for word in second.read().split()])
diff = set1 ^ set2

with open(ans, "w", encoding="UTF-8") as ans:
    print("\n".join(sorted(diff)), file=ans)