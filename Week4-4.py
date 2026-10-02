# Create a list of English verbs
str_ls = ["love", "admire", "cherish", "treasure"]

# Use slicing to get elements from index 1 up to, but not including, index 3
# Slicing does NOT modify the original list
print(str_ls[1:3])

# Use slicing to get elements from the beginning up to, but not including, index 2
# Slicing does NOT modify the original list
print(str_ls[:2])

# Use slicing to get elements from index 2 to the end of the list
# Slicing does NOT modify the original list
print(str_ls[2:])

# Access the last element using a negative index
# Accessing an element does NOT modify the original list
print(str_ls[-1])

# Access the second-to-last element using a negative index
# Accessing an element does NOT modify the original list
print(str_ls[-2])

# Get the last two elements using slicing
# Slicing creates a new list and does NOT modify the original list
print(str_ls[-2:])


# Create another list containing two additional verbs
str_ls_new = ["like", "adore"]

# Combine the two lists using the + operator
# The + operator creates a NEW list and does NOT modify either original list
str_ls_all = str_ls + str_ls_new

# Print the combined list
print(str_ls_all)

# Repeat the elements in str_ls_new two times
# The * operator creates a NEW list and does NOT modify str_ls_new
str_ls_rep = str_ls_new * 2

# Print the repeated list
print(str_ls_rep)


# Add "adore" to the end of str_ls
# append() MODIFIES the original list
# append() adds one element to the existing list
str_ls.append("adore")

# Print the modified original list
print(str_ls)


# Remove the first element from str_ls
# pop() MODIFIES the original list
# pop() removes an element based on its index
# pop() also RETURNS the removed element
str_ls.pop(0)

# Print the modified original list
print(str_ls)


# Remove "treasure" from str_ls
# remove() MODIFIES the original list
# remove() removes an element based on its value
str_ls.remove("treasure")

# Print the modified original list
print(str_ls)


# Create a string containing an English sentence
sen_sample = "John likes Mary"

# Tokenize the sentence by splitting it at each space
# split() does NOT modify the original string
# split() creates and RETURNS a new list containing the pieces
sen_words = sen_sample.split(" ")

# Print the new list created by split()
print(sen_words)

# The original string is still unchanged
print(sen_sample)


# Create a space character to use as a delimiter
sep_ch = " "

# Join the words back together using the space as the delimiter
# join() creates and RETURNS a new string
# join() does NOT modify the original list sen_words
final_sen = sep_ch.join(sen_words)

# Print the new string created by join()
print(final_sen)


# Create a string containing three Chinese characters
sen_ch_sample = "陳宗穎"

# Convert the string into a list of individual characters
# list() creates and RETURNS a new list
# The original string is NOT modified
sen_words_ch = list(sen_ch_sample)

# Print the new list of individual characters
print(sen_words_ch)