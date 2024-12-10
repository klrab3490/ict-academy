'''
Generate Pattern
* * * * *
*       *
*       *
*       *
* * * * *
'''

num=int(input("Square Boarder Pattern: "))

for i in range(num):
	for j in range(num):
		if i==0 or i==num-1 or j==0 or j==num-1: # Checking whether the pointer are at starting or end
			print("*", end=" ")
		else:
			print(" ", end=" ")
				
	print()