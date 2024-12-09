
bal = 100000
choice = int(input("1. Deposite, 2. Withdraw\nWhat to do?\n Choice: "))
if choice==1:
    amt= int(input("Amount to be deposited: "))
    bal+=amt
    print("Available Account Balance :",bal)
elif choice==2:
    amt= int(input("Amount to be withdrawn: "))
    if (bal >= amt):
        bal-=amt 
    else:
        print("Insufficiant Funds")
    print("Available Account Balance :",bal)
else:
    print("Error Choice")