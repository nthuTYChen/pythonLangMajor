# Store the sample sentence as a string
sample_sen = "since a set must include unique values it is optimized for processes such as looking for the same or different values between two sets"

# Split the sentence into individual words using a space as the separator
# The result is a list containing each word, including repeated words
sample_sen_list = sample_sen.split(" ")

# Convert the list of words into a set
# A set stores only unique values, so repeated words are removed
sample_sen_unique_words = set(sample_sen_list)

# Initialize a counter to store the number of unique words longer than five characters
word_count = 0

# Iterate through each unique word in the set
for word in sample_sen_unique_words:
    # Check whether the current word contains more than five characters
    # len(word) returns the number of characters in the word
    if len(word) > 5:
        # Increase the counter by one if the word has more than five characters
        word_count += 1

# Print the total number of unique words longer than five characters
print(word_count)