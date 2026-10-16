subjs_objs = [
    ("John", "Mary"),
    ("the cat", "the dog"),
    ("a person", "a bee")
]

print(subjs_objs[0])

for subj, obj in subjs_objs:
    print("Original: " + subj + " likes " + obj)
    subj, obj = (obj, subj)
    print("Switched: " + subj + " likes " + obj)
    print("------")

freq_table = {
    "like": 42,
    "him": 107,
    "success": 17
}

for item in freq_table.items():
    print(type(item))
    print(item)

for word, freq in freq_table.items():
    print(word + ": " + str(freq))

