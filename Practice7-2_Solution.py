# This script tries to complete the following tasks:
# 1. Create a string object with an English sentence of 30 words.
# 2. Loop through the individual words one by one.
# 3. In each iteration, compare a regular expression that searches for "se" in anywhere in each word"
#    and print the combination of "The word with a match is: " and each word with a match.
# Fix all the issues so the script works as expected.

# Issue 1: You must import the re package for regular expression things
import re

sample_sen = "These students study science because research helps people understand language and discover useful patterns in sentences through careful observation and systematic analysis of different examples and meaningful expressions in everyday communication."

sen_words = sample_sen.split(" ")

# Issue 2: A colon is missing at the end of the for loop statement
# Issue 3: A typo in the name of the word list. It should be "sen_word"
for word in sen_words:
    # Issue 4: No proper indentation for the if statement, which is INSIDE
    #          the for loop block
    # Issue 5: The pattern should be "se" rather than "es"
    # Issue 6: The condition should be "is not None", which means "there is a match".
    if re.search("es", word) is not None:
        # Issue 6: The string that have to be enclosed inside quotation marks is
        #          just "The word with a match is: "
        print("The word with a match is: " + word)

# Expected output:
# The word with a match is: These
# The word with a match is: research
# The word with a match is: sentences
# The word with a match is: examples
# The word with a match is: expressions