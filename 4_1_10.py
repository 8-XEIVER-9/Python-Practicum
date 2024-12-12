def merge(tup1, tup2):
    i, j = 0, 0
    ans = []
    while i < len(tup1) and j < len(tup2):
        if tup1[i] < tup2[j]:
            ans.append(tup1[i])
            i += 1
        else:
            ans.append(tup2[j])
            j += 1
    ans.extend(tup1[i:])
    ans.extend(tup2[j:])
    return tuple(ans)
