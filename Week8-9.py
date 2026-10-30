import re

coca_lemmas_read = open("sources/COCA_free_lemmas.txt", encoding = "utf-8")

pattern = "[0-9]"

for word in coca_lemmas_read:
    word_clean = word.strip()
    if re.search(pattern, word_clean) is not None:
        print(word_clean)

coca_lemmas_read.seek(0)

pattern = "\-"

for word in coca_lemmas_read:
    word_clean = word.strip()
    if re.search(pattern, word_clean) is not None:
        print(word_clean)

coca_lemmas_read.close()