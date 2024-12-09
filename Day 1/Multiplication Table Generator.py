# Taking user input for the multiplication table
table = int(input("Enter the multiplication table that u require: "))

i = 1  # Initialize the counter to 1, as multiplication starts from 1
while i <= 10:
    print(table, "x", i, "=", i * table)  # Print the current multiplication result
    i += 1  # Increment the counter to move to the next number
