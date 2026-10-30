import re

dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

pattern = "Count Dracula[,\.]"

for line in dracula_read:
    if re.search(pattern, line) is not None:
        print(line)

dracula_read.seek(0)

passive_pattern = "(am|is|are|was|were|be|been)\s\w+ed.*\sby\s"

for line in dracula_read:
    if re.search(passive_pattern, line) is not None:
        print(line)

dracula_read.close()