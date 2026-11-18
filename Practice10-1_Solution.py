# This script loads pg345_2_clean.txt from your "sources" folder and try to complete
# the following tasks.

# 1. Create an empty set to collect all unique target words.
# 2. Create a regular expression that matches "Dracula" anywhere in each line,
#    which is followed by a space, one or more letters/digits, another space, and then
#    one or more letters/digits. It aims to isolate the next two words that follows
#    "Dracula" (i.e., dracula_words_pattern).
# 3. When iterating through the full Dracula text line by line in a for loop.
# 3a. In this for loop, replace all punctuation marks with an empty string, so that all
#     punctuation marks are removed.
# 3b. Turn each line string into lower case using lower(), so same words that simply differ in case
#     can be processed as the same word type.
# 3c. Match the "dracula_words_pattern" to each clean, lower-case line string, using re.search().
#     The parameter "flags = re.IGNORECASE" tells the matching process to ignore case differences
#     so that "Dracula" and "dracula" are made equivalent in the process.
# 3d. Check if there is any match.
# 3e. If there is, check whether the first and the second string groups (the first and second word next to
#     "Dracula" anywhere in the line) are stop words.
# 3f. If a string group is not a stop word, add the string group as a unique word to the
#     "dracula_words" set.
# 4. Print the sorted list of unique words from the "dracula_words" set.

import re

dracula_words = set()
# Issue 1: In the practice, the second group is not properly marked with ().
dracula_words_pattern = r"Dracula\s(\w+)\s(\w+)"
puncs_pattern = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"
stop_words = ["a", "an", "the",
    "and", "or", "but",
    "is", "are", "was", "were", "be", "been",
    "to", "of", "in", "on", "at", "for", "from", "with",
    "this", "that", "these", "those",
    "i", "you", "he", "she", "it", "we", "they",
    "my", "your", "his", "her", "its", "our", "their",
    "as", "by", "if", "not", "so"]

# Issue 2: The filename misses "n", so the file is not found.
dracula_reader = open("sources/pg345_2_clean.txt", encoding = "utf-8")

for line in dracula_reader:
    # Issue 3: In the practice, Step 3a is not implemented at all.
    line_no_puncs = re.sub(puncs_pattern, "", line)
    line_lower = line_no_puncs.lower()
    search_res = re.search(dracula_words_pattern, line_lower, flags = re.IGNORECASE)
    # Issue 4: In the practice, this if condition is True when there is NO MATCH, which contradicts
    # 3d and 3e.
    if search_res is not None:
        if search_res.group(1) not in stop_words:
            dracula_words.add(search_res.group(1))
        # Issue 5(?): In the regular expression "dracula_words_pattern", the second group
        # is not marked properly, so searching for the second group from the search result
        # is problematic. If you fixed Issue 1, you would not have to make any change here.
        if search_res.group(2) not in stop_words:
            dracula_words.add(search_res.group(2))

print(sorted(dracula_words))

# The intended output: ['become', 'blood', 'bought', 'could'...