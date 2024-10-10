n = int(input())
cnt = 0
for _ in range(n):
    line = input()
    if line.find("зайка") != -1:
        print(line.find("зайка") + 1)
    else:
        print("Заек нет =(")