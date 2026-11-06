# Import the built-in re package
import re

# Read the lemma list
coca_lemmas_read = open("sources/COCA_free_lemmas.txt")

# Pattern 1: "s" at the end of a string ($) preceded by any four letters (\w{4})
# following the beginning of a string (^)
pattern1 = "^\w{4}s$"
# Pattern 2: "our" preceded by a string onset (^) plus one any letters (\w) and followed by
# any two letters (\w{2}) and the end of the string ($)
pattern2 = "^\wour\w{2}$"
# Pattern 3: "spr" in anywhere in a string
pattern3 = "ing"

# Iterating through the lemma list
for lemma in coca_lemmas_read:
    # Strip off redundant spaces from the beginning and the end of a string
    lemma_clean = lemma.strip()
    # Check if a regular expression pattern has a match in each lemma
    # (i.e., the search result is not None)
    if re.search(pattern1, lemma) is not None:
        # Print each lemma with a match
        print(lemma_clean)
        # Sample outputs: basis, yours, bless, jeans...

# Reset the reader seeker back to the beginning of the file, so we can
# iterate through the lemma list again.
coca_lemmas_read.seek(0)

# Print a separation line
print("-" * 20)

# Same loop with a different pattern
for lemma in coca_lemmas_read:
    lemma_clean = lemma.strip()
    if re.search(pattern2, lemma) is not None:
        print(lemma_clean)
        # The only match is "course"

# Same resetting process
coca_lemmas_read.seek(0)

# Print a separation line
print("-" * 20)

# Same loop with a different pattern
for lemma in coca_lemmas_read:
    lemma_clean = lemma.strip()
    if re.search(pattern3, lemma) is not None:
        print(lemma_clean)
        # Sample output: anything, fingernail, mingle...

# Don't forget to close the reader!
coca_lemmas_read.close()