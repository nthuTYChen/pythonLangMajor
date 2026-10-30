# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Define a regular expression pattern to search for "Count Dracula"
# followed by either a comma or a period.
# [,.] is a character class that matches either a comma or a period.
# \. escapes the period because an unescaped period is a wildcard in regex.
pattern = "Count Dracula[,\.]"

# Read the file one line at a time.
for line in dracula_read:
    # Search for the pattern anywhere in the current line.
    # re.search() returns a match object if a match is found, or None otherwise.
    if re.search(pattern, line) is not None:
        # Print the entire line if the pattern is found.
        print(line)

# Move the file pointer back to the beginning of the file.
# This allows the file to be read again from the first line.
dracula_read.seek(0)

# Define a regular expression pattern to identify possible passive constructions.
# (am|is|are|was|were|be|been) matches one of these forms of "be".
# \s matches one whitespace character.
# \w+ matches one or more word characters (letters, digits, or underscores).
# ed matches the literal letters "ed".
# .* matches zero or more characters (except newlines by default).
# \sby\s matches "by" with whitespace on both sides.
passive_pattern = "(am|is|are|was|were|be|been)\s\w+ed.*\sby\s"

# Read the file again, one line at a time.
for line in dracula_read:
    # Search for a sequence matching the passive-pattern structure.
    if re.search(passive_pattern, line) is not None:
        # Print the entire line if a match is found.
        print(line)

# Close the file after both searches are complete.
dracula_read.close()