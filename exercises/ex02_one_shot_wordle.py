"""Something about only having one try to guess a word!"""

__author__: str = "730482131"

# Variables
secret_word: str = "python"
i: int = 0
j: int = 0
squares: str = ""

# Prompts
word: str = input("What is your 6-letter guess? ")
while len(word) != 6:
    word = input("That was not 6 letters! Try again: ")

# Checks which color block to add to the final result
while i <= 5:
    j = 0
    if word[i] == secret_word[i]:
        squares += "\U0001F7E9"
        i += 1
    else:
        while j <= 5:
            if word[i] == secret_word[j]:
                squares += "\U0001F7E8"
                i += 1
                j = 6
            else:
                j += 1
                if j == 6:
                    squares += "\U00002B1C"
                    i += 1

# Final messages
print(squares)
if word != secret_word:
    print("Not quite. Play again soon!")
elif word == secret_word:
    print("Woo! You got it!")