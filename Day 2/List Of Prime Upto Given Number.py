num=int(input("rime Numbers\nEnter A Number Till Which you Need Prime Numbers: "))
prime=[] # Array To Store Prime numbers

if num<=1: #Check If the number 1 or 0
	print("No Prime Numbers")
else: 
	while num>=2: # Check For all number between 2 & num
		flag=1
		for i in range(2,int(num//2)+1): 
			if (num%i) == 0: # Checking Prim add flag if not prime
				flag=0 
				break

		if flag==1: # If Prime add value to array
			prime.append(num)

			
		num=num-1
	
	print("Prime Numbers :",prime)