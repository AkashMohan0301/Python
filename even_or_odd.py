def odd_or_even(a):
    """Write a function that takes a number and returns "odd" if the number is odd and "even" if the number is even."""
    if a % 2 == 0:
        return "even"
    else:
        return "odd"
while True:
    try:
        print(odd_or_even(int(input("Enter a Number :"))))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
