# Define the keyword to search for.
keyword = "vampire"

# Create two sample sentences for testing.
sen1 = "I love vampire!"
sen2 = "Is anyone still watching the Twilight trilogy?"

# Check whether the keyword appears in each sentence.
# The result is True if found and False otherwise.
print(keyword in sen1)
print(keyword in sen2)

# Open the cleaned Dracula text file for reading.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Read the file line by line.
for line in dracula_read:
    # Check whether the current line contains the keyword.
    if keyword in line:
        # Print the line if the keyword is found.
        print(line)

# Close the file after searching.
dracula_read.close()