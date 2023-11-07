import re
title_body_dict = {}
for num in range(22):
    file = f"reut2-{num:03d}.sgm"
    with open(file=file, mode="r") as f:
        s = f.read()
    value = re.findall("<BODY>(.*?)</BODY>", s, re.S)
    key = re.findall("<TITLE>(.*)</TITLE>", s)
    for i in range(len(key)):
        title_body_dict[key[i]] = value[i]

all_articles = ""

for i in title_body_dict.keys():
    all_articles += title_body_dict[i]

all_words = all_articles.split()
unique_words = set(all_words)

with open("dict.txt", "w") as f:
    f.write(str(title_body_dict))

with open("list_of_words.txt", "w") as f:
    f.write(str(all_words))

with open("unique_list_of_words.txt", "w") as f:
    f.write(str(unique_words))