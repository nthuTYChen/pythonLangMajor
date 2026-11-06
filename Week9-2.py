import re

svo_sens = ["I love Python", "you like phonology", "Mike hates linguistics"]

pattern1 = r"\s\w+\s"

for sen in svo_sens:
    search_res = re.search(pattern1, sen)
    if search_res is not None:
        print(sen)

pattern2 = r"\s(\w+)\s"

for sen in svo_sens:
    search_res = re.search(pattern2, sen)
    if search_res is not None:
        print(search_res.group(1))
