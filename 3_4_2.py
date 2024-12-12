n1 = input().replace(" ", "").split(",")
n2 = input().replace(" ", "").split(",")
for first, second in zip(n1, n2):
    print(f"{first} - {second}")