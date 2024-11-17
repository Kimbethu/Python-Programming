def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


original_price = 100.00  
discount_percent = 25  

#Final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
print(f"The final price is: {final_price:.2f}")
