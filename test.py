try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    print("Error: You must enter whole numbers.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")