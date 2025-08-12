def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if applicable"""
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"After applying a {discount}% discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")