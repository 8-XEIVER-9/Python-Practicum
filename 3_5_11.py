import json
ans = {
    "count": 0,
    "positive_count": 0,
    "min": 0,
    "max": 0,
    "sum": 0,
    "average": 0
}
fin = input()
fout = input()
with open(fin, "r", encoding="UTF-8") as file:
    lines = file.readlines()
    nums = []
    for line in lines:
        nums += list(map(int, line.rstrip().split()))
    ans["count"] = len(nums)
    plus_n = 0
    for num in nums:
        if num > 0:
            plus_n += 1
    ans["positive_count"] = plus_n
    ans["min"] = min(nums)
    ans["max"] = max(nums)
    ans["sum"] = sum(nums)
    ans["average"] = round((sum(nums) / len(nums)), 2)

with open(fout, "w", encoding="UTF-8") as stat:
    json.dump(ans, stat, indent=2)