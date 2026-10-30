# Import Python's regular expression module.
import re

# Define a regular expression pattern to search for "vampire".
pattern = "vampire"

# Search for the exact lowercase word "vampire".
# re.search() returns a match object if a match is found, or None otherwise.
result = re.search(pattern, "I love vampire!")
print(result)

# Search for "vampire" in a sentence with an uppercase "V".
# The search is case-sensitive, so no match is found.
result = re.search(pattern, "I love Vampire!")
print(result)

# Define a pattern that matches either an uppercase or lowercase "V".
pattern = "(V|v)ampire"

# Search for the lowercase form.
result = re.search(pattern, "I love vampire!")
print(result)

# Search for the uppercase form.
result = re.search(pattern, "I love Vampire!")
print(result)

# Add * to allow zero or more occurrences of the letter "s".
# This pattern matches both "vampire" and "vampires", regardless of the initial V's case.
pattern = "(V|v)ampires*"

# Search for the singular form.
result = re.search(pattern, "I love vampire!")
print(result)

# Search for the singular form with an uppercase "V".
result = re.search(pattern, "I love Vampire!")
print(result)

# Search for the plural form "vampires".
result = re.search(pattern, "How many vampires do we have to see in this demo?")
print(result)