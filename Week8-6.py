# Define the singular and plural forms of the search keyword.
keyword_sg = "vampire"
keyword_pl = "vampires"

# Open the cleaned Dracula text file for reading.
dracula_read = open(file = "sources/pg345_2_clean.txt", encoding = "utf-8")

# Read the file line by line.
for line in dracula_read:
    # Check whether the line contains either the singular or plural keyword.
    if keyword_sg in line or keyword_pl in line:
        # Print the line if either keyword is found.
        print(line)

# Close the file after searching.
dracula_read.close()