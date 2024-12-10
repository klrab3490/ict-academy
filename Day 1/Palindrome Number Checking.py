# Get The number
num=int(input("Enter 5 digit number: "))
cnum=num # Create a copy
reverse=0 # Set reverse as 0

# reversing The number num
while num!=0:
	reverse=reverse*10+num%10
	num//=10

# Checking Whether is Palindrome
if cnum==reverse:
	print("Palindrome")
else:
	print("Not Palindrome")