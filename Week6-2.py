lex_pos = {"love": "verb", "cake": "noun", "of": "prep"}

for key in lex_pos:
    print(key)

print(lex_pos.values())

for value in lex_pos.values():
    print(value)

print("hate" in lex_pos)
print("love" in lex_pos)
print("prep" not in lex_pos)

print("adv" not in lex_pos.values())
print("noun" not in lex_pos.values())

like_def = {
    "spelling": "like",
    "IPA": "laik",
    "meaning": "to enjoy something",
    "synonyms": ["admire", "appreciate", "love"]
}

print("admire" in like_def.values())
print("admire" in like_def["synonyms"])

lex_pos["chair"] = "noun"
print(lex_pos)

POS_freq = {}
for pos in lex_pos.values():
    if pos not in POS_freq:
        POS_freq[pos] = 1
    else:
        # Or just POS_freq[pos] += 1
        POS_freq[pos] = POS_freq[pos] + 1

print(POS_freq)