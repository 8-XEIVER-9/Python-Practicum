def secret_replace(text, **code):
    new_text = ''
    for char in text:
        if char in code:
            new_text += code[char][0]
            code[char] = code[char][1:] + (code[char][0],)
        else:
            new_text += char
    return new_text