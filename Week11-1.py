import re  # Import the regular expression module for text processing.

# OVERALL FLOW:
# 1. Load the positive and negative training comments.
# 2. Tokenize each training comment:
#       - Remove punctuation and stop words.
#       - Convert the remaining words to lowercase.
#       - Collect the words from positive and negative comments separately.
# 3. Identify words shared by both training collections and remove them.
#    The remaining words are treated as positive-specific or negative-specific words.
# 4. Load the test comments and classify each one:
#       - Count how many positive-specific words it contains.
#       - Count how many negative-specific words it contains.
#       - Assign "pos", "neg", or "neut" according to which count is larger.
# 5. Compare the predictions with the expected labels:
#       - First 10 test comments are assumed to be positive.
#       - Remaining test comments are assumed to be negative.
# 6. Calculate and print the number and proportion of correct predictions.

# Create a list to collect tokens from positive training comments.
pos_tokens = []

# Create a list to collect tokens from negative training comments.
neg_tokens = []

# Create a list to store the predicted labels of test comments.
comp_res = []

# Define a function to open a file and return its file object.
def file_loader(filename):
    # Open the file in the sources folder using UTF-8 encoding.
    text_reader = open("sources/" + filename, encoding = "utf-8")
    # Return the file object so that the calling code can read its lines.
    return text_reader

# Define a function to clean a comment and extract its tokens.
def tokenizer(comment):
    # Define common words that will be excluded from the analysis.
    stop_words = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
                  "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
                  "their", "as", "by", "if", "not", "so"}

    # Define a regular expression pattern matching punctuation marks to remove.
    puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"

    # Remove whitespace from the beginning and end of the comment.
    comment_new = comment.strip()

    # Remove punctuation by replacing every matching character with an empty string.
    comment_clean = re.sub(puncs_re, "", comment_new)

    # Convert all letters to lowercase.
    comment_lower = comment_clean.lower()

    # Split the comment into tokens wherever a space occurs.
    comment_words = comment_lower.split(" ")

    # Convert the token list into a set to remove duplicate words.
    comment_words_set = set(comment_words)

    # Remove all tokens that appear in the stop-word set.
    comment_words_nostop = comment_words_set - stop_words

    # Convert the remaining set of tokens back into a list.
    comment_words_nostop_list = list(comment_words_nostop)

    # Return the list of cleaned tokens to the function that called tokenizer().
    return comment_words_nostop_list

# Define a function to tokenize a comment and add its tokens to the appropriate list.
def add_tokens(comment, comment_type):
    # Clean the comment and obtain its list of tokens.
    comment_word_list = tokenizer(comment)

    # Check whether the comment belongs to the positive training collection.
    if comment_type == "pos":
        # Add each token to the positive token list.
        pos_tokens.extend(comment_word_list)
    # Otherwise, add each token to the negative token list.
    else:
        neg_tokens.extend(comment_word_list)

# Define a function to classify one test comment.
def comp_comm(comment):
    # Tokenize the test comment using the same procedure as the training comments.
    comment_word_list = tokenizer(comment)

    # Convert the tokens into a set for set operations.
    comment_word_set = set(comment_word_list)

    # Find the words shared by the test comment and the positive-specific training words.
    found_pos = set.intersection(pos_token_final, comment_word_set)

    # Find the words shared by the test comment and the negative-specific training words.
    found_neg = set.intersection(neg_token_final, comment_word_set)

    # Count the positive-specific words found in the test comment.
    found_pos_n = len(found_pos)

    # Count the negative-specific words found in the test comment.
    found_neg_n = len(found_neg)

    # If more positive-specific words are found, classify the comment as positive.
    if found_pos_n > found_neg_n:
        # Add the positive prediction to the results list.
        comp_res.append("pos")

    # If more negative-specific words are found, classify the comment as negative.
    elif found_neg_n > found_pos_n:
        # Add the negative prediction to the results list.
        comp_res.append("neg")

    # If the two counts are equal, including when both are zero, classify as neutral.
    else:
        # Add the neutral prediction to the results list.
        comp_res.append("neut")


# Load the file containing positive training comments.
pos_comm = file_loader("movie_comments_pos_training.txt")

# Read the positive training file one line at a time.
for line in pos_comm:
    # Extract tokens from the current line and add them to the positive token list.
    add_tokens(line, "pos")

# Print the sorted positive token list for inspection (currently commented out).
# print(sorted(pos_tokens))

# Load the file containing negative training comments.
neg_comm = file_loader("movie_comments_neg_training.txt")

# Read the negative training file one line at a time.
for line in neg_comm:
    # Extract tokens from the current line and add them to the negative token list.
    add_tokens(line, "neg")

# Print the sorted negative token list for inspection (currently commented out).
# print(sorted(neg_tokens))

# Convert the positive token list into a set to remove duplicates across comments.
pos_token_set = set(pos_tokens)

# Convert the negative token list into a set to remove duplicates across comments.
neg_token_set = set(neg_tokens)

# Find the tokens that occur in both the positive and negative training collections.
common_tokens = set.intersection(pos_token_set, neg_token_set)

# Print the sorted common tokens for inspection (currently commented out).
# print(sorted(common_tokens))

# Remove shared tokens from the positive set, leaving positive-specific tokens.
pos_token_final = pos_token_set - common_tokens

# Remove shared tokens from the negative set, leaving negative-specific tokens.
neg_token_final = neg_token_set - common_tokens

# Print the sorted positive-specific tokens for inspection (currently commented out).
#print(sorted(pos_token_final))

# Print the sorted negative-specific tokens for inspection (currently commented out).
#print(sorted(neg_token_final))

# Load the file containing test comments.
test_comm = file_loader("movie_comments_test.txt")

# Read the test file one comment at a time.
for line in test_comm:
    # Classify the current test comment and add its predicted label to comp_res.
    comp_comm(line)

# Print the list of predicted labels for all test comments, in their original order.
print(comp_res)

# Initialize a counter for the number of correct predictions.
correct_n = 0

# Loop through the indices of the first 20 test comments (0 through 19).
for index in range(0, 20):

    # Assume that comments at indices 0–9 are positive.
    # Count a prediction as correct if it is "pos".
    if index < 10 and comp_res[index] == "pos":
        correct_n += 1

    # Assume that comments at indices 10–19 are negative.
    # Count a prediction as correct if it is "neg".
    elif index >= 10 and comp_res[index] == "neg":
        correct_n += 1

# Print the total number of correct predictions.
print(correct_n)

# Calculate and print accuracy: correct predictions divided by the total number of predictions.
print(correct_n / len(comp_res))