# List
num_ls = [10, 20, 31, 1, 5]
str_ls = ["love", "admire", "cherish", "treasure"]

# An empty list
empty_ls = []

# Index number
print(num_ls[0])
print(str_ls[0])

# print(empty_ls[0])
# print(num_ls[5])

mixed_ls = [20, "woman", 1000, "years"]
print(mixed_ls[0])
print(mixed_ls[1])

first_val = num_ls[0]
second_val = num_ls[1]
print(first_val + second_val)

# List is Mutable
num_ls[0] = 10000
print(num_ls)
str_ls[0] = str_ls[0] + "s"
print(str_ls)
