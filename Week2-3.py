# Set just_true to True as an alternative example, but keep it commented out
# just_true = True

# Set just_true to False so that the else block will be executed
just_true = False

# Check whether just_true is True
if just_true:
    # Print this message if just_true is True
    print("It's true!")
# Run the following block if just_true is False
else:
    # Print this message if just_true is False
    print("It's False!")

# Use a "conditional expression" to print one of two messages based on the value of just_true
print("It's true!") if just_true else print("It's False!")

# Define a function that creates a sentence using either "likes" or "like"
def verb_like_2(subj, obj, verb_sing):
    # Create a local variable to store the final sentence
    final_sen = None
    # Check whether the verb should have a singular form
    if verb_sing:
        # Use "likes" when verb_sing is True
        final_sen = subj + " likes " + obj
    # Use the following block when verb_sing is False
    else:
        # Use "like" when verb_sing is False
        final_sen = subj + " like " + obj
    # Print the completed sentence
    print(final_sen)

# Call the function with "John" as the subject and use the singular verb "likes"
verb_like_2("John", "Mary", True)

# Call the function with "I" as the subject and use the non-singular verb "like"
verb_like_2("I", "Mary", False)

# Define a similar function with a default value of True for the verb_sing parameter
def verb_like_3(subj, obj, verb_sing = True):
    # Create a local variable to store the final sentence
    final_sen = None
    # Check whether the verb should have a singular form
    if verb_sing:
        # Use "likes" when verb_sing is True
        final_sen = subj + " likes " + obj
    # Use the following block when verb_sing is False
    else:
        # Use "like" when verb_sing is False
        final_sen = subj + " like " + obj
    # Print the completed sentence
    print(final_sen)

# Call the function with specifying the Boolean value for "verb_sing",
# so the function will use the default value True, and "likes" is used
verb_like_3("John", "Mary")

# Call the function by explicitly setting "verb_sing" to False, so "like" is used.
verb_like_3("I", "Mary", False)