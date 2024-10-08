def lines(n):
    n1 = 0
    k = 1
    cnt = 0
    while n1 < n:
        n1 += k
        k += 1
        cnt += 1
    return cnt, n1 - n


def max_length(n):
    max_length = 0
    for i in range(len(n)):
        length = 0
        for j in range(len(n[i])):
            length += len(str(n[i][j]))
        length += len(n[i]) - 1
        if length > max_length:
            max_length = length
    return max_length


n = int(input())
n_lines, dif = lines(n)
cnt_nm = 1
nm = 1
matrix = [[] for i in range(n_lines)]
for i in range(n_lines):
    for j in range(cnt_nm):
        if nm > n:
            break
        matrix[i].append(nm)
        nm += 1
    cnt_nm += 1
wth = max_length(matrix)
for i in range(n_lines):
    ans = ""
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[i][-1]:
            ans += str(matrix[i][j]) + " "
        else:
            ans += str(matrix[i][j])
    print(f"{ans:^{wth}}")