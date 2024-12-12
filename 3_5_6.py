dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
    'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}
ans = []
with open('cyrillic.txt', "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for line in lines:
        res = ''
        for chr in line:
            chr_copy = chr.upper()
            if chr_copy in dict:
                if chr.isupper():
                    chr = dict[chr_copy].capitalize()
                else:
                    chr = dict[chr_copy].lower()
            res += chr
        ans.append(res)
file.close()
with open('transliteration.txt', "w", encoding="UTF-8") as out:
    out.writelines(ans)
out.close()