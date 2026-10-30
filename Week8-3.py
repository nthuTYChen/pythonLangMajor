str = "I love Python."

print(str.startswith("I"))

print(str.startswith("love"))

def isBoundaryMarker(line):
    startWithStars = line.startswith("***")
    return startWithStars

dracula_read = open(file = "sources/pg345_2.txt", encoding = "utf-8")

for line in dracula_read:
    if isBoundaryMarker(line):
        print(line)
        break

dracula_write = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8", mode = "w")

for line in dracula_read:
    if isBoundaryMarker(line):
        break
    dracula_write.write(line)

dracula_read.close()
dracula_write.close()