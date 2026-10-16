# Create a list containing three strings in a specific order
str_list = ["John", "likes", "Mary"]

# Convert the list into a set using the set() function
# A set is a mutable collection of unique elements
# Unlike a list, a set does not preserve a guaranteed positional order
# If the original list contains duplicate values, set() removes the duplicates
str_set = set(str_list)

# Print the set
# The elements may appear in a different order from the original list
print(str_set)

# A set is mutable, meaning elements can be added or removed after creation
# However, individual elements cannot be accessed by numeric index

# Add the string "and" to the set using the add() method
# Sets only store unique elements, so adding an element already present
# does not create a duplicate
str_set.add("and")

# Print the updated set, which now contains "and"
print(str_set)

# Remove the element "John" from the set using the remove() method
# If "John" does not exist in the set, remove() raises a KeyError
str_set.remove("John")

# Print the set after removing "John"
print(str_set)

# List elements have positions, so they can be accessed using indexes
# Set elements do not have guaranteed positional order and cannot be
# accessed using numeric indexes

# Access the element at index 0 of the list
# Since list indexes start at 0, this prints "John"
print(str_list[0])

# Attempt to access the element at index 0 of the set
# This line is commented out, so it will not execute
# If uncommented, it would raise a TypeError because sets do not support indexing

# print(str_set[0])

# Remove and return the element at index 0 of the list using pop(0)
# Because index 0 contains "John", that element is removed
# The remaining list is ["likes", "Mary"]
# Unlike set.pop(), list.pop(0) specifies which positional element to remove
str_list.pop(0)

# Print the modified list
print(str_list)

# Remove and return an arbitrary element from the set using pop()
# Sets have no positional indexes, so pop() does not let you choose
# which element to remove
# The particular element removed should not be assumed from the set's display order
str_set.pop()

# Print the set after one element has been removed
print(str_set)

# Store a sample sentence as a string
# The sentence contains repeated words, including "I", "not", and "in"
sen_sample = "I am not a religious person so I do not believe in God"

# Split the sentence into a list of tokens using a space as the separator
# Each token is stored as a separate string in the resulting list
# Repeated words are retained, and the original word order is preserved
sen_tokens = sen_sample.split(" ")

# Print the token list
print(sen_tokens)

# Convert the token list into a set of unique words
# Duplicate tokens are removed, so each distinct word appears only once
# Unlike the list, the set does not preserve the original word order
sen_types = set(sen_tokens)

# Print the set of unique word types
print(sen_types)

# Add the string "I" to the set using add()
# "I" is already present, so the set remains unchanged
# A set cannot contain duplicate elements
sen_types.add("I")

# Print the set after the attempted addition
# Its contents remain the same because "I" was already a member
print(sen_types)

# Store a second sample sentence as a string
sen_sample2 = "There is really no God because I have never seen one"

# Split the second sentence into a list of tokens
# The list preserves the original order and any repeated words
sen_tokens2 = sen_sample2.split(" ")

# Convert the second token list into a set of unique word types
# Any repeated tokens in the second sentence are removed
sen_types2 = set(sen_tokens2)

# Print the unique words from the second sentence
print(sen_types2)

# Find the intersection of the two sets
# The intersection contains only the elements that occur in both sets
# set.intersection(set1, set2) returns a new set without modifying
# either of the original sets
sen_inter = set.intersection(sen_types, sen_types2)

# Print the words shared by both sentences
print(sen_inter)

# Find the difference between the two sets
# sen_types - sen_types2 returns the elements that occur in sen_types
# but do not occur in sen_types2
# This operation creates a new set and does not modify either original set
sen_comp = sen_types - sen_types2

# Print the words found in the first sentence but not the second
print(sen_comp)