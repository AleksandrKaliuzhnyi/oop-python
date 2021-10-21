from item import Item


class Phone(Item):
    # constructor
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Validation for the receive arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal than zero!"

        # Assign to self object
        self.broken_phones = broken_phones