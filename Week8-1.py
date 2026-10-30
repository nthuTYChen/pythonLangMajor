# Open the text file in read mode using UTF-8 encoding
# The file pointer is initially at the beginning of the file
dracula_read = open(file="sources/pg345_2.txt", encoding="utf-8")

# Read the first line of the file
# The file pointer moves to the beginning of the second line
dracula_firstline = dracula_read.readline()

# Print the first line
# Printing does not affect the file pointer
print(dracula_firstline)

# Read all remaining lines from the current pointer position
# Since the first line has already been read, this starts from the second line
# The file pointer moves to the end of the file (EOF)
dracula_lines = dracula_read.readlines()

# Print the first three lines stored in the list
# These are actually lines 2–4 of the original file
# Slicing a list does not affect the file pointer
print(dracula_lines[:3])

# Print the first five lines stored in the list
# These are actually lines 2–6 of the original file
# The file pointer remains at EOF
print(dracula_lines[:5])

# Close the file and release its associated resources
dracula_read.close()