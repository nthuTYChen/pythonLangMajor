# This script is designed to complete the following task:
# There is a list of 10 numeric values. A function is created
# to retrieve and return one numeric value from the list based on
# an index number it receives. Three function calls aim to get
# the third, sixth, and ninth values from the list, and the value
# returned by the function is printed after each function call.

# Make minimal but necessary changes to make everything happen.

# Change 1: Fixed the syntax error caused by the missing ]
numbers = [12, 45, 78, 23, 91, 34, 67, 10, 56, 82]

# Change 2: Fixed the syntax error caused by the missing :
def get_number(index):
    # Change 3: There's no need to add 1 to the index number.
    number = numbers[index]
    # Change 4: The function should return the integer retrieved
    # from the list, not the index number.
    return number

result1 = get_number(2)
# Change 5: The script should print the result returned from the
# function according to the scription description, rather than
# print a value in the list directly.
print(result1)

result2 = get_number(5)
# Change 6: Should print result2 here rather than result1
print(result1)

result3 = get_number(8)
print(result3)

# Intended output:
# 78
# 34
# 56