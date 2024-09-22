def d2(n):
    if len(n) == 1:
        return "0" + n
    return n


hours = int(input())
minutes = int(input())
minutes_need = int(input())
new_minutes = minutes + minutes_need 
new_hours = (hours + new_minutes // 60) % 24
print(f"{d2(str(new_hours))}:{d2(str(new_minutes % 60))}")