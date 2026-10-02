# Create a list of verbs
verbs = ["love", "like", "greet", "make", "hover"]

# Print the second item in the list
print(verbs[1])

# Print the third item in the list
print(verbs[2])

# Print the second-to-last item in the list
print(verbs[-2])

# Print the items from index 1 up to, but not including, index 3
print(verbs[1:3])

# Iterate through the list "verbs" and assign each value to "verb"
# in every iteration.
for verb in verbs:
    # Print a message that combines the string "The verb is: " with
    # each value from "verbs" assigned to the local variable "verb"
    print("The verb is: " + verb)