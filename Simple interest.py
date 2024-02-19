def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage:
principal_amount = 1000
interest_rate = 5
time_period = 2

result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print(f"The Simple Interest is: {result}")
