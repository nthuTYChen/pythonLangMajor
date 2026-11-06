# Import Python's regular expression module.
import re

# Define a sample string.
sample_str = "treatment"

# Define a regular expression pattern using a greedy quantifier.
# t matches the letter "t" literally.
# (\w+) captures one or more word characters (letters, digits, or underscores).
# The final t matches another literal "t".
# By default, + (and *) is greedy: it matches as many characters as possible
# while still allowing the entire pattern to match.
pattern1 = r"t(\w+)t"

# Search for the pattern in the sample string.
search_res = re.search(pattern1, sample_str)

# Print Group 1, which contains the characters between the two matched "t"s.
print(search_res.group(1))

# Define a second pattern using a non-greedy quantifier.
# t matches the letter "t" literally.
# (\w+?) captures one or more word characters, but as few as possible.
# The final t matches the next "t" that allows the pattern to match.
pattern2 = r"t(\w+?)t"

# Search for the second pattern in the sample string.
search_res = re.search(pattern2, sample_str)

# Print Group 1, which contains the shortest possible sequence
# of word characters between the two matched "t"s.
print(search_res.group(1))