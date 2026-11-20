import spacy  # Import spaCy, a natural language processing library.

# Define a function to open a text file and return its contents as a string.
def file_loader(filename):
    # Open the specified file in the sources folder using UTF-8 encoding.
    text_reader = open("sources/" + filename, encoding = "utf-8")
    # Read and return the entire file as a string.
    return text_reader.read()

# Load the contents of the email sample file into a string.
email_text = file_loader("email-sample-1.txt")

# Print the complete email text for inspection (currently commented out).
# print(email_text)

# Load spaCy's small English language model.
# The model includes components for tasks such as tokenization, sentence segmentation, and part-of-speech tagging.
spacy_model_en = spacy.load("en_core_web_sm")

# Process the email text using the loaded spaCy model.
# The result is a Doc object containing the processed text and its linguistic annotations.
email_text_processed = spacy_model_en(email_text)

# Retrieve the sentences identified by spaCy.
# The result is a sentence iterator (not a regular list).
email_sens = email_text_processed.sents

# Loop through the sentences identified by spaCy and print each one (currently commented out).
# for sen in email_sens:
#     print(sen)

# Loop through all tokens in the processed email text.
# Each token represents a word, punctuation mark, or other text element.
for token in email_text_processed:
    # Print the original text of the current token.
    print(token.text)