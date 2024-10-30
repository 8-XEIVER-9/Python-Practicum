from math import gcd
nums = list(set(map(int, input().split("; "))))
ans = {}
for num1 in nums:
    for num2 in nums:
        if gcd(num1, num2) == 1 and num2 != num1:
            if num1 in ans:
                ans[num1].add(num2)
            else:
                ans[num1] = {num2}
            if num2 in ans:
                ans[num2].add(num1)
            else:
                ans[num2] = {num1}
for key in sorted(ans.keys()):
    print(f"{key} - {", ".join(list(map(str, sorted(list(ans[key])))))}")