keyword = "vampire"
sen1 = "I love vampire!"
sen2 = "Is anyone still watching the Twilight trilogy?"

print(keyword in sen1)
print(keyword in sen2)

dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

for line in dracula_read:
    if keyword in line:
        print(line)

dracula_read.close()