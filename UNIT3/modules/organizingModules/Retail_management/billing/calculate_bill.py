def calculate__bill(cart):
    total = sum(item['price'] * item['quantity'] for item in cart)
    return total
