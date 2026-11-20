# (1)
pos_word_list = []

# (2)
pos_word_reader = open("sources/movie_comments_pos_unique.txt", encoding = "utf-8")

# (3)
for word in pos_word_reader:
    pos_word_list.append(word.strip())

# (4)
sample_comm = "A captivating and heartwarming film with brilliant performances stunning cinematography and a beautifully crafted storyline that leaves a lasting impression"

# (5)
sample_comm_list = sample_comm.split(" ")

# (6)
pos_word_count = 0

# (7)
for word in sample_comm_list:
    if word in pos_word_list:
        # pos_word_count += 1 is equivalent to pos_word_count = pos_word_count + 1
        pos_word_count += 1

# (8)
print(pos_word_count / len(sample_comm_list))

# Close the reader
pos_word_reader.close()