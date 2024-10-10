from math import ceil
timetable = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
ans = []
n = int(input())
new_n = ceil(n / 5)
for _ in range(new_n):
    ans += timetable
for i in range(n):
    print(ans[i])