# Create a list containing four English verbs
str_ls = ["love", "admire", "cherish", "treasure"]

# Check whether the string "admire" is an element of str_ls
# The "in" operator returns True if the specified value exists in the list
# Since "admire" is in str_ls, the result is True
print("admire" in str_ls)

# Check whether "admire" is NOT an element of str_ls
# The "not in" operator returns True if the specified value does not exist in the list
# Since "admire" does exist in str_ls, the result is False
print("admire" not in str_ls)

# Check whether "adore" is an element of str_ls
# "adore" is not in the list, so the condition evaluates to False
print("adore" in str_ls)

# Check whether "adore" is NOT an element of str_ls
# "adore" does not exist in the list, so the condition evaluates to True
print("adore" not in str_ls)

# Check a condition before deciding which block of code to execute
# The condition asks whether "adore" exists in str_ls
if "adore" in str_ls:
    # This block runs only when "adore" is found in the list
    print("It does exist!")
else:
    # This block runs when the condition is False
    # In this example, "adore" is not in str_ls, so this block runs
    print("It doesn't exist!")

# Create a list containing some repeated words
new_str_ls = ["a", "cat", "loves", "a", "dog"]

# Create an empty list to store words that have not been added before
final_ls = []

# Iterate through each word in new_str_ls
for word in new_str_ls:
    # Check whether the current word is NOT already in final_ls
    # The condition is True when the word has not been added yet
    if word not in final_ls:
        # Add the word only when it is not already in final_ls
        # This prevents duplicate words from being added
        final_ls.append(word)

# Print the list containing only the first occurrence of each word
print(final_ls)