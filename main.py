# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
# print(type(item1))


class Item:
    # constructor
    def __init__(self, name: str, price: float, quantity: int):
        # Validation for the receive arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # method, not function
    def calculate_total_price(self):
        return self.price * self.quantity


# 1st line is an instance
ite1 = Item("Phone", 100, 5)
# 1st line is an instance
ite2 = Item("Laptop", 1000, 3)

print(ite1.calculate_total_price())
print(ite2.calculate_total_price())
