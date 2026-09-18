# Check the data type of the string "This is string" and print the result
# type() is a function that actually "returns" the data (i.e., the class type)
# so it can be printed in print().
print(type("This is string"))

# Define a function named return_str that does not take any arguments
def return_str():
    # Return the string "Are you calling me?" to the place where the function is called
    return "Are you calling me?"

# Call the return_str function and store the returned string in the variable res
res = return_str()

# Print the value stored in res
print(res)

# Define a function that checks whether the subject and object are the same
def self_check(subj_check, obj_check):
    # Check whether the subject and object have the same value
    # Do not confuse == with =; the latter is for value assignment.
    if subj_check == obj_check:
        # Return "himself" if the subject and object are the same
        return "himself"
    # Run this block if the subject and object are different
    else:
        # Return the original object
        return obj_check

# Define a function that creates and prints a sentence using a subject and an object
def verb_like_4(subj, obj):
    # Call self_check to determine what should be used as the object
    new_obj = self_check(subj, obj)

    # Combine the subject, "likes", and the new object to create the final sentence
    final_sen = subj + " likes " + new_obj

    # Print the final sentence
    print(final_sen)

# Call the function with different subject and object values,
# so the output will be "John likes Mary".
verb_like_4("John", "Mary")

# Call the function with the same subject and object values,
# so the output will be "John likes himself".
verb_like_4("John", "John")