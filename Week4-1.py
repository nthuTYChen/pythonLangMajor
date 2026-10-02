# Create a string object and store it in the variable str
str = "Is this just a string?"

# Call the lower() object method to convert all letters to lowercase
# lower() is a method that belongs to the string object stored in str
str_lower = str.lower()

# Print the lowercase string
print(str_lower)

# Call the capitalize() object method to capitalize the first letter
# capitalize() is a method that belongs to the string object stored in str
str_cap = str.capitalize()

# Print the capitalized string
print(str_cap)

# Call the upper() object method to convert all letters to uppercase
# upper() is a method that belongs to the string object stored in str
str_upp = str.upper()

# Print the uppercase string
print(str_upp)

# Call the isspace() object method to check whether the string contains only whitespace
# isspace() returns True if all characters are whitespace; otherwise, it returns False
str_isspace = str.isspace()

# Print the Boolean result
print(str_isspace)

# Call the replace() object method to replace "just" with "not"
# replace() creates and returns a new string without changing the original str object
str_new = str.replace("just", "not")

# Print the new string
print(str_new)