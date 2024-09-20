print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!")
print("Как дела?")
status = input()
if status[0] == "х":
    print("Я за вас рада!")
else:
    print("Всё наладится!")