# Simple Shopping Cart

# Take customer name as input
customer_name = input("Enter customer name: ")

# Take names and prices of three products
product1 = input("Enter Product 1 name: ")
price1 = float(input("Enter Product 1 price: "))

product2 = input("Enter Product 2 name: ")
price2 = float(input("Enter Product 2 price: "))

product3 = input("Enter Product 3 name: ")
price3 = float(input("Enter Product 3 price: "))

# Calculate subtotal
subtotal = price1 + price2 + price3

# Determine discount rate
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

# Calculate discount and final total
discount = subtotal * discount_rate
final_total = subtotal - discount

# Display shopping summary
print("\n----- Shopping Summary -----")
print(f"Customer Name: {customer_name}")

print(f"\nProduct 1: {product1}")
print(f"Price: {price1:g}")

print(f"\nProduct 2: {product2}")
print(f"Price: {price2:g}")

print(f"\nProduct 3: {product3}")
print(f"Price: {price3:g}")

print(f"\nSubtotal: {subtotal:g}")
print(f"Discount: {discount:g}")
print(f"Final Total: {final_total:g}")
