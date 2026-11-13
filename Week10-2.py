import re

neg_comm = open("sources/movie_comments_neg_training.txt", encoding = "utf-8")
pos_comm = open("sources/movie_comments_pos_training.txt", encoding = "utf-8")

neg_tokens = []
pos_tokens = []

def line_process(line, comment_type):
    stop_words = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
                  "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
                  "their", "as", "by", "if", "not", "so"}
    line_new = line.strip()
    puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"
    line_clean = re.sub(puncs_re, "", line_new)
    line_lower = line_clean.lower()
    token_list = line_lower.split(" ")
    token_set = set(token_list)
    token_nostop = token_set - stop_words
    token_nostop_list = list(token_nostop)
    if comment_type == "pos":
        pos_tokens.extend(token_nostop_list)
    else:
        neg_tokens.extend(token_nostop_list)

for line in neg_comm:
    line_process(line, "neg")

for line in pos_comm:
    line_process(line, "pos")

# print(pos_tokens)
# print(neg_tokens)

pos_tokens_set = set(pos_tokens)
neg_tokens_set = set(neg_tokens)

common_tokens = set.intersection(pos_tokens_set, neg_tokens_set)

print(common_tokens)

pos_tokens_final = pos_tokens_set - common_tokens
neg_tokens_final = neg_tokens_set - common_tokens

print(pos_tokens_final)
print(neg_tokens_final)