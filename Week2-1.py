# If you only know how to declare variables and use simple operations,
# the code have to be repeated again and again.
num_x = 5
num_y = 10
mean_xy = (num_x + num_y) / 2
print(mean_xy)

num_x = 10
num_y = 70
mean_xy = (num_x + num_y) / 2
print(mean_xy)

num_x = 15
num_y = 3
mean_xy = (num_x + num_y) / 2
print(mean_xy)

# Try calling the function before it is defined, which is illegal.
# Everything has to be defined first (including variables) to be
# accessed in a script.
# mean_cal(20, 40)

# Define a function to calculate the mean of two numbers.
# The two numbers received by mean_cal() are assigned to two
# local variables "num1" and "num2".
def mean_cal(num1, num2):
    # Calculate the mean
    res = (num1 + num2) / 2
    # Print the result
    print(res)

# Call the function with 5 and 10
mean_cal(5, 10)
# Try to print the local variable res outside the mean_cal() code block,
# which is not possible.
# print(res)

# Call the function with 10 and 70
mean_cal(10, 70)

# Call the function with 15 and 3
mean_cal(15, 3)

# Define a function to create a sentence with "likes".
# Just as in syntax, the transitive verb takes two "argument" strings,
# which are assigned to "subj" and "obj" respectively.
def verb_like(subj, obj):
    # Create the sentence by adding all strings together
    msg = subj + " likes " + obj
    # Print the sentence
    print(msg)

# Call the function with John and Mary
verb_like("John", "Mary")