class FeeCalculator:
    @staticmethod
    def discount(amount, percent):
        percent = percent / 100
        discount_amount= amount * percent
        sale_price = amount - discount_amount
        return sale_price
    
    @staticmethod
    def tax(amount, rate):
        rate = rate / 100
        tax_amount = amount*rate
        final = amount + tax_amount
        return final
    
    @staticmethod
    def final_fee(base, discount_percent, tax_rate):
        discount = FeeCalculator.discount(base, discount_percent)
        Tax = FeeCalculator.tax(discount, tax_rate)
        final_price = Tax
        return final_price

base=float(input("Enter your amount: "))
discount= float(input("What is the discount in %: "))
tax= float(input("Enter the tax in %: "))
print (f"Discounted amount: {FeeCalculator.discount(base, discount):.2f}")
print (f"Total amount: {FeeCalculator.final_fee(base, discount, tax):.2f}")
