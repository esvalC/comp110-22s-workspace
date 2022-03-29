""" Examples of default parameters"""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Defaunt parameters give more flexibility to a fxn."""
    # Defaunt parameters mustf ollow required parameters
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))