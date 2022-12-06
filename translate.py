def normalize(transliteration):
    cyrillic_ua = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    latin = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f",
             "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    latter_dict = {}
    for c, l in zip(cyrillic_ua, latin):
        latter_dict[ord(c)] = l
        latter_dict[ord(c.upper())] = l.upper()

    translated = transliteration.translate(latter_dict)
    word_check = (f"")
    for char in translated:
        if char.isdigit() or char.isalpha():
            word_check += char
        else:
            word_check += "_"

    return word_check


print(normalize("олени"))
