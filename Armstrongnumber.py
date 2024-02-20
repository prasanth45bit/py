def is_armstrong_number(number):
    num_str = str(number)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number
user_input = int(input("Enter a number: "))
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
