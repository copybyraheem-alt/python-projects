class FareValidator:
    @staticmethod
    def is_valid_distance(distance):
        if distance > 0:
            return True
        else:
            return False
        
    @staticmethod
    def is_valid_percent(percent):
        if percent >= 0 and percent <= 100:
            return True
        else:
            return False

class FareCalculator:
    @staticmethod
    def base_fare(distance):
        return 10+distance*2
    
    @staticmethod
    def apply_discount(amount, percent):
        percent /= 100
        discount_amount= amount * percent
        sales_price = amount - discount_amount
        return sales_price

    @staticmethod
    def apply_tax(amount, percent):
        percent = percent/100
        tax = amount*percent
        final = amount + tax
        return final

Distance= float(input("Enter your distance: "))
Discount=float(input("Enter your discount: "))
Tax=float(input("Enter your tax: "))


valid_distance= FareValidator.is_valid_distance(Distance)
valid_discount=FareValidator.is_valid_percent(Discount)
valid_tax=FareValidator.is_valid_percent(Tax)



if not valid_distance or not valid_discount or not valid_tax:
    print("Invalid input")
else:
    base_fare=FareCalculator.base_fare(Distance)
    discount_got=FareCalculator.apply_discount(base_fare,Discount)
    print(f"Base fare: {base_fare:.2f}")
    print(f"Discounted fare: {discount_got:.2f}")
    print(f"Final fare: {FareCalculator.apply_tax(discount_got, Tax):.2f}")