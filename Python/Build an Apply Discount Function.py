"""
Apply Discount Function – Notes

This function calculates the final price of an item after applying a percentage discount.

The function takes two inputs: price and discount.
It validates that both inputs are numbers (int or float).
It ensures the price is greater than 0 and the discount is between 0 and 100.
If any input is invalid, the function returns an appropriate error message.
If inputs are valid, it calculates the discount amount and subtracts it from the original price.
The function returns the final price instead of printing it, allowing the result to be reused or tested.
"""


def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
        return("The price should be a number")
    else:
        if not isinstance(discount,(int,float)):
            return("The discount should be a number")
        else:
            if price <= 0:
                return("The price should be greater than 0")
            else:
                if discount < 0 or discount > 100:
                    return("The discount should be between 0 and 100")
                else:
                    discount_price = (price / 100)*discount
                    final_price = price - discount_price
                    return(final_price)

apply_discount(100,20)