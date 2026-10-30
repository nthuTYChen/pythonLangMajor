import re

pattern = "vampire"

result = re.search(pattern, "I love vampire!")
print(result)

result = re.search(pattern, "I love Vampire!")
print(result)

pattern = "(V|v)ampire"

result = re.search(pattern, "I love vampire!")
print(result)

result = re.search(pattern, "I love Vampire!")
print(result)

pattern = "(V|v)ampires*"

result = re.search(pattern, "I love vampire!")
print(result)

result = re.search(pattern, "I love Vampire!")
print(result)

result = re.search(pattern, "How many vampires do we have to see in this demo?")
print(result)