file_name = 'secret.txt'
with open(file_name, encoding='UTF-8') as file:
    data = file.read()
    decoded = ''
    for ch in data:
        code = ord(ch)
        if code >= 128: 
            code = code % 256
        decoded += chr(code)
    print(decoded)
