import nltk  # Import the Natural Language Toolkit (NLTK) library for natural language processing.

# Download the Punkt tokenizer data package used for sentence segmentation.
# This package provides the language-specific resources needed by the sentence tokenizer.
nltk.download("punkt_tab")

# Import PunktTokenizer, which identifies sentence boundaries in text.
from nltk.tokenize import PunktTokenizer

# Create an English sentence tokenizer using the English language model.
nltk_en_tknz = PunktTokenizer("english")

# Open the email sample file in read mode using UTF-8 encoding.
email_reader = open("sources/email-sample-1.txt", encoding = "utf-8")

# Read the entire contents of the email file into a single string.
email_text = email_reader.read()

# Print the complete email text for inspection (currently commented out).
# print(email_text)

# Divide the email text into individual sentences using the English tokenizer.
# The result is a list of sentence strings.
email_sens = nltk_en_tknz.tokenize(email_text)

# Print the first five sentences for inspection (currently commented out).
# [:5] selects list elements from index 0 up to, but not including, index 5.
# print(email_sens[:5])

# Close the email file after reading its contents.
email_reader.close()

# Open the cleaned Dracula text file in read mode using UTF-8 encoding.
dracula_reader = open("sources/pg345_2_clean.txt", encoding = "utf-8")

# Read the entire Dracula text into a single string.
dracula_text = dracula_reader.read()

# Divide the Dracula text into individual sentences using the same English tokenizer.
# The tokenizer applies the same sentence-segmentation procedure used for the email.
dracula_sens = nltk_en_tknz.tokenize(dracula_text)

# Print sentences at indices 41 through 49 (nine sentences in total).
# [41:50] starts at index 41 and stops before index 50.
# The main benefit here using the sentence tokenizer is that in the original Dracula text file,
# a line does not necessarily correspond to a complete sentence (check yourself), as a sentence
# can span over multiple lines. The sentence tokenizer can help us isolate individual sentences,
# which allows us to analyze individual sentences.
print(dracula_sens[41:50])

# Close the Dracula file after reading its contents.
dracula_reader.close()