# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
# print(type(item1))


class Item:
    # The pay rate after 20% discount
    pay_rate = 0.8

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

    def apply_discount(self):
        self.price = self.price * self.pay_rate


# 1st line is an instance
item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)
# 1st line is an instance
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# print(Item.pay_rate)
# # All the attributes from the Class level
# print(Item.__dict__)
# # Firstly try to find pay_rate in the instance level, and after on the class level
# print(item1.pay_rate)
# # All the attributes from the instance level
# print(item1.__dict__)
