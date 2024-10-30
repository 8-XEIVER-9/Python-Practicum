
nums = list(map(int, input().split()))
ans = []
for num in nums:
    template = {"digits": 0, "units": 0, "zeros": 0}
    bn = bin(num)[2:]
    template["digits"] += len(bn)
    template["units"] += bn.count("1")
    template["zeros"] += bn.count("0")
    ans.append(template)
print(ans)