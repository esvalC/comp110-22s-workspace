"""Lets play a game lol."""


from random import randint


rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove item from list from index
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum values of rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")


# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Access length of list
# print(len(rolls))

# # Access last item in list
# print(rolls[len(rolls) - 1]) # Or print(rolls[last_index])
