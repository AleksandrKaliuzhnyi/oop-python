# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
# print(type(item1))


class Item:
    # method, not function
    def calculate_total_price(self, x, y):
        return x * y


ite1 = Item()
ite1.name = "Phone"
ite1.price = 100
ite1.quantity = 5
# item = self, item1.price = x and item1.quantity = y
print(ite1.calculate_total_price(ite1.price, ite1.quantity))

ite2 = Item()
ite2.name = "Laptop"
ite2.price = 1000
ite2.quantity = 3
print(ite2.calculate_total_price(ite2.price, ite2.quantity))
