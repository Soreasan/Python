# Kenneth Adair
# This demos python packages and linking multiple files together
# Taken from Learning to Program Part 2 on Pluralsight
# In order to run use python3 or it won't load correctly
import sales.shopping_cart, sales.shopping_order

cart = sales.shopping_cart.Cart()
order = sales.shopping_order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = sales.shopping_order.Order()
    order.get_input()

print(cart)
