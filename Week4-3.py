# Create a list of integers
num_ls = [10, 20, 31, 1, 5]

# Create a list of strings
str_ls = ["love", "admire", "cherish", "treasure"]

# Iterate through each string in str_ls
# A list is iterable, so a for loop can access its elements one by one
# following their linear order in the list.
for verb in str_ls:
    # Add "s" to the end of the current verb
    sing_form = verb + "s"

    # Print the new string
    print(sing_form)

# Create a list containing the words of a sentence
sen_words = ["John", "loves", "Mary"]

# Create an empty string to store the final sentence
final_sen = ""

# Iterate through each word in sen_words
for word in sen_words:
    # Add the current word and a space to the final sentence
    final_sen = final_sen + word + " "

# Print the completed sentence
print(final_sen)

# Create a variable to store the total of the numbers
# Start with 0 because no numbers have been added yet
total_num = 0

# Iterate through each number in num_ls
for num in num_ls:
    # Add the current number to total_num
    # This is a shorter version of:
    # total_num = total_num + num
    total_num += num

# Print the total of all the numbers
print(total_num)

# Sort the numbers in ascending order and store the result in a new list
sort_num = sorted(num_ls)

# Print the numbers in ascending order
print(sort_num)

# Sort the numbers in descending order
# reverse=True tells sorted() to put the largest value first
sort_num_des = sorted(num_ls, reverse=True)

# Print the numbers in descending order
print(sort_num_des)

# Sort the strings in alphabetical order
sort_str = sorted(str_ls)

# Print the strings in alphabetical order
# You can also specify reverse=True here for a decreasing alphabetical order.
print(sort_str)

# Use the sum() function to calculate the total of all numbers in num_ls
total_num_new = sum(num_ls)

# Print the total calculated by sum()
print(total_num_new)

# Use the max() function to find the largest number in num_ls
max_num = max(num_ls)

# Use the min() function to find the smallest number in num_ls
min_num = min(num_ls)

# Print the largest number
print(max_num)

# Print the smallest number
print(min_num)