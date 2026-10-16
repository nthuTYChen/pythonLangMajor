# Create a list named subjs_objs
# Each item in the list is a tuple containing two strings (yes, you can use more than
# just a string or a number as an item in a list):
# the first string represents a subject, and the second represents an object
# A list can contain multiple tuples as its elements
subjs_objs = [
    # The first tuple contains the subject "John" and the object "Mary"
    ("John", "Mary"),

    # The second tuple contains the subject "the cat" and the object "the dog"
    ("the cat", "the dog"),

    # The third tuple contains the subject "a person" and the object "a bee"
    ("a person", "a bee")
]

# Access the first element of the list using index 0
# The first element is the tuple ("John", "Mary")
# Print the tuple directly
print(subjs_objs[0])

# Iterate through the list of tuples
# In each iteration, Python unpacks the current tuple into two variables:
# the first element is assigned to subj, and the second element to obj
# For example, the first iteration assigns subj = "John" and obj = "Mary"
for subj, obj in subjs_objs:

    # Concatenate strings to construct and print a sentence
    # The + operator joins "Original: ", the subject, " likes ", and the object
    # In the first iteration, the output is "Original: John likes Mary"
    print("Original: " + subj + " likes " + obj)

    # Swap the values of subj and obj using tuple assignment as in Week6-4.py
    subj, obj = (obj, subj)

    # Print the sentence again using the swapped values
    # In the first iteration, the output is now "Switched: Mary likes John"
    print("Switched: " + subj + " likes " + obj)

    # Print a separator line to make the output of each iteration easier to read
    print("------")

# Create a dictionary named freq_table
# Each key is a word, and its corresponding value is a frequency count
freq_table = {
    # The key "like" maps to the integer 42
    "like": 42,

    # The key "him" maps to the integer 107
    "him": 107,

    # The key "success" maps to the integer 17
    "success": 17
}

# Call the items() method of a dictionary object, which returns every key-value pair as a tuple
# Iterating over all the tuples in freq_table returned by items()
# For example, the first pair is ("like", 42)
for item in freq_table.items():

    # Use type() to identify the data type of the current item
    # Each key-value pair returned by items() is a tuple
    # The output is <class 'tuple'>
    print(type(item))

    # Print the current key-value tuple
    # For example, the output may be ('like', 42)
    print(item)

# Iterate through the dictionary's key-value pairs again
# Tuple unpacking assigns the key to word and the value to freq
# For example, the pair ("like", 42) assigns word = "like" and freq = 42
for word, freq in freq_table.items():

    # Concatenate the word, a colon and a space, and the frequency converted to a string
    # str(freq) is necessary because word is a string but freq is an integer
    # The output for this pair is "like: 42"
    print(word + ": " + str(freq))