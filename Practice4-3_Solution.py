# Declare the first list of English words
list1 = [
    "apple", "river", "window", "mountain", "pencil",
    "garden", "silver", "coffee", "lantern", "ocean",
    "bridge", "orange", "forest", "ticket", "mirror"
]

# Declare the second list of English words
list2 = [
    "garden", "thunder", "apple", "notebook", "ocean",
    "candle", "mountain", "velvet", "window", "bicycle",
    "coffee", "island", "silver", "blanket", "bridge"
]

# Iterate through each word in the second list
for word in list2:
    # Check whether the current word is included in the first list
    if word in list1:
        # Remove the word from the first list if it is part of the first list
        list1.remove(word)

# Print the entire first list
print(list1)

# Print the length of the first list
print(len(list1))