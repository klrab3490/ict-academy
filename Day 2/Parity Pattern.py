'''
2 methods
- Odd to 20
- Even to 20

output: 2 1 4 3 6 5 8 7 10 9 12 11 14 13 16 15 18 17 20 19
'''

def even(n):
	return n-1
def odd(n):
	return n+1

number=int(input("Enter number limit: "))
print("List: ",end="")
for i in range(1,number+1):
	if i%2==0:
		print(even(i), end=" ")
	else:
		print(odd(i), end=" ")
		
print()
