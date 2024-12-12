ans = []
with open(f"{input()}", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    nums = []
    for line in lines:
        nums += list(map(int, line.rstrip().split()))
    ans.append(str(len(nums)))
    plus_n = 0
    for num in nums:
        if num > 0:
            plus_n += 1
    ans.append(str(plus_n))
    ans.append(str(min(nums)))
    ans.append(str(max(nums)))
    ans.append(str(sum(nums)))
    ans.append(f"{(sum(nums) / int(ans[0])):.2f}")
    print("\n".join(ans))