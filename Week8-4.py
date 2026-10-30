# Open the cleaned Dracula text file for reading.
dracula_read = open("sources/pg345_2_clean.txt", encoding = "utf-8")

# Read and print the file line by line.
# The file pointer moves forward as each line is read.
for line in dracula_read:
    print(line)

# Move the file pointer back to the beginning of the file.
dracula_read.seek(0)

# Print a separator to distinguish the two outputs.
print("###########")

# Read and print the file again, starting from the beginning.
for line in dracula_read:
    print(line)

# Close the file after reading.
dracula_read.close()