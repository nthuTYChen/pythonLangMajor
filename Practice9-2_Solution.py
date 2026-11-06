# Import Python's regular expression module.
import re

# Open the cleaned Dracula text file for reading using UTF-8 encoding.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Read the file one line at a time.
for line in dracula_read:

    # Search for a pattern consisting of:
    # 1. A comma or period.
    # 2. A whitespace character.
    # 3. One or more word characters (captured as Group 1).
    # 4. A whitespace character.
    # 5. One of the forms "am", "is", "are", or "were" (captured as Group 2).
    # The ? in \w+? makes the match non-greedy (it matches as few characters as possible).
    match_res = re.search("[,\.]\s(\w+?)\s(am|is|are|were)", line)

    # Check whether the regular expression found a match.
    if match_res is not None:

        # Extract and print Group 1: the word between the punctuation and the form of "be".
        # Group 2 (the form of "be") is not printed.
        print(match_res.group(1))
        # The last three outputs should be "We", "there", and "There".

# Close the file after searching.
dracula_read.close()