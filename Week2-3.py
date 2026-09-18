# just_true = True
just_true = False

if just_true:
    print("It's true!")
else:
    print("It's False!")

print("It's true!") if just_true else print("It's False!")

def verb_like_2(subj, obj, verb_sing):
    final_sen = None
    if verb_sing:
        final_sen = subj + " likes " + obj
    else:
        final_sen = subj + " like " + obj
    print(final_sen)

verb_like_2("John", "Mary", True)
verb_like_2("I", "Mary", False)

def verb_like_3(subj, obj, verb_sing = True):
    final_sen = None
    if verb_sing:
        final_sen = subj + " likes " + obj
    else:
        final_sen = subj + " like " + obj
    print(final_sen)

verb_like_3("John", "Mary")
verb_like_3("I", "Mary", False)