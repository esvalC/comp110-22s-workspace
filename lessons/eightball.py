"""I know ur future!"""

from random import randint

input("Ask a yes or no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Hell yeah!!!")
elif response == 1:
    print("Eh, I'll get back to you...")
elif response == 2:
    print("Yeah.... Fuck no.")
elif response == 3:
    print("Thats none of ur business.")
