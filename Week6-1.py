# Dictionary

new_dict = {} # Empty dictionary

lex_pos = {"love": "verb", "cake": "noun", "of": "prep"}

print(lex_pos["love"])
print(lex_pos["cake"])

lex_pos["love"] = "noun"
print(lex_pos["love"])

lex_pos["great"] = "adj"
print(lex_pos["great"])

print(lex_pos)

lex_pos["great"] = "adjective"

print(lex_pos)

like_def = {
    "spelling": "like",
    "IPA": "laik",
    "meaning": "to enjoy something",
    "synonyms": ["admire", "appreciate", "love"]
}

like_syn = like_def["synonyms"]
print(type(like_syn))

print(like_syn[0])
print(like_syn[1])