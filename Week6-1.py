# Dictionary

# Create an empty dictionary named new_dict using {}
# A dictionary stores data as key-value pairs
# This dictionary currently contains no items
new_dict = {}

# Create a dictionary named lex_pos to store words and their parts of speech
# Each key is a word, and its corresponding value is its part-of-speech label
# Each key and its value are separated by a colon
# For example, "love" is initially labeled as "verb"
lex_pos = {"love": "verb", "cake": "noun", "of": "prep"}

# Access the value associated with the key "love" (as a string) and print it
# The current value of lex_pos["love"] is "verb"
print(lex_pos["love"])

# Access the value associated with the key "cake" and print it
# The current value of lex_pos["cake"] is "noun"
print(lex_pos["cake"])

# A dictionary object is mutable, so you can modify its content.
# Update the value associated with the existing key "love"
# Change its part-of-speech label from "verb" to "noun"
# Assigning a new value to an existing key replaces its previous value
lex_pos["love"] = "noun"

# Access the updated value associated with the key "love" and print it
# The output is now "noun", rather than "verb"
print(lex_pos["love"])

# Add a new key-value pair to the dictionary
# The new key is "great", and its value is "adj", an abbreviation for "adjective"
# If a key does not already exist, assigning a value to it adds a new item
lex_pos["great"] = "adj"

# Access the value associated with the newly added key "great" and print it
# The output is "adj"
print(lex_pos["great"])

# Update the value associated with the existing key "great"
# Replace the abbreviated label "adj" with the full word "adjective"
# This changes the value of an existing item; it does not create another key
lex_pos["great"] = "adjective"

# Print the entire lex_pos dictionary again
# The value associated with "great" is now "adjective"
# The other key-value pairs remain unchanged
print(lex_pos)

# Create a dictionary named like_def to store information about the word "like"
# Each key identifies a type of information, and each value stores that information
# Each key-value pair occupies one line simply for increasing code readability.
# This variable declaration is still done in ONE statement.
like_def = {
    # Store the spelling of the word as a string
    "spelling": "like",

    # Store a simplified pronunciation representation as a string
    # "IPA" is the key used to identify the pronunciation information
    "IPA": "laik",

    # Store a brief definition of the word as a string
    "meaning": "to enjoy something",

    # The value of a key need not be one string or not.
    # It can be any object, just like this list with three synonym strings
    "synonyms": ["admire", "appreciate", "love"]
}

# Retrieve the list associated with the key "synonyms"
# Store a reference to that list in the variable like_syn
# The value of like_syn is a list, not a string or a dictionary
like_syn = like_def["synonyms"]

# Print the resulting type object, which is <class 'list'>
print(type(like_syn))

# Access the first item in the like_syn list using index 0
# Python list indexing starts at 0, so like_syn[0] is "admire"
# Print the first synonym
print(like_syn[0])

# Access the second item in the like_syn list using index 1
# like_syn[1] is "appreciate"
# Print the second synonym
print(like_syn[1])