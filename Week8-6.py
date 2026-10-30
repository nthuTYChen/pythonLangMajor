keyword_sg = "vampire"
keyword_pl = "vampires"

dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

for line in dracula_read:
    if keyword_sg in line or keyword_pl in line:
        print(line)

dracula_read.close()