dracula_read = open(file = "sources/pg345_2.txt", encoding = "utf-8")

dracula_firstline = dracula_read.readline()

print(dracula_firstline)

dracula_lines = dracula_read.readlines()
print(dracula_lines[:3])

print(dracula_lines[:5])

dracula_read.close()