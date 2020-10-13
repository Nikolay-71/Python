import re
import json

with open("text_7.txt", "r", encoding='utf-8') as f:
    spisok = {}
    aver = {}
    b = []
    for a in f:
        b = a.split(" ")
        nums = re.findall(r'\d+', a)
        nums = [int(a) for a in nums]
        pr = nums[-2] - nums[-1]
        spisok[b[0]] = pr
        spisok2 = {k: v for k, v in spisok.items() if v > 0}
        s = sum(spisok2.values()) / len(spisok2)
        aver["aver"] = s
        b = [spisok, aver]
    print(b)
with open("text_7_7.json", "w", encoding='utf-8') as write_d:
    json.dump(b, write_d)
