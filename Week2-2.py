final_msg = None

def verb_like(subj, obj):
    global final_msg
    final_msg = subj + " likes " + obj

verb_like("John", "Mary")
print(final_msg)

def verb_like_pas(subj, obj):
    global final_msg
    final_msg = obj + " is liked by " + subj

verb_like_pas("John", "Mary")
print(final_msg)