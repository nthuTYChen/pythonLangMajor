str_ls = ["love", "admire", "cherish", "treasure"]

print("admire" in str_ls)
print("admire" not in str_ls)
print("adore" in str_ls)
print("adore" not in str_ls)

if "adore" in str_ls:
    print("It does exist!")
else:
    print("It doesn't exist!")

new_str_ls = ["a", "cat", "loves", "a", "dog"]

final_ls = []

for word in new_str_ls:
    if word not in final_ls:
        final_ls.append(word)

print(final_ls)