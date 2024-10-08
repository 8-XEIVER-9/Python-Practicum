def ch_s(n, s):
    ans = ""
    while n > 0:
        ans += str(n % s)
        n //= s
    return ans


n = int(input())
max_length = 0
syst = 0
for i in range(2, 11):
    length = sum(map(int, ch_s(n, i)))
    if length > max_length:
        max_length = length
        syst = i
print(syst)