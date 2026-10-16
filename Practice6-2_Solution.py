# Store the first sentence as a string
sen1 = "John likes Mary"

# Store the second sentence as a string
sen2 = "Tom hates Mike"

# Store the third sentence as a string
sen3 = "Brian admires Judy"

# Split the first sentence into individual words using a space as the separator
# The result is a list: ["John", "likes", "Mary"]
sen1_list = sen1.split(" ")

# Split the second sentence into individual words
# The result is a list: ["Tom", "hates", "Mike"]
sen2_list = sen2.split(" ")

# Split the third sentence into individual words
# The result is a list: ["Brian", "admires", "Judy"]
sen3_list = sen3.split(" ")

# Create an empty list to store subject-object pairs
# Each pair will be a tuple containing a subject and an object
subj_obj = []

# Get the subject from the first value of a list (index 0: "John")
# Get the object from the third value of a list (index 2: "Mike")
# Store these two words together as a tuple using () and append it to subj_obj in append()
subj_obj.append((sen1_list[0], sen2_list[2]))

# As above, with a different subject and object from the second list
subj_obj.append((sen2_list[0], sen2_list[2]))

# As above, with a different subject and object from the third list
subj_obj.append((sen3_list[0], sen3_list[2]))

# Iterate through each tuple in subj_obj
# Unpack each tuple into the variables subj and obj (i.e., tuple assignment)
for subj, obj in subj_obj:
    # Combine the subject, the string " loves ", and the object
    # Then print the resulting sentence
    print(subj + " loves " + obj)