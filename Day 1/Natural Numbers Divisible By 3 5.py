'''
Print Natural numers upto the number which are 
1. divisible by 3 hai
2. divisible by 5 hello
3. divisible by 5,3 welocome
4. not divisible by 5,3 quit
'''

i=1
num=int(input("Enter number: "))

while i<=num:
	print(i,end=")")
	if i%15==0:
		print("welcome")
	elif i%3==0:
		print("hai")
	elif i%5==0:
		print("hello")
	elif i%3!=0 and i%5!=0:
		print("quit")
	
	i+=1
print()