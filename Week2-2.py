# Create a global variable named final_msg and initialize it with None
final_msg = None

# Define a function named verb_like that takes a subject and an object as arguments
def verb_like(subj, obj):
    # Declare that the function will use and modify the global variable final_msg
    global final_msg
    # Create an active-voice sentence by combining the subject and object with "likes"
    final_msg = subj + " likes " + obj

# Call verb_like with "John" as the subject and "Mary" as the object
verb_like("John", "Mary")

# Print the sentence stored in the global variable final_msg
print(final_msg)

# Define a function named verb_like_pas that takes a subject and an object as arguments
def verb_like_pas(subj, obj):
    # Declare that the function will use and modify the global variable final_msg
    global final_msg
    # Create a passive-voice sentence by combining the object, "is liked by", and the subject
    final_msg = obj + " is liked by " + subj

# Call verb_like_pas with "John" as the subject and "Mary" as the object
verb_like_pas("John", "Mary")
