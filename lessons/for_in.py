"""An example of for in syntax."""

names: list[str] = ["Cal", "Jackie", "Hugh", "Danny"]

# Example of iterating though names using while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# for...in loop which does the same as above
for name in names:
    print(name)