# Variable declaration and value assignment
num = 7
msg = "This is a message."

# Boolean value; Boolean variable
sen_complete = False
new_process = True

# None means a variable does not have real value just yet. It does not mean
# the variable is EMPTY (because None is assigned to it).
first_wd = None

# You can have access to a variable only AFTER it is declared, so the next line
# leads to a bug.
# print(first_sound)
first_sound = None
print(first_sound)

# Re-assign a value to the same variable
first_sound = "p"
print(first_sound)

# Value assignment
num_x = 25
num_y = 11
# Operations that work with variables rather than values
sum_xy = num_x + num_y
print(sum_xy)

# Using a sentence template as an example - You can have
# different words as the subject, verb, and object, but
# the result of the operation is the same: The output
# is always a Subject-Verb-Object sentence.
subj = "John"
verb = "likes"
obj = "Mary"
svo_sen = subj + " " + verb + " " + obj
print(svo_sen)
