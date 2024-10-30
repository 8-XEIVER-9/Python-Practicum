friends = {}
while (line := input()):
    fr1, fr2 = line.split()
    if fr1 in friends:
        friends[fr1][0].add(fr2)
    else:
        friends[fr1] = [set([fr2]), set()]
    if fr2 in friends:
        friends[fr2][0].add(fr1)
    else:
        friends[fr2] = [set([fr1]), set()]
for name in sorted(friends.keys()):
    for friend in friends[name][0]:
        n1 = friends[name][1]
        n2 = friends[friend][0]
        n3 = friends[name][0]
        n4 = n2.difference(n3, set([name]))
        friends[name][1] = n1 | n4
for key in sorted(friends):
    print(f"{key}: {", ".join(sorted(friends[key][1]))}")