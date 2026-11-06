# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Define a regular expression to identify possible negative passive constructions.
# The "r" prefix creates a raw string, so backslashes such as \s and \w are passed
# directly to the regex engine without being interpreted as Python string escapes.

# To avoid lengthy explanations, copy and paste the regular expression to
# regex101.com for details (or check the Unit 3 handout)
passive_pattern = r"(((am|is|are|was|were)\snot)|(not\s(be|been)))\s\w+ed.*\sby\s"

for line in dracula_read:
    # Search for a sequence matching the passive-pattern structure.
    if re.search(passive_pattern, line) is not None:
        # Print the entire line if a match is found.
        print(line)

# Close the file after both searches are complete.
dracula_read.close()