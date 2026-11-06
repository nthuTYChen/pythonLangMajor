# Import the built-in re package
import re

# Read the lemma list
coca_lemmas_read = open("sources/COCA_free_lemmas.txt")

# Define a function called search_lemmas, which takes one argument "regex"
def search_lemmas(regex):
    # Iterate through each line in coca_lemmas_read, which is just an
    # English lemma
    for lemma in coca_lemmas_read:
        # Strip off extra redundant characters so each string has just the
        # English spelling
        lemma_clean = lemma.strip()
        # Search if there's a match between whatever is in "regex" and "lemma_clean"
        if re.search(regex, lemma_clean) is not None:
            # Print every match
            print(lemma_clean)

# Function call 1: ^ = the beginning of a string, \w = any letter, "le" = just "le"
search_lemmas("^\wle")

# Reset the reader between function calls
coca_lemmas_read.seek(0)

# Function call 3: "ears" = just "ears"
search_lemmas("ears")

# Close the file reader
coca_lemmas_read.close()