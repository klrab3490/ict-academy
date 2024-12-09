# Taking user input for the starting number, ending number, and the number of odd numbers to display
num1 = int(input("Enter a starting number: "))  # Starting number
num2 = int(input("Enter a ending number: "))   # Ending number
num3 = int(input("Enter a required set: "))    # Number of odd numbers to print

i = 1  # Initialize loop counter
# Print the header for the odd numbers
print("Odd Numbers between", num1, "&", num2, end=": ")

# Loop through the numbers from num1 to num2
while num1 <= num2:
    # Check if the number is odd and if we still need to print more odd numbers
    if num1 % 2 != 0 and num3 > 0:
        print(num1, end=", ")  # Print the odd number
        num1 += 2  # Move to the next odd number
        num3 -= 1  # Decrease the count of odd numbers left to print
    else:
        num1 += 1  # Move to the next number, if it's not odd

# Print a new line after all odd numbers are printed
print()
