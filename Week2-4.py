print(type("This is string"))

def return_str():
    return "Are you calling me?"

res = return_str()
print(res)

def self_check(subj_check, obj_check):
    if subj_check == obj_check:
        return "himself"
    else:
        return obj_check

def verb_like_4(subj, obj):
    new_obj = self_check(subj, obj)
    final_sen = subj + " likes " + new_obj
    print(final_sen)

verb_like_4("John", "Mary")
verb_like_4("John", "John")