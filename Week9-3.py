import re

sample_str = "treatment"

pattern1 = r"t(\w+)t"

search_res = re.search(pattern1, sample_str)

print(search_res.group(1))

pattern2 = r"t(\w+?)t"

search_res = re.search(pattern2, sample_str)

print(search_res.group(1))

