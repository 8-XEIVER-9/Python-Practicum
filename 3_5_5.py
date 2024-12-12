from sys import stdin


def is_pal(word):
    return word == word[::-1]


words = []
for line in stdin:
    words += line.rstrip().split()
ans = []
for word in words:
    if is_pal(word.lower()) and word not in ans:
        ans.append(word)
ans.sort()
print("\n".join(ans))