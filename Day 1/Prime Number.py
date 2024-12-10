flag=1
num=int(input("Enter A Numer: "))

if num==0 or num==1:
	print("Number Is Not Prime")
else:
	for i in range(2,num):
		if (num%i) == 0:
			flag=0
			break
	
if flag==1:
	print("Prime")
else:
	print("Not Prime")