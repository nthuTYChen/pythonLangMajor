# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

passive_pattern = r"(am|is|are|was|were|be|been)\s\w+ed.*\sby\s(.+?)[,\.$]"

for line in dracula_read:
    search_res = re.search(passive_pattern, line)
    if search_res is not None:
        print(search_res.group(2))

# Close the file after both searches are complete.
dracula_read.close()