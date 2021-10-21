import csv


class Item:
    # The pay rate after 20% discount
    pay_rate = 0.8
    all = []

    # constructor
    def __init__(self, name: str, price: float, quantity: int):
        # Validation for the receive arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    # method, not function
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_fom_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the float that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}')"
