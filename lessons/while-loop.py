"""An example of a while loop statement."""

counter: int = 0
maximum: int = int(input("What number do you want to count to and square? "))

while counter < maximum + 1:
    counter_squared: int = counter ** 2
    print(counter)
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")