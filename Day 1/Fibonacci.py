a=1
b=1

num=int(input("Enter the possible iterations: "))
i=0

print("Fibonacci Series: ", end=" ")
while i<num:
    print(a, end=" ")
    c=a+b
    a=b
    b=c
    i+=1
    
print()