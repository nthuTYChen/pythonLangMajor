dracula_read = open("sources/pg345_2_clean.txt", encoding = "utf-8")

for line in dracula_read:
    print(line)

dracula_read.seek(0)

print("###########")

for line in dracula_read:
    print(line)

dracula_read.close()