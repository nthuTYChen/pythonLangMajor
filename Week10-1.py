import re

keywords_set = set()

def line_process(text):
    all_word_tokens = []
    stop_words = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been",
                  "to", "of", "in", "on", "at", "for", "from", "with", "this", "that", "these", "those",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her", "its", "our",
                  "their", "as", "by", "if", "not", "so"}
    for line in text:
        line_new = line.strip()
        if re.search(r"^(From:)|(To:)", line_new) is None and len(line_new) > 0:
            puncs_re = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"
            line_clean = re.sub(puncs_re, "", line_new)
            line_lower = line_clean.lower()
            token_list = line_lower.split(" ")
            all_word_tokens.extend(token_list)
    all_word_tokens_set = set(all_word_tokens)
    all_word_tokens_nostop = all_word_tokens_set - stop_words
    global keywords_set
    if len(keywords_set) == 0:
        keywords_set = all_word_tokens_nostop
    else:
        keywords_set = set.intersection(keywords_set, all_word_tokens_nostop)

for n in range(1, 6):
    filename = "email-sample-" + str(n) + ".txt"
    email_reader = open("sources/" + filename, encoding = "utf-8")
    line_process(email_reader)

print(sorted(keywords_set))