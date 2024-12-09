'''
Conditions:
 below 200 units ---> Cost $0
201 to 300 units ---> Cost $1.5
301 to 400 units ---> Cost $2.5
401 to 500 units ---> Cost $3
 above 500 units ---> Cost $6
'''

units=int(input("Tiered Electricity Billing Calculator\nEnter the units used : "))
if (units<=200):
    ebill=0
elif (units<=300):
    ebill=(units-200)*1.5
elif (units<=400):
    n1=units-300
    ebill=(100*1.5)+(n1*2.5)
elif (units<=500):
    n1=units-400
    ebill=(100*1.5)+(100*2.5)+(n1*3)
else:
    n1=units-500
    ebill=(100*1.5)+(100*2.5)+(100*3)+(n1*6)

print("Bill Amount: ",ebill)