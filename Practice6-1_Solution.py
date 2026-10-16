# This script tries to complete the following tasks:
# 1. Split the "sample_sen" string into a list of individual word tokens "word_tokens"
#    with a single space character as the delimiter.
# 2. Iterate through "word_tokens"  in a for loop.
# 3. In the for loop in (3), check if each word in "word_tokens" is included in the
#    "stop_words" list.
# 4. If a word DOES NOT appear in "stop_words", add the word to the dictionary "word_dict"
#    with the word itself as the key, and "non-stop word" as its value.
# 5. If a word DOES appear in "stop_words", add the word to "word_dict", with the word
#    itself as the key, and "stop word" as its value.
# 6. Print all the values in "word_dict".
#
# Note: There are no bugs between line 14 and line 27.

stop_words = [
    "a", "an", "the", "and", "or", "but",
    "is", "am", "are", "was", "were", "be",
    "have", "has", "had", "do", "does", "did",
    "in", "on", "at", "to", "from", "of",
    "for", "with", "by", "as", "it", "this",
    "that", "these", "those", "i", "you", "he",
    "she", "we", "they", "my", "your", "their",
    "not", "so", "if", "then", "than", "too"
]

sample_sen = "a dictionary is a perfect choice when you need to present mixed data types"
word_dict = {}

# Bug 1: The English sentence should be split into individual tokens by ONE space, rather than
#        two.
word_tokens = sample_sen.split(" ")

for word in word_tokens:
    # Bug 2: If a word is "not in" stop_words, label it as a "non-stop word"
    if word not in stop_words:
        # Bug 3: You should specify the variable name "word" to refer to each
        # each value retrieved from word_tokens and assigned to the local variable
        # word.
        word_dict[word] = "non-stop word"
    # Bug 4: Missing a colon for the "else" code block
    else:
        # Bug 5: The same as Bug 3
        word_dict[word] = "stop word"

# Bug 6: You should just print the values from the dictionary object,
# rather than the entire dictionary object.
print(word_dict.values())

# Intended output:
# dict_values(['stop word', 'non-stop word', 'stop word', 'non-stop word',
# 'non-stop word', 'non-stop word', 'stop word', 'non-stop word', 'stop word',
# 'non-stop word', 'non-stop word', 'non-stop word', 'non-stop word'])