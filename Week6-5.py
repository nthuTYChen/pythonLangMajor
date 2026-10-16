str_list = ["John", "likes", "Mary"]
str_set = set(str_list)
print(str_set)

# A set is mutable

str_set.add("and")
print(str_set)

str_set.remove("John")
print(str_set)

# Values are not strictly ordered in a set
print(str_list[0])
# print(str_set[0])

str_list.pop(0)
print(str_list)
str_set.pop()
print(str_set)

sen_sample = "I am not a religious person so I do not believe in God"
sen_tokens = sen_sample.split(" ")
print(sen_tokens)

sen_types = set(sen_tokens)
print(sen_types)

sen_types.add("I")
print(sen_types)

sen_sample2 = "There is really no God because I have never seen one"
sen_tokens2 = sen_sample2.split(" ")
sen_types2 = set(sen_tokens2)
print(sen_types2)

sen_inter = set.intersection(sen_types, sen_types2)
print(sen_inter)

sen_comp = sen_types - sen_types2
print(sen_comp)