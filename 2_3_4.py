start = int(input())
end = int(input())
ans = [i for i in range(min(start, end), max(start, end) + 1)]
if start > end:
    print(*ans[::-1])
else:
    print(*ans)