# Open the text file in read mode using UTF-8 encoding
# The file object is iterable, meaning it can be used in a for loop
dracula_read = open(file = "sources/pg345_2.txt", encoding = "utf-8")

# Iterate through the file one line at a time
# In each iteration, line receives the next line from the file
for line in dracula_read:
    # Print the current line
    print(line)

# Close the file and release its associated resources
dracula_read.close()