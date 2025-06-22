try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))
    print(f"Result {numerator/denominator}")
except ZeroDivisionError:
    print("Can't divide by Zero")
except ValueError:
    print("Enter Valid integer")
