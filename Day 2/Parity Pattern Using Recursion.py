'''
2 methods
- Odd to 20
- Even to 20

output: 2 1 4 3 6 5 8 7 10 9 12 11 14 13 16 15 18 17 20 19
'''

def even(num, limit):
	if(num<=limit):
		print(num-1,end=" ")
		num+=1
		odd(num,limit)
def odd(num, limit):
	if(num<=limit):
		print(num+1,end=" ")
		num+=1
		even(num,limit)

number=int(input("Enter number limit: "))
print("List: ",end="")
odd(1,number)