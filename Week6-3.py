# Create a list of four strings
# A list is an ordered collection that can be modified after it is created
str_ls = ["love", "admire", "cherish", "treasure"]

# Use type() to check the data type of str_ls
# The output is <class 'list'>, indicating that str_ls is a list
print(type(str_ls))

# Create a tuple containing the same four strings
# A tuple is an ordered collection that cannot be modified after it is created
# Tuples are usually created with parentheses (), and every two values are also
# separated by a comma.
str_tp = ("love", "admire", "cherish", "treasure")

# Use type() to check the data type of str_tp
# The output is <class 'tuple'>, indicating that str_tp is a tuple
print(type(str_tp))

# Access the first element of the list using index 0
# Python indexing starts at 0, so str_ls[0] is "love"
print(str_ls[0])

# Access the first element of the tuple using index 0
# Values in tuples are strictly ordered, so tuples support
# indexing just like lists, so str_tp[0] is also "love"
print(str_tp[0])

# Concatenate the original list with another list containing two strings
# The + operator combines the elements of the two lists into a new list
# The original list, str_ls, remains unchanged
str_ls_big = str_ls + ["like", "appreciate"]

# Print the new list containing six strings
print(str_ls_big)

# You can also concatenate the original tuple with another tuple
# The + operator combines the elements into a new tuple
# The original tuple, str_tp, remains unchanged
str_tp_big = str_tp + ("like", "appreciate")

# Print the new tuple containing six strings
print(str_tp_big)

# Tuples are IMMUTABLE, meaning their elements cannot be reassigned or removed
# The following operations are commented out, so Python will not execute them

# Attempt to replace the first element of the tuple with "adore"
# If uncommented, this would raise a TypeError because tuples do not support item assignment

# str_tp_big[0] = "adore"

# Attempt to remove the first element using pop()
# Lists have a pop() method, but tuples do not
# If uncommented, this would raise an AttributeError
# (because you cannot find the pop() attribute for str_tp_big)

# str_tp_big.pop(0)

# Attempt to remove the element "love" using remove()
# Lists have a remove() method, but tuples do not
# If uncommented, this would raise an AttributeError

# str_tp_big.remove("love")

# Attempt to add "adore" using append()
# Lists have an append() method, but tuples do not
# If uncommented, this would raise an AttributeError

# str_tp_big.append("adore")

# Assign the string "John" to the variable name1
name1 = "John"

# Assign the string "Mary" to the variable name2
name2 = "Mary"

# Create a tuple containing the values of name1 and name2
# The tuple stores the two strings in a fixed order
subj_obj = (name1, name2)

# Print the tuple
# The output is ('John', 'Mary')
print(subj_obj)

# Create a list containing the values of name1 and name2
# Unlike the tuple above, this list can be modified after creation
subj_obj_list = [name1, name2]

# Unpack the two elements of the tuple into two separate variables
# The first element, "John", is assigned to subj_tp
# The second element, "Mary", is assigned to obj_tp
# Both lists and tuples can be unpacked in this way
subj_tp, obj_tp = subj_obj

# Print the value assigned to subj_tp, which is "John"
print(subj_tp)

# Print the value assigned to obj_tp, which is "Mary"
print(obj_tp)

# In a tuple assignment, the number of variables must be equal to the number
# of items to be unpacked from a tuple.
# If uncommented, Python would try to unpack six tuple elements in str_tp_big
# into only two variables.
# This would raise a ValueError because the number of elements does not match

# verb1, verb2 = str_tp_big

# Swap the values of subj_tp and obj_tp using tuple packing and unpacking
# The right-hand side creates a temporary tuple containing (obj_tp, subj_tp)
# Python then unpacks that tuple into the variables on the left
# As a result, subj_tp becomes "Mary" and obj_tp becomes "John"
subj_tp, obj_tp = (obj_tp, subj_tp)

# Print the updated value of subj_tp, which is now "Mary"
print(subj_tp)

# Print the updated value of obj_tp, which is now "John"
print(obj_tp)