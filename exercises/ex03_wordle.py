"""This a wordle or smthn..."""

__author__: str = "730482131"


def contains_char(sword: str, char: str) -> bool:
    """CHECK A LETTER (or two, if u wanna be fancy) to see if its there."""
    assert len(char) == 1
    contains_char: bool = False
    i: int = 0
    while i < len(sword):
        if sword[i] == char:
            contains_char = True
            return (contains_char)
        else:
            contains_char = False
            i += 1
    return (contains_char)


def emojified(sword: str, guess: str) -> str:
    """Lets get some emojis on in here!"""
    assert len(guess) == len(sword)
    emojified: str = ""
    j: int = 0
    while j < len(sword):
        if contains_char(guess[j], sword[j]):
            emojified += "\U0001F7E9"
            j += 1
        elif contains_char(guess, sword[j]):
            emojified += "\U0001F7E8"
            j += 1
        else:
            emojified += "\U00002B1C"
            j += 1
    return (emojified)


def input_guess(tries: int) -> str:
    """Checking da numbers and stuf."""
    input_guess: str = input(f"Enter a {tries} character word: ")
    while len(input_guess) != tries:
        input_guess = input(f"That wasn't {tries} chars! Try again: ")
    return (input_guess)


def main() -> None:
    """Main game loop or smthn, idk, im confused (not really)."""
    sword: str = "codes"
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        if guess == sword:
            print(emojified(guess, sword))
            print(f"You won in {turn}/6 turns!")
            turn = 7
        else:
            print(emojified(guess, sword))
            turn += 1
            if turn == 7:
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()