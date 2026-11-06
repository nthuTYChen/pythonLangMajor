# This is just one of many possible solutions.

# Load the source text file
dracula_read = open("sources/pg345_2.txt", "r", encoding="utf-8")

# Declare an empty list to save all the sentences with "you" or "You"
you_sens = []

# Iterate through each lines in the source text file
for line in dracula_read:
    # Check if "you" or "You" appears in a line (a string object)
    if "you" in line or "You" in line:
        # If so append the line to the collection
        you_sens.append(line)

# Print the first 5 items in the list
print(you_sens[:5])

# Don't forget to close the reader!
dracula_read.close()