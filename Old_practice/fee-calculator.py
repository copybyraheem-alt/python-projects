class FeeCalculator:
    @staticmethod
    def discount(amount, percent):
        percent = percent / 100
        discount_amount = amount * percent
        sale_price = amount - discount_amount
        return sale_price
    
    @staticmethod
    def tax(amount, rate):
        rate = rate / 100
        tax_amount = amount * rate
        final = amount + tax_amount
        return final
    
    @staticmethod
    def final_fee(base, discount_percent, tax_rate):
        discount = FeeCalculator.discount(base, discount_percent)
        tax = FeeCalculator.tax(discount, tax_rate)
        return tax


def main():
    try:
        base = float(input("Enter your amount: "))
        discount = float(input("What is the discount in %: "))
        tax = float(input("Enter the tax in %: "))
    except ValueError:
        print("Invalid input: Please enter valid numbers.")
        return

    if base < 0 or discount < 0 or tax < 0:
        print("Invalid input: Values cannot be negative.")
        return

    if discount > 100:
        print("Invalid input: Discount cannot exceed 100%.")
        return

    print(f"Discounted amount: {FeeCalculator.discount(base, discount):.2f}")
    print(f"Total amount: {FeeCalculator.final_fee(base, discount, tax):.2f}")


if __name__ == "__main__":
    main()
