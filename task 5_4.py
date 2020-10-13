from translate import Translator

with open("text_4_1.txt", "r", encoding='utf-8') as f:
    b = []
    translator = Translator(from_lang="english", to_lang="russian")
    for a in f:
        name, figure = a.split("-")
        translation = translator.translate(name)
        b.append(translation + " - " + figure)
    print(b)
    with open("text_4_2.txt", "w", encoding='utf-8') as c:
        c.writelines(b)
