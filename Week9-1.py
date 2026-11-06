# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

passive_pattern = r"(((am|is|are|was|were)\snot)|(not\s(be|been)))\s\w+ed.*\sby\s"

for line in dracula_read:
    # Search for a sequence matching the passive-pattern structure.
    if re.search(passive_pattern, line) is not None:
        # Print the entire line if a match is found.
        print(line)

# Close the file after both searches are complete.
dracula_read.close()