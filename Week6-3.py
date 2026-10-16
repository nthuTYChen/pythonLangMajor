str_ls = ["love", "admire", "cherish", "treasure"]
print(type(str_ls))
str_tp = ("love", "admire", "cherish", "treasure")
print(type(str_tp))

print(str_ls[0])
print(str_tp[0])

str_ls_big = str_ls + ["like", "appreciate"]
print(str_ls_big)
str_tp_big = str_tp + ("like", "appreciate")
print(str_tp_big)

# Tuples are immutable
# str_tp_big[0] = "adore"
# str_tp_big.pop(0)
# str_tp_big.remove("love")
# str_tp_big.append("adore")

# Tuple assignment
name1 = "John"
name2 = "Mary"
subj_obj = (name1, name2)
print(subj_obj)
subj_obj_list = [name1, name2]
print(subj_obj_list)

subj_list = subj_obj_list[0]
obj_list = subj_obj_list[1]

subj_tp, obj_tp = subj_obj
print(subj_tp)
print(obj_tp)

# verb1, verb2 = str_tp_big

subj_tp, obj_tp = (obj_tp, subj_tp)
print(subj_tp)
print(obj_tp)