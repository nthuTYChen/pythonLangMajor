import re  # Import Python's regular expression module for text processing.

# Open the file containing negative movie comments.
# encoding="utf-8" specifies the character encoding used to read the file.
neg_comm = open("sources/movie_comments_neg_training.txt", encoding = "utf-8")

# Open the file containing positive movie comments.
pos_comm = open("sources/movie_comments_pos_training.txt", encoding = "utf-8")

# Create an empty list to store tokens extracted from negative comments.
neg_tokens = []

# Create an empty list to store tokens extracted from positive comments.
pos_tokens = []

# Define a function to process one comment line at a time.
# line is the comment text; comment_type indicates whether it is positive or negative.
def line_process(line, comment_type):

    # Define a set of common words to exclude from the analysis.
    # A set is used because it stores unique items and supports efficient membership checks.
    stop_words = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
                  "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
                  "their", "as", "by", "if", "not", "so"}

    # Remove whitespace characters (including the newline character) from the beginning and end of the line.
    line_new = line.strip()

    # Define a regular expression character class containing punctuation marks to remove.
    # [ ... ] matches any ONE character listed inside the brackets.
    # \. matches a literal period; the backslash prevents . from acting as a wildcard.
    # The other punctuation marks are included as literal characters or escaped where necessary.
    puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"

    # Remove every punctuation mark matching the regular expression by replacing it with an empty string.
    # re.sub() replaces all matches, not just the first one.
    line_clean = re.sub(puncs_re, "", line_new)

    # Convert all letters to lowercase so that words with different capitalization are treated as identical.
    line_lower = line_clean.lower()

    # Split the comment into tokens wherever a space occurs.
    # The result is a list of strings; multiple consecutive spaces may produce empty strings.
    token_list = line_lower.split(" ")

    # Convert the list into a set to remove duplicate tokens within this comment.
    token_set = set(token_list)

    # Use set difference (-) to remove all words that also appear in stop_words.
    # The resulting set contains a set of tokens that are not in the stop-word list.
    token_nostop = token_set - stop_words

    # Convert the set back into a list so that its elements can be added to the global token lists.
    # Note that the order of elements in this list is not guaranteed.
    token_nostop_list = list(token_nostop)

    # Check whether the current comment is positive.
    if comment_type == "pos":

        # Add all remaining tokens to the positive-comment token list.
        # extend() adds each element individually, rather than adding the whole list as one element.
        pos_tokens.extend(token_nostop_list)

    # If comment_type is not "pos", treat the comment as negative.
    else:

        # Add all remaining tokens to the negative-comment token list.
        neg_tokens.extend(token_nostop_list)


# Read the negative-comment file one line at a time.
# Each line is passed to line_process() with "neg" as its comment type.
for line in neg_comm:
    line_process(line, "neg")

# Read the positive-comment file one line at a time.
# Each line is passed to line_process() with "pos" as its comment type.
for line in pos_comm:
    line_process(line, "pos")


# Print the positive token list (currently commented out, so this statement is not executed).
# print(pos_tokens)

# Print the negative token list (currently commented out, so this statement is not executed).
# print(neg_tokens)


# Convert the positive token list into a set to remove duplicates across all positive comments.
pos_tokens_set = set(pos_tokens)

# Convert the negative token list into a set to remove duplicates across all negative comments.
neg_tokens_set = set(neg_tokens)

# Find the intersection of the two sets.
# This produces the tokens that occur in BOTH the positive and negative comment collections.
common_tokens = set.intersection(pos_tokens_set, neg_tokens_set)

# Print the tokens that appear in both collections.
print(common_tokens)

# Subtract the common tokens from the positive token set.
# The result contains tokens found in positive comments but not in negative comments.
pos_tokens_final = pos_tokens_set - common_tokens

# Subtract the common tokens from the negative token set.
# The result contains tokens found in negative comments but not in positive comments.
neg_tokens_final = neg_tokens_set - common_tokens

# Print the tokens found only in positive comments.
print(pos_tokens_final)

# Print the tokens found only in negative comments.
print(neg_tokens_final)