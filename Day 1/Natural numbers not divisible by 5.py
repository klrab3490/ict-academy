i=1
num=int(input("Enter number: "))

print("List of natural numbers not divisible by 5:",end=" ")

while i<=num:
	if i%5!=0:
		print(i, end=", ")
	
	i+=1

print()