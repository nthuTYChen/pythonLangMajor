import re

pos_tokens = []
neg_tokens = []
comp_res = []

def file_loader(filename):
    text_reader = open("sources/" + filename, encoding = "utf-8")
    return text_reader

def tokenizer(comment):
    stop_words = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
                  "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
                  "their", "as", "by", "if", "not", "so"}
    puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"

    comment_new = comment.strip()
    comment_clean = re.sub(puncs_re, "", comment_new)
    comment_lower = comment_clean.lower()
    comment_words = comment_lower.split(" ")
    comment_words_set = set(comment_words)
    comment_words_nostop = comment_words_set - stop_words
    comment_words_nostop_list = list(comment_words_nostop)
    return comment_words_nostop_list

def add_tokens(comment, comment_type):
    comment_word_list = tokenizer(comment)
    if comment_type == "pos":
        pos_tokens.extend(comment_word_list)
    else:
        neg_tokens.extend(comment_word_list)

def comp_comm(comment):
    comment_word_list = tokenizer(comment)
    comment_word_set = set(comment_word_list)
    found_pos = set.intersection(pos_token_final, comment_word_set)
    found_neg = set.intersection(neg_token_final, comment_word_set)
    found_pos_n = len(found_pos)
    found_neg_n = len(found_neg)
    if found_pos_n > found_neg_n:
        comp_res.append("pos")
    elif found_neg_n > found_pos_n:
        comp_res.append("neg")
    else:
        comp_res.append("neut")

pos_comm = file_loader("movie_comments_pos_training.txt")

for line in pos_comm:
    add_tokens(line, "pos")

# print(sorted(pos_tokens))

neg_comm = file_loader("movie_comments_neg_training.txt")

for line in neg_comm:
    add_tokens(line, "neg")

# print(sorted(neg_tokens))

pos_token_set = set(pos_tokens)
neg_token_set = set(neg_tokens)

common_tokens = set.intersection(pos_token_set, neg_token_set)

# print(sorted(common_tokens))

pos_token_final = pos_token_set - common_tokens
neg_token_final = neg_token_set - common_tokens

#print(sorted(pos_token_final))
#print(sorted(neg_token_final))

test_comm = file_loader("movie_comments_test.txt")

for line in test_comm:
    comp_comm(line)

print(comp_res)

correct_n = 0

for index in range(0, 20):
    if index < 10 and comp_res[index] == "pos":
        correct_n += 1
    elif index >= 10 and comp_res[index] == "neg":
        correct_n += 1

print(correct_n)
print(correct_n / len(comp_res))