# Import Python's regular expression module.
import re

# Open the COCA lemma list for reading using UTF-8 encoding.
coca_lemmas_read = open("sources/COCA_free_lemmas.txt", encoding = "utf-8")

# Define a regular expression pattern that matches any digit from 0 to 9.
# [0-9] is a character class: it matches exactly one digit.
# Here, - is treated a special character that represents a range
pattern = "[0-9]"

# Read the file one line at a time.
for word in coca_lemmas_read:
    # Remove leading and trailing whitespace, including the newline character.
    word_clean = word.strip()
    # Search for at least one digit in the current word.
    # re.search() returns a match object if a match is found, or None otherwise.
    if re.search(pattern, word_clean) is not None:
        # Print the word if it contains at least one digit.
        print(word_clean)

# Move the file pointer back to the beginning of the file.
# This allows the file to be read again from the first line.
coca_lemmas_read.seek(0)

# Define a regular expression pattern to match a hyphen for compound words like "far-fetching".
# \- uses a backslash to escape the hyphen from its special function that repesents a range
# in a regular expression.
# Outside a character class [...], a hyphen is normally literal,
# so escaping it here is unnecessary; "-" would work as well.
# But this is an example used to bring escaping to your attention.
pattern = "\-"

# Read the file again, one line at a time.
for word in coca_lemmas_read:
    # Remove leading and trailing whitespace, including the newline character.
    word_clean = word.strip()
    # Search for a hyphen in the current word.
    if re.search(pattern, word_clean) is not None:
        # Print the word if it contains a hyphen.
        print(word_clean)

# Close the file after both searches are complete.
coca_lemmas_read.close()