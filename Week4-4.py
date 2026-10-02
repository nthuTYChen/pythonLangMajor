str_ls = ["love", "admire", "cherish", "treasure"]

print(str_ls[1:3])
print(str_ls[:2])
print(str_ls[2:])

print(str_ls[-1])
print(str_ls[-2])
print(str_ls[-2:])

str_ls_new = ["like", "adore"]

str_ls_all = str_ls + str_ls_new
print(str_ls_all)

str_ls_rep = str_ls_new * 2
print(str_ls_rep)

str_ls.append("adore")
print(str_ls)

str_ls.pop(0)
print(str_ls)

str_ls.remove("treasure")
print(str_ls)

sen_sample = "John likes Mary"

# Tokenization
sen_words = sen_sample.split(" ")
print(sen_words)

# sen_ch_sample = "陳宗穎"
# sen_words_ch = sen_ch_sample.split("")
# print(sen_words_ch)

sep_ch = " " # Delimiter
final_sen = sep_ch.join(sen_words)
print(final_sen)

