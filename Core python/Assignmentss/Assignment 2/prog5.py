# Calculate selling price of a book based on cost price and discount
cost_price = float(input("Enter cost price of book: "))
discount_percent = float(input("Enter discount percentage: "))

discount = cost_price * discount_percent / 100
selling_price = cost_price - discount

print("Discount =", discount)
print("Selling Price =", selling_price)