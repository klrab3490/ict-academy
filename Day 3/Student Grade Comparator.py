'''
Object For Student: attribule Reg, name m1,m2,m3
 -- input how many students: n
 -- add students to disctionary register number as key: name
'''

class Student:
    def __init__(self, num, name, m1, m2, m3):
        self.reg_number = num
        self.name = name
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
    
    def compare(self, other):
        avg_self=(self.mark1+self.mark2+self.mark3)/3
		avg_other=(other.mark1+other.mark2+other.mark3)/3
    	if avg_self>avg_other:
    		print("Reg No.:",self.reg_number,"with name",self.name,"is greater")
    	else:
    		print("Reg No.:",other.reg_number,"with name",other.name,"is greater")
        
class_mark={} # Store data

# Add data from user
count=int(input("Enter How Many Student: "))
for i in range(count):
	print(f"Student {i+1} Data: ")
	name = input("Enter Your Name: ")
	reg = int(input("Enter Register Number: "))
	mrk1 = int(input("Enter Mark 1:"))
	mrk2 = int(input("Enter Mark 2:"))
	mrk3 = int(input("Enter Mark 3:"))
	student = Student(reg, name, mrk1, mrk2, mrk3)
	class_mark[reg] = student
	print()
	
print("Comparing Student Data:")
print("="*10)
reg1 = int(input("Enter the Register Number Of 1st Person: "))
reg2 = int(input("Enter the Register Number Of 2nd Person: "))
class_mark[reg1].compare(class_mark[reg2])