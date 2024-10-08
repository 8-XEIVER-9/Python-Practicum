hash_first = 0
answer = -1
n = int(input())
for i in range(n):
    b_n = int(input())
    h_n = b_n % 256
    r_n = (b_n // 256) % 256
    m_n = b_n // 256 ** 2
    check_h = (37 * (m_n + r_n + hash_first)) % 256
    if check_h != h_n or check_h > 100:
        answer = i
        break
    hash_first = check_h
print(answer)