import re

coca_lemmas_read = open("sources/COCA_free_lemmas.txt", encoding = "utf-8")

coca_lemmas = coca_lemmas_read.readlines()
print(coca_lemmas[:5])

def match_regex(regex, target):
    match_res = re.search(regex, target)
    return match_res is not None

coca_lemmas_read.seek(0)

#pattern = "^gh"
#pattern = "gh$"
#pattern = "gh"
#pattern = "\w+gh\w+"
#pattern = "^tr[eiaou]+[nm]$"
#pattern = "^sp.{3}[nm]$" # Wildcard
pattern = "^sp.{3,5}[nm]$"

for word in coca_lemmas_read:
    word_clean = word.strip()
    # print(word_clean)
    if match_regex(pattern, word_clean):
        print(word_clean)