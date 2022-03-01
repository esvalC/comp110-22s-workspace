"""Writing a function that interrogates a list to see what its hiding!!!"""


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("YU IN DA CLUB!!")
    else:
        print("no.")


def contains(needle: str, haystack: list[str]) -> bool:
    """Check the yeah."""
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()