# Import Python's regular expression module.
import re

# Open the COCA lemma list for reading.
# The encoding argument specifies UTF-8 so the file's characters are decoded correctly.
coca_lemmas_read = open("sources/COCA_free_lemmas.txt", encoding = "utf-8")

# Read all lines from the file and store them in a list.
# Each list item represents one line from the file, usually including its newline character.
# And each line represent one English lemma.
coca_lemmas = coca_lemmas_read.readlines()

# Print the first five lemmas in the list to inspect the file contents.
# [:5] selects items from the beginning up to, but not including, index 5.
print(coca_lemmas[:5])

# Define a function that checks whether a regular expression matches a target string.
# regex is the regular expression pattern; target is the string to be searched.
def match_regex(regex, target):
    # Search for the pattern anywhere in the target string.
    # re.search() returns a match object if a match is found, or None otherwise.
    match_res = re.search(regex, target)
    # Return True if there's a match object; otherwise, return False when there is no match.
    return match_res is not None

# Move the file pointer back to the beginning of the file.
# This is necessary because readlines() has already read the entire file.
coca_lemmas_read.seek(0)

# Match strings that begin with "gh".
# ^ represents the beginning of the string.
# Examples: "ghost", "ghastly".

# pattern = "^gh"

# Match strings that end with "gh".
# $ represents the end of the string.
# Examples: "laugh", "rough".

# pattern = "gh$"

# Match strings containing "gh" anywhere.
# No beginning or ending anchor is used.
# Examples: "ghost", "laugh", "night".

# pattern = "gh"

# Match strings containing at least one word character before and after "gh".
# \w matches a word character: a letter, a digit, or an underscore.
# + means one or more occurrences of the preceding element.
# Examples: "nightly", "highway".

# pattern = "\w+gh\w+"

# Match strings that:
# 1. Begin with "tr".
# 2. Have one or more vowels (e, i, a, o, or u).
# 3. Have either "n" or "m" immediately after the vowels.
# 4. End at that point.
# ^ and $ anchor the pattern to the entire string.
# [eiaou] matches any one character in the specified set.
# + allows one or more consecutive vowels.
# [nm] matches either "n" or "m".

# pattern = "^tr[eiaou]+[nm]$"

# Match strings that:
# 1. Begin with "sp".
# 2. Have exactly three characters after "sp".
# 3. End with either "n" or "m".
# . is a wildcard that matches any character except a newline by default.
# {3} means exactly three occurrences of the preceding element (the wildcard .).
# [nm] matches either "n" or "m".

# pattern = "^sp.{3}[nm]$" # Wildcard

# Match strings that:
# 1. Begin with "sp".
# 2. Have between three and five characters after "sp".
# 3. End with either "n" or "m".
# . matches any single character except a newline by default.
# {3,5} means between three and five occurrences of the preceding element.
# [nm] matches either "n" or "m".
# ^ and $ ensure that the entire string follows this pattern.
pattern = "^sp.{3,5}[nm]$"

# Read the file one line at a time.
# The file pointer advances as each line is read.
for word in coca_lemmas_read:
    # Remove leading and trailing whitespace, including the newline character.
    # This ensures that the regular expression is applied to the lemma itself.
    word_clean = word.strip()
    # Check whether the cleaned word matches the selected regular expression.
    # The function returns True if a match is found and False otherwise.
    if match_regex(pattern, word_clean):
        # Print the word only if it matches the pattern.
        print(word_clean)