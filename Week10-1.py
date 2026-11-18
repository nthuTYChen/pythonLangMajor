# Import Python's regular expression module.
import re

# Create an empty set to store keywords shared across the email files.
# A set stores unique elements and does not preserve a guaranteed order.
keywords_set = set()

# Define a function to process the contents of an email file.
# text is the file object passed to this function.
def line_process(text):

    # Create an empty list to collect word tokens from the file.
    all_word_tokens = []

    # Define a set of common English stop words.
    # These words will be excluded from the final keyword set.
    # A set is useful here because it supports efficient membership testing
    # and set operations.
    stop_words = {
        "a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
        "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
        "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
        "their", "as", "by", "if", "not", "so"
    }

    # Read the email file one line at a time.
    for line in text:

        # Remove leading and trailing whitespace, including newline characters.
        line_new = line.strip()

        # Check two conditions:
        # 1. The line does NOT begin with "From:" or "To:".
        # 2. The line is not empty (its length is greater than zero).
        # We don't need these lines because our focus is not processing email
        # addresses and full names.
        # re.search() returns None if the contact-line pattern is not found.
        # and requires both conditions to be True.
        if re.search(r"^(From:)|(To:)", line_new) is None and len(line_new) > 0:

            # Define a regular expression character class containing punctuation.
            # [...] matches any ONE character listed inside the brackets.
            # The backslash escapes characters that have special meanings in regex,
            # such as . and [ and ].
            puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"

            # Remove every character matching the punctuation pattern.
            # re.sub() replaces each match with an empty string.
            # For example, "don't!" becomes "dont".
            line_clean = re.sub(puncs_re, "", line_new)

            # Convert the entire line to lowercase.
            # This makes words such as "Python" and "python" identical.
            line_lower = line_clean.lower()

            # Split the line into tokens using a space as the delimiter.
            # The result is a list of strings.
            token_list = line_lower.split(" ")

            # Add all tokens from token_list to all_word_tokens.
            # extend() adds individual list elements rather than the entire list.
            all_word_tokens.extend(token_list)

    # Convert the list of tokens into a set.
    # This removes duplicate words within the current email file.
    all_word_tokens_set = set(all_word_tokens)

    # Remove all stop words using set difference (-).
    # The resulting set contains unique tokens that are not in stop_words.
    all_word_tokens_nostop = all_word_tokens_set - stop_words

    # Declare that keywords_set refers to the global variable defined outside
    # this function, rather than creating a new local variable.
    global keywords_set

    # Check whether keywords_set is currently empty.
    if len(keywords_set) == 0:

        # For the first email file, initialize keywords_set with all the
        # non-stop-word tokens found in that file.
        keywords_set = all_word_tokens_nostop

    # If keywords_set is not empty, this is not the first file being processed.
    else:

        # Keep only the words that occur in BOTH keywords_set and
        # all_word_tokens_nostop.
        # set.intersection() returns a new set containing shared elements.
        # This gradually identifies words appearing in every email file.
        keywords_set = set.intersection(keywords_set, all_word_tokens_nostop)


# Use range(1, 6) to generate the numbers 1, 2, 3, 4, and 5.
# Each number corresponds to one of the five email sample files.
for n in range(1, 6):

    # Construct the filename using the current number.
    # str(n) converts the integer to a string so it can be concatenated.
    filename = "email-sample-" + str(n) + ".txt"

    # Open the corresponding email file for reading using UTF-8 encoding.
    email_reader = open("sources/" + filename, encoding = "utf-8")

    # Pass the open file object to line_process() for processing.
    # The function reads the file and updates the global keywords_set.
    line_process(email_reader)

# Sort the keywords alphabetically and print the resulting list.
# sorted() returns a new sorted list without modifying the original set.
print(sorted(keywords_set))