# Import Python's regular expression module.
import re

# Create a list containing three example sentences.
svo_sens = ["I love Python", "you like phonology", "Mike hates linguistics"]

# Define a regular expression pattern to match a word surrounded by whitespace.
# \s matches one whitespace character (e.g., a space or tab).
# \w+ matches one or more word characters (letters, digits, or underscores).
# The first and last \s require whitespace before and after the word.
pattern1 = r"\s\w+\s"

# Go through the sentences one at a time.
for sen in svo_sens:

    # Search for a sequence matching pattern1 anywhere in the sentence.
    # re.search() returns a match object if a match is found, or None otherwise.
    search_res = re.search(pattern1, sen)

    # Check whether a match was found.
    if search_res is not None:

        # Print the entire sentence if it contains a matching sequence.
        print(sen)

# Define a second pattern with parentheses around the word.
# \s matches one whitespace character before and after the word.
# (\w+) captures one or more word characters as Group 1.
# The parentheses allow the matched word to be retrieved separately.
pattern2 = r"\s(\w+)\s"

# Go through the sentences one at a time.
for sen in svo_sens:

    # Search for a sequence matching pattern2 in the current sentence.
    search_res = re.search(pattern2, sen)

    # Check whether a match was found.
    if search_res is not None:

        # Extract and print Group 1, which contains the word between the spaces.
        print(search_res.group(1))