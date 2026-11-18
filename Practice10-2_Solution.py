# 1
import re
pos_comments = open("sources/movie_comments_pos_training.txt", encoding="utf-8")
# 2
stop_words = ["a", "an", "the",
    "and", "or", "but",
    "is", "are", "was", "were", "be", "been",
    "to", "of", "in", "on", "at", "for", "from", "with",
    "this", "that", "these", "those",
    "i", "you", "he", "she", "it", "we", "they",
    "my", "your", "his", "her", "its", "our", "their",
    "as", "by", "if", "not", "so"]
# 3
puncs_pattern = r"[\.,!?;:'()[\]{}\-_/@#$%&*]"
# 4
pos_adj_pattern = r"(is|are|am|was|were)\s(\w+)"
# 5
possible_pos_adj = set()
# 6
for comment in pos_comments:
    # 7a
    comment_no_puncs = re.sub(puncs_pattern, "", comment)
    # 7b
    comment_lower = comment_no_puncs.lower()
    # 7c
    search_res = re.search(pos_adj_pattern, comment_lower)
    # 7d
    if search_res is not None:
        # We have two groups in the phrase pattern, and the potential adjective
        # is in the second group
        target_str = search_res.group(2)
        if target_str not in stop_words:
            possible_pos_adj.add(target_str)

# 8
print(sorted(possible_pos_adj))