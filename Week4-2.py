# Create a list containing integer values
num_ls = [10, 20, 31, 1, 5]

# Create a list containing string values
str_ls = ["love", "admire", "cherish", "treasure"]

# Create an empty list with no elements
empty_ls = []

# Access the first element of num_ls using index 0 and print it
print(num_ls[0])

# Access the first element of str_ls using index 0 and print it
print(str_ls[0])

# This would cause an IndexError because empty_ls has no elements
# print(empty_ls[0])

# This would cause an IndexError because the largest valid index is 4
# print(num_ls[5])

# Create a list containing both integers and strings
# A Python list can contain different types of data,
# but this is not a recommended practice.
mixed_ls = [20, "woman", 1000, "years"]

# It is not straightforward to tell which index position
# refers to which type of data.
print(mixed_ls[0])
print(mixed_ls[1])

# Store the first integer from num_ls in first_val
first_val = num_ls[0]

# Store the second integer from num_ls in second_val
second_val = num_ls[1]

# Add the two integer values and print the result
print(first_val + second_val)

# Lists are mutable, which means their elements can be changed after the list is created

# Change the first element of num_ls from 10 to 10000
num_ls[0] = 10000

# Print the modified list
print(num_ls)

# Add "s" to the first string in str_ls and replace the original value
str_ls[0] = str_ls[0] + "s"