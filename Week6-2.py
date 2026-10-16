# Create a dictionary named lex_pos to store words and their parts of speech
# as three key-value pairs
lex_pos = {"love": "verb", "cake": "noun", "of": "prep"}

# Iterate through the dictionary
# When a dictionary is used directly in a for loop, Python iterates over its keys by default
# In each iteration, the local variable "key" receives one key as a string from the dictionary
for key in lex_pos:
    # Print the current key
    # The output is a key such as "love", "cake", or "of"
    print(key)

# Retrieve all values from the dictionary using the values() method
# values() returns all the values in a dict_value object, which is similar to a list
# print() displays these values, which are "verb", "noun", and "prep"
print(lex_pos.values())

# Iterate through all the values in the dictionary
# The values() method allows the loop to access values directly without accessing keys
# In each iteration, value receives one value from the dictionary
for value in lex_pos.values():
    # Print the current value
    # The output is "verb", "noun", and "prep", one per line
    print(value)

# Check whether the string "hate" exists as a key in lex_pos
# The in operator checks dictionary keys by default, not dictionary values
# Since "hate" is not a key, the result is False
print("hate" in lex_pos)

# Check whether the string "love" exists as a key in lex_pos
# Since "love" is a key, the result is True
print("love" in lex_pos)

# Check whether the string "prep" does not exist as a key in lex_pos
# "prep" is a value, not a key, so it is not in the dictionary's keys
# Therefore, the expression evaluates to True
print("prep" not in lex_pos)

# Check whether the string "adv" does not occur among the dictionary's values
# values() provides the values "verb", "noun", and "prep"
# Since "adv" is not one of these values, the result is True
print("adv" not in lex_pos.values())

# Check whether the string "noun" does not occur among the dictionary's values
# Since "noun" is one of the values, the expression evaluates to False
print("noun" not in lex_pos.values())

# The same dictionary object from Week6-1.py
like_def = {
    # The key "spelling" maps to the string "like"
    "spelling": "like",

    # The key "IPA" maps to a string representing the pronunciation
    "IPA": "laik",

    # The key "meaning" maps to a definition of the word
    "meaning": "to enjoy something",

    # The key "synonyms" maps to a list of three synonyms
    "synonyms": ["admire", "appreciate", "love"]
}

# Check whether "admire" occurs among the values of like_def
# The dictionary's values are "like", "laik", "to enjoy something",
# and the entire list ["admire", "appreciate", "love"]
# The values() method does not search inside a list stored as a value
# Therefore, "admire" is not itself a direct dictionary value, and the result is False
print("admire" in like_def.values())

# First, access the value associated with the key "synonyms"
# This value is the list ["admire", "appreciate", "love"]
# Then, use in to check whether "admire" is an item in that list
# Since "admire" is in the list, the result is True
print("admire" in like_def["synonyms"])

# Assign a value "noun" to the "chair" key in lex_pos.
# Since the key does not already exist, this assignment adds a new key-value pair
lex_pos["chair"] = "noun"

# Print the entire lex_pos dictionary, including the newly added item
# The dictionary now contains four keys: "love", "cake", "of", and "chair"
print(lex_pos)

# Create an empty dictionary to count the frequency of each part-of-speech label
# Each key will be a part-of-speech label, and each value will be its frequency
# For example, "noun": 2 means that the value "noun" occurs twice
POS_freq = {}

# Iterate through all values in lex_pos
# The values are "verb", "noun", "prep", and "noun"
# Each value is assigned to the local variable "pos" in turn
for pos in lex_pos.values():

    # Check whether the current part-of-speech label is already a key in POS_freq
    # The in operator checks dictionary keys by default
    if pos not in POS_freq:

        # If the label is not yet a key, add it with an initial frequency of 1
        # For example, the first time "verb" is encountered, add "verb": 1
        POS_freq[pos] = 1

    # If the label is already a key in POS_freq, its frequency has been counted before
    else:
        # Increase the existing frequency by 1
        # For example, when "noun" is encountered for the second time,
        # its value increases from 1 to 2
        # The shorter equivalent is POS_freq[pos] += 1
        POS_freq[pos] = POS_freq[pos] + 1

# Print the completed frequency dictionary
# The expected result is {'verb': 1, 'noun': 2, 'prep': 1}
print(POS_freq)