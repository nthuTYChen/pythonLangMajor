# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Define a regular expression to identify possible passive constructions
# and capture the potential subject (the noun phrase following "by").
# (am|is|are|was|were|be|been) matches one of the listed forms of "be".
# \s matches one whitespace character.
# \w+ed matches one or more word characters followed by the letters "ed".
# .* matches zero or more characters (except newlines by default).
# \sby\s matches "by" with whitespace on both sides.
# (.+?) captures one or more characters as Group 2, using non-greedy matching.
# This aims to capture the potential subject after "by", stopping at the
# first comma, period, or dollar sign that allows the pattern to match.
# [,.$] matches one character from the set: comma, period, or dollar sign.
passive_pattern = r"(am|is|are|was|were|be|been)\s\w+ed.*\sby\s(.+?)[,\.$]"

# Read the file one line at a time.
for line in dracula_read:

    # Search for the passive pattern in the current line.
    # re.search() returns a match object if a match is found, or None otherwise.
    search_res = re.search(passive_pattern, line)

    # Check whether a possible passive construction was found.
    if search_res is not None:

        # Extract and print Group 2: the potential subject following "by".
        # Group 1 contains the form of "be" matched at the beginning of the pattern.
        print(search_res.group(2))

# Close the file after searching.
dracula_read.close()