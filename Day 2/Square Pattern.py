'''
Generate Pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

num=int(input("Square Pattern Of Star: "))

for i in range(num):
	for j in range(num):
		print("*", end=" ") # Print at all locations (i,j)
	print()