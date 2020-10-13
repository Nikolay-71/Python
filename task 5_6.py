import re

with open("text_6.txt", "r", encoding='utf-8') as f:
    workers = {}
    b = []
    for a in f:
        b = a.split(":")
        nums = re.findall(r'\d+', a)
        nums = [int(a) for a in nums]
        c = sum(nums)
        workers[b[0]] = c
    print(workers)
