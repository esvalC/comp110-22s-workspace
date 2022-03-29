"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute defs
    size: str = "Small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initializing attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate price of pizza."""
        total: float = 0.0

        if self.size == "Large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1

        total *= tax

        return total


a_pizza: Pizza = Pizza("Large", 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("Small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")
