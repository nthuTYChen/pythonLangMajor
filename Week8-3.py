# Create a string object
# startswith() checks whether a string begins with the specified characters
str = "I love Python."

# Check whether the string starts with "I"
# The result is True
print(str.startswith("I"))

# Check whether the string starts with "love"
# The result is False because "love" is not at the beginning
print(str.startswith("love"))

# Define a function to check whether a line starts with a boundary marker
def isBoundaryMarker(line):
    # Check whether the line starts with three asterisks
    # In the source file, the two lines that marks the scope of the
    # body text begins with ***. Check it your self.
    # Return True if it does; otherwise, return False
    startWithStars = line.startswith("***")
    # Return the result of the check
    return startWithStars

# Open the original text file in read mode using UTF-8 encoding
# The file pointer is initially at the beginning
dracula_read = open(file="sources/pg345_2.txt", encoding="utf-8")

# Iterate through the file one line at a time
# Each iteration reads the next line and advances the file pointer
for line in dracula_read:
    # Check whether the current line starts with three asterisks
    if isBoundaryMarker(line):
        # Print the boundary-marker line
        print(line)
        # Stop the loop after finding the first boundary marker
        # which is marks the beginning of the body text
        # The file pointer remains immediately after this line
        # i.e., the first line of the body text
        break

# Open a new file in write mode
# If the file does not exist, Python creates it
# If it already exists, its previous contents are erased
dracula_write = open(file="sources/pg345_2_clean.txt", encoding="utf-8", mode="w")

# The loop does not restart from the beginning of the file
# Continue iterating through the original file from its current pointer position
# i.e., the first line of the body text.
for line in dracula_read:
    # Check whether the current line starts with three asterisks
    # If so, it marks the end of the body text.
    if isBoundaryMarker(line):
        # Stop reading when the end boundary marker is found
        break
    # Otherwise, write the current line from the body text into the new file
    # The line is copied only if it is not a boundary marker
    dracula_write.write(line)

# Close the original file and release its resources
dracula_read.close()

# Close the new file and ensure the written content is saved
dracula_write.close()