num_ls = [10, 20, 31, 1, 5]
str_ls = ["love", "admire", "cherish", "treasure"]

# Iteration; iterability

for verb in str_ls:
    sing_form = verb + "s"
    print(sing_form)

sen_words = ["John", "loves", "Mary"]

final_sen = ""

for word in sen_words:
    final_sen = final_sen + word + " "

print(final_sen)

total_num = 0

for num in num_ls:
    # total_num = total_num + num
    total_num += num

print(total_num)

sort_num = sorted(num_ls)
print(sort_num)

sort_num_des = sorted(num_ls, reverse = True)
print(sort_num_des)

sort_str = sorted(str_ls)
print(sort_str)

total_num_new = sum(num_ls)
print(total_num_new)

max_num = max(num_ls)
min_num = min(num_ls)
print(max_num)
print(min_num)