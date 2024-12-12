import string
file_out = 'private.txt'
alphabet = list(string.ascii_lowercase) 
shift = int(input())
data = open("public.txt", "r", encoding="UTF-8")
line = data.read()
ans = ""
for ch in line:
    if ch.lower() in alphabet:
        if ch.isupper():
            ans += alphabet[(alphabet.index(ch.lower()) + shift) % 26].capitalize()
        else:
            ans += alphabet[(alphabet.index(ch.lower()) + shift) % 26]
    else:
        ans += ch
with open(file_out, 'w', encoding='UTF-8') as file:
    file.write(ans)