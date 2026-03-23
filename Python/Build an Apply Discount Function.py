


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