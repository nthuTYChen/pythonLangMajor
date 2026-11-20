import nltk  # Import the Natural Language Toolkit (NLTK) library for natural language processing.

# Import word_tokenize(), a function that divides text into individual word and punctuation tokens.
from nltk.tokenize import word_tokenize

# Open the email sample file in read mode using UTF-8 encoding.
email_reader = open("sources/email-sample-1.txt", encoding = "utf-8")

# Read the entire contents of the file into a single string.
email_text = email_reader.read()

# Tokenize the email text into individual words and punctuation marks.
# The result is a list of tokens; punctuation marks are treated as separate tokens,
# unlike in our own tokenization process, in which we identify and remove punctuation marks
# on our own.
email_words = word_tokenize(email_text)

# Print the last 10 tokens in the list.
# [-10:] selects elements from the tenth-to-last position through the end of the list.
print(email_words[-10:])

# Close the file after reading its contents.
email_reader.close()