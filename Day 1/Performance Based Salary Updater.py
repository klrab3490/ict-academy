'''
Given Input: Salary, Performance

Conditions:
1. If the performance is greater than or equal to 80, the hike is 30% of the current salary.
2. If the performance is below 80, the hike is calculated proportionally (i.e., based on the performance percentage).

Example:
10000   80  13000
10000   60  12250
10000   40  11500
'''

# Input salary and performance
salary = int(input("Enter the Salary: "))
performance = int(input("Enter the Performance: "))

# Calculate salary hike based on performance
if performance >= 80:
    hike = (salary * 0.3)
else:
    # Proportional hike for performance below 80
    x = (3 * performance) / 8
    hike = (salary * x) / 100

# Print the total salary after hike
print("Salary Hike: ", salary + hike)
