number = int(input("Enter a number with more than 6 digits: "))
if number >= 1000000:
    last_digit = number % 10
    number //= 10
    new_last_digit = int(input("Enter the new last digit: "))
    number = number * 10 + new_last_digit
    print("Result:", number)
else:
    print("Please enter a valid number with more than 6 digits.")
