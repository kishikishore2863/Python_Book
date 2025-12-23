from inventory.add_product import add_product
from billing.calculate_bill import calculate__bill
from utilities.logger import log_message

log_message("Application start")
add_product("Loptop",10)
cart = [
    {'name':'laptop','price':10000,'quantity':2},
    {'name':'Mouse','price':250,'quantity':4}
]

total = calculate__bill(cart)
log_message(f"The total bill is: Rs{total}")