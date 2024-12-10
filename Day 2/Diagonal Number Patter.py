'''
Generate Pattern
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1
'''

num=int(input("Diagonal Number Pattern: "))

for i in range(num):
	for j in range(1,num+1-i):
		print(j, end=" ")
				
	print()