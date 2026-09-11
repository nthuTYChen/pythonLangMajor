# Debugging practices

# Bug 1: Syntax Error - Missing the closing quotation mark for the end of a string
print("This is a string.)

# Bug 2: Semantic Error - Python programming is case-sensitive, so Print() is
# different from print()
Print("This is a string.")

# Bug 3: Semantic Error - It's type(), not typ(). Typos are common causes of bugs.
print(typ("This is a string"))